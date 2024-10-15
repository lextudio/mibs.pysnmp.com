# SNMP MIB module (LBHUB-MSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LBHUB-MSH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:27 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



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
    (0, "LBHUB-MSH-MIB", "ifIndex"),
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
    (0, "LBHUB-MSH-MIB", "ipAdEntAddr"),
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
    (0, "LBHUB-MSH-MIB", "ipRouteDest"),
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
    (0, "LBHUB-MSH-MIB", "ipNetToMediaIfIndex"),
    (0, "LBHUB-MSH-MIB", "ipNetToMediaNetAddress"),
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
    (0, "LBHUB-MSH-MIB", "tcpConnLocalAddress"),
    (0, "LBHUB-MSH-MIB", "tcpConnLocalPort"),
    (0, "LBHUB-MSH-MIB", "tcpConnRemAddress"),
    (0, "LBHUB-MSH-MIB", "tcpConnRemPort"),
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
    (0, "LBHUB-MSH-MIB", "udpLocalAddress"),
    (0, "LBHUB-MSH-MIB", "udpLocalPort"),
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
_Rmon_ObjectIdentity = ObjectIdentity
rmon = _Rmon_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16)
)
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 1)
)
_History_ObjectIdentity = ObjectIdentity
history = _History_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 2)
)
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 3)
)
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("mandatory")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1)
)
alarmEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("mandatory")


class _AlarmIndex_Type(Integer32):
    """Custom type alarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlarmIndex_Type.__name__ = "Integer32"
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("mandatory")
_AlarmInterval_Type = Integer32
_AlarmInterval_Object = MibTableColumn
alarmInterval = _AlarmInterval_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 2),
    _AlarmInterval_Type()
)
alarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmInterval.setStatus("mandatory")
_AlarmVariable_Type = ObjectIdentifier
_AlarmVariable_Object = MibTableColumn
alarmVariable = _AlarmVariable_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 3),
    _AlarmVariable_Type()
)
alarmVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmVariable.setStatus("mandatory")


class _AlarmSampleType_Type(Integer32):
    """Custom type alarmSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_AlarmSampleType_Type.__name__ = "Integer32"
_AlarmSampleType_Object = MibTableColumn
alarmSampleType = _AlarmSampleType_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 4),
    _AlarmSampleType_Type()
)
alarmSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSampleType.setStatus("mandatory")
_AlarmValue_Type = Integer32
_AlarmValue_Object = MibTableColumn
alarmValue = _AlarmValue_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 5),
    _AlarmValue_Type()
)
alarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmValue.setStatus("mandatory")


class _AlarmStartupAlarm_Type(Integer32):
    """Custom type alarmStartupAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallingAlarm", 2),
          ("risingAlarm", 1),
          ("risingOrFallingAlarm", 3))
    )


_AlarmStartupAlarm_Type.__name__ = "Integer32"
_AlarmStartupAlarm_Object = MibTableColumn
alarmStartupAlarm = _AlarmStartupAlarm_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 6),
    _AlarmStartupAlarm_Type()
)
alarmStartupAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmStartupAlarm.setStatus("mandatory")
_AlarmRisingThreshold_Type = Integer32
_AlarmRisingThreshold_Object = MibTableColumn
alarmRisingThreshold = _AlarmRisingThreshold_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 7),
    _AlarmRisingThreshold_Type()
)
alarmRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRisingThreshold.setStatus("mandatory")
_AlarmFallingThreshold_Type = Integer32
_AlarmFallingThreshold_Object = MibTableColumn
alarmFallingThreshold = _AlarmFallingThreshold_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 8),
    _AlarmFallingThreshold_Type()
)
alarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmFallingThreshold.setStatus("mandatory")


class _AlarmRisingEventIndex_Type(Integer32):
    """Custom type alarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlarmRisingEventIndex_Type.__name__ = "Integer32"
_AlarmRisingEventIndex_Object = MibTableColumn
alarmRisingEventIndex = _AlarmRisingEventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 9),
    _AlarmRisingEventIndex_Type()
)
alarmRisingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRisingEventIndex.setStatus("mandatory")


class _AlarmFallingEventIndex_Type(Integer32):
    """Custom type alarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlarmFallingEventIndex_Type.__name__ = "Integer32"
_AlarmFallingEventIndex_Object = MibTableColumn
alarmFallingEventIndex = _AlarmFallingEventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 10),
    _AlarmFallingEventIndex_Type()
)
alarmFallingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmFallingEventIndex.setStatus("mandatory")
_AlarmOwner_Type = DisplayString
_AlarmOwner_Object = MibTableColumn
alarmOwner = _AlarmOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 11),
    _AlarmOwner_Type()
)
alarmOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmOwner.setStatus("mandatory")


class _AlarmStatus_Type(Integer32):
    """Custom type alarmStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_AlarmStatus_Type.__name__ = "Integer32"
_AlarmStatus_Object = MibTableColumn
alarmStatus = _AlarmStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 12),
    _AlarmStatus_Type()
)
alarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmStatus.setStatus("mandatory")
_Hosts_ObjectIdentity = ObjectIdentity
hosts = _Hosts_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 4)
)
_HostTopN_ObjectIdentity = ObjectIdentity
hostTopN = _HostTopN_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 5)
)
_Matrix_ObjectIdentity = ObjectIdentity
matrix = _Matrix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 6)
)
_Filter_ObjectIdentity = ObjectIdentity
filter = _Filter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 7)
)
_Capture_ObjectIdentity = ObjectIdentity
capture = _Capture_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 8)
)
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 9)
)
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("mandatory")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1)
)
eventEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "eventIndex"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("mandatory")


class _EventIndex_Type(Integer32):
    """Custom type eventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EventIndex_Type.__name__ = "Integer32"
_EventIndex_Object = MibTableColumn
eventIndex = _EventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 1),
    _EventIndex_Type()
)
eventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventIndex.setStatus("mandatory")


class _EventDescription_Type(DisplayString):
    """Custom type eventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EventDescription_Type.__name__ = "DisplayString"
_EventDescription_Object = MibTableColumn
eventDescription = _EventDescription_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 2),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventDescription.setStatus("mandatory")


class _EventType_Type(Integer32):
    """Custom type eventType based on Integer32"""
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
        *(("log", 2),
          ("log-and-trap", 4),
          ("none", 1),
          ("snmp-trap", 3))
    )


_EventType_Type.__name__ = "Integer32"
_EventType_Object = MibTableColumn
eventType = _EventType_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 3),
    _EventType_Type()
)
eventType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventType.setStatus("mandatory")


class _EventCommunity_Type(OctetString):
    """Custom type eventCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EventCommunity_Type.__name__ = "OctetString"
_EventCommunity_Object = MibTableColumn
eventCommunity = _EventCommunity_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 4),
    _EventCommunity_Type()
)
eventCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventCommunity.setStatus("mandatory")
_EventLastTimeSent_Type = TimeTicks
_EventLastTimeSent_Object = MibTableColumn
eventLastTimeSent = _EventLastTimeSent_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 5),
    _EventLastTimeSent_Type()
)
eventLastTimeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLastTimeSent.setStatus("mandatory")
_EventOwner_Type = DisplayString
_EventOwner_Object = MibTableColumn
eventOwner = _EventOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 6),
    _EventOwner_Type()
)
eventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventOwner.setStatus("mandatory")


class _EventStatus_Type(Integer32):
    """Custom type eventStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_EventStatus_Type.__name__ = "Integer32"
_EventStatus_Object = MibTableColumn
eventStatus = _EventStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 7),
    _EventStatus_Type()
)
eventStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventStatus.setStatus("mandatory")
_LogTable_Object = MibTable
logTable = _LogTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2)
)
if mibBuilder.loadTexts:
    logTable.setStatus("mandatory")
_LogEntry_Object = MibTableRow
logEntry = _LogEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1)
)
logEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "logEventIndex"),
    (0, "LBHUB-MSH-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    logEntry.setStatus("mandatory")


class _LogEventIndex_Type(Integer32):
    """Custom type logEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LogEventIndex_Type.__name__ = "Integer32"
_LogEventIndex_Object = MibTableColumn
logEventIndex = _LogEventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 1),
    _LogEventIndex_Type()
)
logEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventIndex.setStatus("mandatory")
_LogIndex_Type = Integer32
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 2),
    _LogIndex_Type()
)
logIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logIndex.setStatus("mandatory")
_LogTime_Type = TimeTicks
_LogTime_Object = MibTableColumn
logTime = _LogTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 3),
    _LogTime_Type()
)
logTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTime.setStatus("mandatory")


class _LogDescription_Type(DisplayString):
    """Custom type logDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LogDescription_Type.__name__ = "DisplayString"
_LogDescription_Object = MibTableColumn
logDescription = _LogDescription_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 4),
    _LogDescription_Type()
)
logDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logDescription.setStatus("mandatory")
_Dot1dBridge_ObjectIdentity = ObjectIdentity
dot1dBridge = _Dot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17)
)
_SnmpDot3RptrMgt_ObjectIdentity = ObjectIdentity
snmpDot3RptrMgt = _SnmpDot3RptrMgt_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22)
)
_RptrBasicPackage_ObjectIdentity = ObjectIdentity
rptrBasicPackage = _RptrBasicPackage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1)
)
_RptrRptrInfo_ObjectIdentity = ObjectIdentity
rptrRptrInfo = _RptrRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 1)
)


class _RptrGroupCapacity_Type(Integer32):
    """Custom type rptrGroupCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrGroupCapacity_Type.__name__ = "Integer32"
_RptrGroupCapacity_Object = MibScalar
rptrGroupCapacity = _RptrGroupCapacity_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 1),
    _RptrGroupCapacity_Type()
)
rptrGroupCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupCapacity.setStatus("mandatory")


class _RptrOperStatus_Type(Integer32):
    """Custom type rptrOperStatus based on Integer32"""
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
        *(("generalFailure", 6),
          ("groupFailure", 4),
          ("ok", 2),
          ("other", 1),
          ("portFailure", 5),
          ("rptrFailure", 3))
    )


_RptrOperStatus_Type.__name__ = "Integer32"
_RptrOperStatus_Object = MibScalar
rptrOperStatus = _RptrOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 2),
    _RptrOperStatus_Type()
)
rptrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrOperStatus.setStatus("mandatory")


class _RptrHealthText_Type(DisplayString):
    """Custom type rptrHealthText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RptrHealthText_Type.__name__ = "DisplayString"
_RptrHealthText_Object = MibScalar
rptrHealthText = _RptrHealthText_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 3),
    _RptrHealthText_Type()
)
rptrHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrHealthText.setStatus("mandatory")


class _RptrReset_Type(Integer32):
    """Custom type rptrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_RptrReset_Type.__name__ = "Integer32"
_RptrReset_Object = MibScalar
rptrReset = _RptrReset_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 4),
    _RptrReset_Type()
)
rptrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrReset.setStatus("mandatory")


class _RptrNonDisruptTest_Type(Integer32):
    """Custom type rptrNonDisruptTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSelfTest", 1),
          ("selfTest", 2))
    )


_RptrNonDisruptTest_Type.__name__ = "Integer32"
_RptrNonDisruptTest_Object = MibScalar
rptrNonDisruptTest = _RptrNonDisruptTest_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 5),
    _RptrNonDisruptTest_Type()
)
rptrNonDisruptTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrNonDisruptTest.setStatus("mandatory")
_RptrTotalPartitionedPorts_Type = Gauge32
_RptrTotalPartitionedPorts_Object = MibScalar
rptrTotalPartitionedPorts = _RptrTotalPartitionedPorts_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 6),
    _RptrTotalPartitionedPorts_Type()
)
rptrTotalPartitionedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrTotalPartitionedPorts.setStatus("mandatory")
_RptrGroupInfo_ObjectIdentity = ObjectIdentity
rptrGroupInfo = _RptrGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 2)
)
_RptrGroupTable_Object = MibTable
rptrGroupTable = _RptrGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rptrGroupTable.setStatus("mandatory")
_RptrGroupEntry_Object = MibTableRow
rptrGroupEntry = _RptrGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1)
)
rptrGroupEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "rptrGroupIndex"),
)
if mibBuilder.loadTexts:
    rptrGroupEntry.setStatus("mandatory")


class _RptrGroupIndex_Type(Integer32):
    """Custom type rptrGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrGroupIndex_Type.__name__ = "Integer32"
_RptrGroupIndex_Object = MibTableColumn
rptrGroupIndex = _RptrGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 1),
    _RptrGroupIndex_Type()
)
rptrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupIndex.setStatus("mandatory")


class _RptrGroupDescr_Type(DisplayString):
    """Custom type rptrGroupDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RptrGroupDescr_Type.__name__ = "DisplayString"
_RptrGroupDescr_Object = MibTableColumn
rptrGroupDescr = _RptrGroupDescr_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 2),
    _RptrGroupDescr_Type()
)
rptrGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupDescr.setStatus("mandatory")
_RptrGroupObjectID_Type = ObjectIdentifier
_RptrGroupObjectID_Object = MibTableColumn
rptrGroupObjectID = _RptrGroupObjectID_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 3),
    _RptrGroupObjectID_Type()
)
rptrGroupObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupObjectID.setStatus("mandatory")


class _RptrGroupOperStatus_Type(Integer32):
    """Custom type rptrGroupOperStatus based on Integer32"""
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
        *(("malfunctioning", 3),
          ("notPresent", 4),
          ("operational", 2),
          ("other", 1),
          ("resetInProgress", 6),
          ("underTest", 5))
    )


_RptrGroupOperStatus_Type.__name__ = "Integer32"
_RptrGroupOperStatus_Object = MibTableColumn
rptrGroupOperStatus = _RptrGroupOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 4),
    _RptrGroupOperStatus_Type()
)
rptrGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupOperStatus.setStatus("mandatory")
_RptrGroupLastOperStatusChange_Type = TimeTicks
_RptrGroupLastOperStatusChange_Object = MibTableColumn
rptrGroupLastOperStatusChange = _RptrGroupLastOperStatusChange_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 5),
    _RptrGroupLastOperStatusChange_Type()
)
rptrGroupLastOperStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupLastOperStatusChange.setStatus("mandatory")


class _RptrGroupPortCapacity_Type(Integer32):
    """Custom type rptrGroupPortCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrGroupPortCapacity_Type.__name__ = "Integer32"
_RptrGroupPortCapacity_Object = MibTableColumn
rptrGroupPortCapacity = _RptrGroupPortCapacity_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 6),
    _RptrGroupPortCapacity_Type()
)
rptrGroupPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupPortCapacity.setStatus("mandatory")
_RptrPortInfo_ObjectIdentity = ObjectIdentity
rptrPortInfo = _RptrPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 3)
)
_RptrPortTable_Object = MibTable
rptrPortTable = _RptrPortTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rptrPortTable.setStatus("mandatory")
_RptrPortEntry_Object = MibTableRow
rptrPortEntry = _RptrPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1)
)
rptrPortEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "rptrPortGroupIndex"),
    (0, "LBHUB-MSH-MIB", "rptrPortIndex"),
)
if mibBuilder.loadTexts:
    rptrPortEntry.setStatus("mandatory")


class _RptrPortGroupIndex_Type(Integer32):
    """Custom type rptrPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrPortGroupIndex_Type.__name__ = "Integer32"
_RptrPortGroupIndex_Object = MibTableColumn
rptrPortGroupIndex = _RptrPortGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 1),
    _RptrPortGroupIndex_Type()
)
rptrPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGroupIndex.setStatus("mandatory")


class _RptrPortIndex_Type(Integer32):
    """Custom type rptrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrPortIndex_Type.__name__ = "Integer32"
_RptrPortIndex_Object = MibTableColumn
rptrPortIndex = _RptrPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 2),
    _RptrPortIndex_Type()
)
rptrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortIndex.setStatus("mandatory")


class _RptrPortAdminStatus_Type(Integer32):
    """Custom type rptrPortAdminStatus based on Integer32"""
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


_RptrPortAdminStatus_Type.__name__ = "Integer32"
_RptrPortAdminStatus_Object = MibTableColumn
rptrPortAdminStatus = _RptrPortAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 3),
    _RptrPortAdminStatus_Type()
)
rptrPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAdminStatus.setStatus("mandatory")


class _RptrPortAutoPartitionState_Type(Integer32):
    """Custom type rptrPortAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoPartitioned", 2),
          ("notAutoPartitioned", 1))
    )


_RptrPortAutoPartitionState_Type.__name__ = "Integer32"
_RptrPortAutoPartitionState_Object = MibTableColumn
rptrPortAutoPartitionState = _RptrPortAutoPartitionState_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 4),
    _RptrPortAutoPartitionState_Type()
)
rptrPortAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortAutoPartitionState.setStatus("mandatory")


class _RptrPortOperStatus_Type(Integer32):
    """Custom type rptrPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 2),
          ("notPresent", 3),
          ("operational", 1))
    )


_RptrPortOperStatus_Type.__name__ = "Integer32"
_RptrPortOperStatus_Object = MibTableColumn
rptrPortOperStatus = _RptrPortOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 5),
    _RptrPortOperStatus_Type()
)
rptrPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortOperStatus.setStatus("mandatory")
_RptrMonitorPackage_ObjectIdentity = ObjectIdentity
rptrMonitorPackage = _RptrMonitorPackage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2)
)
_RptrMonitorRptrInfo_ObjectIdentity = ObjectIdentity
rptrMonitorRptrInfo = _RptrMonitorRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2, 1)
)
_RptrMonitorTransmitCollisions_Type = Counter32
_RptrMonitorTransmitCollisions_Object = MibScalar
rptrMonitorTransmitCollisions = _RptrMonitorTransmitCollisions_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 1, 1),
    _RptrMonitorTransmitCollisions_Type()
)
rptrMonitorTransmitCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorTransmitCollisions.setStatus("mandatory")
_RptrMonitorGroupInfo_ObjectIdentity = ObjectIdentity
rptrMonitorGroupInfo = _RptrMonitorGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2, 2)
)
_RptrMonitorGroupTable_Object = MibTable
rptrMonitorGroupTable = _RptrMonitorGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rptrMonitorGroupTable.setStatus("mandatory")
_RptrMonitorGroupEntry_Object = MibTableRow
rptrMonitorGroupEntry = _RptrMonitorGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1)
)
rptrMonitorGroupEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "rptrMonitorGroupIndex"),
)
if mibBuilder.loadTexts:
    rptrMonitorGroupEntry.setStatus("mandatory")


class _RptrMonitorGroupIndex_Type(Integer32):
    """Custom type rptrMonitorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrMonitorGroupIndex_Type.__name__ = "Integer32"
_RptrMonitorGroupIndex_Object = MibTableColumn
rptrMonitorGroupIndex = _RptrMonitorGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 1),
    _RptrMonitorGroupIndex_Type()
)
rptrMonitorGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorGroupIndex.setStatus("mandatory")
_RptrMonitorGroupTotalFrames_Type = Counter32
_RptrMonitorGroupTotalFrames_Object = MibTableColumn
rptrMonitorGroupTotalFrames = _RptrMonitorGroupTotalFrames_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 2),
    _RptrMonitorGroupTotalFrames_Type()
)
rptrMonitorGroupTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorGroupTotalFrames.setStatus("mandatory")
_RptrMonitorGroupTotalOctets_Type = Counter32
_RptrMonitorGroupTotalOctets_Object = MibTableColumn
rptrMonitorGroupTotalOctets = _RptrMonitorGroupTotalOctets_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 3),
    _RptrMonitorGroupTotalOctets_Type()
)
rptrMonitorGroupTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorGroupTotalOctets.setStatus("mandatory")
_RptrMonitorGroupTotalErrors_Type = Counter32
_RptrMonitorGroupTotalErrors_Object = MibTableColumn
rptrMonitorGroupTotalErrors = _RptrMonitorGroupTotalErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 4),
    _RptrMonitorGroupTotalErrors_Type()
)
rptrMonitorGroupTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorGroupTotalErrors.setStatus("mandatory")
_RptrMonitorPortInfo_ObjectIdentity = ObjectIdentity
rptrMonitorPortInfo = _RptrMonitorPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2, 3)
)
_RptrMonitorPortTable_Object = MibTable
rptrMonitorPortTable = _RptrMonitorPortTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1)
)
if mibBuilder.loadTexts:
    rptrMonitorPortTable.setStatus("mandatory")
_RptrMonitorPortEntry_Object = MibTableRow
rptrMonitorPortEntry = _RptrMonitorPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1)
)
rptrMonitorPortEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "rptrMonitorPortGroupIndex"),
    (0, "LBHUB-MSH-MIB", "rptrMonitorPortIndex"),
)
if mibBuilder.loadTexts:
    rptrMonitorPortEntry.setStatus("mandatory")


class _RptrMonitorPortGroupIndex_Type(Integer32):
    """Custom type rptrMonitorPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrMonitorPortGroupIndex_Type.__name__ = "Integer32"
_RptrMonitorPortGroupIndex_Object = MibTableColumn
rptrMonitorPortGroupIndex = _RptrMonitorPortGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 1),
    _RptrMonitorPortGroupIndex_Type()
)
rptrMonitorPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortGroupIndex.setStatus("mandatory")


class _RptrMonitorPortIndex_Type(Integer32):
    """Custom type rptrMonitorPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrMonitorPortIndex_Type.__name__ = "Integer32"
_RptrMonitorPortIndex_Object = MibTableColumn
rptrMonitorPortIndex = _RptrMonitorPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 2),
    _RptrMonitorPortIndex_Type()
)
rptrMonitorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortIndex.setStatus("mandatory")
_RptrMonitorPortReadableFrames_Type = Counter32
_RptrMonitorPortReadableFrames_Object = MibTableColumn
rptrMonitorPortReadableFrames = _RptrMonitorPortReadableFrames_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 3),
    _RptrMonitorPortReadableFrames_Type()
)
rptrMonitorPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortReadableFrames.setStatus("mandatory")
_RptrMonitorPortReadableOctets_Type = Counter32
_RptrMonitorPortReadableOctets_Object = MibTableColumn
rptrMonitorPortReadableOctets = _RptrMonitorPortReadableOctets_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 4),
    _RptrMonitorPortReadableOctets_Type()
)
rptrMonitorPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortReadableOctets.setStatus("mandatory")
_RptrMonitorPortFCSErrors_Type = Counter32
_RptrMonitorPortFCSErrors_Object = MibTableColumn
rptrMonitorPortFCSErrors = _RptrMonitorPortFCSErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 5),
    _RptrMonitorPortFCSErrors_Type()
)
rptrMonitorPortFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortFCSErrors.setStatus("mandatory")
_RptrMonitorPortAlignmentErrors_Type = Counter32
_RptrMonitorPortAlignmentErrors_Object = MibTableColumn
rptrMonitorPortAlignmentErrors = _RptrMonitorPortAlignmentErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 6),
    _RptrMonitorPortAlignmentErrors_Type()
)
rptrMonitorPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortAlignmentErrors.setStatus("mandatory")
_RptrMonitorPortFrameTooLongs_Type = Counter32
_RptrMonitorPortFrameTooLongs_Object = MibTableColumn
rptrMonitorPortFrameTooLongs = _RptrMonitorPortFrameTooLongs_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 7),
    _RptrMonitorPortFrameTooLongs_Type()
)
rptrMonitorPortFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortFrameTooLongs.setStatus("mandatory")
_RptrMonitorPortShortEvents_Type = Counter32
_RptrMonitorPortShortEvents_Object = MibTableColumn
rptrMonitorPortShortEvents = _RptrMonitorPortShortEvents_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 8),
    _RptrMonitorPortShortEvents_Type()
)
rptrMonitorPortShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortShortEvents.setStatus("mandatory")
_RptrMonitorPortRunts_Type = Counter32
_RptrMonitorPortRunts_Object = MibTableColumn
rptrMonitorPortRunts = _RptrMonitorPortRunts_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 9),
    _RptrMonitorPortRunts_Type()
)
rptrMonitorPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortRunts.setStatus("mandatory")
_RptrMonitorPortCollisions_Type = Counter32
_RptrMonitorPortCollisions_Object = MibTableColumn
rptrMonitorPortCollisions = _RptrMonitorPortCollisions_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 10),
    _RptrMonitorPortCollisions_Type()
)
rptrMonitorPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortCollisions.setStatus("mandatory")
_RptrMonitorPortLateEvents_Type = Counter32
_RptrMonitorPortLateEvents_Object = MibTableColumn
rptrMonitorPortLateEvents = _RptrMonitorPortLateEvents_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 11),
    _RptrMonitorPortLateEvents_Type()
)
rptrMonitorPortLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortLateEvents.setStatus("mandatory")
_RptrMonitorPortVeryLongEvents_Type = Counter32
_RptrMonitorPortVeryLongEvents_Object = MibTableColumn
rptrMonitorPortVeryLongEvents = _RptrMonitorPortVeryLongEvents_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 12),
    _RptrMonitorPortVeryLongEvents_Type()
)
rptrMonitorPortVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortVeryLongEvents.setStatus("mandatory")
_RptrMonitorPortDataRateMismatches_Type = Counter32
_RptrMonitorPortDataRateMismatches_Object = MibTableColumn
rptrMonitorPortDataRateMismatches = _RptrMonitorPortDataRateMismatches_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 13),
    _RptrMonitorPortDataRateMismatches_Type()
)
rptrMonitorPortDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortDataRateMismatches.setStatus("mandatory")
_RptrMonitorPortAutoPartitions_Type = Counter32
_RptrMonitorPortAutoPartitions_Object = MibTableColumn
rptrMonitorPortAutoPartitions = _RptrMonitorPortAutoPartitions_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 14),
    _RptrMonitorPortAutoPartitions_Type()
)
rptrMonitorPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortAutoPartitions.setStatus("mandatory")
_RptrMonitorPortTotalErrors_Type = Counter32
_RptrMonitorPortTotalErrors_Object = MibTableColumn
rptrMonitorPortTotalErrors = _RptrMonitorPortTotalErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 15),
    _RptrMonitorPortTotalErrors_Type()
)
rptrMonitorPortTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortTotalErrors.setStatus("mandatory")
_RptrAddrTrackPackage_ObjectIdentity = ObjectIdentity
rptrAddrTrackPackage = _RptrAddrTrackPackage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3)
)
_RptrAddrTrackRptrInfo_ObjectIdentity = ObjectIdentity
rptrAddrTrackRptrInfo = _RptrAddrTrackRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3, 1)
)
_RptrAddrTrackGroupInfo_ObjectIdentity = ObjectIdentity
rptrAddrTrackGroupInfo = _RptrAddrTrackGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3, 2)
)
_RptrAddrTrackPortInfo_ObjectIdentity = ObjectIdentity
rptrAddrTrackPortInfo = _RptrAddrTrackPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3, 3)
)
_RptrAddrTrackTable_Object = MibTable
rptrAddrTrackTable = _RptrAddrTrackTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1)
)
if mibBuilder.loadTexts:
    rptrAddrTrackTable.setStatus("mandatory")
_RptrAddrTrackEntry_Object = MibTableRow
rptrAddrTrackEntry = _RptrAddrTrackEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1)
)
rptrAddrTrackEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "rptrAddrTrackGroupIndex"),
    (0, "LBHUB-MSH-MIB", "rptrAddrTrackPortIndex"),
)
if mibBuilder.loadTexts:
    rptrAddrTrackEntry.setStatus("mandatory")


class _RptrAddrTrackGroupIndex_Type(Integer32):
    """Custom type rptrAddrTrackGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrAddrTrackGroupIndex_Type.__name__ = "Integer32"
_RptrAddrTrackGroupIndex_Object = MibTableColumn
rptrAddrTrackGroupIndex = _RptrAddrTrackGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 1),
    _RptrAddrTrackGroupIndex_Type()
)
rptrAddrTrackGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackGroupIndex.setStatus("mandatory")


class _RptrAddrTrackPortIndex_Type(Integer32):
    """Custom type rptrAddrTrackPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrAddrTrackPortIndex_Type.__name__ = "Integer32"
_RptrAddrTrackPortIndex_Object = MibTableColumn
rptrAddrTrackPortIndex = _RptrAddrTrackPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 2),
    _RptrAddrTrackPortIndex_Type()
)
rptrAddrTrackPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackPortIndex.setStatus("mandatory")
_RptrAddrTrackLastSourceAddress_Type = PhysAddress
_RptrAddrTrackLastSourceAddress_Object = MibTableColumn
rptrAddrTrackLastSourceAddress = _RptrAddrTrackLastSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 3),
    _RptrAddrTrackLastSourceAddress_Type()
)
rptrAddrTrackLastSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackLastSourceAddress.setStatus("mandatory")
_RptrAddrTrackSourceAddrChanges_Type = Counter32
_RptrAddrTrackSourceAddrChanges_Object = MibTableColumn
rptrAddrTrackSourceAddrChanges = _RptrAddrTrackSourceAddrChanges_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 4),
    _RptrAddrTrackSourceAddrChanges_Type()
)
rptrAddrTrackSourceAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackSourceAddrChanges.setStatus("mandatory")
_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_Ipx_ObjectIdentity = ObjectIdentity
ipx = _Ipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5)
)
_IpxSystem_ObjectIdentity = ObjectIdentity
ipxSystem = _IpxSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1)
)
_IpxBasicSysTable_Object = MibTable
ipxBasicSysTable = _IpxBasicSysTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    ipxBasicSysTable.setStatus("mandatory")
_IpxBasicSysEntry_Object = MibTableRow
ipxBasicSysEntry = _IpxBasicSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1)
)
ipxBasicSysEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "ipxBasicSysInstance"),
)
if mibBuilder.loadTexts:
    ipxBasicSysEntry.setStatus("mandatory")
_IpxBasicSysInstance_Type = Integer32
_IpxBasicSysInstance_Object = MibTableColumn
ipxBasicSysInstance = _IpxBasicSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 1),
    _IpxBasicSysInstance_Type()
)
ipxBasicSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInstance.setStatus("mandatory")


class _IpxBasicSysExistState_Type(Integer32):
    """Custom type ipxBasicSysExistState based on Integer32"""
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


_IpxBasicSysExistState_Type.__name__ = "Integer32"
_IpxBasicSysExistState_Object = MibTableColumn
ipxBasicSysExistState = _IpxBasicSysExistState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 2),
    _IpxBasicSysExistState_Type()
)
ipxBasicSysExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysExistState.setStatus("mandatory")


class _IpxBasicSysNetNumber_Type(OctetString):
    """Custom type ipxBasicSysNetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxBasicSysNetNumber_Type.__name__ = "OctetString"
_IpxBasicSysNetNumber_Object = MibTableColumn
ipxBasicSysNetNumber = _IpxBasicSysNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 3),
    _IpxBasicSysNetNumber_Type()
)
ipxBasicSysNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysNetNumber.setStatus("mandatory")


class _IpxBasicSysNode_Type(OctetString):
    """Custom type ipxBasicSysNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxBasicSysNode_Type.__name__ = "OctetString"
_IpxBasicSysNode_Object = MibTableColumn
ipxBasicSysNode = _IpxBasicSysNode_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 4),
    _IpxBasicSysNode_Type()
)
ipxBasicSysNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysNode.setStatus("mandatory")


class _IpxBasicSysName_Type(OctetString):
    """Custom type ipxBasicSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_IpxBasicSysName_Type.__name__ = "OctetString"
_IpxBasicSysName_Object = MibTableColumn
ipxBasicSysName = _IpxBasicSysName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 5),
    _IpxBasicSysName_Type()
)
ipxBasicSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysName.setStatus("mandatory")
_IpxBasicSysInReceives_Type = Counter32
_IpxBasicSysInReceives_Object = MibTableColumn
ipxBasicSysInReceives = _IpxBasicSysInReceives_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 6),
    _IpxBasicSysInReceives_Type()
)
ipxBasicSysInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInReceives.setStatus("mandatory")
_IpxBasicSysInHdrErrors_Type = Counter32
_IpxBasicSysInHdrErrors_Object = MibTableColumn
ipxBasicSysInHdrErrors = _IpxBasicSysInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 7),
    _IpxBasicSysInHdrErrors_Type()
)
ipxBasicSysInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInHdrErrors.setStatus("mandatory")
_IpxBasicSysInUnknownSockets_Type = Counter32
_IpxBasicSysInUnknownSockets_Object = MibTableColumn
ipxBasicSysInUnknownSockets = _IpxBasicSysInUnknownSockets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 8),
    _IpxBasicSysInUnknownSockets_Type()
)
ipxBasicSysInUnknownSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInUnknownSockets.setStatus("mandatory")
_IpxBasicSysInDiscards_Type = Counter32
_IpxBasicSysInDiscards_Object = MibTableColumn
ipxBasicSysInDiscards = _IpxBasicSysInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 9),
    _IpxBasicSysInDiscards_Type()
)
ipxBasicSysInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInDiscards.setStatus("mandatory")
_IpxBasicSysInBadChecksums_Type = Counter32
_IpxBasicSysInBadChecksums_Object = MibTableColumn
ipxBasicSysInBadChecksums = _IpxBasicSysInBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 10),
    _IpxBasicSysInBadChecksums_Type()
)
ipxBasicSysInBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInBadChecksums.setStatus("mandatory")
_IpxBasicSysInDelivers_Type = Counter32
_IpxBasicSysInDelivers_Object = MibTableColumn
ipxBasicSysInDelivers = _IpxBasicSysInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 11),
    _IpxBasicSysInDelivers_Type()
)
ipxBasicSysInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInDelivers.setStatus("mandatory")
_IpxBasicSysNoRoutes_Type = Counter32
_IpxBasicSysNoRoutes_Object = MibTableColumn
ipxBasicSysNoRoutes = _IpxBasicSysNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 12),
    _IpxBasicSysNoRoutes_Type()
)
ipxBasicSysNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysNoRoutes.setStatus("mandatory")
_IpxBasicSysOutRequests_Type = Counter32
_IpxBasicSysOutRequests_Object = MibTableColumn
ipxBasicSysOutRequests = _IpxBasicSysOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 13),
    _IpxBasicSysOutRequests_Type()
)
ipxBasicSysOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutRequests.setStatus("mandatory")
_IpxBasicSysOutMalformedRequests_Type = Counter32
_IpxBasicSysOutMalformedRequests_Object = MibTableColumn
ipxBasicSysOutMalformedRequests = _IpxBasicSysOutMalformedRequests_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 14),
    _IpxBasicSysOutMalformedRequests_Type()
)
ipxBasicSysOutMalformedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutMalformedRequests.setStatus("mandatory")
_IpxBasicSysOutDiscards_Type = Counter32
_IpxBasicSysOutDiscards_Object = MibTableColumn
ipxBasicSysOutDiscards = _IpxBasicSysOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 15),
    _IpxBasicSysOutDiscards_Type()
)
ipxBasicSysOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutDiscards.setStatus("mandatory")
_IpxBasicSysOutPackets_Type = Counter32
_IpxBasicSysOutPackets_Object = MibTableColumn
ipxBasicSysOutPackets = _IpxBasicSysOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 16),
    _IpxBasicSysOutPackets_Type()
)
ipxBasicSysOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutPackets.setStatus("mandatory")
_IpxBasicSysConfigSockets_Type = Integer32
_IpxBasicSysConfigSockets_Object = MibTableColumn
ipxBasicSysConfigSockets = _IpxBasicSysConfigSockets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 17),
    _IpxBasicSysConfigSockets_Type()
)
ipxBasicSysConfigSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysConfigSockets.setStatus("mandatory")
_IpxBasicSysOpenSocketFails_Type = Counter32
_IpxBasicSysOpenSocketFails_Object = MibTableColumn
ipxBasicSysOpenSocketFails = _IpxBasicSysOpenSocketFails_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 18),
    _IpxBasicSysOpenSocketFails_Type()
)
ipxBasicSysOpenSocketFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOpenSocketFails.setStatus("mandatory")
_IpxAdvSysTable_Object = MibTable
ipxAdvSysTable = _IpxAdvSysTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    ipxAdvSysTable.setStatus("mandatory")
_IpxAdvSysEntry_Object = MibTableRow
ipxAdvSysEntry = _IpxAdvSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1)
)
ipxAdvSysEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "ipxAdvSysInstance"),
)
if mibBuilder.loadTexts:
    ipxAdvSysEntry.setStatus("mandatory")
_IpxAdvSysInstance_Type = Integer32
_IpxAdvSysInstance_Object = MibTableColumn
ipxAdvSysInstance = _IpxAdvSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 1),
    _IpxAdvSysInstance_Type()
)
ipxAdvSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAdvSysInstance.setStatus("mandatory")


class _IpxAdvSysMaxPathSplits_Type(Integer32):
    """Custom type ipxAdvSysMaxPathSplits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IpxAdvSysMaxPathSplits_Type.__name__ = "Integer32"
_IpxAdvSysMaxPathSplits_Object = MibTableColumn
ipxAdvSysMaxPathSplits = _IpxAdvSysMaxPathSplits_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 2),
    _IpxAdvSysMaxPathSplits_Type()
)
ipxAdvSysMaxPathSplits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAdvSysMaxPathSplits.setStatus("mandatory")


class _IpxAdvSysMaxHops_Type(Integer32):
    """Custom type ipxAdvSysMaxHops based on Integer32"""
    defaultValue = 64


_IpxAdvSysMaxHops_Object = MibTableColumn
ipxAdvSysMaxHops = _IpxAdvSysMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 3),
    _IpxAdvSysMaxHops_Type()
)
ipxAdvSysMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAdvSysMaxHops.setStatus("mandatory")
_IpxAdvSysTooManyHops_Type = Counter32
_IpxAdvSysTooManyHops_Object = MibTableColumn
ipxAdvSysTooManyHops = _IpxAdvSysTooManyHops_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 4),
    _IpxAdvSysTooManyHops_Type()
)
ipxAdvSysTooManyHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysTooManyHops.setStatus("mandatory")
_IpxAdvSysInFiltered_Type = Counter32
_IpxAdvSysInFiltered_Object = MibTableColumn
ipxAdvSysInFiltered = _IpxAdvSysInFiltered_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 5),
    _IpxAdvSysInFiltered_Type()
)
ipxAdvSysInFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysInFiltered.setStatus("mandatory")
_IpxAdvSysCompressDiscards_Type = Counter32
_IpxAdvSysCompressDiscards_Object = MibTableColumn
ipxAdvSysCompressDiscards = _IpxAdvSysCompressDiscards_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 6),
    _IpxAdvSysCompressDiscards_Type()
)
ipxAdvSysCompressDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysCompressDiscards.setStatus("mandatory")
_IpxAdvSysNETBIOSPackets_Type = Counter32
_IpxAdvSysNETBIOSPackets_Object = MibTableColumn
ipxAdvSysNETBIOSPackets = _IpxAdvSysNETBIOSPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 7),
    _IpxAdvSysNETBIOSPackets_Type()
)
ipxAdvSysNETBIOSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysNETBIOSPackets.setStatus("mandatory")
_IpxAdvSysForwPackets_Type = Counter32
_IpxAdvSysForwPackets_Object = MibTableColumn
ipxAdvSysForwPackets = _IpxAdvSysForwPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 8),
    _IpxAdvSysForwPackets_Type()
)
ipxAdvSysForwPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysForwPackets.setStatus("mandatory")
_IpxAdvSysOutFiltered_Type = Counter32
_IpxAdvSysOutFiltered_Object = MibTableColumn
ipxAdvSysOutFiltered = _IpxAdvSysOutFiltered_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 9),
    _IpxAdvSysOutFiltered_Type()
)
ipxAdvSysOutFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysOutFiltered.setStatus("mandatory")
_IpxAdvSysOutCompressDiscards_Type = Counter32
_IpxAdvSysOutCompressDiscards_Object = MibTableColumn
ipxAdvSysOutCompressDiscards = _IpxAdvSysOutCompressDiscards_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 10),
    _IpxAdvSysOutCompressDiscards_Type()
)
ipxAdvSysOutCompressDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysOutCompressDiscards.setStatus("mandatory")
_IpxAdvSysCircCount_Type = Counter32
_IpxAdvSysCircCount_Object = MibTableColumn
ipxAdvSysCircCount = _IpxAdvSysCircCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 11),
    _IpxAdvSysCircCount_Type()
)
ipxAdvSysCircCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysCircCount.setStatus("mandatory")
_IpxAdvSysDestCount_Type = Counter32
_IpxAdvSysDestCount_Object = MibTableColumn
ipxAdvSysDestCount = _IpxAdvSysDestCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 12),
    _IpxAdvSysDestCount_Type()
)
ipxAdvSysDestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysDestCount.setStatus("mandatory")
_IpxAdvSysServCount_Type = Counter32
_IpxAdvSysServCount_Object = MibTableColumn
ipxAdvSysServCount = _IpxAdvSysServCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 13),
    _IpxAdvSysServCount_Type()
)
ipxAdvSysServCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysServCount.setStatus("mandatory")
_IpxCircuit_ObjectIdentity = ObjectIdentity
ipxCircuit = _IpxCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2)
)
_IpxForwarding_ObjectIdentity = ObjectIdentity
ipxForwarding = _IpxForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3)
)
_IpxServices_ObjectIdentity = ObjectIdentity
ipxServices = _IpxServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4)
)
_IpxTraps_ObjectIdentity = ObjectIdentity
ipxTraps = _IpxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 5)
)
_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1)
)
_TerminalServer_ObjectIdentity = ObjectIdentity
terminalServer = _TerminalServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1)
)
_DedicatedBridgeServer_ObjectIdentity = ObjectIdentity
dedicatedBridgeServer = _DedicatedBridgeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 2)
)
_DedicatedRouteServer_ObjectIdentity = ObjectIdentity
dedicatedRouteServer = _DedicatedRouteServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 3)
)
_Brouter_ObjectIdentity = ObjectIdentity
brouter = _Brouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4)
)
_GenericMSWorkstation_ObjectIdentity = ObjectIdentity
genericMSWorkstation = _GenericMSWorkstation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 5)
)
_GenericMSServer_ObjectIdentity = ObjectIdentity
genericMSServer = _GenericMSServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 6)
)
_GenericUnixServer_ObjectIdentity = ObjectIdentity
genericUnixServer = _GenericUnixServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 7)
)
_Hub_ObjectIdentity = ObjectIdentity
hub = _Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8)
)
_LinkBuilder3GH_ObjectIdentity = ObjectIdentity
linkBuilder3GH = _LinkBuilder3GH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 1)
)
_LinkBuilder10BTi_ObjectIdentity = ObjectIdentity
linkBuilder10BTi = _LinkBuilder10BTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 2)
)
_LinkBuilderECS_ObjectIdentity = ObjectIdentity
linkBuilderECS = _LinkBuilderECS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 3)
)
_LinkBuilderMSH_ObjectIdentity = ObjectIdentity
linkBuilderMSH = _LinkBuilderMSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4)
)
_Misc_ObjectIdentity = ObjectIdentity
misc = _Misc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1)
)


class _TempSensorOutput_Type(Integer32):
    """Custom type tempSensorOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("danger", 3),
          ("ok", 1),
          ("warm", 2))
    )


_TempSensorOutput_Type.__name__ = "Integer32"
_TempSensorOutput_Object = MibScalar
tempSensorOutput = _TempSensorOutput_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 1),
    _TempSensorOutput_Type()
)
tempSensorOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorOutput.setStatus("mandatory")
_StatusInputTable_Object = MibTable
statusInputTable = _StatusInputTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 2)
)
if mibBuilder.loadTexts:
    statusInputTable.setStatus("mandatory")
_StatusInputTableEntry_Object = MibTableRow
statusInputTableEntry = _StatusInputTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 2, 1)
)
statusInputTableEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "statusInputIndex"),
)
if mibBuilder.loadTexts:
    statusInputTableEntry.setStatus("mandatory")
_StatusInputIndex_Type = Integer32
_StatusInputIndex_Object = MibTableColumn
statusInputIndex = _StatusInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 2, 1, 1),
    _StatusInputIndex_Type()
)
statusInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusInputIndex.setStatus("mandatory")


class _StatusInputState_Type(Integer32):
    """Custom type statusInputState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_StatusInputState_Type.__name__ = "Integer32"
_StatusInputState_Object = MibTableColumn
statusInputState = _StatusInputState_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 2, 1, 2),
    _StatusInputState_Type()
)
statusInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusInputState.setStatus("mandatory")


class _StatusTrapEnable_Type(Integer32):
    """Custom type statusTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_StatusTrapEnable_Type.__name__ = "Integer32"
_StatusTrapEnable_Object = MibTableColumn
statusTrapEnable = _StatusTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 2, 1, 3),
    _StatusTrapEnable_Type()
)
statusTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statusTrapEnable.setStatus("mandatory")
_StatusName_Type = DisplayString
_StatusName_Object = MibTableColumn
statusName = _StatusName_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 2, 1, 4),
    _StatusName_Type()
)
statusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statusName.setStatus("mandatory")
_ChassisMgmtMACTable_Object = MibTable
chassisMgmtMACTable = _ChassisMgmtMACTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 3)
)
if mibBuilder.loadTexts:
    chassisMgmtMACTable.setStatus("mandatory")
_ChassisMgmtMACEntry_Object = MibTableRow
chassisMgmtMACEntry = _ChassisMgmtMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 3, 1)
)
chassisMgmtMACEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "macSlotNumber"),
    (0, "LBHUB-MSH-MIB", "macIndex"),
)
if mibBuilder.loadTexts:
    chassisMgmtMACEntry.setStatus("mandatory")
_MacSlotNumber_Type = Integer32
_MacSlotNumber_Object = MibTableColumn
macSlotNumber = _MacSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 3, 1, 1),
    _MacSlotNumber_Type()
)
macSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macSlotNumber.setStatus("mandatory")
_MacIndex_Type = Integer32
_MacIndex_Object = MibTableColumn
macIndex = _MacIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 3, 1, 2),
    _MacIndex_Type()
)
macIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macIndex.setStatus("mandatory")


class _MacBroadcastAvailable_Type(Integer32):
    """Custom type macBroadcastAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MacBroadcastAvailable_Type.__name__ = "Integer32"
_MacBroadcastAvailable_Object = MibTableColumn
macBroadcastAvailable = _MacBroadcastAvailable_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 3, 1, 3),
    _MacBroadcastAvailable_Type()
)
macBroadcastAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macBroadcastAvailable.setStatus("mandatory")


class _MacLSAPFiltering_Type(Integer32):
    """Custom type macLSAPFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MacLSAPFiltering_Type.__name__ = "Integer32"
_MacLSAPFiltering_Object = MibTableColumn
macLSAPFiltering = _MacLSAPFiltering_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 3, 1, 4),
    _MacLSAPFiltering_Type()
)
macLSAPFiltering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macLSAPFiltering.setStatus("mandatory")
_MacTypeFiltering_Type = Integer32
_MacTypeFiltering_Object = MibTableColumn
macTypeFiltering = _MacTypeFiltering_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 3, 1, 5),
    _MacTypeFiltering_Type()
)
macTypeFiltering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macTypeFiltering.setStatus("mandatory")
_MacMaxPDUsize_Type = Integer32
_MacMaxPDUsize_Object = MibTableColumn
macMaxPDUsize = _MacMaxPDUsize_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 3, 1, 6),
    _MacMaxPDUsize_Type()
)
macMaxPDUsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macMaxPDUsize.setStatus("mandatory")
_MacPhyAddress_Type = OctetString
_MacPhyAddress_Object = MibTableColumn
macPhyAddress = _MacPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 3, 1, 7),
    _MacPhyAddress_Type()
)
macPhyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macPhyAddress.setStatus("mandatory")


class _MacStatus_Type(Integer32):
    """Custom type macStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("snmpMac", 3),
          ("unavailable", 2))
    )


_MacStatus_Type.__name__ = "Integer32"
_MacStatus_Object = MibTableColumn
macStatus = _MacStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 3, 1, 8),
    _MacStatus_Type()
)
macStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macStatus.setStatus("mandatory")
_ChassisLedTable_Object = MibTable
chassisLedTable = _ChassisLedTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 4)
)
if mibBuilder.loadTexts:
    chassisLedTable.setStatus("mandatory")
_ChassisLedEntry_Object = MibTableRow
chassisLedEntry = _ChassisLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 4, 1)
)
chassisLedEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "chassisSlotNumber"),
)
if mibBuilder.loadTexts:
    chassisLedEntry.setStatus("mandatory")
_ChassisSlotNumber_Type = Integer32
_ChassisSlotNumber_Object = MibTableColumn
chassisSlotNumber = _ChassisSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 4, 1, 1),
    _ChassisSlotNumber_Type()
)
chassisSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlotNumber.setStatus("mandatory")


class _ChassisLedColour_Type(Integer32):
    """Custom type chassisLedColour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 2),
          ("off", 1),
          ("red", 3))
    )


_ChassisLedColour_Type.__name__ = "Integer32"
_ChassisLedColour_Object = MibTableColumn
chassisLedColour = _ChassisLedColour_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 4, 1, 2),
    _ChassisLedColour_Type()
)
chassisLedColour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisLedColour.setStatus("mandatory")


class _ChassisAttentionState_Type(Integer32):
    """Custom type chassisAttentionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attention", 2),
          ("ok", 1))
    )


_ChassisAttentionState_Type.__name__ = "Integer32"
_ChassisAttentionState_Object = MibTableColumn
chassisAttentionState = _ChassisAttentionState_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 1, 4, 1, 3),
    _ChassisAttentionState_Type()
)
chassisAttentionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisAttentionState.setStatus("mandatory")
_MshFault_ObjectIdentity = ObjectIdentity
mshFault = _MshFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 2)
)


class _MshFaultModifiedFlag_Type(Integer32):
    """Custom type mshFaultModifiedFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean-read", 1),
          ("modified", 2))
    )


_MshFaultModifiedFlag_Type.__name__ = "Integer32"
_MshFaultModifiedFlag_Object = MibScalar
mshFaultModifiedFlag = _MshFaultModifiedFlag_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 2, 1),
    _MshFaultModifiedFlag_Type()
)
mshFaultModifiedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mshFaultModifiedFlag.setStatus("deprecated")
_MshFaultTable_Object = MibTable
mshFaultTable = _MshFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 2, 2)
)
if mibBuilder.loadTexts:
    mshFaultTable.setStatus("deprecated")
_MshFaultEntry_Object = MibTableRow
mshFaultEntry = _MshFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 2, 2, 1)
)
mshFaultEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "mshFaultIndex"),
)
if mibBuilder.loadTexts:
    mshFaultEntry.setStatus("deprecated")
_MshFaultIndex_Type = Integer32
_MshFaultIndex_Object = MibTableColumn
mshFaultIndex = _MshFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 2, 2, 1, 1),
    _MshFaultIndex_Type()
)
mshFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mshFaultIndex.setStatus("deprecated")
_MshFaultErrorNumber_Type = Integer32
_MshFaultErrorNumber_Object = MibTableColumn
mshFaultErrorNumber = _MshFaultErrorNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 2, 2, 1, 2),
    _MshFaultErrorNumber_Type()
)
mshFaultErrorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mshFaultErrorNumber.setStatus("deprecated")
_MshFaultTimeStamp_Type = TimeTicks
_MshFaultTimeStamp_Object = MibTableColumn
mshFaultTimeStamp = _MshFaultTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 2, 2, 1, 3),
    _MshFaultTimeStamp_Type()
)
mshFaultTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mshFaultTimeStamp.setStatus("deprecated")
_MshFaultRestartCount_Type = Integer32
_MshFaultRestartCount_Object = MibTableColumn
mshFaultRestartCount = _MshFaultRestartCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4, 2, 2, 1, 4),
    _MshFaultRestartCount_Type()
)
mshFaultRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mshFaultRestartCount.setStatus("deprecated")
_LinkBuilderFMS_ObjectIdentity = ObjectIdentity
linkBuilderFMS = _LinkBuilderFMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 5)
)
_LinkBuilderFddiWorkGroupHub_ObjectIdentity = ObjectIdentity
linkBuilderFddiWorkGroupHub = _LinkBuilderFddiWorkGroupHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 6)
)
_LinkBuilderFMSII_ObjectIdentity = ObjectIdentity
linkBuilderFMSII = _LinkBuilderFMSII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 7)
)
_LinkSwitchFMS_ObjectIdentity = ObjectIdentity
linkSwitchFMS = _LinkSwitchFMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 8)
)
_LinkSwitchMSH_ObjectIdentity = ObjectIdentity
linkSwitchMSH = _LinkSwitchMSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 9)
)
_LinkBuilderFMSLBridge_ObjectIdentity = ObjectIdentity
linkBuilderFMSLBridge = _LinkBuilderFMSLBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 10)
)
_LinkBuilderTP8i_ObjectIdentity = ObjectIdentity
linkBuilderTP8i = _LinkBuilderTP8i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 11)
)
_Cards_ObjectIdentity = ObjectIdentity
cards = _Cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9)
)
_LinkBuilder3GH_cards_ObjectIdentity = ObjectIdentity
linkBuilder3GH_cards = _LinkBuilder3GH_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 1)
)
_LinkBuilder10BTi_cards_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_cards = _LinkBuilder10BTi_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2)
)
_LinkBuilder10BTi_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_cards_utp = _LinkBuilder10BTi_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2, 1)
)
_LinkBuilder10BT_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilder10BT_cards_utp = _LinkBuilder10BT_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2, 2)
)
_LinkBuilderECS_cards_ObjectIdentity = ObjectIdentity
linkBuilderECS_cards = _LinkBuilderECS_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 3)
)
_LinkBuilderMSH_cards_ObjectIdentity = ObjectIdentity
linkBuilderMSH_cards = _LinkBuilderMSH_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 4)
)
_LinkBuilderFMS_cards_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards = _LinkBuilderFMS_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5)
)
_LinkBuilderFMS_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_utp = _LinkBuilderFMS_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 1)
)
_LinkBuilderFMS_cards_coax_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_coax = _LinkBuilderFMS_cards_coax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 2)
)
_LinkBuilderFMS_cards_fiber_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_fiber = _LinkBuilderFMS_cards_fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 3)
)
_LinkBuilderFMS_cards_12fiber_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_12fiber = _LinkBuilderFMS_cards_12fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 4)
)
_LinkBuilderFMS_cards_24utp_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_24utp = _LinkBuilderFMS_cards_24utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 5)
)
_LinkBuilderFMSII_cards_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards = _LinkBuilderFMSII_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6)
)
_LinkBuilderFMSII_cards_12tp_rj45_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_12tp_rj45 = _LinkBuilderFMSII_cards_12tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 1)
)
_LinkBuilderFMSII_cards_10coax_bnc_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_10coax_bnc = _LinkBuilderFMSII_cards_10coax_bnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 2)
)
_LinkBuilderFMSII_cards_6fiber_st_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_6fiber_st = _LinkBuilderFMSII_cards_6fiber_st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 3)
)
_LinkBuilderFMSII_cards_12fiber_st_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_12fiber_st = _LinkBuilderFMSII_cards_12fiber_st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 4)
)
_LinkBuilderFMSII_cards_24tp_rj45_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_24tp_rj45 = _LinkBuilderFMSII_cards_24tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 5)
)
_LinkBuilderFMSII_cards_24tp_telco_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_24tp_telco = _LinkBuilderFMSII_cards_24tp_telco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 6)
)
_A3C512_ObjectIdentity = ObjectIdentity
a3C512 = _A3C512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 7)
)
_LinkBuilderTP8i_cards_ObjectIdentity = ObjectIdentity
linkBuilderTP8i_cards = _LinkBuilderTP8i_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 8)
)
_LinkBuilderTP8i_cards_8tp_rj45_ObjectIdentity = ObjectIdentity
linkBuilderTP8i_cards_8tp_rj45 = _LinkBuilderTP8i_cards_8tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 8, 1)
)
_Chipsets_ObjectIdentity = ObjectIdentity
chipsets = _Chipsets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 10)
)
_Amp_mib_ObjectIdentity = ObjectIdentity
amp_mib = _Amp_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 3)
)
_GenericTrap_ObjectIdentity = ObjectIdentity
genericTrap = _GenericTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 4)
)
_ViewBuilderApps_ObjectIdentity = ObjectIdentity
viewBuilderApps = _ViewBuilderApps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 5)
)
_SpecificTrap_ObjectIdentity = ObjectIdentity
specificTrap = _SpecificTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 6)
)
_LinkBuilder3GH_mib_ObjectIdentity = ObjectIdentity
linkBuilder3GH_mib = _LinkBuilder3GH_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7)
)
_LinkBuilder10BTi_mib_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_mib = _LinkBuilder10BTi_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8)
)
_LinkBuilderECS_mib_ObjectIdentity = ObjectIdentity
linkBuilderECS_mib = _LinkBuilderECS_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 9)
)
_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10)
)
_GenExperimental_ObjectIdentity = ObjectIdentity
genExperimental = _GenExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1)
)
_TestData_ObjectIdentity = ObjectIdentity
testData = _TestData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 1)
)
_IfExtensions_ObjectIdentity = ObjectIdentity
ifExtensions = _IfExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 2)
)
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 2)
)
_SetupGeneral_ObjectIdentity = ObjectIdentity
setupGeneral = _SetupGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 1)
)


class _HeartbeatInterval_Type(Integer32):
    """Custom type heartbeatInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HeartbeatInterval_Type.__name__ = "Integer32"
_HeartbeatInterval_Object = MibScalar
heartbeatInterval = _HeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 1, 1),
    _HeartbeatInterval_Type()
)
heartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heartbeatInterval.setStatus("mandatory")
_SetupIp_ObjectIdentity = ObjectIdentity
setupIp = _SetupIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 2)
)
_SetIpIfTable_Object = MibTable
setIpIfTable = _SetIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 2, 1)
)
if mibBuilder.loadTexts:
    setIpIfTable.setStatus("mandatory")
_SetIpIfEntry_Object = MibTableRow
setIpIfEntry = _SetIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 2, 1, 1)
)
setIpIfEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "setIpIfIndex"),
)
if mibBuilder.loadTexts:
    setIpIfEntry.setStatus("mandatory")
_SetIpIfIndex_Type = Integer32
_SetIpIfIndex_Object = MibTableColumn
setIpIfIndex = _SetIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 2, 1, 1, 1),
    _SetIpIfIndex_Type()
)
setIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIpIfIndex.setStatus("mandatory")
_SetIpIfAddr_Type = IpAddress
_SetIpIfAddr_Object = MibTableColumn
setIpIfAddr = _SetIpIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 2, 1, 1, 2),
    _SetIpIfAddr_Type()
)
setIpIfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpIfAddr.setStatus("mandatory")
_SetIpIfMask_Type = IpAddress
_SetIpIfMask_Object = MibTableColumn
setIpIfMask = _SetIpIfMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 2, 1, 1, 3),
    _SetIpIfMask_Type()
)
setIpIfMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpIfMask.setStatus("mandatory")
_SetIpIfRouter_Type = IpAddress
_SetIpIfRouter_Object = MibScalar
setIpIfRouter = _SetIpIfRouter_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 2, 2),
    _SetIpIfRouter_Type()
)
setIpIfRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpIfRouter.setStatus("mandatory")
_SetupStart_ObjectIdentity = ObjectIdentity
setupStart = _SetupStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 3)
)


class _StartPROMSwVerNo_Type(DisplayString):
    """Custom type startPROMSwVerNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_StartPROMSwVerNo_Type.__name__ = "DisplayString"
_StartPROMSwVerNo_Object = MibScalar
startPROMSwVerNo = _StartPROMSwVerNo_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 3, 1),
    _StartPROMSwVerNo_Type()
)
startPROMSwVerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startPROMSwVerNo.setStatus("mandatory")
_StartRestartCount_Type = Counter32
_StartRestartCount_Object = MibScalar
startRestartCount = _StartRestartCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 3, 2),
    _StartRestartCount_Type()
)
startRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startRestartCount.setStatus("mandatory")


class _StartLastRestartType_Type(Integer32):
    """Custom type startLastRestartType based on Integer32"""
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
        *(("command", 2),
          ("other", 1),
          ("power-reset", 4),
          ("system-error", 5),
          ("watchdog", 3))
    )


_StartLastRestartType_Type.__name__ = "Integer32"
_StartLastRestartType_Object = MibScalar
startLastRestartType = _StartLastRestartType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 3, 3),
    _StartLastRestartType_Type()
)
startLastRestartType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startLastRestartType.setStatus("mandatory")


class _StartResetAction_Type(Integer32):
    """Custom type startResetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manDefaultReset", 2),
          ("nochange", 1))
    )


_StartResetAction_Type.__name__ = "Integer32"
_StartResetAction_Object = MibScalar
startResetAction = _StartResetAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 3, 4),
    _StartResetAction_Type()
)
startResetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startResetAction.setStatus("mandatory")
_StartLastSystemError_Type = Integer32
_StartLastSystemError_Object = MibScalar
startLastSystemError = _StartLastSystemError_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 3, 5),
    _StartLastSystemError_Type()
)
startLastSystemError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startLastSystemError.setStatus("mandatory")


class _StartRestartAction_Type(Integer32):
    """Custom type startRestartAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nochange", 1),
          ("restart", 2))
    )


_StartRestartAction_Type.__name__ = "Integer32"
_StartRestartAction_Object = MibScalar
startRestartAction = _StartRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 3, 6),
    _StartRestartAction_Type()
)
startRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startRestartAction.setStatus("mandatory")
_SystemConfigChangeTime_Type = TimeTicks
_SystemConfigChangeTime_Object = MibScalar
systemConfigChangeTime = _SystemConfigChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 4),
    _SystemConfigChangeTime_Type()
)
systemConfigChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigChangeTime.setStatus("mandatory")
_SysLoader_ObjectIdentity = ObjectIdentity
sysLoader = _SysLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 3)
)
_LoadableDeviceTable_Object = MibTable
loadableDeviceTable = _LoadableDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1)
)
if mibBuilder.loadTexts:
    loadableDeviceTable.setStatus("mandatory")
_LoadableDeviceEntry_Object = MibTableRow
loadableDeviceEntry = _LoadableDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1)
)
loadableDeviceEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "slDeviceType"),
    (0, "LBHUB-MSH-MIB", "slDeviceInstance"),
)
if mibBuilder.loadTexts:
    loadableDeviceEntry.setStatus("mandatory")


class _SlDeviceType_Type(Integer32):
    """Custom type slDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("component", 2),
          ("system", 1))
    )


_SlDeviceType_Type.__name__ = "Integer32"
_SlDeviceType_Object = MibTableColumn
slDeviceType = _SlDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 1),
    _SlDeviceType_Type()
)
slDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slDeviceType.setStatus("mandatory")
_SlDeviceInstance_Type = Integer32
_SlDeviceInstance_Object = MibTableColumn
slDeviceInstance = _SlDeviceInstance_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 2),
    _SlDeviceInstance_Type()
)
slDeviceInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slDeviceInstance.setStatus("mandatory")


class _SlLoadStatus_Type(Integer32):
    """Custom type slLoadStatus based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
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
              200,
              201,
              202,
              203,
              204,
              205,
              255)
        )
    )
    namedValues = NamedValues(
        *(("accessViolation", 2),
          ("byteCountError", 16),
          ("checksumError", 12),
          ("eraseFailed", 18),
          ("fileNotFound", 1),
          ("illegalOperation", 4),
          ("invalidProgAddress", 17),
          ("invalidRecType", 11),
          ("loadActive", 21),
          ("loadPending", 20),
          ("modBusy", 203),
          ("modChecksumError", 201),
          ("modFailure", 255),
          ("modInvalidAdress", 200),
          ("modNoResource", 205),
          ("modRemoved", 204),
          ("modTimeout", 202),
          ("noFileHeader", 15),
          ("noResource", 9),
          ("noResponse", 8),
          ("noSuchUser", 7),
          ("paused", 23),
          ("progFailed", 19),
          ("recLenMismatch", 10),
          ("success", 22),
          ("unknownTransferID", 5),
          ("wrongDevice", 13),
          ("wrongHardwareVersion", 14))
    )


_SlLoadStatus_Type.__name__ = "Integer32"
_SlLoadStatus_Object = MibTableColumn
slLoadStatus = _SlLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 3),
    _SlLoadStatus_Type()
)
slLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slLoadStatus.setStatus("mandatory")


class _SlSoftwareVersion_Type(DisplayString):
    """Custom type slSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlSoftwareVersion_Type.__name__ = "DisplayString"
_SlSoftwareVersion_Object = MibTableColumn
slSoftwareVersion = _SlSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 4),
    _SlSoftwareVersion_Type()
)
slSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSoftwareVersion.setStatus("mandatory")
_SlHardwareVersion_Type = Integer32
_SlHardwareVersion_Object = MibTableColumn
slHardwareVersion = _SlHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 5),
    _SlHardwareVersion_Type()
)
slHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slHardwareVersion.setStatus("mandatory")


class _SlFilename_Type(DisplayString):
    """Custom type slFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SlFilename_Type.__name__ = "DisplayString"
_SlFilename_Object = MibTableColumn
slFilename = _SlFilename_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 6),
    _SlFilename_Type()
)
slFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slFilename.setStatus("mandatory")


class _SlServerIpAddress_Type(IpAddress):
    """Custom type slServerIpAddress based on IpAddress"""
    defaultValue = 0


_SlServerIpAddress_Object = MibTableColumn
slServerIpAddress = _SlServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 7),
    _SlServerIpAddress_Type()
)
slServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slServerIpAddress.setStatus("deprecated")


class _SlLoad_Type(Integer32):
    """Custom type slLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("startDownload", 2))
    )


_SlLoad_Type.__name__ = "Integer32"
_SlLoad_Object = MibTableColumn
slLoad = _SlLoad_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 8),
    _SlLoad_Type()
)
slLoad.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    slLoad.setStatus("mandatory")


class _SlServerAddress_Type(DisplayString):
    """Custom type slServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SlServerAddress_Type.__name__ = "DisplayString"
_SlServerAddress_Object = MibTableColumn
slServerAddress = _SlServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 9),
    _SlServerAddress_Type()
)
slServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slServerAddress.setStatus("mandatory")


class _SlServerProtocol_Type(Integer32):
    """Custom type slServerProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tftp-ip", 2),
          ("tftp-ipx", 3),
          ("unknown", 1))
    )


_SlServerProtocol_Type.__name__ = "Integer32"
_SlServerProtocol_Object = MibTableColumn
slServerProtocol = _SlServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 10),
    _SlServerProtocol_Type()
)
slServerProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slServerProtocol.setStatus("mandatory")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 4)
)
_SecurityEnableTable_Object = MibTable
securityEnableTable = _SecurityEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 1)
)
if mibBuilder.loadTexts:
    securityEnableTable.setStatus("mandatory")
_SecurityEnableTableEntry_Object = MibTableRow
securityEnableTableEntry = _SecurityEnableTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 1, 1)
)
securityEnableTableEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "securityLevel"),
)
if mibBuilder.loadTexts:
    securityEnableTableEntry.setStatus("mandatory")


class _SecurityLevel_Type(Integer32):
    """Custom type securityLevel based on Integer32"""
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
        *(("manager", 3),
          ("monitor", 1),
          ("secureMonitor", 2),
          ("security", 5),
          ("specialist", 4))
    )


_SecurityLevel_Type.__name__ = "Integer32"
_SecurityLevel_Object = MibTableColumn
securityLevel = _SecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 1, 1, 1),
    _SecurityLevel_Type()
)
securityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityLevel.setStatus("mandatory")


class _SecurityCommunityEnable_Type(Integer32):
    """Custom type securityCommunityEnable based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("permanentlyDisabled", 4),
          ("permanentlyEnabled", 3))
    )


_SecurityCommunityEnable_Type.__name__ = "Integer32"
_SecurityCommunityEnable_Object = MibTableColumn
securityCommunityEnable = _SecurityCommunityEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 1, 1, 2),
    _SecurityCommunityEnable_Type()
)
securityCommunityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityCommunityEnable.setStatus("mandatory")


class _SecuritySecureEnable_Type(Integer32):
    """Custom type securitySecureEnable based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("permanentlyDisabled", 4),
          ("permanentlyEnabled", 3))
    )


_SecuritySecureEnable_Type.__name__ = "Integer32"
_SecuritySecureEnable_Object = MibTableColumn
securitySecureEnable = _SecuritySecureEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 1, 1, 3),
    _SecuritySecureEnable_Type()
)
securitySecureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securitySecureEnable.setStatus("mandatory")


class _SecurityTermEnable_Type(Integer32):
    """Custom type securityTermEnable based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("permanentlyDisabled", 4),
          ("permanentlyEnabled", 3))
    )


_SecurityTermEnable_Type.__name__ = "Integer32"
_SecurityTermEnable_Object = MibTableColumn
securityTermEnable = _SecurityTermEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 1, 1, 4),
    _SecurityTermEnable_Type()
)
securityTermEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityTermEnable.setStatus("mandatory")


class _SecurityTelnetEnable_Type(Integer32):
    """Custom type securityTelnetEnable based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("permanentlyDisabled", 4),
          ("permanentlyEnabled", 3))
    )


_SecurityTelnetEnable_Type.__name__ = "Integer32"
_SecurityTelnetEnable_Object = MibTableColumn
securityTelnetEnable = _SecurityTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 1, 1, 5),
    _SecurityTelnetEnable_Type()
)
securityTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityTelnetEnable.setStatus("mandatory")


class _SecurityFrontPanelEnable_Type(Integer32):
    """Custom type securityFrontPanelEnable based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("permanentlyDisabled", 4),
          ("permanentlyEnabled", 3))
    )


_SecurityFrontPanelEnable_Type.__name__ = "Integer32"
_SecurityFrontPanelEnable_Object = MibTableColumn
securityFrontPanelEnable = _SecurityFrontPanelEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 1, 1, 6),
    _SecurityFrontPanelEnable_Type()
)
securityFrontPanelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityFrontPanelEnable.setStatus("mandatory")
_SecurityUserTable_Object = MibTable
securityUserTable = _SecurityUserTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2)
)
if mibBuilder.loadTexts:
    securityUserTable.setStatus("mandatory")
_SecurityUserTableEntry_Object = MibTableRow
securityUserTableEntry = _SecurityUserTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2, 1)
)
securityUserTableEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "securityUserName"),
)
if mibBuilder.loadTexts:
    securityUserTableEntry.setStatus("mandatory")


class _SecurityUserStatus_Type(Integer32):
    """Custom type securityUserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SecurityUserStatus_Type.__name__ = "Integer32"
_SecurityUserStatus_Object = MibTableColumn
securityUserStatus = _SecurityUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2, 1, 1),
    _SecurityUserStatus_Type()
)
securityUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityUserStatus.setStatus("mandatory")


class _SecurityUserName_Type(DisplayString):
    """Custom type securityUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SecurityUserName_Type.__name__ = "DisplayString"
_SecurityUserName_Object = MibTableColumn
securityUserName = _SecurityUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2, 1, 2),
    _SecurityUserName_Type()
)
securityUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityUserName.setStatus("mandatory")


class _SecurityUserLevel_Type(Integer32):
    """Custom type securityUserLevel based on Integer32"""
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
        *(("manager", 3),
          ("monitor", 1),
          ("secureMonitor", 2),
          ("security", 5),
          ("specialist", 4))
    )


_SecurityUserLevel_Type.__name__ = "Integer32"
_SecurityUserLevel_Object = MibTableColumn
securityUserLevel = _SecurityUserLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2, 1, 3),
    _SecurityUserLevel_Type()
)
securityUserLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityUserLevel.setStatus("mandatory")


class _SecurityUserPassword_Type(DisplayString):
    """Custom type securityUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SecurityUserPassword_Type.__name__ = "DisplayString"
_SecurityUserPassword_Object = MibTableColumn
securityUserPassword = _SecurityUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2, 1, 4),
    _SecurityUserPassword_Type()
)
securityUserPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    securityUserPassword.setStatus("mandatory")


class _SecurityUserCommunity_Type(DisplayString):
    """Custom type securityUserCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SecurityUserCommunity_Type.__name__ = "DisplayString"
_SecurityUserCommunity_Object = MibTableColumn
securityUserCommunity = _SecurityUserCommunity_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2, 1, 5),
    _SecurityUserCommunity_Type()
)
securityUserCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityUserCommunity.setStatus("mandatory")
_SecurityUserLocParty_Type = ObjectIdentifier
_SecurityUserLocParty_Object = MibTableColumn
securityUserLocParty = _SecurityUserLocParty_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2, 1, 6),
    _SecurityUserLocParty_Type()
)
securityUserLocParty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityUserLocParty.setStatus("mandatory")
_SecurityUserMgrParty_Type = ObjectIdentifier
_SecurityUserMgrParty_Object = MibTableColumn
securityUserMgrParty = _SecurityUserMgrParty_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2, 1, 7),
    _SecurityUserMgrParty_Type()
)
securityUserMgrParty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityUserMgrParty.setStatus("mandatory")
_SecurityAuditLogTable_Object = MibTable
securityAuditLogTable = _SecurityAuditLogTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 3)
)
if mibBuilder.loadTexts:
    securityAuditLogTable.setStatus("mandatory")
_SecurityAuditLogEntry_Object = MibTableRow
securityAuditLogEntry = _SecurityAuditLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 3, 1)
)
securityAuditLogEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "securityAuditIndex"),
)
if mibBuilder.loadTexts:
    securityAuditLogEntry.setStatus("mandatory")


class _SecurityAuditIndex_Type(Integer32):
    """Custom type securityAuditIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SecurityAuditIndex_Type.__name__ = "Integer32"
_SecurityAuditIndex_Object = MibTableColumn
securityAuditIndex = _SecurityAuditIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 3, 1, 1),
    _SecurityAuditIndex_Type()
)
securityAuditIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityAuditIndex.setStatus("mandatory")
_SecurityAuditTime_Type = TimeTicks
_SecurityAuditTime_Object = MibTableColumn
securityAuditTime = _SecurityAuditTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 3, 1, 2),
    _SecurityAuditTime_Type()
)
securityAuditTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityAuditTime.setStatus("mandatory")


class _SecurityAuditUser_Type(DisplayString):
    """Custom type securityAuditUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SecurityAuditUser_Type.__name__ = "DisplayString"
_SecurityAuditUser_Object = MibTableColumn
securityAuditUser = _SecurityAuditUser_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 3, 1, 3),
    _SecurityAuditUser_Type()
)
securityAuditUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityAuditUser.setStatus("mandatory")
_SecurityAuditObject_Type = ObjectIdentifier
_SecurityAuditObject_Object = MibTableColumn
securityAuditObject = _SecurityAuditObject_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 3, 1, 4),
    _SecurityAuditObject_Type()
)
securityAuditObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityAuditObject.setStatus("mandatory")


class _SecurityAuditValue_Type(OctetString):
    """Custom type securityAuditValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_SecurityAuditValue_Type.__name__ = "OctetString"
_SecurityAuditValue_Object = MibTableColumn
securityAuditValue = _SecurityAuditValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 3, 1, 5),
    _SecurityAuditValue_Type()
)
securityAuditValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityAuditValue.setStatus("mandatory")


class _SecurityAuditResult_Type(Integer32):
    """Custom type securityAuditResult based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("locked", 4),
          ("no-such-function", 6),
          ("no-such-item", 7),
          ("pending", 1),
          ("security-violation", 5),
          ("success", 255),
          ("too-big", 2))
    )


_SecurityAuditResult_Type.__name__ = "Integer32"
_SecurityAuditResult_Object = MibTableColumn
securityAuditResult = _SecurityAuditResult_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 3, 1, 6),
    _SecurityAuditResult_Type()
)
securityAuditResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityAuditResult.setStatus("mandatory")
_Gauges_ObjectIdentity = ObjectIdentity
gauges = _Gauges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 5)
)
_GaugeTable_Object = MibTable
gaugeTable = _GaugeTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1)
)
if mibBuilder.loadTexts:
    gaugeTable.setStatus("mandatory")
_GaugeTableEntry_Object = MibTableRow
gaugeTableEntry = _GaugeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1)
)
gaugeTableEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "gaugeIndex"),
)
if mibBuilder.loadTexts:
    gaugeTableEntry.setStatus("mandatory")
_GaugeIndex_Type = Integer32
_GaugeIndex_Object = MibTableColumn
gaugeIndex = _GaugeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 1),
    _GaugeIndex_Type()
)
gaugeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gaugeIndex.setStatus("mandatory")
_GaugeItemId_Type = ObjectIdentifier
_GaugeItemId_Object = MibTableColumn
gaugeItemId = _GaugeItemId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 2),
    _GaugeItemId_Type()
)
gaugeItemId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeItemId.setStatus("mandatory")


class _GaugeItemType_Type(Integer32):
    """Custom type gaugeItemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("counter", 1),
          ("signedMeter", 2),
          ("unsignedMeter", 3))
    )


_GaugeItemType_Type.__name__ = "Integer32"
_GaugeItemType_Object = MibTableColumn
gaugeItemType = _GaugeItemType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 3),
    _GaugeItemType_Type()
)
gaugeItemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeItemType.setStatus("mandatory")


class _GaugeSamplesPerAverage_Type(Integer32):
    """Custom type gaugeSamplesPerAverage based on Integer32"""
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
        *(("maxSamples", 4),
          ("nonAveraging", 1),
          ("threeSamples", 3),
          ("twoSamples", 2))
    )


_GaugeSamplesPerAverage_Type.__name__ = "Integer32"
_GaugeSamplesPerAverage_Object = MibTableColumn
gaugeSamplesPerAverage = _GaugeSamplesPerAverage_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 4),
    _GaugeSamplesPerAverage_Type()
)
gaugeSamplesPerAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeSamplesPerAverage.setStatus("mandatory")


class _GaugeSamplePeriod_Type(Integer32):
    """Custom type gaugeSamplePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_GaugeSamplePeriod_Type.__name__ = "Integer32"
_GaugeSamplePeriod_Object = MibTableColumn
gaugeSamplePeriod = _GaugeSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 5),
    _GaugeSamplePeriod_Type()
)
gaugeSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeSamplePeriod.setStatus("mandatory")


class _GaugeValue_Type(Integer32):
    """Custom type gaugeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GaugeValue_Type.__name__ = "Integer32"
_GaugeValue_Object = MibTableColumn
gaugeValue = _GaugeValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 6),
    _GaugeValue_Type()
)
gaugeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeValue.setStatus("mandatory")


class _GaugePeakValue_Type(Integer32):
    """Custom type gaugePeakValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GaugePeakValue_Type.__name__ = "Integer32"
_GaugePeakValue_Object = MibTableColumn
gaugePeakValue = _GaugePeakValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 7),
    _GaugePeakValue_Type()
)
gaugePeakValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugePeakValue.setStatus("mandatory")


class _GaugeThresholdLevel_Type(Integer32):
    """Custom type gaugeThresholdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GaugeThresholdLevel_Type.__name__ = "Integer32"
_GaugeThresholdLevel_Object = MibTableColumn
gaugeThresholdLevel = _GaugeThresholdLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 8),
    _GaugeThresholdLevel_Type()
)
gaugeThresholdLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeThresholdLevel.setStatus("mandatory")
_GaugeRecoveryLevel_Type = Integer32
_GaugeRecoveryLevel_Object = MibTableColumn
gaugeRecoveryLevel = _GaugeRecoveryLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 9),
    _GaugeRecoveryLevel_Type()
)
gaugeRecoveryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeRecoveryLevel.setStatus("mandatory")


class _GaugeThresholdAction_Type(Integer32):
    """Custom type gaugeThresholdAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              12,
              13,
              14,
              15,
              18,
              19,
              20,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("blipCardOff", 13),
          ("blipPortOff", 12),
          ("disable", 3),
          ("disableCard", 15),
          ("disablePort", 14),
          ("enable", 4),
          ("noAction", 1),
          ("notifyAndBlipCardOff", 6),
          ("notifyAndBlipPortOff", 5),
          ("notifyAndDisableCard", 9),
          ("notifyAndDisablePort", 8),
          ("notifyAndResilientSwitch", 18),
          ("notifyBandwidthExceeded", 19),
          ("notifyErrorsExceeded", 20),
          ("notifyFilterBridgePort", 23),
          ("notifyPollFailed", 22),
          ("sendTrap", 2))
    )


_GaugeThresholdAction_Type.__name__ = "Integer32"
_GaugeThresholdAction_Object = MibTableColumn
gaugeThresholdAction = _GaugeThresholdAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 10),
    _GaugeThresholdAction_Type()
)
gaugeThresholdAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeThresholdAction.setStatus("mandatory")


class _GaugeRecoveryAction_Type(Integer32):
    """Custom type gaugeRecoveryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10,
              11,
              16,
              17,
              21,
              24)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 4),
          ("enableCard", 17),
          ("enablePort", 16),
          ("noAction", 1),
          ("notifyAndEnableCard", 11),
          ("notifyAndEnablePort", 10),
          ("notifyPollSuccess", 21),
          ("notifyUnfilterBridgePort", 24),
          ("sendTrap", 2))
    )


_GaugeRecoveryAction_Type.__name__ = "Integer32"
_GaugeRecoveryAction_Object = MibTableColumn
gaugeRecoveryAction = _GaugeRecoveryAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 11),
    _GaugeRecoveryAction_Type()
)
gaugeRecoveryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeRecoveryAction.setStatus("mandatory")


class _GaugeState_Type(Integer32):
    """Custom type gaugeState based on Integer32"""
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
        *(("autoCalibrate", 5),
          ("deleted", 4),
          ("off", 3),
          ("onTriggersDisabled", 2),
          ("onTriggersEnabled", 1))
    )


_GaugeState_Type.__name__ = "Integer32"
_GaugeState_Object = MibTableColumn
gaugeState = _GaugeState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 12),
    _GaugeState_Type()
)
gaugeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeState.setStatus("mandatory")
_GaugeOwner_Type = DisplayString
_GaugeOwner_Object = MibTableColumn
gaugeOwner = _GaugeOwner_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 13),
    _GaugeOwner_Type()
)
gaugeOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeOwner.setStatus("mandatory")


class _GaugeTableSize_Type(Integer32):
    """Custom type gaugeTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GaugeTableSize_Type.__name__ = "Integer32"
_GaugeTableSize_Object = MibScalar
gaugeTableSize = _GaugeTableSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 2),
    _GaugeTableSize_Type()
)
gaugeTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gaugeTableSize.setStatus("mandatory")


class _GaugeThresholdLevelScaler_Type(Integer32):
    """Custom type gaugeThresholdLevelScaler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GaugeThresholdLevelScaler_Type.__name__ = "Integer32"
_GaugeThresholdLevelScaler_Object = MibScalar
gaugeThresholdLevelScaler = _GaugeThresholdLevelScaler_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 3),
    _GaugeThresholdLevelScaler_Type()
)
gaugeThresholdLevelScaler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeThresholdLevelScaler.setStatus("mandatory")


class _GaugeRecoveryLevelScaler_Type(Integer32):
    """Custom type gaugeRecoveryLevelScaler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GaugeRecoveryLevelScaler_Type.__name__ = "Integer32"
_GaugeRecoveryLevelScaler_Object = MibScalar
gaugeRecoveryLevelScaler = _GaugeRecoveryLevelScaler_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 4),
    _GaugeRecoveryLevelScaler_Type()
)
gaugeRecoveryLevelScaler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeRecoveryLevelScaler.setStatus("mandatory")


class _GaugeTableUpdate_Type(Integer32):
    """Custom type gaugeTableUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deleteAll", 1)
    )


_GaugeTableUpdate_Type.__name__ = "Integer32"
_GaugeTableUpdate_Object = MibScalar
gaugeTableUpdate = _GaugeTableUpdate_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 5),
    _GaugeTableUpdate_Type()
)
gaugeTableUpdate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gaugeTableUpdate.setStatus("mandatory")
_GaugeConfigureObjId_Type = ObjectIdentifier
_GaugeConfigureObjId_Object = MibScalar
gaugeConfigureObjId = _GaugeConfigureObjId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 6),
    _GaugeConfigureObjId_Type()
)
gaugeConfigureObjId.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gaugeConfigureObjId.setStatus("mandatory")


class _GaugeConfigureColumn_Type(Integer32):
    """Custom type gaugeConfigureColumn based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("gaugeState", 8),
          ("itemType", 1),
          ("recoveryAction", 7),
          ("recoveryLevel", 5),
          ("samplePeriod", 3),
          ("samplesPerAverage", 2),
          ("thresholdAction", 6),
          ("thresholdLevel", 4))
    )


_GaugeConfigureColumn_Type.__name__ = "Integer32"
_GaugeConfigureColumn_Object = MibScalar
gaugeConfigureColumn = _GaugeConfigureColumn_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 7),
    _GaugeConfigureColumn_Type()
)
gaugeConfigureColumn.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gaugeConfigureColumn.setStatus("mandatory")


class _GaugeConfigureValue_Type(Integer32):
    """Custom type gaugeConfigureValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_GaugeConfigureValue_Type.__name__ = "Integer32"
_GaugeConfigureValue_Object = MibScalar
gaugeConfigureValue = _GaugeConfigureValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 8),
    _GaugeConfigureValue_Type()
)
gaugeConfigureValue.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gaugeConfigureValue.setStatus("mandatory")
_GaugeNextFreeIndex_Type = Integer32
_GaugeNextFreeIndex_Object = MibScalar
gaugeNextFreeIndex = _GaugeNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 9),
    _GaugeNextFreeIndex_Type()
)
gaugeNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gaugeNextFreeIndex.setStatus("mandatory")
_AsciiAgent_ObjectIdentity = ObjectIdentity
asciiAgent = _AsciiAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 6)
)
_AscTimeAttemptedLogin_Type = TimeTicks
_AscTimeAttemptedLogin_Object = MibScalar
ascTimeAttemptedLogin = _AscTimeAttemptedLogin_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 6, 1),
    _AscTimeAttemptedLogin_Type()
)
ascTimeAttemptedLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascTimeAttemptedLogin.setStatus("mandatory")


class _AscUserNameForLastAttemptedLogin_Type(DisplayString):
    """Custom type ascUserNameForLastAttemptedLogin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AscUserNameForLastAttemptedLogin_Type.__name__ = "DisplayString"
_AscUserNameForLastAttemptedLogin_Object = MibScalar
ascUserNameForLastAttemptedLogin = _AscUserNameForLastAttemptedLogin_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 6, 2),
    _AscUserNameForLastAttemptedLogin_Type()
)
ascUserNameForLastAttemptedLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascUserNameForLastAttemptedLogin.setStatus("mandatory")


class _AscLoginStatus_Type(Integer32):
    """Custom type ascLoginStatus based on Integer32"""
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
        *(("deniedAccessFromSerialPort", 4),
          ("deniedAccessFromTelnet", 3),
          ("incorrectPasswordFromSerialPort", 8),
          ("incorrectPasswordFromTelnet", 7),
          ("loginOKFromSerialPort", 2),
          ("loginOKFromTelnet", 1),
          ("nologin", 11),
          ("securityViolationFromSerialPort", 10),
          ("securityViolationFromTelnet", 9),
          ("unknownUserFromSerialPort", 6),
          ("unknownUserFromTelnet", 5))
    )


_AscLoginStatus_Type.__name__ = "Integer32"
_AscLoginStatus_Object = MibScalar
ascLoginStatus = _AscLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 6, 3),
    _AscLoginStatus_Type()
)
ascLoginStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascLoginStatus.setStatus("mandatory")


class _AscLocalManagementBanner_Type(DisplayString):
    """Custom type ascLocalManagementBanner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 490),
    )


_AscLocalManagementBanner_Type.__name__ = "DisplayString"
_AscLocalManagementBanner_Object = MibScalar
ascLocalManagementBanner = _AscLocalManagementBanner_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 6, 4),
    _AscLocalManagementBanner_Type()
)
ascLocalManagementBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascLocalManagementBanner.setStatus("mandatory")
_SerialIf_ObjectIdentity = ObjectIdentity
serialIf = _SerialIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 7)
)
_SiSlipPort_Type = Integer32
_SiSlipPort_Object = MibScalar
siSlipPort = _SiSlipPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 1),
    _SiSlipPort_Type()
)
siSlipPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siSlipPort.setStatus("mandatory")
_ConfigV24Table_Object = MibTable
configV24Table = _ConfigV24Table_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2)
)
if mibBuilder.loadTexts:
    configV24Table.setStatus("mandatory")
_ConfigV24Entry_Object = MibTableRow
configV24Entry = _ConfigV24Entry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1)
)
configV24Entry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "configV24PortID"),
)
if mibBuilder.loadTexts:
    configV24Entry.setStatus("mandatory")


class _ConfigV24PortID_Type(Integer32):
    """Custom type configV24PortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ConfigV24PortID_Type.__name__ = "Integer32"
_ConfigV24PortID_Object = MibTableColumn
configV24PortID = _ConfigV24PortID_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 1),
    _ConfigV24PortID_Type()
)
configV24PortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configV24PortID.setStatus("mandatory")


class _ConfigV24ConnType_Type(Integer32):
    """Custom type configV24ConnType based on Integer32"""
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


_ConfigV24ConnType_Type.__name__ = "Integer32"
_ConfigV24ConnType_Object = MibTableColumn
configV24ConnType = _ConfigV24ConnType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 2),
    _ConfigV24ConnType_Type()
)
configV24ConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24ConnType.setStatus("mandatory")


class _ConfigV24AutoConfig_Type(Integer32):
    """Custom type configV24AutoConfig based on Integer32"""
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


_ConfigV24AutoConfig_Type.__name__ = "Integer32"
_ConfigV24AutoConfig_Object = MibTableColumn
configV24AutoConfig = _ConfigV24AutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 3),
    _ConfigV24AutoConfig_Type()
)
configV24AutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24AutoConfig.setStatus("mandatory")


class _ConfigV24Speed_Type(Integer32):
    """Custom type configV24Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 4),
          ("speed19200", 8),
          ("speed2400", 5),
          ("speed38400", 9),
          ("speed4800", 6),
          ("speed9600", 7))
    )


_ConfigV24Speed_Type.__name__ = "Integer32"
_ConfigV24Speed_Object = MibTableColumn
configV24Speed = _ConfigV24Speed_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 4),
    _ConfigV24Speed_Type()
)
configV24Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24Speed.setStatus("mandatory")


class _ConfigV24CharSize_Type(Integer32):
    """Custom type configV24CharSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("size7", 3),
          ("size8", 4))
    )


_ConfigV24CharSize_Type.__name__ = "Integer32"
_ConfigV24CharSize_Object = MibTableColumn
configV24CharSize = _ConfigV24CharSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 5),
    _ConfigV24CharSize_Type()
)
configV24CharSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24CharSize.setStatus("mandatory")


class _ConfigV24StopBits_Type(Integer32):
    """Custom type configV24StopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stopOne", 1),
          ("stopOneDotFive", 2),
          ("stopTwo", 3))
    )


_ConfigV24StopBits_Type.__name__ = "Integer32"
_ConfigV24StopBits_Object = MibTableColumn
configV24StopBits = _ConfigV24StopBits_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 6),
    _ConfigV24StopBits_Type()
)
configV24StopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24StopBits.setStatus("mandatory")


class _ConfigV24Parity_Type(Integer32):
    """Custom type configV24Parity based on Integer32"""
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
        *(("evenParity", 5),
          ("markParity", 3),
          ("noParity", 1),
          ("oddParity", 4),
          ("spaceParity", 2))
    )


_ConfigV24Parity_Type.__name__ = "Integer32"
_ConfigV24Parity_Object = MibTableColumn
configV24Parity = _ConfigV24Parity_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 7),
    _ConfigV24Parity_Type()
)
configV24Parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24Parity.setStatus("mandatory")


class _ConfigV24DSRControl_Type(Integer32):
    """Custom type configV24DSRControl based on Integer32"""
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


_ConfigV24DSRControl_Type.__name__ = "Integer32"
_ConfigV24DSRControl_Object = MibTableColumn
configV24DSRControl = _ConfigV24DSRControl_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 8),
    _ConfigV24DSRControl_Type()
)
configV24DSRControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24DSRControl.setStatus("mandatory")


class _ConfigV24DCDControl_Type(Integer32):
    """Custom type configV24DCDControl based on Integer32"""
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


_ConfigV24DCDControl_Type.__name__ = "Integer32"
_ConfigV24DCDControl_Object = MibTableColumn
configV24DCDControl = _ConfigV24DCDControl_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 9),
    _ConfigV24DCDControl_Type()
)
configV24DCDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24DCDControl.setStatus("mandatory")


class _ConfigV24FlowControl_Type(Integer32):
    """Custom type configV24FlowControl based on Integer32"""
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
        *(("noFlowControl", 1),
          ("rtsCtsFullDplx", 3),
          ("rtsCtsHalfDplx", 4),
          ("xonXoff", 2))
    )


_ConfigV24FlowControl_Type.__name__ = "Integer32"
_ConfigV24FlowControl_Object = MibTableColumn
configV24FlowControl = _ConfigV24FlowControl_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 10),
    _ConfigV24FlowControl_Type()
)
configV24FlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24FlowControl.setStatus("mandatory")


class _ConfigV24Update_Type(Integer32):
    """Custom type configV24Update based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nochange", 1),
          ("update", 2))
    )


_ConfigV24Update_Type.__name__ = "Integer32"
_ConfigV24Update_Object = MibTableColumn
configV24Update = _ConfigV24Update_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 11),
    _ConfigV24Update_Type()
)
configV24Update.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24Update.setStatus("mandatory")
_RepeaterMgmt_ObjectIdentity = ObjectIdentity
repeaterMgmt = _RepeaterMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8)
)
_MrmSecurityPackage_ObjectIdentity = ObjectIdentity
mrmSecurityPackage = _MrmSecurityPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 6)
)
_MrmSecurePortTable_Object = MibTable
mrmSecurePortTable = _MrmSecurePortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 6, 1)
)
if mibBuilder.loadTexts:
    mrmSecurePortTable.setStatus("mandatory")
_MrmSecurePortEntry_Object = MibTableRow
mrmSecurePortEntry = _MrmSecurePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 6, 1, 1)
)
mrmSecurePortEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "mrmSecRepIndex"),
    (0, "LBHUB-MSH-MIB", "mrmSecSlotIndex"),
    (0, "LBHUB-MSH-MIB", "mrmSecPortIndex"),
)
if mibBuilder.loadTexts:
    mrmSecurePortEntry.setStatus("mandatory")
_MrmSecRepIndex_Type = Integer32
_MrmSecRepIndex_Object = MibTableColumn
mrmSecRepIndex = _MrmSecRepIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 6, 1, 1, 1),
    _MrmSecRepIndex_Type()
)
mrmSecRepIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmSecRepIndex.setStatus("mandatory")
_MrmSecSlotIndex_Type = Integer32
_MrmSecSlotIndex_Object = MibTableColumn
mrmSecSlotIndex = _MrmSecSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 6, 1, 1, 2),
    _MrmSecSlotIndex_Type()
)
mrmSecSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmSecSlotIndex.setStatus("mandatory")
_MrmSecPortIndex_Type = Integer32
_MrmSecPortIndex_Object = MibTableColumn
mrmSecPortIndex = _MrmSecPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 6, 1, 1, 3),
    _MrmSecPortIndex_Type()
)
mrmSecPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmSecPortIndex.setStatus("mandatory")


class _MrmSecPortState_Type(Integer32):
    """Custom type mrmSecPortState based on Integer32"""
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
        *(("authorised-station-learnt", 4),
          ("other", 1),
          ("unauthorised-station-port-disabled", 3),
          ("unauthorised-station-seen", 2))
    )


_MrmSecPortState_Type.__name__ = "Integer32"
_MrmSecPortState_Object = MibTableColumn
mrmSecPortState = _MrmSecPortState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 6, 1, 1, 5),
    _MrmSecPortState_Type()
)
mrmSecPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmSecPortState.setStatus("mandatory")


class _MrmSecNTKState_Type(Integer32):
    """Custom type mrmSecNTKState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_MrmSecNTKState_Type.__name__ = "Integer32"
_MrmSecNTKState_Object = MibTableColumn
mrmSecNTKState = _MrmSecNTKState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 6, 1, 1, 6),
    _MrmSecNTKState_Type()
)
mrmSecNTKState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmSecNTKState.setStatus("mandatory")


class _MrmSecBroadcastState_Type(Integer32):
    """Custom type mrmSecBroadcastState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_MrmSecBroadcastState_Type.__name__ = "Integer32"
_MrmSecBroadcastState_Object = MibTableColumn
mrmSecBroadcastState = _MrmSecBroadcastState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 6, 1, 1, 7),
    _MrmSecBroadcastState_Type()
)
mrmSecBroadcastState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmSecBroadcastState.setStatus("mandatory")


class _MrmSecMulticastState_Type(Integer32):
    """Custom type mrmSecMulticastState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_MrmSecMulticastState_Type.__name__ = "Integer32"
_MrmSecMulticastState_Object = MibTableColumn
mrmSecMulticastState = _MrmSecMulticastState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 6, 1, 1, 8),
    _MrmSecMulticastState_Type()
)
mrmSecMulticastState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmSecMulticastState.setStatus("mandatory")


class _MrmSecLearnMode_Type(Integer32):
    """Custom type mrmSecLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("continual", 3),
          ("off", 1),
          ("single", 2))
    )


_MrmSecLearnMode_Type.__name__ = "Integer32"
_MrmSecLearnMode_Object = MibTableColumn
mrmSecLearnMode = _MrmSecLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 6, 1, 1, 9),
    _MrmSecLearnMode_Type()
)
mrmSecLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmSecLearnMode.setStatus("mandatory")


class _MrmSecReportMode_Type(Integer32):
    """Custom type mrmSecReportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnectandreport", 3),
          ("off", 1),
          ("reportonly", 2))
    )


_MrmSecReportMode_Type.__name__ = "Integer32"
_MrmSecReportMode_Object = MibTableColumn
mrmSecReportMode = _MrmSecReportMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 6, 1, 1, 10),
    _MrmSecReportMode_Type()
)
mrmSecReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmSecReportMode.setStatus("mandatory")


class _MrmSecMACAddress_Type(OctetString):
    """Custom type mrmSecMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MrmSecMACAddress_Type.__name__ = "OctetString"
_MrmSecMACAddress_Object = MibTableColumn
mrmSecMACAddress = _MrmSecMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 6, 1, 1, 11),
    _MrmSecMACAddress_Type()
)
mrmSecMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmSecMACAddress.setStatus("mandatory")


class _MrmSecRowStatus_Type(Integer32):
    """Custom type mrmSecRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stable", 2),
          ("under-modification", 1))
    )


_MrmSecRowStatus_Type.__name__ = "Integer32"
_MrmSecRowStatus_Object = MibTableColumn
mrmSecRowStatus = _MrmSecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 6, 1, 1, 12),
    _MrmSecRowStatus_Type()
)
mrmSecRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmSecRowStatus.setStatus("mandatory")
_EndStation_ObjectIdentity = ObjectIdentity
endStation = _EndStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 9)
)


class _EsDatabaseState_Type(Integer32):
    """Custom type esDatabaseState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modified", 2),
          ("noChange", 1))
    )


_EsDatabaseState_Type.__name__ = "Integer32"
_EsDatabaseState_Object = MibScalar
esDatabaseState = _EsDatabaseState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 1),
    _EsDatabaseState_Type()
)
esDatabaseState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esDatabaseState.setStatus("mandatory")


class _EsDatabaseFlush_Type(Integer32):
    """Custom type esDatabaseFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("flush", 1)
    )


_EsDatabaseFlush_Type.__name__ = "Integer32"
_EsDatabaseFlush_Object = MibScalar
esDatabaseFlush = _EsDatabaseFlush_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 2),
    _EsDatabaseFlush_Type()
)
esDatabaseFlush.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    esDatabaseFlush.setStatus("mandatory")
_EsTable_Object = MibTable
esTable = _EsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 3)
)
if mibBuilder.loadTexts:
    esTable.setStatus("mandatory")
_EsTableEntry_Object = MibTableRow
esTableEntry = _EsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 3, 1)
)
esTableEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "esAddrType"),
    (0, "LBHUB-MSH-MIB", "esAddress"),
)
if mibBuilder.loadTexts:
    esTableEntry.setStatus("mandatory")


class _EsAddrType_Type(Integer32):
    """Custom type esAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021", 1),
          ("internet", 2),
          ("ipx", 3))
    )


_EsAddrType_Type.__name__ = "Integer32"
_EsAddrType_Object = MibTableColumn
esAddrType = _EsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 3, 1, 1),
    _EsAddrType_Type()
)
esAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAddrType.setStatus("mandatory")


class _EsAddress_Type(OctetString):
    """Custom type esAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EsAddress_Type.__name__ = "OctetString"
_EsAddress_Object = MibTableColumn
esAddress = _EsAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 3, 1, 2),
    _EsAddress_Type()
)
esAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAddress.setStatus("mandatory")
_EsSlotNumber_Type = Integer32
_EsSlotNumber_Object = MibTableColumn
esSlotNumber = _EsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 3, 1, 3),
    _EsSlotNumber_Type()
)
esSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esSlotNumber.setStatus("mandatory")
_EsPortNumber_Type = Integer32
_EsPortNumber_Object = MibTableColumn
esPortNumber = _EsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 3, 1, 4),
    _EsPortNumber_Type()
)
esPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esPortNumber.setStatus("mandatory")
_EsModTable_Object = MibTable
esModTable = _EsModTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 4)
)
if mibBuilder.loadTexts:
    esModTable.setStatus("mandatory")
_EsModTableEntry_Object = MibTableRow
esModTableEntry = _EsModTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 4, 1)
)
esModTableEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "esModAddrType"),
    (0, "LBHUB-MSH-MIB", "esModAddress"),
)
if mibBuilder.loadTexts:
    esModTableEntry.setStatus("mandatory")


class _EsModAddrType_Type(Integer32):
    """Custom type esModAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021", 1),
          ("internet", 2),
          ("ipx", 3))
    )


_EsModAddrType_Type.__name__ = "Integer32"
_EsModAddrType_Object = MibTableColumn
esModAddrType = _EsModAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 4, 1, 1),
    _EsModAddrType_Type()
)
esModAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModAddrType.setStatus("mandatory")


class _EsModAddress_Type(OctetString):
    """Custom type esModAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EsModAddress_Type.__name__ = "OctetString"
_EsModAddress_Object = MibTableColumn
esModAddress = _EsModAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 4, 1, 2),
    _EsModAddress_Type()
)
esModAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModAddress.setStatus("mandatory")
_EsModSlotNumber_Type = Integer32
_EsModSlotNumber_Object = MibTableColumn
esModSlotNumber = _EsModSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 4, 1, 3),
    _EsModSlotNumber_Type()
)
esModSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModSlotNumber.setStatus("mandatory")
_EsModPortNumber_Type = Integer32
_EsModPortNumber_Object = MibTableColumn
esModPortNumber = _EsModPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 4, 1, 4),
    _EsModPortNumber_Type()
)
esModPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModPortNumber.setStatus("mandatory")
_EsPortAccessTable_Object = MibTable
esPortAccessTable = _EsPortAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 5)
)
if mibBuilder.loadTexts:
    esPortAccessTable.setStatus("mandatory")
_EsPortAccessEntry_Object = MibTableRow
esPortAccessEntry = _EsPortAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 5, 1)
)
esPortAccessEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "ecPortCardNo"),
    (0, "LBHUB-MSH-MIB", "ecPortPortNo"),
    (0, "LBHUB-MSH-MIB", "ecPortIndex"),
)
if mibBuilder.loadTexts:
    esPortAccessEntry.setStatus("mandatory")
_EcPortCardNo_Type = Integer32
_EcPortCardNo_Object = MibTableColumn
ecPortCardNo = _EcPortCardNo_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 5, 1, 2),
    _EcPortCardNo_Type()
)
ecPortCardNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecPortCardNo.setStatus("mandatory")
_EcPortPortNo_Type = Integer32
_EcPortPortNo_Object = MibTableColumn
ecPortPortNo = _EcPortPortNo_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 5, 1, 3),
    _EcPortPortNo_Type()
)
ecPortPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecPortPortNo.setStatus("mandatory")
_EcPortIndex_Type = Integer32
_EcPortIndex_Object = MibTableColumn
ecPortIndex = _EcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 5, 1, 4),
    _EcPortIndex_Type()
)
ecPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecPortIndex.setStatus("mandatory")


class _EcPortAddrType_Type(Integer32):
    """Custom type ecPortAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021", 1),
          ("internet", 2),
          ("ipx", 3))
    )


_EcPortAddrType_Type.__name__ = "Integer32"
_EcPortAddrType_Object = MibTableColumn
ecPortAddrType = _EcPortAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 5, 1, 5),
    _EcPortAddrType_Type()
)
ecPortAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecPortAddrType.setStatus("mandatory")


class _EcPortAddress_Type(OctetString):
    """Custom type ecPortAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EcPortAddress_Type.__name__ = "OctetString"
_EcPortAddress_Object = MibTableColumn
ecPortAddress = _EcPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 5, 1, 6),
    _EcPortAddress_Type()
)
ecPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecPortAddress.setStatus("mandatory")
_LocalSnmp_ObjectIdentity = ObjectIdentity
localSnmp = _LocalSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 10)
)
_TrapTable_Object = MibTable
trapTable = _TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 1)
)
if mibBuilder.loadTexts:
    trapTable.setStatus("deprecated")
_TrapEntry_Object = MibTableRow
trapEntry = _TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 1, 1)
)
trapEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "trapDestination"),
)
if mibBuilder.loadTexts:
    trapEntry.setStatus("deprecated")


class _TrapStatus_Type(Integer32):
    """Custom type trapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_TrapStatus_Type.__name__ = "Integer32"
_TrapStatus_Object = MibTableColumn
trapStatus = _TrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 1, 1, 1),
    _TrapStatus_Type()
)
trapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapStatus.setStatus("deprecated")
_TrapDestination_Type = IpAddress
_TrapDestination_Object = MibTableColumn
trapDestination = _TrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 1, 1, 2),
    _TrapDestination_Type()
)
trapDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDestination.setStatus("deprecated")


class _TrapCommunity_Type(DisplayString):
    """Custom type trapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrapCommunity_Type.__name__ = "DisplayString"
_TrapCommunity_Object = MibTableColumn
trapCommunity = _TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 1, 1, 3),
    _TrapCommunity_Type()
)
trapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunity.setStatus("deprecated")
_TrapSubject_Type = ObjectIdentifier
_TrapSubject_Object = MibTableColumn
trapSubject = _TrapSubject_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 1, 1, 4),
    _TrapSubject_Type()
)
trapSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSubject.setStatus("deprecated")
_TrapCategory_Type = Integer32
_TrapCategory_Object = MibTableColumn
trapCategory = _TrapCategory_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 1, 1, 5),
    _TrapCategory_Type()
)
trapCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCategory.setStatus("deprecated")
_TrapThrottle_Type = Integer32
_TrapThrottle_Object = MibTableColumn
trapThrottle = _TrapThrottle_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 1, 1, 6),
    _TrapThrottle_Type()
)
trapThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapThrottle.setStatus("deprecated")
_SnmpTrapTable_Object = MibTable
snmpTrapTable = _SnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2)
)
if mibBuilder.loadTexts:
    snmpTrapTable.setStatus("mandatory")
_SnmpTrapEntry_Object = MibTableRow
snmpTrapEntry = _SnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2, 1)
)
snmpTrapEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "snmpTrapIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapEntry.setStatus("mandatory")


class _SnmpTrapIndex_Type(Integer32):
    """Custom type snmpTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnmpTrapIndex_Type.__name__ = "Integer32"
_SnmpTrapIndex_Object = MibTableColumn
snmpTrapIndex = _SnmpTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2, 1, 1),
    _SnmpTrapIndex_Type()
)
snmpTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapIndex.setStatus("mandatory")


class _SnmpTrapDestination_Type(DisplayString):
    """Custom type snmpTrapDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SnmpTrapDestination_Type.__name__ = "DisplayString"
_SnmpTrapDestination_Object = MibTableColumn
snmpTrapDestination = _SnmpTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2, 1, 2),
    _SnmpTrapDestination_Type()
)
snmpTrapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestination.setStatus("mandatory")


class _SnmpTrapProtocol_Type(Integer32):
    """Custom type snmpTrapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("ipx", 3),
          ("unknown", 1))
    )


_SnmpTrapProtocol_Type.__name__ = "Integer32"
_SnmpTrapProtocol_Object = MibTableColumn
snmpTrapProtocol = _SnmpTrapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2, 1, 3),
    _SnmpTrapProtocol_Type()
)
snmpTrapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapProtocol.setStatus("mandatory")


class _SnmpTrapCommunity_Type(DisplayString):
    """Custom type snmpTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpTrapCommunity_Type.__name__ = "DisplayString"
_SnmpTrapCommunity_Object = MibTableColumn
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2, 1, 4),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("mandatory")


class _SnmpTrapCategory_Type(OctetString):
    """Custom type snmpTrapCategory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SnmpTrapCategory_Type.__name__ = "OctetString"
_SnmpTrapCategory_Object = MibTableColumn
snmpTrapCategory = _SnmpTrapCategory_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2, 1, 5),
    _SnmpTrapCategory_Type()
)
snmpTrapCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCategory.setStatus("mandatory")


class _SnmpTrapThrottle_Type(Integer32):
    """Custom type snmpTrapThrottle based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_SnmpTrapThrottle_Type.__name__ = "Integer32"
_SnmpTrapThrottle_Object = MibTableColumn
snmpTrapThrottle = _SnmpTrapThrottle_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2, 1, 6),
    _SnmpTrapThrottle_Type()
)
snmpTrapThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapThrottle.setStatus("mandatory")


class _SnmpTrapRowStatus_Type(Integer32):
    """Custom type snmpTrapRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_SnmpTrapRowStatus_Type.__name__ = "Integer32"
_SnmpTrapRowStatus_Object = MibTableColumn
snmpTrapRowStatus = _SnmpTrapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2, 1, 7),
    _SnmpTrapRowStatus_Type()
)
snmpTrapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRowStatus.setStatus("mandatory")


class _SnmpTrapNextFreeIndex_Type(Integer32):
    """Custom type snmpTrapNextFreeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnmpTrapNextFreeIndex_Type.__name__ = "Integer32"
_SnmpTrapNextFreeIndex_Object = MibScalar
snmpTrapNextFreeIndex = _SnmpTrapNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 3),
    _SnmpTrapNextFreeIndex_Type()
)
snmpTrapNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapNextFreeIndex.setStatus("mandatory")
_Manager_ObjectIdentity = ObjectIdentity
manager = _Manager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 11)
)
_UnusedGeneric12_ObjectIdentity = ObjectIdentity
unusedGeneric12 = _UnusedGeneric12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 12)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 14)
)
_Enclosure_ObjectIdentity = ObjectIdentity
enclosure = _Enclosure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 1)
)


class _EnclosureName_Type(DisplayString):
    """Custom type enclosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EnclosureName_Type.__name__ = "DisplayString"
_EnclosureName_Object = MibScalar
enclosureName = _EnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 1, 1),
    _EnclosureName_Type()
)
enclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureName.setStatus("mandatory")
_EnclosureObjId_Type = ObjectIdentifier
_EnclosureObjId_Object = MibScalar
enclosureObjId = _EnclosureObjId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 1, 2),
    _EnclosureObjId_Type()
)
enclosureObjId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureObjId.setStatus("mandatory")


class _EnclosureHardwareVers_Type(DisplayString):
    """Custom type enclosureHardwareVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EnclosureHardwareVers_Type.__name__ = "DisplayString"
_EnclosureHardwareVers_Object = MibScalar
enclosureHardwareVers = _EnclosureHardwareVers_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 1, 3),
    _EnclosureHardwareVers_Type()
)
enclosureHardwareVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureHardwareVers.setStatus("mandatory")
_PhysicalConfig_ObjectIdentity = ObjectIdentity
physicalConfig = _PhysicalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2)
)
_PhyConfigTable_Object = MibTable
phyConfigTable = _PhyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 1)
)
if mibBuilder.loadTexts:
    phyConfigTable.setStatus("mandatory")
_PhyConfigEntry_Object = MibTableRow
phyConfigEntry = _PhyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 1, 1)
)
phyConfigEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "phyLocationType"),
    (0, "LBHUB-MSH-MIB", "phyLocation"),
)
if mibBuilder.loadTexts:
    phyConfigEntry.setStatus("mandatory")


class _PhyLocationType_Type(Integer32):
    """Custom type phyLocationType based on Integer32"""
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
        *(("backplane", 4),
          ("fan", 3),
          ("module", 1),
          ("power-supply", 2))
    )


_PhyLocationType_Type.__name__ = "Integer32"
_PhyLocationType_Object = MibTableColumn
phyLocationType = _PhyLocationType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 1, 1, 1),
    _PhyLocationType_Type()
)
phyLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyLocationType.setStatus("mandatory")
_PhyLocation_Type = Integer32
_PhyLocation_Object = MibTableColumn
phyLocation = _PhyLocation_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 1, 1, 2),
    _PhyLocation_Type()
)
phyLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyLocation.setStatus("mandatory")
_PhySysObjId_Type = ObjectIdentifier
_PhySysObjId_Object = MibTableColumn
phySysObjId = _PhySysObjId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 1, 1, 3),
    _PhySysObjId_Type()
)
phySysObjId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phySysObjId.setStatus("mandatory")


class _PhyServiceType_Type(Integer32):
    """Custom type phyServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              12,
              13,
              14,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("bridgePerPort", 20),
          ("displayPanel", 14),
          ("dumb8023Repeater", 1),
          ("extendedBackplane", 13),
          ("fan", 17),
          ("fddiConcentrator", 5),
          ("fddiLinkSwitch", 25),
          ("fddiMIC", 23),
          ("ieee8023Repeater", 2),
          ("ieee8025MauModule", 3),
          ("ieee8025Ringbuilder", 4),
          ("managementModule", 6),
          ("notAllocated", 24),
          ("powerSupply", 18),
          ("remoteBridge", 22),
          ("standardBackplane", 12),
          ("standardBridge", 19),
          ("terminalServer", 21))
    )


_PhyServiceType_Type.__name__ = "Integer32"
_PhyServiceType_Object = MibTableColumn
phyServiceType = _PhyServiceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 1, 1, 4),
    _PhyServiceType_Type()
)
phyServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyServiceType.setStatus("mandatory")


class _PhyEntityType_Type(Integer32):
    """Custom type phyEntityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhyEntityType_Type.__name__ = "Integer32"
_PhyEntityType_Object = MibTableColumn
phyEntityType = _PhyEntityType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 1, 1, 5),
    _PhyEntityType_Type()
)
phyEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyEntityType.setStatus("mandatory")
_PhyHwVersion_Type = DisplayString
_PhyHwVersion_Object = MibTableColumn
phyHwVersion = _PhyHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 1, 1, 6),
    _PhyHwVersion_Type()
)
phyHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyHwVersion.setStatus("mandatory")
_PhySwVersion_Type = DisplayString
_PhySwVersion_Object = MibTableColumn
phySwVersion = _PhySwVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 1, 1, 7),
    _PhySwVersion_Type()
)
phySwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phySwVersion.setStatus("mandatory")
_PhyServiceId_Type = Integer32
_PhyServiceId_Object = MibTableColumn
phyServiceId = _PhyServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 1, 1, 8),
    _PhyServiceId_Type()
)
phyServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyServiceId.setStatus("mandatory")


class _PhyEntityName_Type(DisplayString):
    """Custom type phyEntityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PhyEntityName_Type.__name__ = "DisplayString"
_PhyEntityName_Object = MibTableColumn
phyEntityName = _PhyEntityName_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 1, 1, 9),
    _PhyEntityName_Type()
)
phyEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyEntityName.setStatus("mandatory")
_PhyPowerReq_Type = Integer32
_PhyPowerReq_Object = MibTableColumn
phyPowerReq = _PhyPowerReq_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 1, 1, 10),
    _PhyPowerReq_Type()
)
phyPowerReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyPowerReq.setStatus("mandatory")
_PhyNumberOfPorts_Type = Integer32
_PhyNumberOfPorts_Object = MibTableColumn
phyNumberOfPorts = _PhyNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 1, 1, 11),
    _PhyNumberOfPorts_Type()
)
phyNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyNumberOfPorts.setStatus("mandatory")


class _PhyLampTest_Type(Integer32):
    """Custom type phyLampTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("test-off", 1),
          ("test-on", 2))
    )


_PhyLampTest_Type.__name__ = "Integer32"
_PhyLampTest_Object = MibTableColumn
phyLampTest = _PhyLampTest_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 1, 1, 12),
    _PhyLampTest_Type()
)
phyLampTest.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    phyLampTest.setStatus("mandatory")


class _PhyEntityState_Type(Integer32):
    """Custom type phyEntityState based on Integer32"""
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
        *(("failure", 4),
          ("initialising", 2),
          ("operational", 3),
          ("unknown", 1))
    )


_PhyEntityState_Type.__name__ = "Integer32"
_PhyEntityState_Object = MibTableColumn
phyEntityState = _PhyEntityState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 1, 1, 13),
    _PhyEntityState_Type()
)
phyEntityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyEntityState.setStatus("mandatory")


class _PhyAction_Type(Integer32):
    """Custom type phyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_PhyAction_Type.__name__ = "Integer32"
_PhyAction_Object = MibTableColumn
phyAction = _PhyAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 1, 1, 14),
    _PhyAction_Type()
)
phyAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    phyAction.setStatus("mandatory")
_PhyLimits_Object = MibTable
phyLimits = _PhyLimits_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 2)
)
if mibBuilder.loadTexts:
    phyLimits.setStatus("mandatory")
_PhyLimitEntry_Object = MibTableRow
phyLimitEntry = _PhyLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 2, 1)
)
phyLimitEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "phyLimLocationType"),
)
if mibBuilder.loadTexts:
    phyLimitEntry.setStatus("mandatory")


class _PhyLimLocationType_Type(Integer32):
    """Custom type phyLimLocationType based on Integer32"""
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
        *(("backplane", 4),
          ("fan", 3),
          ("module", 1),
          ("power-supply", 2))
    )


_PhyLimLocationType_Type.__name__ = "Integer32"
_PhyLimLocationType_Object = MibTableColumn
phyLimLocationType = _PhyLimLocationType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 2, 1, 1),
    _PhyLimLocationType_Type()
)
phyLimLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyLimLocationType.setStatus("mandatory")
_PhyLimLimit_Type = Integer32
_PhyLimLimit_Object = MibTableColumn
phyLimLimit = _PhyLimLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 2, 1, 2),
    _PhyLimLimit_Type()
)
phyLimLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyLimLimit.setStatus("mandatory")
_FrontPanelDisplayMessage_Type = DisplayString
_FrontPanelDisplayMessage_Object = MibScalar
frontPanelDisplayMessage = _FrontPanelDisplayMessage_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 2, 3),
    _FrontPanelDisplayMessage_Type()
)
frontPanelDisplayMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frontPanelDisplayMessage.setStatus("mandatory")
_LogicalConfig_ObjectIdentity = ObjectIdentity
logicalConfig = _LogicalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3)
)
_ServiceTable_Object = MibTable
serviceTable = _ServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 1)
)
if mibBuilder.loadTexts:
    serviceTable.setStatus("mandatory")
_ServiceEntry_Object = MibTableRow
serviceEntry = _ServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 1, 1)
)
serviceEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "serviceId"),
)
if mibBuilder.loadTexts:
    serviceEntry.setStatus("mandatory")
_ServiceId_Type = Integer32
_ServiceId_Object = MibTableColumn
serviceId = _ServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 1, 1, 1),
    _ServiceId_Type()
)
serviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceId.setStatus("mandatory")


class _ServiceName_Type(DisplayString):
    """Custom type serviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ServiceName_Type.__name__ = "DisplayString"
_ServiceName_Object = MibTableColumn
serviceName = _ServiceName_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 1, 1, 2),
    _ServiceName_Type()
)
serviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceName.setStatus("mandatory")


class _ServiceReset_Type(Integer32):
    """Custom type serviceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ServiceReset_Type.__name__ = "Integer32"
_ServiceReset_Object = MibTableColumn
serviceReset = _ServiceReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 1, 1, 3),
    _ServiceReset_Type()
)
serviceReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    serviceReset.setStatus("mandatory")
_AddressTable_Object = MibTable
addressTable = _AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 2)
)
if mibBuilder.loadTexts:
    addressTable.setStatus("mandatory")
_AddressTableEntry_Object = MibTableRow
addressTableEntry = _AddressTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 2, 1)
)
addressTableEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "mgmtServiceId"),
    (0, "LBHUB-MSH-MIB", "mgmtSubIndex"),
)
if mibBuilder.loadTexts:
    addressTableEntry.setStatus("mandatory")
_MgmtServiceId_Type = Integer32
_MgmtServiceId_Object = MibTableColumn
mgmtServiceId = _MgmtServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 2, 1, 1),
    _MgmtServiceId_Type()
)
mgmtServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtServiceId.setStatus("mandatory")
_MgmtSubIndex_Type = Integer32
_MgmtSubIndex_Object = MibTableColumn
mgmtSubIndex = _MgmtSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 2, 1, 2),
    _MgmtSubIndex_Type()
)
mgmtSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtSubIndex.setStatus("mandatory")


class _MgmtAddressType_Type(Integer32):
    """Custom type mgmtAddressType based on Integer32"""
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
        *(("ieee8023address", 1),
          ("ieee8025address", 2),
          ("ipaddress", 3),
          ("slipaddress", 4))
    )


_MgmtAddressType_Type.__name__ = "Integer32"
_MgmtAddressType_Object = MibTableColumn
mgmtAddressType = _MgmtAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 2, 1, 3),
    _MgmtAddressType_Type()
)
mgmtAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtAddressType.setStatus("mandatory")
_MgmtAddress_Type = OctetString
_MgmtAddress_Object = MibTableColumn
mgmtAddress = _MgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 2, 1, 4),
    _MgmtAddress_Type()
)
mgmtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtAddress.setStatus("mandatory")
_FacilityTable_Object = MibTable
facilityTable = _FacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 3)
)
if mibBuilder.loadTexts:
    facilityTable.setStatus("mandatory")
_FacilityEntry_Object = MibTableRow
facilityEntry = _FacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 3, 1)
)
facilityEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "fcSlotNumber"),
    (0, "LBHUB-MSH-MIB", "fcFacilityIndex"),
)
if mibBuilder.loadTexts:
    facilityEntry.setStatus("mandatory")
_FcSlotNumber_Type = Integer32
_FcSlotNumber_Object = MibTableColumn
fcSlotNumber = _FcSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 3, 1, 1),
    _FcSlotNumber_Type()
)
fcSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcSlotNumber.setStatus("mandatory")
_FcFacilityIndex_Type = Integer32
_FcFacilityIndex_Object = MibTableColumn
fcFacilityIndex = _FcFacilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 3, 1, 2),
    _FcFacilityIndex_Type()
)
fcFacilityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFacilityIndex.setStatus("mandatory")


class _FcType_Type(Integer32):
    """Custom type fcType based on Integer32"""
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
        *(("atm", 6),
          ("fddi", 3),
          ("ieee8023", 1),
          ("ieee8023v3", 5),
          ("ieee8025", 2),
          ("ieee8025rb", 4),
          ("smds", 7))
    )


_FcType_Type.__name__ = "Integer32"
_FcType_Object = MibTableColumn
fcType = _FcType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 3, 1, 3),
    _FcType_Type()
)
fcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcType.setStatus("mandatory")
_FcConnection_Type = Integer32
_FcConnection_Object = MibTableColumn
fcConnection = _FcConnection_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 14, 3, 3, 1, 4),
    _FcConnection_Type()
)
fcConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcConnection.setStatus("mandatory")
_MrmResilience_ObjectIdentity = ObjectIdentity
mrmResilience = _MrmResilience_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 15)
)
_ResTable_Object = MibTable
resTable = _ResTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1)
)
if mibBuilder.loadTexts:
    resTable.setStatus("mandatory")
_ResTableEntry_Object = MibTableRow
resTableEntry = _ResTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1)
)
resTableEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "resRepeater"),
    (0, "LBHUB-MSH-MIB", "resMainSlot"),
    (0, "LBHUB-MSH-MIB", "resMainPort"),
)
if mibBuilder.loadTexts:
    resTableEntry.setStatus("mandatory")
_ResRepeater_Type = Integer32
_ResRepeater_Object = MibTableColumn
resRepeater = _ResRepeater_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 1),
    _ResRepeater_Type()
)
resRepeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resRepeater.setStatus("mandatory")
_ResMainSlot_Type = Integer32
_ResMainSlot_Object = MibTableColumn
resMainSlot = _ResMainSlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 2),
    _ResMainSlot_Type()
)
resMainSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resMainSlot.setStatus("mandatory")
_ResMainPort_Type = Integer32
_ResMainPort_Object = MibTableColumn
resMainPort = _ResMainPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 3),
    _ResMainPort_Type()
)
resMainPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resMainPort.setStatus("mandatory")


class _ResMainState_Type(Integer32):
    """Custom type resMainState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ok", 2),
          ("ok-and-active", 3))
    )


_ResMainState_Type.__name__ = "Integer32"
_ResMainState_Object = MibTableColumn
resMainState = _ResMainState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 4),
    _ResMainState_Type()
)
resMainState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resMainState.setStatus("mandatory")
_ResStandbySlot_Type = Integer32
_ResStandbySlot_Object = MibTableColumn
resStandbySlot = _ResStandbySlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 5),
    _ResStandbySlot_Type()
)
resStandbySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resStandbySlot.setStatus("mandatory")
_ResStandbyPort_Type = Integer32
_ResStandbyPort_Object = MibTableColumn
resStandbyPort = _ResStandbyPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 6),
    _ResStandbyPort_Type()
)
resStandbyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resStandbyPort.setStatus("mandatory")


class _ResStandbyState_Type(Integer32):
    """Custom type resStandbyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ok", 2),
          ("ok-and-active", 3))
    )


_ResStandbyState_Type.__name__ = "Integer32"
_ResStandbyState_Object = MibTableColumn
resStandbyState = _ResStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 7),
    _ResStandbyState_Type()
)
resStandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resStandbyState.setStatus("mandatory")


class _ResPairState_Type(Integer32):
    """Custom type resPairState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("operational", 2))
    )


_ResPairState_Type.__name__ = "Integer32"
_ResPairState_Object = MibTableColumn
resPairState = _ResPairState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 8),
    _ResPairState_Type()
)
resPairState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resPairState.setStatus("mandatory")


class _ResPairModificationStatus_Type(Integer32):
    """Custom type resPairModificationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stable", 2),
          ("under-modification", 1))
    )


_ResPairModificationStatus_Type.__name__ = "Integer32"
_ResPairModificationStatus_Object = MibTableColumn
resPairModificationStatus = _ResPairModificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 9),
    _ResPairModificationStatus_Type()
)
resPairModificationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resPairModificationStatus.setStatus("mandatory")


class _ResPairAction_Type(Integer32):
    """Custom type resPairAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2),
          ("togglePort", 3))
    )


_ResPairAction_Type.__name__ = "Integer32"
_ResPairAction_Object = MibTableColumn
resPairAction = _ResPairAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 10),
    _ResPairAction_Type()
)
resPairAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    resPairAction.setStatus("mandatory")


class _ResPairEnable_Type(Integer32):
    """Custom type resPairEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ResPairEnable_Type.__name__ = "Integer32"
_ResPairEnable_Object = MibTableColumn
resPairEnable = _ResPairEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 11),
    _ResPairEnable_Type()
)
resPairEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resPairEnable.setStatus("mandatory")
_ResStandbyMapTable_Object = MibTable
resStandbyMapTable = _ResStandbyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2)
)
if mibBuilder.loadTexts:
    resStandbyMapTable.setStatus("mandatory")
_ResStandbyMapTableEntry_Object = MibTableRow
resStandbyMapTableEntry = _ResStandbyMapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1)
)
resStandbyMapTableEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "resSbRepeater"),
    (0, "LBHUB-MSH-MIB", "resSbSlot"),
    (0, "LBHUB-MSH-MIB", "resSbPort"),
)
if mibBuilder.loadTexts:
    resStandbyMapTableEntry.setStatus("mandatory")
_ResSbRepeater_Type = Integer32
_ResSbRepeater_Object = MibTableColumn
resSbRepeater = _ResSbRepeater_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 1),
    _ResSbRepeater_Type()
)
resSbRepeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbRepeater.setStatus("mandatory")
_ResSbSlot_Type = Integer32
_ResSbSlot_Object = MibTableColumn
resSbSlot = _ResSbSlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 2),
    _ResSbSlot_Type()
)
resSbSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbSlot.setStatus("mandatory")
_ResSbPort_Type = Integer32
_ResSbPort_Object = MibTableColumn
resSbPort = _ResSbPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 3),
    _ResSbPort_Type()
)
resSbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbPort.setStatus("mandatory")


class _ResSbType_Type(Integer32):
    """Custom type resSbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("standby", 2))
    )


_ResSbType_Type.__name__ = "Integer32"
_ResSbType_Object = MibTableColumn
resSbType = _ResSbType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 4),
    _ResSbType_Type()
)
resSbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbType.setStatus("mandatory")
_ResSbMainSlot_Type = Integer32
_ResSbMainSlot_Object = MibTableColumn
resSbMainSlot = _ResSbMainSlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 5),
    _ResSbMainSlot_Type()
)
resSbMainSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbMainSlot.setStatus("mandatory")
_ResSbMainPort_Type = Integer32
_ResSbMainPort_Object = MibTableColumn
resSbMainPort = _ResSbMainPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 6),
    _ResSbMainPort_Type()
)
resSbMainPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbMainPort.setStatus("mandatory")
_ResFlushTable_Type = Integer32
_ResFlushTable_Object = MibScalar
resFlushTable = _ResFlushTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 3),
    _ResFlushTable_Type()
)
resFlushTable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    resFlushTable.setStatus("mandatory")
_TokenRing_ObjectIdentity = ObjectIdentity
tokenRing = _TokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 16)
)
_A3ComRingParams_ObjectIdentity = ObjectIdentity
a3ComRingParams = _A3ComRingParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1)
)
_A3ComRingConfig_Object = MibTable
a3ComRingConfig = _A3ComRingConfig_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 1)
)
if mibBuilder.loadTexts:
    a3ComRingConfig.setStatus("mandatory")
_A3ComRingConfigEntry_Object = MibTableRow
a3ComRingConfigEntry = _A3ComRingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 1, 1)
)
a3ComRingConfigEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "a3ComRingConfigServiceId"),
)
if mibBuilder.loadTexts:
    a3ComRingConfigEntry.setStatus("mandatory")
_A3ComRingConfigServiceId_Type = Integer32
_A3ComRingConfigServiceId_Object = MibTableColumn
a3ComRingConfigServiceId = _A3ComRingConfigServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 1, 1, 1),
    _A3ComRingConfigServiceId_Type()
)
a3ComRingConfigServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingConfigServiceId.setStatus("mandatory")


class _A3ComRingNumber_Type(Integer32):
    """Custom type a3ComRingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_A3ComRingNumber_Type.__name__ = "Integer32"
_A3ComRingNumber_Object = MibTableColumn
a3ComRingNumber = _A3ComRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 1, 1, 2),
    _A3ComRingNumber_Type()
)
a3ComRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingNumber.setStatus("mandatory")


class _A3ComRingSpeed_Type(Integer32):
    """Custom type a3ComRingSpeed based on Integer32"""
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
        *(("s16MegaBPS", 4),
          ("s1MegaBPS", 2),
          ("s4MegaBPS", 3),
          ("unknown", 1))
    )


_A3ComRingSpeed_Type.__name__ = "Integer32"
_A3ComRingSpeed_Object = MibTableColumn
a3ComRingSpeed = _A3ComRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 1, 1, 3),
    _A3ComRingSpeed_Type()
)
a3ComRingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingSpeed.setStatus("mandatory")


class _A3ComRingState_Type(Integer32):
    """Custom type a3ComRingState based on Integer32"""
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
        *(("beacon", 3),
          ("fault", 5),
          ("normal", 2),
          ("notAvailable", 1),
          ("soft-error", 4))
    )


_A3ComRingState_Type.__name__ = "Integer32"
_A3ComRingState_Object = MibTableColumn
a3ComRingState = _A3ComRingState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 1, 1, 4),
    _A3ComRingState_Type()
)
a3ComRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingState.setStatus("mandatory")


class _A3ComRingBackupState_Type(Integer32):
    """Custom type a3ComRingBackupState based on Integer32"""
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
        *(("beacon", 3),
          ("fault", 5),
          ("normal", 2),
          ("notAvailable", 1),
          ("soft-error", 4))
    )


_A3ComRingBackupState_Type.__name__ = "Integer32"
_A3ComRingBackupState_Object = MibTableColumn
a3ComRingBackupState = _A3ComRingBackupState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 1, 1, 5),
    _A3ComRingBackupState_Type()
)
a3ComRingBackupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingBackupState.setStatus("mandatory")


class _A3ComRingWrapState_Type(Integer32):
    """Custom type a3ComRingWrapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 3),
          ("ringNotWrapped", 1),
          ("ringWrapped", 2))
    )


_A3ComRingWrapState_Type.__name__ = "Integer32"
_A3ComRingWrapState_Object = MibTableColumn
a3ComRingWrapState = _A3ComRingWrapState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 1, 1, 6),
    _A3ComRingWrapState_Type()
)
a3ComRingWrapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingWrapState.setStatus("mandatory")


class _A3ComRingMapChanged_Type(Integer32):
    """Custom type a3ComRingMapChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_A3ComRingMapChanged_Type.__name__ = "Integer32"
_A3ComRingMapChanged_Object = MibTableColumn
a3ComRingMapChanged = _A3ComRingMapChanged_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 1, 1, 7),
    _A3ComRingMapChanged_Type()
)
a3ComRingMapChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComRingMapChanged.setStatus("mandatory")
_A3ComRingMapChangeTime_Type = TimeTicks
_A3ComRingMapChangeTime_Object = MibTableColumn
a3ComRingMapChangeTime = _A3ComRingMapChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 1, 1, 8),
    _A3ComRingMapChangeTime_Type()
)
a3ComRingMapChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingMapChangeTime.setStatus("mandatory")


class _A3ComRingAction_Type(Integer32):
    """Custom type a3ComRingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearAllCounters", 3),
          ("clearRingCounters", 2),
          ("noAction", 1))
    )


_A3ComRingAction_Type.__name__ = "Integer32"
_A3ComRingAction_Object = MibTableColumn
a3ComRingAction = _A3ComRingAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 1, 1, 9),
    _A3ComRingAction_Type()
)
a3ComRingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComRingAction.setStatus("mandatory")
_A3ComRingStdStats_Object = MibTable
a3ComRingStdStats = _A3ComRingStdStats_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 2)
)
if mibBuilder.loadTexts:
    a3ComRingStdStats.setStatus("mandatory")
_A3ComRingStdStatsEntry_Object = MibTableRow
a3ComRingStdStatsEntry = _A3ComRingStdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 2, 1)
)
a3ComRingStdStatsEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "a3ComRingStdStatsServiceId"),
)
if mibBuilder.loadTexts:
    a3ComRingStdStatsEntry.setStatus("mandatory")
_A3ComRingStdStatsServiceId_Type = Integer32
_A3ComRingStdStatsServiceId_Object = MibTableColumn
a3ComRingStdStatsServiceId = _A3ComRingStdStatsServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 2, 1, 1),
    _A3ComRingStdStatsServiceId_Type()
)
a3ComRingStdStatsServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStdStatsServiceId.setStatus("mandatory")
_A3ComRingBeaconCount_Type = Counter32
_A3ComRingBeaconCount_Object = MibTableColumn
a3ComRingBeaconCount = _A3ComRingBeaconCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 2, 1, 2),
    _A3ComRingBeaconCount_Type()
)
a3ComRingBeaconCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingBeaconCount.setStatus("mandatory")
_A3ComRingSoftErrors_Type = Counter32
_A3ComRingSoftErrors_Object = MibTableColumn
a3ComRingSoftErrors = _A3ComRingSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 2, 1, 3),
    _A3ComRingSoftErrors_Type()
)
a3ComRingSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingSoftErrors.setStatus("mandatory")
_A3ComRingActiveMonitorChanges_Type = Counter32
_A3ComRingActiveMonitorChanges_Object = MibTableColumn
a3ComRingActiveMonitorChanges = _A3ComRingActiveMonitorChanges_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 2, 1, 4),
    _A3ComRingActiveMonitorChanges_Type()
)
a3ComRingActiveMonitorChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingActiveMonitorChanges.setStatus("mandatory")
_A3ComRingTop_Object = MibTable
a3ComRingTop = _A3ComRingTop_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 4)
)
if mibBuilder.loadTexts:
    a3ComRingTop.setStatus("mandatory")
_A3ComRingTopEntry_Object = MibTableRow
a3ComRingTopEntry = _A3ComRingTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 4, 1)
)
a3ComRingTopEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "a3ComRingTopServiceId"),
    (0, "LBHUB-MSH-MIB", "a3ComRingTopIndex"),
)
if mibBuilder.loadTexts:
    a3ComRingTopEntry.setStatus("mandatory")
_A3ComRingTopServiceId_Type = Integer32
_A3ComRingTopServiceId_Object = MibTableColumn
a3ComRingTopServiceId = _A3ComRingTopServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 4, 1, 1),
    _A3ComRingTopServiceId_Type()
)
a3ComRingTopServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingTopServiceId.setStatus("mandatory")
_A3ComRingTopIndex_Type = Integer32
_A3ComRingTopIndex_Object = MibTableColumn
a3ComRingTopIndex = _A3ComRingTopIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 4, 1, 2),
    _A3ComRingTopIndex_Type()
)
a3ComRingTopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingTopIndex.setStatus("mandatory")
_A3ComRingTopStationAddress_Type = OctetString
_A3ComRingTopStationAddress_Object = MibTableColumn
a3ComRingTopStationAddress = _A3ComRingTopStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 4, 1, 3),
    _A3ComRingTopStationAddress_Type()
)
a3ComRingTopStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingTopStationAddress.setStatus("mandatory")


class _A3ComRingTopMonitor_Type(Integer32):
    """Custom type a3ComRingTopMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active-monitor", 1),
          ("standby-monitor", 2))
    )


_A3ComRingTopMonitor_Type.__name__ = "Integer32"
_A3ComRingTopMonitor_Object = MibTableColumn
a3ComRingTopMonitor = _A3ComRingTopMonitor_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 1, 4, 1, 4),
    _A3ComRingTopMonitor_Type()
)
a3ComRingTopMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingTopMonitor.setStatus("mandatory")
_A3ComRingStationParams_ObjectIdentity = ObjectIdentity
a3ComRingStationParams = _A3ComRingStationParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2)
)
_A3ComRingStatConfig_Object = MibTable
a3ComRingStatConfig = _A3ComRingStatConfig_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 1)
)
if mibBuilder.loadTexts:
    a3ComRingStatConfig.setStatus("mandatory")
_A3ComRingStatConfigEntry_Object = MibTableRow
a3ComRingStatConfigEntry = _A3ComRingStatConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 1, 1)
)
a3ComRingStatConfigEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "a3ComRingStatConfigServiceId"),
    (0, "LBHUB-MSH-MIB", "a3ComRingStatConfigAddress"),
)
if mibBuilder.loadTexts:
    a3ComRingStatConfigEntry.setStatus("mandatory")
_A3ComRingStatConfigServiceId_Type = Integer32
_A3ComRingStatConfigServiceId_Object = MibTableColumn
a3ComRingStatConfigServiceId = _A3ComRingStatConfigServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 1, 1, 1),
    _A3ComRingStatConfigServiceId_Type()
)
a3ComRingStatConfigServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStatConfigServiceId.setStatus("mandatory")
_A3ComRingStatConfigAddress_Type = PhysAddress
_A3ComRingStatConfigAddress_Object = MibTableColumn
a3ComRingStatConfigAddress = _A3ComRingStatConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 1, 1, 2),
    _A3ComRingStatConfigAddress_Type()
)
a3ComRingStatConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStatConfigAddress.setStatus("mandatory")


class _A3ComRingStatState_Type(Integer32):
    """Custom type a3ComRingStatState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("present", 1))
    )


_A3ComRingStatState_Type.__name__ = "Integer32"
_A3ComRingStatState_Object = MibTableColumn
a3ComRingStatState = _A3ComRingStatState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 1, 1, 3),
    _A3ComRingStatState_Type()
)
a3ComRingStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStatState.setStatus("mandatory")
_A3ComRingStatLocation_Type = Integer32
_A3ComRingStatLocation_Object = MibTableColumn
a3ComRingStatLocation = _A3ComRingStatLocation_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 1, 1, 4),
    _A3ComRingStatLocation_Type()
)
a3ComRingStatLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStatLocation.setStatus("mandatory")


class _A3ComRingStatAction_Type(Integer32):
    """Custom type a3ComRingStatAction based on Integer32"""
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
        *(("clearCounters", 3),
          ("deleteEntry", 4),
          ("forwardTest", 5),
          ("noAction", 1),
          ("removeStation", 2))
    )


_A3ComRingStatAction_Type.__name__ = "Integer32"
_A3ComRingStatAction_Object = MibTableColumn
a3ComRingStatAction = _A3ComRingStatAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 1, 1, 5),
    _A3ComRingStatAction_Type()
)
a3ComRingStatAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComRingStatAction.setStatus("mandatory")
_A3ComRingStatStandardStats_Object = MibTable
a3ComRingStatStandardStats = _A3ComRingStatStandardStats_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 2)
)
if mibBuilder.loadTexts:
    a3ComRingStatStandardStats.setStatus("mandatory")
_A3ComRingStatStdStatsEntry_Object = MibTableRow
a3ComRingStatStdStatsEntry = _A3ComRingStatStdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 2, 1)
)
a3ComRingStatStdStatsEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "a3ComRingStatStdStatsServiceId"),
    (0, "LBHUB-MSH-MIB", "a3ComRingStatStdStatsAddress"),
)
if mibBuilder.loadTexts:
    a3ComRingStatStdStatsEntry.setStatus("mandatory")
_A3ComRingStatStdStatsServiceId_Type = Integer32
_A3ComRingStatStdStatsServiceId_Object = MibTableColumn
a3ComRingStatStdStatsServiceId = _A3ComRingStatStdStatsServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 2, 1, 1),
    _A3ComRingStatStdStatsServiceId_Type()
)
a3ComRingStatStdStatsServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStatStdStatsServiceId.setStatus("mandatory")
_A3ComRingStatStdStatsAddress_Type = PhysAddress
_A3ComRingStatStdStatsAddress_Object = MibTableColumn
a3ComRingStatStdStatsAddress = _A3ComRingStatStdStatsAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 2, 1, 2),
    _A3ComRingStatStdStatsAddress_Type()
)
a3ComRingStatStdStatsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStatStdStatsAddress.setStatus("mandatory")
_A3ComRingStatLineErrors_Type = Counter32
_A3ComRingStatLineErrors_Object = MibTableColumn
a3ComRingStatLineErrors = _A3ComRingStatLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 2, 1, 3),
    _A3ComRingStatLineErrors_Type()
)
a3ComRingStatLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStatLineErrors.setStatus("mandatory")
_A3ComRingStatInternalErrors_Type = Counter32
_A3ComRingStatInternalErrors_Object = MibTableColumn
a3ComRingStatInternalErrors = _A3ComRingStatInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 2, 1, 4),
    _A3ComRingStatInternalErrors_Type()
)
a3ComRingStatInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStatInternalErrors.setStatus("mandatory")
_A3ComRingStatBurstErrors_Type = Counter32
_A3ComRingStatBurstErrors_Object = MibTableColumn
a3ComRingStatBurstErrors = _A3ComRingStatBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 2, 1, 5),
    _A3ComRingStatBurstErrors_Type()
)
a3ComRingStatBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStatBurstErrors.setStatus("mandatory")
_A3ComRingStatMonitorErrors_Type = Counter32
_A3ComRingStatMonitorErrors_Object = MibTableColumn
a3ComRingStatMonitorErrors = _A3ComRingStatMonitorErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 2, 1, 6),
    _A3ComRingStatMonitorErrors_Type()
)
a3ComRingStatMonitorErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStatMonitorErrors.setStatus("mandatory")
_A3ComRingStatLostFrames_Type = Counter32
_A3ComRingStatLostFrames_Object = MibTableColumn
a3ComRingStatLostFrames = _A3ComRingStatLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 2, 1, 7),
    _A3ComRingStatLostFrames_Type()
)
a3ComRingStatLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStatLostFrames.setStatus("mandatory")
_A3ComRingStatFrameCopyErrors_Type = Counter32
_A3ComRingStatFrameCopyErrors_Object = MibTableColumn
a3ComRingStatFrameCopyErrors = _A3ComRingStatFrameCopyErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 2, 1, 8),
    _A3ComRingStatFrameCopyErrors_Type()
)
a3ComRingStatFrameCopyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStatFrameCopyErrors.setStatus("mandatory")
_A3ComRingStatRxCongestion_Type = Counter32
_A3ComRingStatRxCongestion_Object = MibTableColumn
a3ComRingStatRxCongestion = _A3ComRingStatRxCongestion_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 2, 1, 9),
    _A3ComRingStatRxCongestion_Type()
)
a3ComRingStatRxCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStatRxCongestion.setStatus("mandatory")
_A3ComRingStatTokenErrors_Type = Counter32
_A3ComRingStatTokenErrors_Object = MibTableColumn
a3ComRingStatTokenErrors = _A3ComRingStatTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 2, 1, 10),
    _A3ComRingStatTokenErrors_Type()
)
a3ComRingStatTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStatTokenErrors.setStatus("mandatory")
_A3ComRingStatFreqErrors_Type = Counter32
_A3ComRingStatFreqErrors_Object = MibTableColumn
a3ComRingStatFreqErrors = _A3ComRingStatFreqErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 2, 1, 11),
    _A3ComRingStatFreqErrors_Type()
)
a3ComRingStatFreqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStatFreqErrors.setStatus("mandatory")
_A3ComRingStatSoftErrors_Type = Counter32
_A3ComRingStatSoftErrors_Object = MibTableColumn
a3ComRingStatSoftErrors = _A3ComRingStatSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 16, 2, 2, 1, 12),
    _A3ComRingStatSoftErrors_Type()
)
a3ComRingStatSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComRingStatSoftErrors.setStatus("mandatory")
_MultiRepeater_ObjectIdentity = ObjectIdentity
multiRepeater = _MultiRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17)
)
_MrmBasicPackage_ObjectIdentity = ObjectIdentity
mrmBasicPackage = _MrmBasicPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1)
)
_MrmBasCardPackage_ObjectIdentity = ObjectIdentity
mrmBasCardPackage = _MrmBasCardPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1)
)
_MrmCardTable_Object = MibTable
mrmCardTable = _MrmCardTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mrmCardTable.setStatus("mandatory")
_MrmCardEntry_Object = MibTableRow
mrmCardEntry = _MrmCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1, 1, 1)
)
mrmCardEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "mrmCardServiceId"),
    (0, "LBHUB-MSH-MIB", "mrmCardIndex"),
)
if mibBuilder.loadTexts:
    mrmCardEntry.setStatus("mandatory")
_MrmCardServiceId_Type = Integer32
_MrmCardServiceId_Object = MibTableColumn
mrmCardServiceId = _MrmCardServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1, 1, 1, 1),
    _MrmCardServiceId_Type()
)
mrmCardServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmCardServiceId.setStatus("mandatory")
_MrmCardIndex_Type = Integer32
_MrmCardIndex_Object = MibTableColumn
mrmCardIndex = _MrmCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1, 1, 1, 2),
    _MrmCardIndex_Type()
)
mrmCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmCardIndex.setStatus("mandatory")
_MrmCardPortCapacity_Type = Integer32
_MrmCardPortCapacity_Object = MibTableColumn
mrmCardPortCapacity = _MrmCardPortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1, 1, 1, 3),
    _MrmCardPortCapacity_Type()
)
mrmCardPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmCardPortCapacity.setStatus("mandatory")


class _MrmCardTest_Type(Integer32):
    """Custom type mrmCardTest based on Integer32"""
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
        *(("failed", 5),
          ("noTest", 1),
          ("passed", 4),
          ("test", 2),
          ("testing", 3))
    )


_MrmCardTest_Type.__name__ = "Integer32"
_MrmCardTest_Object = MibTableColumn
mrmCardTest = _MrmCardTest_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1, 1, 1, 4),
    _MrmCardTest_Type()
)
mrmCardTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmCardTest.setStatus("mandatory")
_MrmCardDOBPorts_Type = Integer32
_MrmCardDOBPorts_Object = MibTableColumn
mrmCardDOBPorts = _MrmCardDOBPorts_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1, 1, 1, 5),
    _MrmCardDOBPorts_Type()
)
mrmCardDOBPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmCardDOBPorts.setStatus("mandatory")


class _MrmCardMDIenable_Type(Integer32):
    """Custom type mrmCardMDIenable based on Integer32"""
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
        *(("mdiDisabled", 2),
          ("mdiEnabled", 3),
          ("notApplicable", 4),
          ("unknown", 1))
    )


_MrmCardMDIenable_Type.__name__ = "Integer32"
_MrmCardMDIenable_Object = MibTableColumn
mrmCardMDIenable = _MrmCardMDIenable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1, 1, 1, 6),
    _MrmCardMDIenable_Type()
)
mrmCardMDIenable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmCardMDIenable.setStatus("mandatory")
_MrmBasPortPackage_ObjectIdentity = ObjectIdentity
mrmBasPortPackage = _MrmBasPortPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2)
)
_MrmPortTable_Object = MibTable
mrmPortTable = _MrmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mrmPortTable.setStatus("mandatory")
_MrmPortEntry_Object = MibTableRow
mrmPortEntry = _MrmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1)
)
mrmPortEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "mrmPortServiceId"),
    (0, "LBHUB-MSH-MIB", "mrmPortCardIndex"),
    (0, "LBHUB-MSH-MIB", "mrmPortIndex"),
)
if mibBuilder.loadTexts:
    mrmPortEntry.setStatus("mandatory")
_MrmPortServiceId_Type = Integer32
_MrmPortServiceId_Object = MibTableColumn
mrmPortServiceId = _MrmPortServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 1),
    _MrmPortServiceId_Type()
)
mrmPortServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortServiceId.setStatus("mandatory")
_MrmPortCardIndex_Type = Integer32
_MrmPortCardIndex_Object = MibTableColumn
mrmPortCardIndex = _MrmPortCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 2),
    _MrmPortCardIndex_Type()
)
mrmPortCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortCardIndex.setStatus("mandatory")
_MrmPortIndex_Type = Integer32
_MrmPortIndex_Object = MibTableColumn
mrmPortIndex = _MrmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 3),
    _MrmPortIndex_Type()
)
mrmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortIndex.setStatus("mandatory")


class _MrmPortInterfaceType_Type(Integer32):
    """Custom type mrmPortInterfaceType based on Integer32"""
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
        *(("femaleAUI", 3),
          ("fiber", 7),
          ("maleAUI", 2),
          ("thinCoax", 4),
          ("twistedPair", 5),
          ("unknown", 1),
          ("unshieldedTP", 6))
    )


_MrmPortInterfaceType_Type.__name__ = "Integer32"
_MrmPortInterfaceType_Object = MibTableColumn
mrmPortInterfaceType = _MrmPortInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 4),
    _MrmPortInterfaceType_Type()
)
mrmPortInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortInterfaceType.setStatus("mandatory")


class _MrmPortConnectorType_Type(Integer32):
    """Custom type mrmPortConnectorType based on Integer32"""
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
        *(("bnc", 7),
          ("dtype-15", 6),
          ("rj45", 2),
          ("sma", 5),
          ("st", 4),
          ("telco", 3),
          ("unknown", 1))
    )


_MrmPortConnectorType_Type.__name__ = "Integer32"
_MrmPortConnectorType_Object = MibTableColumn
mrmPortConnectorType = _MrmPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 5),
    _MrmPortConnectorType_Type()
)
mrmPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortConnectorType.setStatus("mandatory")


class _MrmPortAdminStatus_Type(Integer32):
    """Custom type mrmPortAdminStatus based on Integer32"""
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


_MrmPortAdminStatus_Type.__name__ = "Integer32"
_MrmPortAdminStatus_Object = MibTableColumn
mrmPortAdminStatus = _MrmPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 6),
    _MrmPortAdminStatus_Type()
)
mrmPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmPortAdminStatus.setStatus("mandatory")


class _MrmPortAutoPartitionState_Type(Integer32):
    """Custom type mrmPortAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("partitioned", 1),
          ("unpartitioned", 2))
    )


_MrmPortAutoPartitionState_Type.__name__ = "Integer32"
_MrmPortAutoPartitionState_Object = MibTableColumn
mrmPortAutoPartitionState = _MrmPortAutoPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 7),
    _MrmPortAutoPartitionState_Type()
)
mrmPortAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortAutoPartitionState.setStatus("mandatory")


class _MrmPortLinkState_Type(Integer32):
    """Custom type mrmPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("present", 1))
    )


_MrmPortLinkState_Type.__name__ = "Integer32"
_MrmPortLinkState_Object = MibTableColumn
mrmPortLinkState = _MrmPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 8),
    _MrmPortLinkState_Type()
)
mrmPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortLinkState.setStatus("mandatory")


class _MrmPortBootState_Type(Integer32):
    """Custom type mrmPortBootState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_MrmPortBootState_Type.__name__ = "Integer32"
_MrmPortBootState_Object = MibTableColumn
mrmPortBootState = _MrmPortBootState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 9),
    _MrmPortBootState_Type()
)
mrmPortBootState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortBootState.setStatus("mandatory")


class _MrmPortESTFilter_Type(Integer32):
    """Custom type mrmPortESTFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              127,
              128)
        )
    )
    namedValues = NamedValues(
        *(("forwardAll", 127),
          ("forwardIP", 2),
          ("forwardMAC", 1),
          ("forwardNone", 128))
    )


_MrmPortESTFilter_Type.__name__ = "Integer32"
_MrmPortESTFilter_Object = MibTableColumn
mrmPortESTFilter = _MrmPortESTFilter_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 10),
    _MrmPortESTFilter_Type()
)
mrmPortESTFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmPortESTFilter.setStatus("mandatory")


class _MrmPortPartitionEvent_Type(Integer32):
    """Custom type mrmPortPartitionEvent based on Integer32"""
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


_MrmPortPartitionEvent_Type.__name__ = "Integer32"
_MrmPortPartitionEvent_Object = MibTableColumn
mrmPortPartitionEvent = _MrmPortPartitionEvent_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 11),
    _MrmPortPartitionEvent_Type()
)
mrmPortPartitionEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmPortPartitionEvent.setStatus("mandatory")


class _MrmPortLinkStateEvent_Type(Integer32):
    """Custom type mrmPortLinkStateEvent based on Integer32"""
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


_MrmPortLinkStateEvent_Type.__name__ = "Integer32"
_MrmPortLinkStateEvent_Object = MibTableColumn
mrmPortLinkStateEvent = _MrmPortLinkStateEvent_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 12),
    _MrmPortLinkStateEvent_Type()
)
mrmPortLinkStateEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmPortLinkStateEvent.setStatus("mandatory")


class _MrmPortSecurityAvailable_Type(Integer32):
    """Custom type mrmPortSecurityAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_MrmPortSecurityAvailable_Type.__name__ = "Integer32"
_MrmPortSecurityAvailable_Object = MibTableColumn
mrmPortSecurityAvailable = _MrmPortSecurityAvailable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 13),
    _MrmPortSecurityAvailable_Type()
)
mrmPortSecurityAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortSecurityAvailable.setStatus("mandatory")


class _MrmPortLinkPulse_Type(Integer32):
    """Custom type mrmPortLinkPulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_MrmPortLinkPulse_Type.__name__ = "Integer32"
_MrmPortLinkPulse_Object = MibTableColumn
mrmPortLinkPulse = _MrmPortLinkPulse_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 14),
    _MrmPortLinkPulse_Type()
)
mrmPortLinkPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmPortLinkPulse.setStatus("mandatory")
_MrmMonitorPackage_ObjectIdentity = ObjectIdentity
mrmMonitorPackage = _MrmMonitorPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2)
)
_MrmMonRepeaterPackage_ObjectIdentity = ObjectIdentity
mrmMonRepeaterPackage = _MrmMonRepeaterPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1)
)
_MrmMonitorRepTable_Object = MibTable
mrmMonitorRepTable = _MrmMonitorRepTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mrmMonitorRepTable.setStatus("mandatory")
_MrmMonitorRepEntry_Object = MibTableRow
mrmMonitorRepEntry = _MrmMonitorRepEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1)
)
mrmMonitorRepEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "mrmMonRepServiceId"),
)
if mibBuilder.loadTexts:
    mrmMonitorRepEntry.setStatus("mandatory")
_MrmMonRepServiceId_Type = Integer32
_MrmMonRepServiceId_Object = MibTableColumn
mrmMonRepServiceId = _MrmMonRepServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 1),
    _MrmMonRepServiceId_Type()
)
mrmMonRepServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepServiceId.setStatus("mandatory")
_MrmMonRepReadableFrames_Type = Counter32
_MrmMonRepReadableFrames_Object = MibTableColumn
mrmMonRepReadableFrames = _MrmMonRepReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 2),
    _MrmMonRepReadableFrames_Type()
)
mrmMonRepReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepReadableFrames.setStatus("mandatory")
_MrmMonRepUnicastFrames_Type = Counter32
_MrmMonRepUnicastFrames_Object = MibTableColumn
mrmMonRepUnicastFrames = _MrmMonRepUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 3),
    _MrmMonRepUnicastFrames_Type()
)
mrmMonRepUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepUnicastFrames.setStatus("mandatory")
_MrmMonRepMulticastFrames_Type = Counter32
_MrmMonRepMulticastFrames_Object = MibTableColumn
mrmMonRepMulticastFrames = _MrmMonRepMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 4),
    _MrmMonRepMulticastFrames_Type()
)
mrmMonRepMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepMulticastFrames.setStatus("mandatory")
_MrmMonRepBroadcastFrames_Type = Counter32
_MrmMonRepBroadcastFrames_Object = MibTableColumn
mrmMonRepBroadcastFrames = _MrmMonRepBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 5),
    _MrmMonRepBroadcastFrames_Type()
)
mrmMonRepBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBroadcastFrames.setStatus("mandatory")
_MrmMonRepReadableOctets_Type = Counter32
_MrmMonRepReadableOctets_Object = MibTableColumn
mrmMonRepReadableOctets = _MrmMonRepReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 6),
    _MrmMonRepReadableOctets_Type()
)
mrmMonRepReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepReadableOctets.setStatus("mandatory")
_MrmMonRepUnicastOctets_Type = Counter32
_MrmMonRepUnicastOctets_Object = MibTableColumn
mrmMonRepUnicastOctets = _MrmMonRepUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 7),
    _MrmMonRepUnicastOctets_Type()
)
mrmMonRepUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepUnicastOctets.setStatus("mandatory")
_MrmMonRepMulticastOctets_Type = Counter32
_MrmMonRepMulticastOctets_Object = MibTableColumn
mrmMonRepMulticastOctets = _MrmMonRepMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 8),
    _MrmMonRepMulticastOctets_Type()
)
mrmMonRepMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepMulticastOctets.setStatus("mandatory")
_MrmMonRepBroadcastOctets_Type = Counter32
_MrmMonRepBroadcastOctets_Object = MibTableColumn
mrmMonRepBroadcastOctets = _MrmMonRepBroadcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 9),
    _MrmMonRepBroadcastOctets_Type()
)
mrmMonRepBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBroadcastOctets.setStatus("mandatory")
_MrmMonRepFCSErrors_Type = Counter32
_MrmMonRepFCSErrors_Object = MibTableColumn
mrmMonRepFCSErrors = _MrmMonRepFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 10),
    _MrmMonRepFCSErrors_Type()
)
mrmMonRepFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepFCSErrors.setStatus("mandatory")
_MrmMonRepAlignmentErrors_Type = Counter32
_MrmMonRepAlignmentErrors_Object = MibTableColumn
mrmMonRepAlignmentErrors = _MrmMonRepAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 11),
    _MrmMonRepAlignmentErrors_Type()
)
mrmMonRepAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepAlignmentErrors.setStatus("mandatory")
_MrmMonRepFrameTooLongs_Type = Counter32
_MrmMonRepFrameTooLongs_Object = MibTableColumn
mrmMonRepFrameTooLongs = _MrmMonRepFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 12),
    _MrmMonRepFrameTooLongs_Type()
)
mrmMonRepFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepFrameTooLongs.setStatus("mandatory")
_MrmMonRepShortEvents_Type = Counter32
_MrmMonRepShortEvents_Object = MibTableColumn
mrmMonRepShortEvents = _MrmMonRepShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 13),
    _MrmMonRepShortEvents_Type()
)
mrmMonRepShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepShortEvents.setStatus("mandatory")
_MrmMonRepRunts_Type = Counter32
_MrmMonRepRunts_Object = MibTableColumn
mrmMonRepRunts = _MrmMonRepRunts_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 14),
    _MrmMonRepRunts_Type()
)
mrmMonRepRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepRunts.setStatus("mandatory")
_MrmMonRepTxCollisions_Type = Counter32
_MrmMonRepTxCollisions_Object = MibTableColumn
mrmMonRepTxCollisions = _MrmMonRepTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 15),
    _MrmMonRepTxCollisions_Type()
)
mrmMonRepTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepTxCollisions.setStatus("mandatory")
_MrmMonRepLateEvents_Type = Counter32
_MrmMonRepLateEvents_Object = MibTableColumn
mrmMonRepLateEvents = _MrmMonRepLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 16),
    _MrmMonRepLateEvents_Type()
)
mrmMonRepLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepLateEvents.setStatus("mandatory")
_MrmMonRepVeryLongEvents_Type = Counter32
_MrmMonRepVeryLongEvents_Object = MibTableColumn
mrmMonRepVeryLongEvents = _MrmMonRepVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 17),
    _MrmMonRepVeryLongEvents_Type()
)
mrmMonRepVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepVeryLongEvents.setStatus("mandatory")
_MrmMonRepDataRateMismatches_Type = Counter32
_MrmMonRepDataRateMismatches_Object = MibTableColumn
mrmMonRepDataRateMismatches = _MrmMonRepDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 18),
    _MrmMonRepDataRateMismatches_Type()
)
mrmMonRepDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepDataRateMismatches.setStatus("mandatory")
_MrmMonRepAutoPartitions_Type = Counter32
_MrmMonRepAutoPartitions_Object = MibTableColumn
mrmMonRepAutoPartitions = _MrmMonRepAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 19),
    _MrmMonRepAutoPartitions_Type()
)
mrmMonRepAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepAutoPartitions.setStatus("mandatory")
_MrmMonRepTotalErrors_Type = Counter32
_MrmMonRepTotalErrors_Object = MibTableColumn
mrmMonRepTotalErrors = _MrmMonRepTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 20),
    _MrmMonRepTotalErrors_Type()
)
mrmMonRepTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepTotalErrors.setStatus("mandatory")
_MrmMonRepBound0_Type = Counter32
_MrmMonRepBound0_Object = MibTableColumn
mrmMonRepBound0 = _MrmMonRepBound0_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 21),
    _MrmMonRepBound0_Type()
)
mrmMonRepBound0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBound0.setStatus("mandatory")
_MrmMonRepBound1_Type = Counter32
_MrmMonRepBound1_Object = MibTableColumn
mrmMonRepBound1 = _MrmMonRepBound1_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 22),
    _MrmMonRepBound1_Type()
)
mrmMonRepBound1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBound1.setStatus("mandatory")
_MrmMonRepBound2_Type = Counter32
_MrmMonRepBound2_Object = MibTableColumn
mrmMonRepBound2 = _MrmMonRepBound2_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 23),
    _MrmMonRepBound2_Type()
)
mrmMonRepBound2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBound2.setStatus("mandatory")
_MrmMonRepBound3_Type = Counter32
_MrmMonRepBound3_Object = MibTableColumn
mrmMonRepBound3 = _MrmMonRepBound3_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 24),
    _MrmMonRepBound3_Type()
)
mrmMonRepBound3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBound3.setStatus("mandatory")
_MrmMonRepBound4_Type = Counter32
_MrmMonRepBound4_Object = MibTableColumn
mrmMonRepBound4 = _MrmMonRepBound4_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 25),
    _MrmMonRepBound4_Type()
)
mrmMonRepBound4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBound4.setStatus("mandatory")
_MrmMonRepBound5_Type = Counter32
_MrmMonRepBound5_Object = MibTableColumn
mrmMonRepBound5 = _MrmMonRepBound5_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 26),
    _MrmMonRepBound5_Type()
)
mrmMonRepBound5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBound5.setStatus("mandatory")


class _MrmMonRepAction_Type(Integer32):
    """Custom type mrmMonRepAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearCounters", 1)
    )


_MrmMonRepAction_Type.__name__ = "Integer32"
_MrmMonRepAction_Object = MibTableColumn
mrmMonRepAction = _MrmMonRepAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 27),
    _MrmMonRepAction_Type()
)
mrmMonRepAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mrmMonRepAction.setStatus("mandatory")
_MrmMonCardPackage_ObjectIdentity = ObjectIdentity
mrmMonCardPackage = _MrmMonCardPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2)
)
_MrmMonitorCardTable_Object = MibTable
mrmMonitorCardTable = _MrmMonitorCardTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mrmMonitorCardTable.setStatus("mandatory")
_MrmMonitorCardEntry_Object = MibTableRow
mrmMonitorCardEntry = _MrmMonitorCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1)
)
mrmMonitorCardEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "mrmMonCardServiceId"),
    (0, "LBHUB-MSH-MIB", "mrmMonCardIndex"),
)
if mibBuilder.loadTexts:
    mrmMonitorCardEntry.setStatus("mandatory")
_MrmMonCardServiceId_Type = Integer32
_MrmMonCardServiceId_Object = MibTableColumn
mrmMonCardServiceId = _MrmMonCardServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 1),
    _MrmMonCardServiceId_Type()
)
mrmMonCardServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardServiceId.setStatus("mandatory")
_MrmMonCardIndex_Type = Integer32
_MrmMonCardIndex_Object = MibTableColumn
mrmMonCardIndex = _MrmMonCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 2),
    _MrmMonCardIndex_Type()
)
mrmMonCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardIndex.setStatus("mandatory")
_MrmMonCardReadableFrames_Type = Counter32
_MrmMonCardReadableFrames_Object = MibTableColumn
mrmMonCardReadableFrames = _MrmMonCardReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 3),
    _MrmMonCardReadableFrames_Type()
)
mrmMonCardReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardReadableFrames.setStatus("mandatory")
_MrmMonCardUnicastFrames_Type = Counter32
_MrmMonCardUnicastFrames_Object = MibTableColumn
mrmMonCardUnicastFrames = _MrmMonCardUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 4),
    _MrmMonCardUnicastFrames_Type()
)
mrmMonCardUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardUnicastFrames.setStatus("mandatory")
_MrmMonCardMulticastFrames_Type = Counter32
_MrmMonCardMulticastFrames_Object = MibTableColumn
mrmMonCardMulticastFrames = _MrmMonCardMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 5),
    _MrmMonCardMulticastFrames_Type()
)
mrmMonCardMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardMulticastFrames.setStatus("mandatory")
_MrmMonCardBroadcastFrames_Type = Counter32
_MrmMonCardBroadcastFrames_Object = MibTableColumn
mrmMonCardBroadcastFrames = _MrmMonCardBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 6),
    _MrmMonCardBroadcastFrames_Type()
)
mrmMonCardBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBroadcastFrames.setStatus("mandatory")
_MrmMonCardReadableOctets_Type = Counter32
_MrmMonCardReadableOctets_Object = MibTableColumn
mrmMonCardReadableOctets = _MrmMonCardReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 7),
    _MrmMonCardReadableOctets_Type()
)
mrmMonCardReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardReadableOctets.setStatus("mandatory")
_MrmMonCardUnicastOctets_Type = Counter32
_MrmMonCardUnicastOctets_Object = MibTableColumn
mrmMonCardUnicastOctets = _MrmMonCardUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 8),
    _MrmMonCardUnicastOctets_Type()
)
mrmMonCardUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardUnicastOctets.setStatus("mandatory")
_MrmMonCardMulticastOctets_Type = Counter32
_MrmMonCardMulticastOctets_Object = MibTableColumn
mrmMonCardMulticastOctets = _MrmMonCardMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 9),
    _MrmMonCardMulticastOctets_Type()
)
mrmMonCardMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardMulticastOctets.setStatus("mandatory")
_MrmMonCardBroadcastOctets_Type = Counter32
_MrmMonCardBroadcastOctets_Object = MibTableColumn
mrmMonCardBroadcastOctets = _MrmMonCardBroadcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 10),
    _MrmMonCardBroadcastOctets_Type()
)
mrmMonCardBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBroadcastOctets.setStatus("mandatory")
_MrmMonCardFCSErrors_Type = Counter32
_MrmMonCardFCSErrors_Object = MibTableColumn
mrmMonCardFCSErrors = _MrmMonCardFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 11),
    _MrmMonCardFCSErrors_Type()
)
mrmMonCardFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardFCSErrors.setStatus("mandatory")
_MrmMonCardAlignmentErrors_Type = Counter32
_MrmMonCardAlignmentErrors_Object = MibTableColumn
mrmMonCardAlignmentErrors = _MrmMonCardAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 12),
    _MrmMonCardAlignmentErrors_Type()
)
mrmMonCardAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardAlignmentErrors.setStatus("mandatory")
_MrmMonCardFrameTooLongs_Type = Counter32
_MrmMonCardFrameTooLongs_Object = MibTableColumn
mrmMonCardFrameTooLongs = _MrmMonCardFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 13),
    _MrmMonCardFrameTooLongs_Type()
)
mrmMonCardFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardFrameTooLongs.setStatus("mandatory")
_MrmMonCardShortEvents_Type = Counter32
_MrmMonCardShortEvents_Object = MibTableColumn
mrmMonCardShortEvents = _MrmMonCardShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 14),
    _MrmMonCardShortEvents_Type()
)
mrmMonCardShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardShortEvents.setStatus("mandatory")
_MrmMonCardRunts_Type = Counter32
_MrmMonCardRunts_Object = MibTableColumn
mrmMonCardRunts = _MrmMonCardRunts_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 15),
    _MrmMonCardRunts_Type()
)
mrmMonCardRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardRunts.setStatus("mandatory")
_MrmMonCardLateEvents_Type = Counter32
_MrmMonCardLateEvents_Object = MibTableColumn
mrmMonCardLateEvents = _MrmMonCardLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 16),
    _MrmMonCardLateEvents_Type()
)
mrmMonCardLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardLateEvents.setStatus("mandatory")
_MrmMonCardVeryLongEvents_Type = Counter32
_MrmMonCardVeryLongEvents_Object = MibTableColumn
mrmMonCardVeryLongEvents = _MrmMonCardVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 17),
    _MrmMonCardVeryLongEvents_Type()
)
mrmMonCardVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardVeryLongEvents.setStatus("mandatory")
_MrmMonCardDataRateMismatches_Type = Counter32
_MrmMonCardDataRateMismatches_Object = MibTableColumn
mrmMonCardDataRateMismatches = _MrmMonCardDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 18),
    _MrmMonCardDataRateMismatches_Type()
)
mrmMonCardDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardDataRateMismatches.setStatus("mandatory")
_MrmMonCardAutoPartitions_Type = Counter32
_MrmMonCardAutoPartitions_Object = MibTableColumn
mrmMonCardAutoPartitions = _MrmMonCardAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 19),
    _MrmMonCardAutoPartitions_Type()
)
mrmMonCardAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardAutoPartitions.setStatus("mandatory")
_MrmMonCardTotalErrors_Type = Counter32
_MrmMonCardTotalErrors_Object = MibTableColumn
mrmMonCardTotalErrors = _MrmMonCardTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 20),
    _MrmMonCardTotalErrors_Type()
)
mrmMonCardTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardTotalErrors.setStatus("mandatory")
_MrmMonCardBound0_Type = Counter32
_MrmMonCardBound0_Object = MibTableColumn
mrmMonCardBound0 = _MrmMonCardBound0_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 21),
    _MrmMonCardBound0_Type()
)
mrmMonCardBound0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBound0.setStatus("mandatory")
_MrmMonCardBound1_Type = Counter32
_MrmMonCardBound1_Object = MibTableColumn
mrmMonCardBound1 = _MrmMonCardBound1_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 22),
    _MrmMonCardBound1_Type()
)
mrmMonCardBound1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBound1.setStatus("mandatory")
_MrmMonCardBound2_Type = Counter32
_MrmMonCardBound2_Object = MibTableColumn
mrmMonCardBound2 = _MrmMonCardBound2_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 23),
    _MrmMonCardBound2_Type()
)
mrmMonCardBound2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBound2.setStatus("mandatory")
_MrmMonCardBound3_Type = Counter32
_MrmMonCardBound3_Object = MibTableColumn
mrmMonCardBound3 = _MrmMonCardBound3_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 24),
    _MrmMonCardBound3_Type()
)
mrmMonCardBound3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBound3.setStatus("mandatory")
_MrmMonCardBound4_Type = Counter32
_MrmMonCardBound4_Object = MibTableColumn
mrmMonCardBound4 = _MrmMonCardBound4_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 25),
    _MrmMonCardBound4_Type()
)
mrmMonCardBound4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBound4.setStatus("mandatory")
_MrmMonCardBound5_Type = Counter32
_MrmMonCardBound5_Object = MibTableColumn
mrmMonCardBound5 = _MrmMonCardBound5_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 26),
    _MrmMonCardBound5_Type()
)
mrmMonCardBound5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBound5.setStatus("mandatory")


class _MrmMonCardClearCounters_Type(Integer32):
    """Custom type mrmMonCardClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearCounters", 2),
          ("noChangeCounters", 1))
    )


_MrmMonCardClearCounters_Type.__name__ = "Integer32"
_MrmMonCardClearCounters_Object = MibTableColumn
mrmMonCardClearCounters = _MrmMonCardClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 27),
    _MrmMonCardClearCounters_Type()
)
mrmMonCardClearCounters.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mrmMonCardClearCounters.setStatus("mandatory")
_MrmMonPortPackage_ObjectIdentity = ObjectIdentity
mrmMonPortPackage = _MrmMonPortPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3)
)
_MrmMonitorPortTable_Object = MibTable
mrmMonitorPortTable = _MrmMonitorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mrmMonitorPortTable.setStatus("mandatory")
_MrmMonitorPortEntry_Object = MibTableRow
mrmMonitorPortEntry = _MrmMonitorPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1)
)
mrmMonitorPortEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "mrmMonPortServiceId"),
    (0, "LBHUB-MSH-MIB", "mrmMonPortCardIndex"),
    (0, "LBHUB-MSH-MIB", "mrmMonPortIndex"),
)
if mibBuilder.loadTexts:
    mrmMonitorPortEntry.setStatus("mandatory")


class _MrmMonPortServiceId_Type(Integer32):
    """Custom type mrmMonPortServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_MrmMonPortServiceId_Type.__name__ = "Integer32"
_MrmMonPortServiceId_Object = MibTableColumn
mrmMonPortServiceId = _MrmMonPortServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 1),
    _MrmMonPortServiceId_Type()
)
mrmMonPortServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortServiceId.setStatus("mandatory")
_MrmMonPortCardIndex_Type = Integer32
_MrmMonPortCardIndex_Object = MibTableColumn
mrmMonPortCardIndex = _MrmMonPortCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 2),
    _MrmMonPortCardIndex_Type()
)
mrmMonPortCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortCardIndex.setStatus("mandatory")
_MrmMonPortIndex_Type = Integer32
_MrmMonPortIndex_Object = MibTableColumn
mrmMonPortIndex = _MrmMonPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 3),
    _MrmMonPortIndex_Type()
)
mrmMonPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortIndex.setStatus("mandatory")
_MrmMonPortReadableFrames_Type = Counter32
_MrmMonPortReadableFrames_Object = MibTableColumn
mrmMonPortReadableFrames = _MrmMonPortReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 4),
    _MrmMonPortReadableFrames_Type()
)
mrmMonPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortReadableFrames.setStatus("mandatory")
_MrmMonPortUnicastFrames_Type = Counter32
_MrmMonPortUnicastFrames_Object = MibTableColumn
mrmMonPortUnicastFrames = _MrmMonPortUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 5),
    _MrmMonPortUnicastFrames_Type()
)
mrmMonPortUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortUnicastFrames.setStatus("mandatory")
_MrmMonPortMulticastFrames_Type = Counter32
_MrmMonPortMulticastFrames_Object = MibTableColumn
mrmMonPortMulticastFrames = _MrmMonPortMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 6),
    _MrmMonPortMulticastFrames_Type()
)
mrmMonPortMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortMulticastFrames.setStatus("mandatory")
_MrmMonPortBroadcastFrames_Type = Counter32
_MrmMonPortBroadcastFrames_Object = MibTableColumn
mrmMonPortBroadcastFrames = _MrmMonPortBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 7),
    _MrmMonPortBroadcastFrames_Type()
)
mrmMonPortBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBroadcastFrames.setStatus("mandatory")
_MrmMonPortReadableOctets_Type = Counter32
_MrmMonPortReadableOctets_Object = MibTableColumn
mrmMonPortReadableOctets = _MrmMonPortReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 8),
    _MrmMonPortReadableOctets_Type()
)
mrmMonPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortReadableOctets.setStatus("mandatory")
_MrmMonPortUnicastOctets_Type = Counter32
_MrmMonPortUnicastOctets_Object = MibTableColumn
mrmMonPortUnicastOctets = _MrmMonPortUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 9),
    _MrmMonPortUnicastOctets_Type()
)
mrmMonPortUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortUnicastOctets.setStatus("mandatory")
_MrmMonPortMulticastOctets_Type = Counter32
_MrmMonPortMulticastOctets_Object = MibTableColumn
mrmMonPortMulticastOctets = _MrmMonPortMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 10),
    _MrmMonPortMulticastOctets_Type()
)
mrmMonPortMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortMulticastOctets.setStatus("mandatory")
_MrmMonPortBroadcastOctets_Type = Counter32
_MrmMonPortBroadcastOctets_Object = MibTableColumn
mrmMonPortBroadcastOctets = _MrmMonPortBroadcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 11),
    _MrmMonPortBroadcastOctets_Type()
)
mrmMonPortBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBroadcastOctets.setStatus("mandatory")
_MrmMonPortFCSErrors_Type = Counter32
_MrmMonPortFCSErrors_Object = MibTableColumn
mrmMonPortFCSErrors = _MrmMonPortFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 12),
    _MrmMonPortFCSErrors_Type()
)
mrmMonPortFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortFCSErrors.setStatus("mandatory")
_MrmMonPortAlignmentErrors_Type = Counter32
_MrmMonPortAlignmentErrors_Object = MibTableColumn
mrmMonPortAlignmentErrors = _MrmMonPortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 13),
    _MrmMonPortAlignmentErrors_Type()
)
mrmMonPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortAlignmentErrors.setStatus("mandatory")
_MrmMonPortFrameTooLongs_Type = Counter32
_MrmMonPortFrameTooLongs_Object = MibTableColumn
mrmMonPortFrameTooLongs = _MrmMonPortFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 14),
    _MrmMonPortFrameTooLongs_Type()
)
mrmMonPortFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortFrameTooLongs.setStatus("mandatory")
_MrmMonPortShortEvents_Type = Counter32
_MrmMonPortShortEvents_Object = MibTableColumn
mrmMonPortShortEvents = _MrmMonPortShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 15),
    _MrmMonPortShortEvents_Type()
)
mrmMonPortShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortShortEvents.setStatus("mandatory")
_MrmMonPortRunts_Type = Counter32
_MrmMonPortRunts_Object = MibTableColumn
mrmMonPortRunts = _MrmMonPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 16),
    _MrmMonPortRunts_Type()
)
mrmMonPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortRunts.setStatus("mandatory")
_MrmMonPortCollisions_Type = Counter32
_MrmMonPortCollisions_Object = MibTableColumn
mrmMonPortCollisions = _MrmMonPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 17),
    _MrmMonPortCollisions_Type()
)
mrmMonPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortCollisions.setStatus("mandatory")
_MrmMonPortLateEvents_Type = Counter32
_MrmMonPortLateEvents_Object = MibTableColumn
mrmMonPortLateEvents = _MrmMonPortLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 18),
    _MrmMonPortLateEvents_Type()
)
mrmMonPortLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortLateEvents.setStatus("mandatory")
_MrmMonPortVeryLongEvents_Type = Counter32
_MrmMonPortVeryLongEvents_Object = MibTableColumn
mrmMonPortVeryLongEvents = _MrmMonPortVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 19),
    _MrmMonPortVeryLongEvents_Type()
)
mrmMonPortVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortVeryLongEvents.setStatus("mandatory")
_MrmMonPortDataRateMismatches_Type = Counter32
_MrmMonPortDataRateMismatches_Object = MibTableColumn
mrmMonPortDataRateMismatches = _MrmMonPortDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 20),
    _MrmMonPortDataRateMismatches_Type()
)
mrmMonPortDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortDataRateMismatches.setStatus("mandatory")
_MrmMonPortAutoPartitions_Type = Counter32
_MrmMonPortAutoPartitions_Object = MibTableColumn
mrmMonPortAutoPartitions = _MrmMonPortAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 21),
    _MrmMonPortAutoPartitions_Type()
)
mrmMonPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortAutoPartitions.setStatus("mandatory")
_MrmMonPortTotalErrors_Type = Counter32
_MrmMonPortTotalErrors_Object = MibTableColumn
mrmMonPortTotalErrors = _MrmMonPortTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 22),
    _MrmMonPortTotalErrors_Type()
)
mrmMonPortTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortTotalErrors.setStatus("mandatory")
_MrmMonPortBound0_Type = Counter32
_MrmMonPortBound0_Object = MibTableColumn
mrmMonPortBound0 = _MrmMonPortBound0_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 23),
    _MrmMonPortBound0_Type()
)
mrmMonPortBound0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBound0.setStatus("mandatory")
_MrmMonPortBound1_Type = Counter32
_MrmMonPortBound1_Object = MibTableColumn
mrmMonPortBound1 = _MrmMonPortBound1_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 24),
    _MrmMonPortBound1_Type()
)
mrmMonPortBound1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBound1.setStatus("mandatory")
_MrmMonPortBound2_Type = Counter32
_MrmMonPortBound2_Object = MibTableColumn
mrmMonPortBound2 = _MrmMonPortBound2_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 25),
    _MrmMonPortBound2_Type()
)
mrmMonPortBound2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBound2.setStatus("mandatory")
_MrmMonPortBound3_Type = Counter32
_MrmMonPortBound3_Object = MibTableColumn
mrmMonPortBound3 = _MrmMonPortBound3_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 26),
    _MrmMonPortBound3_Type()
)
mrmMonPortBound3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBound3.setStatus("mandatory")
_MrmMonPortBound4_Type = Counter32
_MrmMonPortBound4_Object = MibTableColumn
mrmMonPortBound4 = _MrmMonPortBound4_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 27),
    _MrmMonPortBound4_Type()
)
mrmMonPortBound4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBound4.setStatus("mandatory")
_MrmMonPortBound5_Type = Counter32
_MrmMonPortBound5_Object = MibTableColumn
mrmMonPortBound5 = _MrmMonPortBound5_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 28),
    _MrmMonPortBound5_Type()
)
mrmMonPortBound5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBound5.setStatus("mandatory")
_MrmMonPortBandwidthUsed_Type = Counter32
_MrmMonPortBandwidthUsed_Object = MibTableColumn
mrmMonPortBandwidthUsed = _MrmMonPortBandwidthUsed_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 29),
    _MrmMonPortBandwidthUsed_Type()
)
mrmMonPortBandwidthUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBandwidthUsed.setStatus("mandatory")
_MrmMonPortErrorsPer10000Packets_Type = Counter32
_MrmMonPortErrorsPer10000Packets_Object = MibTableColumn
mrmMonPortErrorsPer10000Packets = _MrmMonPortErrorsPer10000Packets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 30),
    _MrmMonPortErrorsPer10000Packets_Type()
)
mrmMonPortErrorsPer10000Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortErrorsPer10000Packets.setStatus("mandatory")


class _MrmMonPortClearCounters_Type(Integer32):
    """Custom type mrmMonPortClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearCounters", 2),
          ("noChangeCounters", 1))
    )


_MrmMonPortClearCounters_Type.__name__ = "Integer32"
_MrmMonPortClearCounters_Object = MibTableColumn
mrmMonPortClearCounters = _MrmMonPortClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 31),
    _MrmMonPortClearCounters_Type()
)
mrmMonPortClearCounters.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mrmMonPortClearCounters.setStatus("mandatory")
_MrmMonPortLastAddress_Type = OctetString
_MrmMonPortLastAddress_Object = MibTableColumn
mrmMonPortLastAddress = _MrmMonPortLastAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 32),
    _MrmMonPortLastAddress_Type()
)
mrmMonPortLastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortLastAddress.setStatus("mandatory")
_MrmMonPortAddressChanges_Type = Counter32
_MrmMonPortAddressChanges_Object = MibTableColumn
mrmMonPortAddressChanges = _MrmMonPortAddressChanges_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 33),
    _MrmMonPortAddressChanges_Type()
)
mrmMonPortAddressChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortAddressChanges.setStatus("mandatory")
_MrmMonDummyPackage_ObjectIdentity = ObjectIdentity
mrmMonDummyPackage = _MrmMonDummyPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 4)
)
_TrafficLevel_Type = Counter32
_TrafficLevel_Object = MibScalar
trafficLevel = _TrafficLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 4, 1),
    _TrafficLevel_Type()
)
trafficLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficLevel.setStatus("mandatory")
_ErrorFrames_Type = Counter32
_ErrorFrames_Object = MibScalar
errorFrames = _ErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 4, 2),
    _ErrorFrames_Type()
)
errorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorFrames.setStatus("mandatory")
_BridgeMgmt_ObjectIdentity = ObjectIdentity
bridgeMgmt = _BridgeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 18)
)
_Fault_ObjectIdentity = ObjectIdentity
fault = _Fault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 19)
)


class _FaultModifiedFlag_Type(Integer32):
    """Custom type faultModifiedFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean-read", 1),
          ("modified", 2))
    )


_FaultModifiedFlag_Type.__name__ = "Integer32"
_FaultModifiedFlag_Object = MibScalar
faultModifiedFlag = _FaultModifiedFlag_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 19, 1),
    _FaultModifiedFlag_Type()
)
faultModifiedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultModifiedFlag.setStatus("mandatory")
_FaultTable_Object = MibTable
faultTable = _FaultTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 19, 2)
)
if mibBuilder.loadTexts:
    faultTable.setStatus("mandatory")
_FaultEntry_Object = MibTableRow
faultEntry = _FaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 19, 2, 1)
)
faultEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "faultIndex"),
)
if mibBuilder.loadTexts:
    faultEntry.setStatus("mandatory")
_FaultIndex_Type = Integer32
_FaultIndex_Object = MibScalar
faultIndex = _FaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 19, 2, 1, 1),
    _FaultIndex_Type()
)
faultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultIndex.setStatus("mandatory")
_FaultErrorNumber_Type = Integer32
_FaultErrorNumber_Object = MibScalar
faultErrorNumber = _FaultErrorNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 19, 2, 1, 2),
    _FaultErrorNumber_Type()
)
faultErrorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultErrorNumber.setStatus("mandatory")
_FaultTimeStamp_Type = TimeTicks
_FaultTimeStamp_Object = MibScalar
faultTimeStamp = _FaultTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 19, 2, 1, 3),
    _FaultTimeStamp_Type()
)
faultTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultTimeStamp.setStatus("mandatory")
_FaultRestartCount_Type = Integer32
_FaultRestartCount_Object = MibScalar
faultRestartCount = _FaultRestartCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 19, 2, 1, 4),
    _FaultRestartCount_Type()
)
faultRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultRestartCount.setStatus("mandatory")
_Poll_ObjectIdentity = ObjectIdentity
poll = _Poll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 20)
)
_PollTable_Object = MibTable
pollTable = _PollTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1)
)
if mibBuilder.loadTexts:
    pollTable.setStatus("mandatory")
_PollTableEntry_Object = MibTableRow
pollTableEntry = _PollTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1)
)
pollTableEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "pollIndex"),
)
if mibBuilder.loadTexts:
    pollTableEntry.setStatus("mandatory")


class _PollIndex_Type(Integer32):
    """Custom type pollIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PollIndex_Type.__name__ = "Integer32"
_PollIndex_Object = MibTableColumn
pollIndex = _PollIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 1),
    _PollIndex_Type()
)
pollIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollIndex.setStatus("mandatory")


class _PollAddress_Type(DisplayString):
    """Custom type pollAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_PollAddress_Type.__name__ = "DisplayString"
_PollAddress_Object = MibTableColumn
pollAddress = _PollAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 2),
    _PollAddress_Type()
)
pollAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pollAddress.setStatus("mandatory")


class _PollProtocol_Type(Integer32):
    """Custom type pollProtocol based on Integer32"""
    defaultValue = 1

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
        *(("ip", 2),
          ("ipx", 3),
          ("learn", 4),
          ("llc", 5),
          ("unknown", 1))
    )


_PollProtocol_Type.__name__ = "Integer32"
_PollProtocol_Object = MibTableColumn
pollProtocol = _PollProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 3),
    _PollProtocol_Type()
)
pollProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pollProtocol.setStatus("mandatory")


class _PollRate_Type(Integer32):
    """Custom type pollRate based on Integer32"""
    defaultValue = 1

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
        *(("every-30-minutes", 5),
          ("every-30-seconds", 2),
          ("every-5-minutes", 4),
          ("every-hour", 6),
          ("every-minute", 3),
          ("once-only", 1))
    )


_PollRate_Type.__name__ = "Integer32"
_PollRate_Object = MibTableColumn
pollRate = _PollRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 4),
    _PollRate_Type()
)
pollRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pollRate.setStatus("mandatory")


class _PollTargetType_Type(Integer32):
    """Custom type pollTargetType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("file-server", 2),
          ("other", 1))
    )


_PollTargetType_Type.__name__ = "Integer32"
_PollTargetType_Object = MibTableColumn
pollTargetType = _PollTargetType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 5),
    _PollTargetType_Type()
)
pollTargetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pollTargetType.setStatus("mandatory")


class _PollLastPollSent_Type(TimeTicks):
    """Custom type pollLastPollSent based on TimeTicks"""
    defaultValue = 0


_PollLastPollSent_Object = MibTableColumn
pollLastPollSent = _PollLastPollSent_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 6),
    _PollLastPollSent_Type()
)
pollLastPollSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollLastPollSent.setStatus("mandatory")


class _PollRoundTripTime_Type(Integer32):
    """Custom type pollRoundTripTime based on Integer32"""
    defaultValue = 0


_PollRoundTripTime_Object = MibTableColumn
pollRoundTripTime = _PollRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 7),
    _PollRoundTripTime_Type()
)
pollRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollRoundTripTime.setStatus("mandatory")


class _PollInformation_Type(DisplayString):
    """Custom type pollInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 500),
    )


_PollInformation_Type.__name__ = "DisplayString"
_PollInformation_Object = MibTableColumn
pollInformation = _PollInformation_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 8),
    _PollInformation_Type()
)
pollInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollInformation.setStatus("mandatory")


class _PollAlarmIndex_Type(Integer32):
    """Custom type pollAlarmIndex based on Integer32"""
    defaultValue = 0


_PollAlarmIndex_Object = MibTableColumn
pollAlarmIndex = _PollAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 9),
    _PollAlarmIndex_Type()
)
pollAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollAlarmIndex.setStatus("mandatory")
_PollOwner_Type = DisplayString
_PollOwner_Object = MibTableColumn
pollOwner = _PollOwner_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 10),
    _PollOwner_Type()
)
pollOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pollOwner.setStatus("mandatory")


class _PollRowStatus_Type(Integer32):
    """Custom type pollRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_PollRowStatus_Type.__name__ = "Integer32"
_PollRowStatus_Object = MibTableColumn
pollRowStatus = _PollRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 11),
    _PollRowStatus_Type()
)
pollRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pollRowStatus.setStatus("mandatory")


class _PollNextFreeIndex_Type(Integer32):
    """Custom type pollNextFreeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PollNextFreeIndex_Type.__name__ = "Integer32"
_PollNextFreeIndex_Object = MibScalar
pollNextFreeIndex = _PollNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 2),
    _PollNextFreeIndex_Type()
)
pollNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollNextFreeIndex.setStatus("mandatory")
_PowerSupply_ObjectIdentity = ObjectIdentity
powerSupply = _PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 21)
)
_NetBuilder_mib_ObjectIdentity = ObjectIdentity
netBuilder_mib = _NetBuilder_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 11)
)
_LBridgeECS_mib_ObjectIdentity = ObjectIdentity
lBridgeECS_mib = _LBridgeECS_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 12)
)
_DeskMan_mib_ObjectIdentity = ObjectIdentity
deskMan_mib = _DeskMan_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 13)
)
_LinkBuilderMSH_mib_ObjectIdentity = ObjectIdentity
linkBuilderMSH_mib = _LinkBuilderMSH_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 14)
)
_SnmpDot3RpMauMgt_ObjectIdentity = ObjectIdentity
snmpDot3RpMauMgt = _SnmpDot3RpMauMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 14, 2)
)
_RpMauBasicGroup_ObjectIdentity = ObjectIdentity
rpMauBasicGroup = _RpMauBasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 14, 2, 1)
)
_RpMauTable_Object = MibTable
rpMauTable = _RpMauTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rpMauTable.setStatus("mandatory")
_RpMauEntry_Object = MibTableRow
rpMauEntry = _RpMauEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 2, 1, 1, 1)
)
rpMauEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "rpMauGroupIndex"),
    (0, "LBHUB-MSH-MIB", "rpMauPortIndex"),
    (0, "LBHUB-MSH-MIB", "rpMauIndex"),
)
if mibBuilder.loadTexts:
    rpMauEntry.setStatus("mandatory")


class _RpMauGroupIndex_Type(Integer32):
    """Custom type rpMauGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RpMauGroupIndex_Type.__name__ = "Integer32"
_RpMauGroupIndex_Object = MibTableColumn
rpMauGroupIndex = _RpMauGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 2, 1, 1, 1, 1),
    _RpMauGroupIndex_Type()
)
rpMauGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauGroupIndex.setStatus("mandatory")


class _RpMauPortIndex_Type(Integer32):
    """Custom type rpMauPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RpMauPortIndex_Type.__name__ = "Integer32"
_RpMauPortIndex_Object = MibTableColumn
rpMauPortIndex = _RpMauPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 2, 1, 1, 1, 2),
    _RpMauPortIndex_Type()
)
rpMauPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauPortIndex.setStatus("mandatory")


class _RpMauIndex_Type(Integer32):
    """Custom type rpMauIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RpMauIndex_Type.__name__ = "Integer32"
_RpMauIndex_Object = MibTableColumn
rpMauIndex = _RpMauIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 2, 1, 1, 1, 3),
    _RpMauIndex_Type()
)
rpMauIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauIndex.setStatus("mandatory")


class _RpMauType_Type(Integer32):
    """Custom type rpMauType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7,
              8,
              9,
              10,
              14,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("aui", 7),
          ("foirl", 9),
          ("other", 1),
          ("tenbase2", 10),
          ("tenbase5", 8),
          ("tenbaseFB", 17),
          ("tenbaseFL", 18),
          ("tenbaseFP", 16),
          ("tenbaseT", 14),
          ("unknown", 2))
    )


_RpMauType_Type.__name__ = "Integer32"
_RpMauType_Object = MibTableColumn
rpMauType = _RpMauType_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 2, 1, 1, 1, 4),
    _RpMauType_Type()
)
rpMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauType.setStatus("mandatory")


class _RpMauAdminState_Type(Integer32):
    """Custom type rpMauAdminState based on Integer32"""
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
        *(("operational", 3),
          ("other", 1),
          ("reset", 6),
          ("shutdown", 5),
          ("standby", 4),
          ("unknown", 2))
    )


_RpMauAdminState_Type.__name__ = "Integer32"
_RpMauAdminState_Object = MibTableColumn
rpMauAdminState = _RpMauAdminState_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 2, 1, 1, 1, 5),
    _RpMauAdminState_Type()
)
rpMauAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpMauAdminState.setStatus("mandatory")


class _RpMauMediaAvailable_Type(Integer32):
    """Custom type rpMauMediaAvailable based on Integer32"""
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
        *(("available", 3),
          ("invalidSignal", 6),
          ("notAvailable", 4),
          ("other", 1),
          ("remoteFault", 5),
          ("unknown", 2))
    )


_RpMauMediaAvailable_Type.__name__ = "Integer32"
_RpMauMediaAvailable_Object = MibTableColumn
rpMauMediaAvailable = _RpMauMediaAvailable_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 2, 1, 1, 1, 6),
    _RpMauMediaAvailable_Type()
)
rpMauMediaAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauMediaAvailable.setStatus("mandatory")
_RpMauLostMedias_Type = Counter32
_RpMauLostMedias_Object = MibTableColumn
rpMauLostMedias = _RpMauLostMedias_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 2, 1, 1, 1, 7),
    _RpMauLostMedias_Type()
)
rpMauLostMedias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauLostMedias.setStatus("mandatory")


class _RpMauJabberState_Type(Integer32):
    """Custom type rpMauJabberState based on Integer32"""
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
        *(("jabbering", 4),
          ("noJabber", 3),
          ("other", 1),
          ("unknown", 2))
    )


_RpMauJabberState_Type.__name__ = "Integer32"
_RpMauJabberState_Object = MibTableColumn
rpMauJabberState = _RpMauJabberState_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 2, 1, 1, 1, 8),
    _RpMauJabberState_Type()
)
rpMauJabberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauJabberState.setStatus("mandatory")
_RpMauJabbers_Type = Counter32
_RpMauJabbers_Object = MibTableColumn
rpMauJabbers = _RpMauJabbers_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 2, 1, 1, 1, 9),
    _RpMauJabbers_Type()
)
rpMauJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauJabbers.setStatus("mandatory")
_RingBuilder_ObjectIdentity = ObjectIdentity
ringBuilder = _RingBuilder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 14, 3)
)
_RingBuilderTable_Object = MibTable
ringBuilderTable = _RingBuilderTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 1)
)
if mibBuilder.loadTexts:
    ringBuilderTable.setStatus("mandatory")
_RingBuilderTableEntry_Object = MibTableRow
ringBuilderTableEntry = _RingBuilderTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 1, 1)
)
ringBuilderTableEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "rbServiceId"),
)
if mibBuilder.loadTexts:
    ringBuilderTableEntry.setStatus("mandatory")
_RbServiceId_Type = Integer32
_RbServiceId_Object = MibTableColumn
rbServiceId = _RbServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 1, 1, 1),
    _RbServiceId_Type()
)
rbServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbServiceId.setStatus("mandatory")


class _RbRingInMedia_Type(Integer32):
    """Custom type rbRingInMedia based on Integer32"""
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
        *(("fiber", 4),
          ("shieldedTp", 3),
          ("unknown", 1),
          ("unshieldedTp", 2))
    )


_RbRingInMedia_Type.__name__ = "Integer32"
_RbRingInMedia_Object = MibTableColumn
rbRingInMedia = _RbRingInMedia_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 1, 1, 3),
    _RbRingInMedia_Type()
)
rbRingInMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRingInMedia.setStatus("mandatory")


class _RbRingInMode_Type(Integer32):
    """Custom type rbRingInMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failSafe", 3),
          ("openRing", 1),
          ("wrapRing", 2))
    )


_RbRingInMode_Type.__name__ = "Integer32"
_RbRingInMode_Object = MibTableColumn
rbRingInMode = _RbRingInMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 1, 1, 4),
    _RbRingInMode_Type()
)
rbRingInMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRingInMode.setStatus("mandatory")


class _RbRingInState_Type(Integer32):
    """Custom type rbRingInState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("wrap", 2))
    )


_RbRingInState_Type.__name__ = "Integer32"
_RbRingInState_Object = MibTableColumn
rbRingInState = _RbRingInState_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 1, 1, 5),
    _RbRingInState_Type()
)
rbRingInState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRingInState.setStatus("mandatory")


class _RbRingOutMedia_Type(Integer32):
    """Custom type rbRingOutMedia based on Integer32"""
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
        *(("fiber", 4),
          ("shieldedTp", 3),
          ("unknown", 1),
          ("unshieldedTp", 2))
    )


_RbRingOutMedia_Type.__name__ = "Integer32"
_RbRingOutMedia_Object = MibTableColumn
rbRingOutMedia = _RbRingOutMedia_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 1, 1, 6),
    _RbRingOutMedia_Type()
)
rbRingOutMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRingOutMedia.setStatus("mandatory")


class _RbRingOutMode_Type(Integer32):
    """Custom type rbRingOutMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failSafe", 3),
          ("openRing", 1),
          ("wrapRing", 2))
    )


_RbRingOutMode_Type.__name__ = "Integer32"
_RbRingOutMode_Object = MibTableColumn
rbRingOutMode = _RbRingOutMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 1, 1, 7),
    _RbRingOutMode_Type()
)
rbRingOutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRingOutMode.setStatus("mandatory")


class _RbRingOutState_Type(Integer32):
    """Custom type rbRingOutState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("wrap", 2))
    )


_RbRingOutState_Type.__name__ = "Integer32"
_RbRingOutState_Object = MibTableColumn
rbRingOutState = _RbRingOutState_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 1, 1, 8),
    _RbRingOutState_Type()
)
rbRingOutState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRingOutState.setStatus("mandatory")


class _RbMode_Type(Integer32):
    """Custom type rbMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("repeater", 2))
    )


_RbMode_Type.__name__ = "Integer32"
_RbMode_Object = MibTableColumn
rbMode = _RbMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 1, 1, 9),
    _RbMode_Type()
)
rbMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbMode.setStatus("mandatory")


class _RbTest_Type(Integer32):
    """Custom type rbTest based on Integer32"""
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
        *(("fail", 5),
          ("noTest", 1),
          ("pass", 4),
          ("test", 2),
          ("testing", 3))
    )


_RbTest_Type.__name__ = "Integer32"
_RbTest_Object = MibTableColumn
rbTest = _RbTest_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 1, 1, 10),
    _RbTest_Type()
)
rbTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbTest.setStatus("mandatory")


class _RbDRIState_Type(Integer32):
    """Custom type rbDRIState based on Integer32"""
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
          ("enabledWithLock", 3))
    )


_RbDRIState_Type.__name__ = "Integer32"
_RbDRIState_Object = MibTableColumn
rbDRIState = _RbDRIState_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 1, 1, 11),
    _RbDRIState_Type()
)
rbDRIState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbDRIState.setStatus("mandatory")
_RingMauPortTable_Object = MibTable
ringMauPortTable = _RingMauPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 2)
)
if mibBuilder.loadTexts:
    ringMauPortTable.setStatus("mandatory")
_RingMauPortTableEntry_Object = MibTableRow
ringMauPortTableEntry = _RingMauPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 2, 1)
)
ringMauPortTableEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "rbMauServiceId"),
    (0, "LBHUB-MSH-MIB", "rbMauSlot"),
    (0, "LBHUB-MSH-MIB", "rbMauPort"),
)
if mibBuilder.loadTexts:
    ringMauPortTableEntry.setStatus("mandatory")
_RbMauServiceId_Type = Integer32
_RbMauServiceId_Object = MibTableColumn
rbMauServiceId = _RbMauServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 2, 1, 1),
    _RbMauServiceId_Type()
)
rbMauServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMauServiceId.setStatus("mandatory")
_RbMauSlot_Type = Integer32
_RbMauSlot_Object = MibTableColumn
rbMauSlot = _RbMauSlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 2, 1, 2),
    _RbMauSlot_Type()
)
rbMauSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMauSlot.setStatus("mandatory")
_RbMauPort_Type = Integer32
_RbMauPort_Object = MibTableColumn
rbMauPort = _RbMauPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 2, 1, 3),
    _RbMauPort_Type()
)
rbMauPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMauPort.setStatus("mandatory")


class _RbMauMedia_Type(Integer32):
    """Custom type rbMauMedia based on Integer32"""
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
        *(("fiber", 4),
          ("shieldedTp", 3),
          ("twistedPair", 5),
          ("unknown", 1),
          ("unshieldedTp", 2))
    )


_RbMauMedia_Type.__name__ = "Integer32"
_RbMauMedia_Object = MibTableColumn
rbMauMedia = _RbMauMedia_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 2, 1, 4),
    _RbMauMedia_Type()
)
rbMauMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMauMedia.setStatus("mandatory")


class _RbMauPortAdminState_Type(Integer32):
    """Custom type rbMauPortAdminState based on Integer32"""
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


_RbMauPortAdminState_Type.__name__ = "Integer32"
_RbMauPortAdminState_Object = MibTableColumn
rbMauPortAdminState = _RbMauPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 2, 1, 5),
    _RbMauPortAdminState_Type()
)
rbMauPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbMauPortAdminState.setStatus("mandatory")


class _RbMauPortAttachState_Type(Integer32):
    """Custom type rbMauPortAttachState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("present", 2))
    )


_RbMauPortAttachState_Type.__name__ = "Integer32"
_RbMauPortAttachState_Object = MibTableColumn
rbMauPortAttachState = _RbMauPortAttachState_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 2, 1, 6),
    _RbMauPortAttachState_Type()
)
rbMauPortAttachState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMauPortAttachState.setStatus("mandatory")


class _RbMauPortZDLState_Type(Integer32):
    """Custom type rbMauPortZDLState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_RbMauPortZDLState_Type.__name__ = "Integer32"
_RbMauPortZDLState_Object = MibTableColumn
rbMauPortZDLState = _RbMauPortZDLState_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 2, 1, 8),
    _RbMauPortZDLState_Type()
)
rbMauPortZDLState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbMauPortZDLState.setStatus("mandatory")


class _RbMauPortDisableReason_Type(Integer32):
    """Custom type rbMauPortDisableReason based on Integer32"""
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
        *(("disabledByDRI", 4),
          ("disabledByMgmt", 2),
          ("disabledByZDL", 3),
          ("none", 1))
    )


_RbMauPortDisableReason_Type.__name__ = "Integer32"
_RbMauPortDisableReason_Object = MibTableColumn
rbMauPortDisableReason = _RbMauPortDisableReason_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 2, 1, 9),
    _RbMauPortDisableReason_Type()
)
rbMauPortDisableReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMauPortDisableReason.setStatus("mandatory")
_RingBuilderMACTable_Object = MibTable
ringBuilderMACTable = _RingBuilderMACTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 3)
)
if mibBuilder.loadTexts:
    ringBuilderMACTable.setStatus("mandatory")
_RingBuilderMACTableEntry_Object = MibTableRow
ringBuilderMACTableEntry = _RingBuilderMACTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 3, 1)
)
ringBuilderMACTableEntry.setIndexNames(
    (0, "LBHUB-MSH-MIB", "rbMACServiceId"),
    (0, "LBHUB-MSH-MIB", "rbMACinstance"),
)
if mibBuilder.loadTexts:
    ringBuilderMACTableEntry.setStatus("mandatory")
_RbMACServiceId_Type = Integer32
_RbMACServiceId_Object = MibTableColumn
rbMACServiceId = _RbMACServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 3, 1, 1),
    _RbMACServiceId_Type()
)
rbMACServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMACServiceId.setStatus("mandatory")
_RbMACinstance_Type = Integer32
_RbMACinstance_Object = MibTableColumn
rbMACinstance = _RbMACinstance_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 3, 1, 2),
    _RbMACinstance_Type()
)
rbMACinstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMACinstance.setStatus("mandatory")
_RbMACAddress_Type = PhysAddress
_RbMACAddress_Object = MibTableColumn
rbMACAddress = _RbMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 14, 3, 3, 1, 3),
    _RbMACAddress_Type()
)
rbMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMACAddress.setStatus("mandatory")
_LinkBuilderFMS_mib_ObjectIdentity = ObjectIdentity
linkBuilderFMS_mib = _LinkBuilderFMS_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 15)
)
_LinkBuilderFDDI_wghub_mib_ObjectIdentity = ObjectIdentity
linkBuilderFDDI_wghub_mib = _LinkBuilderFDDI_wghub_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 16)
)
_LinkSwitch_mib_ObjectIdentity = ObjectIdentity
linkSwitch_mib = _LinkSwitch_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 17)
)

# Managed Objects groups


# Notification objects

risingAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 0, 1)
)
risingAlarm.setObjects(
      *(("LBHUB-MSH-MIB", "alarmIndex"),
        ("LBHUB-MSH-MIB", "alarmVariable"),
        ("LBHUB-MSH-MIB", "alarmSampleType"),
        ("LBHUB-MSH-MIB", "alarmValue"),
        ("LBHUB-MSH-MIB", "alarmRisingThreshold"))
)
if mibBuilder.loadTexts:
    risingAlarm.setStatus(
        ""
    )

fallingAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 0, 2)
)
fallingAlarm.setObjects(
      *(("LBHUB-MSH-MIB", "alarmIndex"),
        ("LBHUB-MSH-MIB", "alarmVariable"),
        ("LBHUB-MSH-MIB", "alarmSampleType"),
        ("LBHUB-MSH-MIB", "alarmValue"),
        ("LBHUB-MSH-MIB", "alarmFallingThreshold"))
)
if mibBuilder.loadTexts:
    fallingAlarm.setStatus(
        ""
    )

rptrHealth = NotificationType(
    (1, 3, 6, 1, 2, 1, 22, 0, 1)
)
rptrHealth.setObjects(
    ("LBHUB-MSH-MIB", "rptrOperStatus")
)
if mibBuilder.loadTexts:
    rptrHealth.setStatus(
        ""
    )

rptrGroupChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 22, 0, 2)
)
rptrGroupChange.setObjects(
    ("LBHUB-MSH-MIB", "rptrGroupIndex")
)
if mibBuilder.loadTexts:
    rptrGroupChange.setStatus(
        ""
    )

heartbeatEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 13)
)
if mibBuilder.loadTexts:
    heartbeatEvent.setStatus(
        ""
    )

localManagementUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 14)
)
if mibBuilder.loadTexts:
    localManagementUpdate.setStatus(
        ""
    )

securityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 15)
)
securityViolation.setObjects(
      *(("LBHUB-MSH-MIB", "ascUserNameForLastAttemptedLogin"),
        ("LBHUB-MSH-MIB", "ascLoginStatus"))
)
if mibBuilder.loadTexts:
    securityViolation.setStatus(
        ""
    )

gaugesThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 16)
)
gaugesThresholdTrap.setObjects(
      *(("LBHUB-MSH-MIB", "gaugeItemId"),
        ("LBHUB-MSH-MIB", "gaugeThresholdLevel"),
        ("LBHUB-MSH-MIB", "gaugeSamplePeriod"),
        ("LBHUB-MSH-MIB", "gaugeSamplesPerAverage"))
)
if mibBuilder.loadTexts:
    gaugesThresholdTrap.setStatus(
        ""
    )

gaugesRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 17)
)
gaugesRecoveryTrap.setObjects(
      *(("LBHUB-MSH-MIB", "gaugeItemId"),
        ("LBHUB-MSH-MIB", "gaugeRecoveryLevel"),
        ("LBHUB-MSH-MIB", "gaugeSamplePeriod"),
        ("LBHUB-MSH-MIB", "gaugeSamplesPerAverage"))
)
if mibBuilder.loadTexts:
    gaugesRecoveryTrap.setStatus(
        ""
    )

slFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 18)
)
slFailed.setObjects(
    ("LBHUB-MSH-MIB", "slLoadStatus")
)
if mibBuilder.loadTexts:
    slFailed.setStatus(
        ""
    )

estStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 19)
)
if mibBuilder.loadTexts:
    estStateChange.setStatus(
        ""
    )

estTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 20)
)
if mibBuilder.loadTexts:
    estTableFull.setStatus(
        ""
    )

phyEntityInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 27)
)
phyEntityInserted.setObjects(
      *(("LBHUB-MSH-MIB", "phyServiceType"),
        ("LBHUB-MSH-MIB", "phyEntityType"),
        ("LBHUB-MSH-MIB", "phyServiceId"),
        ("LBHUB-MSH-MIB", "phyNumberOfPorts"),
        ("LBHUB-MSH-MIB", "phyEntityName"))
)
if mibBuilder.loadTexts:
    phyEntityInserted.setStatus(
        ""
    )

phyEntityRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 28)
)
phyEntityRemoved.setObjects(
      *(("LBHUB-MSH-MIB", "phyServiceId"),
        ("LBHUB-MSH-MIB", "phyEntityName"))
)
if mibBuilder.loadTexts:
    phyEntityRemoved.setStatus(
        ""
    )

phyFacilityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 29)
)
phyFacilityChanged.setObjects(
      *(("LBHUB-MSH-MIB", "phyServiceId"),
        ("LBHUB-MSH-MIB", "fcType"),
        ("LBHUB-MSH-MIB", "fcConnection"))
)
if mibBuilder.loadTexts:
    phyFacilityChanged.setStatus(
        ""
    )

serviceEntityAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 30)
)
serviceEntityAdded.setObjects(
    ("LBHUB-MSH-MIB", "phyServiceId")
)
if mibBuilder.loadTexts:
    serviceEntityAdded.setStatus(
        ""
    )

serviceEntityRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 31)
)
serviceEntityRemoved.setObjects(
    ("LBHUB-MSH-MIB", "phyServiceId")
)
if mibBuilder.loadTexts:
    serviceEntityRemoved.setStatus(
        ""
    )

physicalStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 32)
)
physicalStateChange.setObjects(
      *(("LBHUB-MSH-MIB", "phyServiceId"),
        ("LBHUB-MSH-MIB", "phyEntityState"))
)
if mibBuilder.loadTexts:
    physicalStateChange.setStatus(
        ""
    )

psuCapacityExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 33)
)
if mibBuilder.loadTexts:
    psuCapacityExceeded.setStatus(
        ""
    )

tempStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 34)
)
tempStateChange.setObjects(
    ("LBHUB-MSH-MIB", "tempSensorOutput")
)
if mibBuilder.loadTexts:
    tempStateChange.setStatus(
        ""
    )

statusInputStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 35)
)
statusInputStateChange.setObjects(
      *(("LBHUB-MSH-MIB", "statusInputState"),
        ("LBHUB-MSH-MIB", "statusName"))
)
if mibBuilder.loadTexts:
    statusInputStateChange.setStatus(
        ""
    )

mrmStationLearnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 36)
)
mrmStationLearnTrap.setObjects(
      *(("LBHUB-MSH-MIB", "mrmSecLearnMode"),
        ("LBHUB-MSH-MIB", "mrmSecMACAddress"))
)
if mibBuilder.loadTexts:
    mrmStationLearnTrap.setStatus(
        ""
    )

mrmSecurityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 37)
)
mrmSecurityTrap.setObjects(
    ("LBHUB-MSH-MIB", "mrmSecPortState")
)
if mibBuilder.loadTexts:
    mrmSecurityTrap.setStatus(
        ""
    )

repPartitionStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 38)
)
repPartitionStateChange.setObjects(
    ("LBHUB-MSH-MIB", "mrmPortAutoPartitionState")
)
if mibBuilder.loadTexts:
    repPartitionStateChange.setStatus(
        ""
    )

repLinkStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 39)
)
repLinkStateChange.setObjects(
    ("LBHUB-MSH-MIB", "mrmPortLinkState")
)
if mibBuilder.loadTexts:
    repLinkStateChange.setStatus(
        ""
    )

repAdminStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 40)
)
repAdminStateChange.setObjects(
    ("LBHUB-MSH-MIB", "mrmPortAdminStatus")
)
if mibBuilder.loadTexts:
    repAdminStateChange.setStatus(
        ""
    )

repPortTopUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 41)
)
repPortTopUsage.setObjects(
      *(("LBHUB-MSH-MIB", "mrmMonPortBandwidthUsed"),
        ("LBHUB-MSH-MIB", "gaugeThresholdLevel"),
        ("LBHUB-MSH-MIB", "gaugeSamplePeriod"),
        ("LBHUB-MSH-MIB", "gaugeSamplesPerAverage"))
)
if mibBuilder.loadTexts:
    repPortTopUsage.setStatus(
        ""
    )

repPortErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 42)
)
repPortErrors.setObjects(
      *(("LBHUB-MSH-MIB", "mrmMonPortErrorsPer10000Packets"),
        ("LBHUB-MSH-MIB", "gaugeThresholdLevel"),
        ("LBHUB-MSH-MIB", "gaugeSamplePeriod"),
        ("LBHUB-MSH-MIB", "gaugeSamplesPerAverage"))
)
if mibBuilder.loadTexts:
    repPortErrors.setStatus(
        ""
    )

resResilienceSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 43)
)
resResilienceSwitch.setObjects(
      *(("LBHUB-MSH-MIB", "resMainState"),
        ("LBHUB-MSH-MIB", "resStandbyState"))
)
if mibBuilder.loadTexts:
    resResilienceSwitch.setStatus(
        ""
    )

resStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 44)
)
resStateChange.setObjects(
      *(("LBHUB-MSH-MIB", "resMainState"),
        ("LBHUB-MSH-MIB", "resStandbyState"))
)
if mibBuilder.loadTexts:
    resStateChange.setStatus(
        ""
    )

a3ComRingTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 45)
)
a3ComRingTopologyChange.setObjects(
    ("LBHUB-MSH-MIB", "a3ComRingMapChangeTime")
)
if mibBuilder.loadTexts:
    a3ComRingTopologyChange.setStatus(
        ""
    )

a3ComRingStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 46)
)
a3ComRingStateChange.setObjects(
    ("LBHUB-MSH-MIB", "a3ComRingState")
)
if mibBuilder.loadTexts:
    a3ComRingStateChange.setStatus(
        ""
    )

a3ComRingBackupStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 47)
)
a3ComRingBackupStateChange.setObjects(
    ("LBHUB-MSH-MIB", "a3ComRingBackupState")
)
if mibBuilder.loadTexts:
    a3ComRingBackupStateChange.setStatus(
        ""
    )

a3ComRingWrapChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 48)
)
a3ComRingWrapChange.setObjects(
    ("LBHUB-MSH-MIB", "a3ComRingWrapState")
)
if mibBuilder.loadTexts:
    a3ComRingWrapChange.setStatus(
        ""
    )

a3ComAttachStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 49)
)
a3ComAttachStateChange.setObjects(
    ("LBHUB-MSH-MIB", "rbMauPortAttachState")
)
if mibBuilder.loadTexts:
    a3ComAttachStateChange.setStatus(
        ""
    )

rbRingInStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 50)
)
rbRingInStateChange.setObjects(
    ("LBHUB-MSH-MIB", "rbRingInState")
)
if mibBuilder.loadTexts:
    rbRingInStateChange.setStatus(
        ""
    )

rbRingOutStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 51)
)
rbRingOutStateChange.setObjects(
    ("LBHUB-MSH-MIB", "rbRingOutState")
)
if mibBuilder.loadTexts:
    rbRingOutStateChange.setStatus(
        ""
    )

rbMauPortStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 60)
)
rbMauPortStateChange.setObjects(
      *(("LBHUB-MSH-MIB", "rbMauPortAdminState"),
        ("LBHUB-MSH-MIB", "rbMauPortDisableReason"))
)
if mibBuilder.loadTexts:
    rbMauPortStateChange.setStatus(
        ""
    )

pollTableSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 61)
)
pollTableSuccessTrap.setObjects(
      *(("LBHUB-MSH-MIB", "pollAddress"),
        ("LBHUB-MSH-MIB", "pollProtocol"),
        ("LBHUB-MSH-MIB", "pollTargetType"))
)
if mibBuilder.loadTexts:
    pollTableSuccessTrap.setStatus(
        ""
    )

pollTableFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 62)
)
pollTableFailedTrap.setObjects(
      *(("LBHUB-MSH-MIB", "pollAddress"),
        ("LBHUB-MSH-MIB", "pollProtocol"),
        ("LBHUB-MSH-MIB", "pollTargetType"))
)
if mibBuilder.loadTexts:
    pollTableFailedTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LBHUB-MSH-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
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
       "rmon": rmon,
       "risingAlarm": risingAlarm,
       "fallingAlarm": fallingAlarm,
       "statistics": statistics,
       "history": history,
       "alarm": alarm,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmIndex": alarmIndex,
       "alarmInterval": alarmInterval,
       "alarmVariable": alarmVariable,
       "alarmSampleType": alarmSampleType,
       "alarmValue": alarmValue,
       "alarmStartupAlarm": alarmStartupAlarm,
       "alarmRisingThreshold": alarmRisingThreshold,
       "alarmFallingThreshold": alarmFallingThreshold,
       "alarmRisingEventIndex": alarmRisingEventIndex,
       "alarmFallingEventIndex": alarmFallingEventIndex,
       "alarmOwner": alarmOwner,
       "alarmStatus": alarmStatus,
       "hosts": hosts,
       "hostTopN": hostTopN,
       "matrix": matrix,
       "filter": filter,
       "capture": capture,
       "event": event,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "eventIndex": eventIndex,
       "eventDescription": eventDescription,
       "eventType": eventType,
       "eventCommunity": eventCommunity,
       "eventLastTimeSent": eventLastTimeSent,
       "eventOwner": eventOwner,
       "eventStatus": eventStatus,
       "logTable": logTable,
       "logEntry": logEntry,
       "logEventIndex": logEventIndex,
       "logIndex": logIndex,
       "logTime": logTime,
       "logDescription": logDescription,
       "dot1dBridge": dot1dBridge,
       "snmpDot3RptrMgt": snmpDot3RptrMgt,
       "rptrHealth": rptrHealth,
       "rptrGroupChange": rptrGroupChange,
       "rptrBasicPackage": rptrBasicPackage,
       "rptrRptrInfo": rptrRptrInfo,
       "rptrGroupCapacity": rptrGroupCapacity,
       "rptrOperStatus": rptrOperStatus,
       "rptrHealthText": rptrHealthText,
       "rptrReset": rptrReset,
       "rptrNonDisruptTest": rptrNonDisruptTest,
       "rptrTotalPartitionedPorts": rptrTotalPartitionedPorts,
       "rptrGroupInfo": rptrGroupInfo,
       "rptrGroupTable": rptrGroupTable,
       "rptrGroupEntry": rptrGroupEntry,
       "rptrGroupIndex": rptrGroupIndex,
       "rptrGroupDescr": rptrGroupDescr,
       "rptrGroupObjectID": rptrGroupObjectID,
       "rptrGroupOperStatus": rptrGroupOperStatus,
       "rptrGroupLastOperStatusChange": rptrGroupLastOperStatusChange,
       "rptrGroupPortCapacity": rptrGroupPortCapacity,
       "rptrPortInfo": rptrPortInfo,
       "rptrPortTable": rptrPortTable,
       "rptrPortEntry": rptrPortEntry,
       "rptrPortGroupIndex": rptrPortGroupIndex,
       "rptrPortIndex": rptrPortIndex,
       "rptrPortAdminStatus": rptrPortAdminStatus,
       "rptrPortAutoPartitionState": rptrPortAutoPartitionState,
       "rptrPortOperStatus": rptrPortOperStatus,
       "rptrMonitorPackage": rptrMonitorPackage,
       "rptrMonitorRptrInfo": rptrMonitorRptrInfo,
       "rptrMonitorTransmitCollisions": rptrMonitorTransmitCollisions,
       "rptrMonitorGroupInfo": rptrMonitorGroupInfo,
       "rptrMonitorGroupTable": rptrMonitorGroupTable,
       "rptrMonitorGroupEntry": rptrMonitorGroupEntry,
       "rptrMonitorGroupIndex": rptrMonitorGroupIndex,
       "rptrMonitorGroupTotalFrames": rptrMonitorGroupTotalFrames,
       "rptrMonitorGroupTotalOctets": rptrMonitorGroupTotalOctets,
       "rptrMonitorGroupTotalErrors": rptrMonitorGroupTotalErrors,
       "rptrMonitorPortInfo": rptrMonitorPortInfo,
       "rptrMonitorPortTable": rptrMonitorPortTable,
       "rptrMonitorPortEntry": rptrMonitorPortEntry,
       "rptrMonitorPortGroupIndex": rptrMonitorPortGroupIndex,
       "rptrMonitorPortIndex": rptrMonitorPortIndex,
       "rptrMonitorPortReadableFrames": rptrMonitorPortReadableFrames,
       "rptrMonitorPortReadableOctets": rptrMonitorPortReadableOctets,
       "rptrMonitorPortFCSErrors": rptrMonitorPortFCSErrors,
       "rptrMonitorPortAlignmentErrors": rptrMonitorPortAlignmentErrors,
       "rptrMonitorPortFrameTooLongs": rptrMonitorPortFrameTooLongs,
       "rptrMonitorPortShortEvents": rptrMonitorPortShortEvents,
       "rptrMonitorPortRunts": rptrMonitorPortRunts,
       "rptrMonitorPortCollisions": rptrMonitorPortCollisions,
       "rptrMonitorPortLateEvents": rptrMonitorPortLateEvents,
       "rptrMonitorPortVeryLongEvents": rptrMonitorPortVeryLongEvents,
       "rptrMonitorPortDataRateMismatches": rptrMonitorPortDataRateMismatches,
       "rptrMonitorPortAutoPartitions": rptrMonitorPortAutoPartitions,
       "rptrMonitorPortTotalErrors": rptrMonitorPortTotalErrors,
       "rptrAddrTrackPackage": rptrAddrTrackPackage,
       "rptrAddrTrackRptrInfo": rptrAddrTrackRptrInfo,
       "rptrAddrTrackGroupInfo": rptrAddrTrackGroupInfo,
       "rptrAddrTrackPortInfo": rptrAddrTrackPortInfo,
       "rptrAddrTrackTable": rptrAddrTrackTable,
       "rptrAddrTrackEntry": rptrAddrTrackEntry,
       "rptrAddrTrackGroupIndex": rptrAddrTrackGroupIndex,
       "rptrAddrTrackPortIndex": rptrAddrTrackPortIndex,
       "rptrAddrTrackLastSourceAddress": rptrAddrTrackLastSourceAddress,
       "rptrAddrTrackSourceAddrChanges": rptrAddrTrackSourceAddrChanges,
       "novell": novell,
       "mibDoc": mibDoc,
       "ipx": ipx,
       "ipxSystem": ipxSystem,
       "ipxBasicSysTable": ipxBasicSysTable,
       "ipxBasicSysEntry": ipxBasicSysEntry,
       "ipxBasicSysInstance": ipxBasicSysInstance,
       "ipxBasicSysExistState": ipxBasicSysExistState,
       "ipxBasicSysNetNumber": ipxBasicSysNetNumber,
       "ipxBasicSysNode": ipxBasicSysNode,
       "ipxBasicSysName": ipxBasicSysName,
       "ipxBasicSysInReceives": ipxBasicSysInReceives,
       "ipxBasicSysInHdrErrors": ipxBasicSysInHdrErrors,
       "ipxBasicSysInUnknownSockets": ipxBasicSysInUnknownSockets,
       "ipxBasicSysInDiscards": ipxBasicSysInDiscards,
       "ipxBasicSysInBadChecksums": ipxBasicSysInBadChecksums,
       "ipxBasicSysInDelivers": ipxBasicSysInDelivers,
       "ipxBasicSysNoRoutes": ipxBasicSysNoRoutes,
       "ipxBasicSysOutRequests": ipxBasicSysOutRequests,
       "ipxBasicSysOutMalformedRequests": ipxBasicSysOutMalformedRequests,
       "ipxBasicSysOutDiscards": ipxBasicSysOutDiscards,
       "ipxBasicSysOutPackets": ipxBasicSysOutPackets,
       "ipxBasicSysConfigSockets": ipxBasicSysConfigSockets,
       "ipxBasicSysOpenSocketFails": ipxBasicSysOpenSocketFails,
       "ipxAdvSysTable": ipxAdvSysTable,
       "ipxAdvSysEntry": ipxAdvSysEntry,
       "ipxAdvSysInstance": ipxAdvSysInstance,
       "ipxAdvSysMaxPathSplits": ipxAdvSysMaxPathSplits,
       "ipxAdvSysMaxHops": ipxAdvSysMaxHops,
       "ipxAdvSysTooManyHops": ipxAdvSysTooManyHops,
       "ipxAdvSysInFiltered": ipxAdvSysInFiltered,
       "ipxAdvSysCompressDiscards": ipxAdvSysCompressDiscards,
       "ipxAdvSysNETBIOSPackets": ipxAdvSysNETBIOSPackets,
       "ipxAdvSysForwPackets": ipxAdvSysForwPackets,
       "ipxAdvSysOutFiltered": ipxAdvSysOutFiltered,
       "ipxAdvSysOutCompressDiscards": ipxAdvSysOutCompressDiscards,
       "ipxAdvSysCircCount": ipxAdvSysCircCount,
       "ipxAdvSysDestCount": ipxAdvSysDestCount,
       "ipxAdvSysServCount": ipxAdvSysServCount,
       "ipxCircuit": ipxCircuit,
       "ipxForwarding": ipxForwarding,
       "ipxServices": ipxServices,
       "ipxTraps": ipxTraps,
       "a3Com": a3Com,
       "heartbeatEvent": heartbeatEvent,
       "localManagementUpdate": localManagementUpdate,
       "securityViolation": securityViolation,
       "gaugesThresholdTrap": gaugesThresholdTrap,
       "gaugesRecoveryTrap": gaugesRecoveryTrap,
       "slFailed": slFailed,
       "estStateChange": estStateChange,
       "estTableFull": estTableFull,
       "phyEntityInserted": phyEntityInserted,
       "phyEntityRemoved": phyEntityRemoved,
       "phyFacilityChanged": phyFacilityChanged,
       "serviceEntityAdded": serviceEntityAdded,
       "serviceEntityRemoved": serviceEntityRemoved,
       "physicalStateChange": physicalStateChange,
       "psuCapacityExceeded": psuCapacityExceeded,
       "tempStateChange": tempStateChange,
       "statusInputStateChange": statusInputStateChange,
       "mrmStationLearnTrap": mrmStationLearnTrap,
       "mrmSecurityTrap": mrmSecurityTrap,
       "repPartitionStateChange": repPartitionStateChange,
       "repLinkStateChange": repLinkStateChange,
       "repAdminStateChange": repAdminStateChange,
       "repPortTopUsage": repPortTopUsage,
       "repPortErrors": repPortErrors,
       "resResilienceSwitch": resResilienceSwitch,
       "resStateChange": resStateChange,
       "a3ComRingTopologyChange": a3ComRingTopologyChange,
       "a3ComRingStateChange": a3ComRingStateChange,
       "a3ComRingBackupStateChange": a3ComRingBackupStateChange,
       "a3ComRingWrapChange": a3ComRingWrapChange,
       "a3ComAttachStateChange": a3ComAttachStateChange,
       "rbRingInStateChange": rbRingInStateChange,
       "rbRingOutStateChange": rbRingOutStateChange,
       "rbMauPortStateChange": rbMauPortStateChange,
       "pollTableSuccessTrap": pollTableSuccessTrap,
       "pollTableFailedTrap": pollTableFailedTrap,
       "products": products,
       "terminalServer": terminalServer,
       "dedicatedBridgeServer": dedicatedBridgeServer,
       "dedicatedRouteServer": dedicatedRouteServer,
       "brouter": brouter,
       "genericMSWorkstation": genericMSWorkstation,
       "genericMSServer": genericMSServer,
       "genericUnixServer": genericUnixServer,
       "hub": hub,
       "linkBuilder3GH": linkBuilder3GH,
       "linkBuilder10BTi": linkBuilder10BTi,
       "linkBuilderECS": linkBuilderECS,
       "linkBuilderMSH": linkBuilderMSH,
       "misc": misc,
       "tempSensorOutput": tempSensorOutput,
       "statusInputTable": statusInputTable,
       "statusInputTableEntry": statusInputTableEntry,
       "statusInputIndex": statusInputIndex,
       "statusInputState": statusInputState,
       "statusTrapEnable": statusTrapEnable,
       "statusName": statusName,
       "chassisMgmtMACTable": chassisMgmtMACTable,
       "chassisMgmtMACEntry": chassisMgmtMACEntry,
       "macSlotNumber": macSlotNumber,
       "macIndex": macIndex,
       "macBroadcastAvailable": macBroadcastAvailable,
       "macLSAPFiltering": macLSAPFiltering,
       "macTypeFiltering": macTypeFiltering,
       "macMaxPDUsize": macMaxPDUsize,
       "macPhyAddress": macPhyAddress,
       "macStatus": macStatus,
       "chassisLedTable": chassisLedTable,
       "chassisLedEntry": chassisLedEntry,
       "chassisSlotNumber": chassisSlotNumber,
       "chassisLedColour": chassisLedColour,
       "chassisAttentionState": chassisAttentionState,
       "mshFault": mshFault,
       "mshFaultModifiedFlag": mshFaultModifiedFlag,
       "mshFaultTable": mshFaultTable,
       "mshFaultEntry": mshFaultEntry,
       "mshFaultIndex": mshFaultIndex,
       "mshFaultErrorNumber": mshFaultErrorNumber,
       "mshFaultTimeStamp": mshFaultTimeStamp,
       "mshFaultRestartCount": mshFaultRestartCount,
       "linkBuilderFMS": linkBuilderFMS,
       "linkBuilderFddiWorkGroupHub": linkBuilderFddiWorkGroupHub,
       "linkBuilderFMSII": linkBuilderFMSII,
       "linkSwitchFMS": linkSwitchFMS,
       "linkSwitchMSH": linkSwitchMSH,
       "linkBuilderFMSLBridge": linkBuilderFMSLBridge,
       "linkBuilderTP8i": linkBuilderTP8i,
       "cards": cards,
       "linkBuilder3GH-cards": linkBuilder3GH_cards,
       "linkBuilder10BTi-cards": linkBuilder10BTi_cards,
       "linkBuilder10BTi-cards-utp": linkBuilder10BTi_cards_utp,
       "linkBuilder10BT-cards-utp": linkBuilder10BT_cards_utp,
       "linkBuilderECS-cards": linkBuilderECS_cards,
       "linkBuilderMSH-cards": linkBuilderMSH_cards,
       "linkBuilderFMS-cards": linkBuilderFMS_cards,
       "linkBuilderFMS-cards-utp": linkBuilderFMS_cards_utp,
       "linkBuilderFMS-cards-coax": linkBuilderFMS_cards_coax,
       "linkBuilderFMS-cards-fiber": linkBuilderFMS_cards_fiber,
       "linkBuilderFMS-cards-12fiber": linkBuilderFMS_cards_12fiber,
       "linkBuilderFMS-cards-24utp": linkBuilderFMS_cards_24utp,
       "linkBuilderFMSII-cards": linkBuilderFMSII_cards,
       "linkBuilderFMSII-cards-12tp-rj45": linkBuilderFMSII_cards_12tp_rj45,
       "linkBuilderFMSII-cards-10coax-bnc": linkBuilderFMSII_cards_10coax_bnc,
       "linkBuilderFMSII-cards-6fiber-st": linkBuilderFMSII_cards_6fiber_st,
       "linkBuilderFMSII-cards-12fiber-st": linkBuilderFMSII_cards_12fiber_st,
       "linkBuilderFMSII-cards-24tp-rj45": linkBuilderFMSII_cards_24tp_rj45,
       "linkBuilderFMSII-cards-24tp-telco": linkBuilderFMSII_cards_24tp_telco,
       "a3C512": a3C512,
       "linkBuilderTP8i-cards": linkBuilderTP8i_cards,
       "linkBuilderTP8i-cards-8tp-rj45": linkBuilderTP8i_cards_8tp_rj45,
       "chipsets": chipsets,
       "amp-mib": amp_mib,
       "genericTrap": genericTrap,
       "viewBuilderApps": viewBuilderApps,
       "specificTrap": specificTrap,
       "linkBuilder3GH-mib": linkBuilder3GH_mib,
       "linkBuilder10BTi-mib": linkBuilder10BTi_mib,
       "linkBuilderECS-mib": linkBuilderECS_mib,
       "generic": generic,
       "genExperimental": genExperimental,
       "testData": testData,
       "ifExtensions": ifExtensions,
       "setup": setup,
       "setupGeneral": setupGeneral,
       "heartbeatInterval": heartbeatInterval,
       "setupIp": setupIp,
       "setIpIfTable": setIpIfTable,
       "setIpIfEntry": setIpIfEntry,
       "setIpIfIndex": setIpIfIndex,
       "setIpIfAddr": setIpIfAddr,
       "setIpIfMask": setIpIfMask,
       "setIpIfRouter": setIpIfRouter,
       "setupStart": setupStart,
       "startPROMSwVerNo": startPROMSwVerNo,
       "startRestartCount": startRestartCount,
       "startLastRestartType": startLastRestartType,
       "startResetAction": startResetAction,
       "startLastSystemError": startLastSystemError,
       "startRestartAction": startRestartAction,
       "systemConfigChangeTime": systemConfigChangeTime,
       "sysLoader": sysLoader,
       "loadableDeviceTable": loadableDeviceTable,
       "loadableDeviceEntry": loadableDeviceEntry,
       "slDeviceType": slDeviceType,
       "slDeviceInstance": slDeviceInstance,
       "slLoadStatus": slLoadStatus,
       "slSoftwareVersion": slSoftwareVersion,
       "slHardwareVersion": slHardwareVersion,
       "slFilename": slFilename,
       "slServerIpAddress": slServerIpAddress,
       "slLoad": slLoad,
       "slServerAddress": slServerAddress,
       "slServerProtocol": slServerProtocol,
       "security": security,
       "securityEnableTable": securityEnableTable,
       "securityEnableTableEntry": securityEnableTableEntry,
       "securityLevel": securityLevel,
       "securityCommunityEnable": securityCommunityEnable,
       "securitySecureEnable": securitySecureEnable,
       "securityTermEnable": securityTermEnable,
       "securityTelnetEnable": securityTelnetEnable,
       "securityFrontPanelEnable": securityFrontPanelEnable,
       "securityUserTable": securityUserTable,
       "securityUserTableEntry": securityUserTableEntry,
       "securityUserStatus": securityUserStatus,
       "securityUserName": securityUserName,
       "securityUserLevel": securityUserLevel,
       "securityUserPassword": securityUserPassword,
       "securityUserCommunity": securityUserCommunity,
       "securityUserLocParty": securityUserLocParty,
       "securityUserMgrParty": securityUserMgrParty,
       "securityAuditLogTable": securityAuditLogTable,
       "securityAuditLogEntry": securityAuditLogEntry,
       "securityAuditIndex": securityAuditIndex,
       "securityAuditTime": securityAuditTime,
       "securityAuditUser": securityAuditUser,
       "securityAuditObject": securityAuditObject,
       "securityAuditValue": securityAuditValue,
       "securityAuditResult": securityAuditResult,
       "gauges": gauges,
       "gaugeTable": gaugeTable,
       "gaugeTableEntry": gaugeTableEntry,
       "gaugeIndex": gaugeIndex,
       "gaugeItemId": gaugeItemId,
       "gaugeItemType": gaugeItemType,
       "gaugeSamplesPerAverage": gaugeSamplesPerAverage,
       "gaugeSamplePeriod": gaugeSamplePeriod,
       "gaugeValue": gaugeValue,
       "gaugePeakValue": gaugePeakValue,
       "gaugeThresholdLevel": gaugeThresholdLevel,
       "gaugeRecoveryLevel": gaugeRecoveryLevel,
       "gaugeThresholdAction": gaugeThresholdAction,
       "gaugeRecoveryAction": gaugeRecoveryAction,
       "gaugeState": gaugeState,
       "gaugeOwner": gaugeOwner,
       "gaugeTableSize": gaugeTableSize,
       "gaugeThresholdLevelScaler": gaugeThresholdLevelScaler,
       "gaugeRecoveryLevelScaler": gaugeRecoveryLevelScaler,
       "gaugeTableUpdate": gaugeTableUpdate,
       "gaugeConfigureObjId": gaugeConfigureObjId,
       "gaugeConfigureColumn": gaugeConfigureColumn,
       "gaugeConfigureValue": gaugeConfigureValue,
       "gaugeNextFreeIndex": gaugeNextFreeIndex,
       "asciiAgent": asciiAgent,
       "ascTimeAttemptedLogin": ascTimeAttemptedLogin,
       "ascUserNameForLastAttemptedLogin": ascUserNameForLastAttemptedLogin,
       "ascLoginStatus": ascLoginStatus,
       "ascLocalManagementBanner": ascLocalManagementBanner,
       "serialIf": serialIf,
       "siSlipPort": siSlipPort,
       "configV24Table": configV24Table,
       "configV24Entry": configV24Entry,
       "configV24PortID": configV24PortID,
       "configV24ConnType": configV24ConnType,
       "configV24AutoConfig": configV24AutoConfig,
       "configV24Speed": configV24Speed,
       "configV24CharSize": configV24CharSize,
       "configV24StopBits": configV24StopBits,
       "configV24Parity": configV24Parity,
       "configV24DSRControl": configV24DSRControl,
       "configV24DCDControl": configV24DCDControl,
       "configV24FlowControl": configV24FlowControl,
       "configV24Update": configV24Update,
       "repeaterMgmt": repeaterMgmt,
       "mrmSecurityPackage": mrmSecurityPackage,
       "mrmSecurePortTable": mrmSecurePortTable,
       "mrmSecurePortEntry": mrmSecurePortEntry,
       "mrmSecRepIndex": mrmSecRepIndex,
       "mrmSecSlotIndex": mrmSecSlotIndex,
       "mrmSecPortIndex": mrmSecPortIndex,
       "mrmSecPortState": mrmSecPortState,
       "mrmSecNTKState": mrmSecNTKState,
       "mrmSecBroadcastState": mrmSecBroadcastState,
       "mrmSecMulticastState": mrmSecMulticastState,
       "mrmSecLearnMode": mrmSecLearnMode,
       "mrmSecReportMode": mrmSecReportMode,
       "mrmSecMACAddress": mrmSecMACAddress,
       "mrmSecRowStatus": mrmSecRowStatus,
       "endStation": endStation,
       "esDatabaseState": esDatabaseState,
       "esDatabaseFlush": esDatabaseFlush,
       "esTable": esTable,
       "esTableEntry": esTableEntry,
       "esAddrType": esAddrType,
       "esAddress": esAddress,
       "esSlotNumber": esSlotNumber,
       "esPortNumber": esPortNumber,
       "esModTable": esModTable,
       "esModTableEntry": esModTableEntry,
       "esModAddrType": esModAddrType,
       "esModAddress": esModAddress,
       "esModSlotNumber": esModSlotNumber,
       "esModPortNumber": esModPortNumber,
       "esPortAccessTable": esPortAccessTable,
       "esPortAccessEntry": esPortAccessEntry,
       "ecPortCardNo": ecPortCardNo,
       "ecPortPortNo": ecPortPortNo,
       "ecPortIndex": ecPortIndex,
       "ecPortAddrType": ecPortAddrType,
       "ecPortAddress": ecPortAddress,
       "localSnmp": localSnmp,
       "trapTable": trapTable,
       "trapEntry": trapEntry,
       "trapStatus": trapStatus,
       "trapDestination": trapDestination,
       "trapCommunity": trapCommunity,
       "trapSubject": trapSubject,
       "trapCategory": trapCategory,
       "trapThrottle": trapThrottle,
       "snmpTrapTable": snmpTrapTable,
       "snmpTrapEntry": snmpTrapEntry,
       "snmpTrapIndex": snmpTrapIndex,
       "snmpTrapDestination": snmpTrapDestination,
       "snmpTrapProtocol": snmpTrapProtocol,
       "snmpTrapCommunity": snmpTrapCommunity,
       "snmpTrapCategory": snmpTrapCategory,
       "snmpTrapThrottle": snmpTrapThrottle,
       "snmpTrapRowStatus": snmpTrapRowStatus,
       "snmpTrapNextFreeIndex": snmpTrapNextFreeIndex,
       "manager": manager,
       "unusedGeneric12": unusedGeneric12,
       "chassis": chassis,
       "enclosure": enclosure,
       "enclosureName": enclosureName,
       "enclosureObjId": enclosureObjId,
       "enclosureHardwareVers": enclosureHardwareVers,
       "physicalConfig": physicalConfig,
       "phyConfigTable": phyConfigTable,
       "phyConfigEntry": phyConfigEntry,
       "phyLocationType": phyLocationType,
       "phyLocation": phyLocation,
       "phySysObjId": phySysObjId,
       "phyServiceType": phyServiceType,
       "phyEntityType": phyEntityType,
       "phyHwVersion": phyHwVersion,
       "phySwVersion": phySwVersion,
       "phyServiceId": phyServiceId,
       "phyEntityName": phyEntityName,
       "phyPowerReq": phyPowerReq,
       "phyNumberOfPorts": phyNumberOfPorts,
       "phyLampTest": phyLampTest,
       "phyEntityState": phyEntityState,
       "phyAction": phyAction,
       "phyLimits": phyLimits,
       "phyLimitEntry": phyLimitEntry,
       "phyLimLocationType": phyLimLocationType,
       "phyLimLimit": phyLimLimit,
       "frontPanelDisplayMessage": frontPanelDisplayMessage,
       "logicalConfig": logicalConfig,
       "serviceTable": serviceTable,
       "serviceEntry": serviceEntry,
       "serviceId": serviceId,
       "serviceName": serviceName,
       "serviceReset": serviceReset,
       "addressTable": addressTable,
       "addressTableEntry": addressTableEntry,
       "mgmtServiceId": mgmtServiceId,
       "mgmtSubIndex": mgmtSubIndex,
       "mgmtAddressType": mgmtAddressType,
       "mgmtAddress": mgmtAddress,
       "facilityTable": facilityTable,
       "facilityEntry": facilityEntry,
       "fcSlotNumber": fcSlotNumber,
       "fcFacilityIndex": fcFacilityIndex,
       "fcType": fcType,
       "fcConnection": fcConnection,
       "mrmResilience": mrmResilience,
       "resTable": resTable,
       "resTableEntry": resTableEntry,
       "resRepeater": resRepeater,
       "resMainSlot": resMainSlot,
       "resMainPort": resMainPort,
       "resMainState": resMainState,
       "resStandbySlot": resStandbySlot,
       "resStandbyPort": resStandbyPort,
       "resStandbyState": resStandbyState,
       "resPairState": resPairState,
       "resPairModificationStatus": resPairModificationStatus,
       "resPairAction": resPairAction,
       "resPairEnable": resPairEnable,
       "resStandbyMapTable": resStandbyMapTable,
       "resStandbyMapTableEntry": resStandbyMapTableEntry,
       "resSbRepeater": resSbRepeater,
       "resSbSlot": resSbSlot,
       "resSbPort": resSbPort,
       "resSbType": resSbType,
       "resSbMainSlot": resSbMainSlot,
       "resSbMainPort": resSbMainPort,
       "resFlushTable": resFlushTable,
       "tokenRing": tokenRing,
       "a3ComRingParams": a3ComRingParams,
       "a3ComRingConfig": a3ComRingConfig,
       "a3ComRingConfigEntry": a3ComRingConfigEntry,
       "a3ComRingConfigServiceId": a3ComRingConfigServiceId,
       "a3ComRingNumber": a3ComRingNumber,
       "a3ComRingSpeed": a3ComRingSpeed,
       "a3ComRingState": a3ComRingState,
       "a3ComRingBackupState": a3ComRingBackupState,
       "a3ComRingWrapState": a3ComRingWrapState,
       "a3ComRingMapChanged": a3ComRingMapChanged,
       "a3ComRingMapChangeTime": a3ComRingMapChangeTime,
       "a3ComRingAction": a3ComRingAction,
       "a3ComRingStdStats": a3ComRingStdStats,
       "a3ComRingStdStatsEntry": a3ComRingStdStatsEntry,
       "a3ComRingStdStatsServiceId": a3ComRingStdStatsServiceId,
       "a3ComRingBeaconCount": a3ComRingBeaconCount,
       "a3ComRingSoftErrors": a3ComRingSoftErrors,
       "a3ComRingActiveMonitorChanges": a3ComRingActiveMonitorChanges,
       "a3ComRingTop": a3ComRingTop,
       "a3ComRingTopEntry": a3ComRingTopEntry,
       "a3ComRingTopServiceId": a3ComRingTopServiceId,
       "a3ComRingTopIndex": a3ComRingTopIndex,
       "a3ComRingTopStationAddress": a3ComRingTopStationAddress,
       "a3ComRingTopMonitor": a3ComRingTopMonitor,
       "a3ComRingStationParams": a3ComRingStationParams,
       "a3ComRingStatConfig": a3ComRingStatConfig,
       "a3ComRingStatConfigEntry": a3ComRingStatConfigEntry,
       "a3ComRingStatConfigServiceId": a3ComRingStatConfigServiceId,
       "a3ComRingStatConfigAddress": a3ComRingStatConfigAddress,
       "a3ComRingStatState": a3ComRingStatState,
       "a3ComRingStatLocation": a3ComRingStatLocation,
       "a3ComRingStatAction": a3ComRingStatAction,
       "a3ComRingStatStandardStats": a3ComRingStatStandardStats,
       "a3ComRingStatStdStatsEntry": a3ComRingStatStdStatsEntry,
       "a3ComRingStatStdStatsServiceId": a3ComRingStatStdStatsServiceId,
       "a3ComRingStatStdStatsAddress": a3ComRingStatStdStatsAddress,
       "a3ComRingStatLineErrors": a3ComRingStatLineErrors,
       "a3ComRingStatInternalErrors": a3ComRingStatInternalErrors,
       "a3ComRingStatBurstErrors": a3ComRingStatBurstErrors,
       "a3ComRingStatMonitorErrors": a3ComRingStatMonitorErrors,
       "a3ComRingStatLostFrames": a3ComRingStatLostFrames,
       "a3ComRingStatFrameCopyErrors": a3ComRingStatFrameCopyErrors,
       "a3ComRingStatRxCongestion": a3ComRingStatRxCongestion,
       "a3ComRingStatTokenErrors": a3ComRingStatTokenErrors,
       "a3ComRingStatFreqErrors": a3ComRingStatFreqErrors,
       "a3ComRingStatSoftErrors": a3ComRingStatSoftErrors,
       "multiRepeater": multiRepeater,
       "mrmBasicPackage": mrmBasicPackage,
       "mrmBasCardPackage": mrmBasCardPackage,
       "mrmCardTable": mrmCardTable,
       "mrmCardEntry": mrmCardEntry,
       "mrmCardServiceId": mrmCardServiceId,
       "mrmCardIndex": mrmCardIndex,
       "mrmCardPortCapacity": mrmCardPortCapacity,
       "mrmCardTest": mrmCardTest,
       "mrmCardDOBPorts": mrmCardDOBPorts,
       "mrmCardMDIenable": mrmCardMDIenable,
       "mrmBasPortPackage": mrmBasPortPackage,
       "mrmPortTable": mrmPortTable,
       "mrmPortEntry": mrmPortEntry,
       "mrmPortServiceId": mrmPortServiceId,
       "mrmPortCardIndex": mrmPortCardIndex,
       "mrmPortIndex": mrmPortIndex,
       "mrmPortInterfaceType": mrmPortInterfaceType,
       "mrmPortConnectorType": mrmPortConnectorType,
       "mrmPortAdminStatus": mrmPortAdminStatus,
       "mrmPortAutoPartitionState": mrmPortAutoPartitionState,
       "mrmPortLinkState": mrmPortLinkState,
       "mrmPortBootState": mrmPortBootState,
       "mrmPortESTFilter": mrmPortESTFilter,
       "mrmPortPartitionEvent": mrmPortPartitionEvent,
       "mrmPortLinkStateEvent": mrmPortLinkStateEvent,
       "mrmPortSecurityAvailable": mrmPortSecurityAvailable,
       "mrmPortLinkPulse": mrmPortLinkPulse,
       "mrmMonitorPackage": mrmMonitorPackage,
       "mrmMonRepeaterPackage": mrmMonRepeaterPackage,
       "mrmMonitorRepTable": mrmMonitorRepTable,
       "mrmMonitorRepEntry": mrmMonitorRepEntry,
       "mrmMonRepServiceId": mrmMonRepServiceId,
       "mrmMonRepReadableFrames": mrmMonRepReadableFrames,
       "mrmMonRepUnicastFrames": mrmMonRepUnicastFrames,
       "mrmMonRepMulticastFrames": mrmMonRepMulticastFrames,
       "mrmMonRepBroadcastFrames": mrmMonRepBroadcastFrames,
       "mrmMonRepReadableOctets": mrmMonRepReadableOctets,
       "mrmMonRepUnicastOctets": mrmMonRepUnicastOctets,
       "mrmMonRepMulticastOctets": mrmMonRepMulticastOctets,
       "mrmMonRepBroadcastOctets": mrmMonRepBroadcastOctets,
       "mrmMonRepFCSErrors": mrmMonRepFCSErrors,
       "mrmMonRepAlignmentErrors": mrmMonRepAlignmentErrors,
       "mrmMonRepFrameTooLongs": mrmMonRepFrameTooLongs,
       "mrmMonRepShortEvents": mrmMonRepShortEvents,
       "mrmMonRepRunts": mrmMonRepRunts,
       "mrmMonRepTxCollisions": mrmMonRepTxCollisions,
       "mrmMonRepLateEvents": mrmMonRepLateEvents,
       "mrmMonRepVeryLongEvents": mrmMonRepVeryLongEvents,
       "mrmMonRepDataRateMismatches": mrmMonRepDataRateMismatches,
       "mrmMonRepAutoPartitions": mrmMonRepAutoPartitions,
       "mrmMonRepTotalErrors": mrmMonRepTotalErrors,
       "mrmMonRepBound0": mrmMonRepBound0,
       "mrmMonRepBound1": mrmMonRepBound1,
       "mrmMonRepBound2": mrmMonRepBound2,
       "mrmMonRepBound3": mrmMonRepBound3,
       "mrmMonRepBound4": mrmMonRepBound4,
       "mrmMonRepBound5": mrmMonRepBound5,
       "mrmMonRepAction": mrmMonRepAction,
       "mrmMonCardPackage": mrmMonCardPackage,
       "mrmMonitorCardTable": mrmMonitorCardTable,
       "mrmMonitorCardEntry": mrmMonitorCardEntry,
       "mrmMonCardServiceId": mrmMonCardServiceId,
       "mrmMonCardIndex": mrmMonCardIndex,
       "mrmMonCardReadableFrames": mrmMonCardReadableFrames,
       "mrmMonCardUnicastFrames": mrmMonCardUnicastFrames,
       "mrmMonCardMulticastFrames": mrmMonCardMulticastFrames,
       "mrmMonCardBroadcastFrames": mrmMonCardBroadcastFrames,
       "mrmMonCardReadableOctets": mrmMonCardReadableOctets,
       "mrmMonCardUnicastOctets": mrmMonCardUnicastOctets,
       "mrmMonCardMulticastOctets": mrmMonCardMulticastOctets,
       "mrmMonCardBroadcastOctets": mrmMonCardBroadcastOctets,
       "mrmMonCardFCSErrors": mrmMonCardFCSErrors,
       "mrmMonCardAlignmentErrors": mrmMonCardAlignmentErrors,
       "mrmMonCardFrameTooLongs": mrmMonCardFrameTooLongs,
       "mrmMonCardShortEvents": mrmMonCardShortEvents,
       "mrmMonCardRunts": mrmMonCardRunts,
       "mrmMonCardLateEvents": mrmMonCardLateEvents,
       "mrmMonCardVeryLongEvents": mrmMonCardVeryLongEvents,
       "mrmMonCardDataRateMismatches": mrmMonCardDataRateMismatches,
       "mrmMonCardAutoPartitions": mrmMonCardAutoPartitions,
       "mrmMonCardTotalErrors": mrmMonCardTotalErrors,
       "mrmMonCardBound0": mrmMonCardBound0,
       "mrmMonCardBound1": mrmMonCardBound1,
       "mrmMonCardBound2": mrmMonCardBound2,
       "mrmMonCardBound3": mrmMonCardBound3,
       "mrmMonCardBound4": mrmMonCardBound4,
       "mrmMonCardBound5": mrmMonCardBound5,
       "mrmMonCardClearCounters": mrmMonCardClearCounters,
       "mrmMonPortPackage": mrmMonPortPackage,
       "mrmMonitorPortTable": mrmMonitorPortTable,
       "mrmMonitorPortEntry": mrmMonitorPortEntry,
       "mrmMonPortServiceId": mrmMonPortServiceId,
       "mrmMonPortCardIndex": mrmMonPortCardIndex,
       "mrmMonPortIndex": mrmMonPortIndex,
       "mrmMonPortReadableFrames": mrmMonPortReadableFrames,
       "mrmMonPortUnicastFrames": mrmMonPortUnicastFrames,
       "mrmMonPortMulticastFrames": mrmMonPortMulticastFrames,
       "mrmMonPortBroadcastFrames": mrmMonPortBroadcastFrames,
       "mrmMonPortReadableOctets": mrmMonPortReadableOctets,
       "mrmMonPortUnicastOctets": mrmMonPortUnicastOctets,
       "mrmMonPortMulticastOctets": mrmMonPortMulticastOctets,
       "mrmMonPortBroadcastOctets": mrmMonPortBroadcastOctets,
       "mrmMonPortFCSErrors": mrmMonPortFCSErrors,
       "mrmMonPortAlignmentErrors": mrmMonPortAlignmentErrors,
       "mrmMonPortFrameTooLongs": mrmMonPortFrameTooLongs,
       "mrmMonPortShortEvents": mrmMonPortShortEvents,
       "mrmMonPortRunts": mrmMonPortRunts,
       "mrmMonPortCollisions": mrmMonPortCollisions,
       "mrmMonPortLateEvents": mrmMonPortLateEvents,
       "mrmMonPortVeryLongEvents": mrmMonPortVeryLongEvents,
       "mrmMonPortDataRateMismatches": mrmMonPortDataRateMismatches,
       "mrmMonPortAutoPartitions": mrmMonPortAutoPartitions,
       "mrmMonPortTotalErrors": mrmMonPortTotalErrors,
       "mrmMonPortBound0": mrmMonPortBound0,
       "mrmMonPortBound1": mrmMonPortBound1,
       "mrmMonPortBound2": mrmMonPortBound2,
       "mrmMonPortBound3": mrmMonPortBound3,
       "mrmMonPortBound4": mrmMonPortBound4,
       "mrmMonPortBound5": mrmMonPortBound5,
       "mrmMonPortBandwidthUsed": mrmMonPortBandwidthUsed,
       "mrmMonPortErrorsPer10000Packets": mrmMonPortErrorsPer10000Packets,
       "mrmMonPortClearCounters": mrmMonPortClearCounters,
       "mrmMonPortLastAddress": mrmMonPortLastAddress,
       "mrmMonPortAddressChanges": mrmMonPortAddressChanges,
       "mrmMonDummyPackage": mrmMonDummyPackage,
       "trafficLevel": trafficLevel,
       "errorFrames": errorFrames,
       "bridgeMgmt": bridgeMgmt,
       "fault": fault,
       "faultModifiedFlag": faultModifiedFlag,
       "faultTable": faultTable,
       "faultEntry": faultEntry,
       "faultIndex": faultIndex,
       "faultErrorNumber": faultErrorNumber,
       "faultTimeStamp": faultTimeStamp,
       "faultRestartCount": faultRestartCount,
       "poll": poll,
       "pollTable": pollTable,
       "pollTableEntry": pollTableEntry,
       "pollIndex": pollIndex,
       "pollAddress": pollAddress,
       "pollProtocol": pollProtocol,
       "pollRate": pollRate,
       "pollTargetType": pollTargetType,
       "pollLastPollSent": pollLastPollSent,
       "pollRoundTripTime": pollRoundTripTime,
       "pollInformation": pollInformation,
       "pollAlarmIndex": pollAlarmIndex,
       "pollOwner": pollOwner,
       "pollRowStatus": pollRowStatus,
       "pollNextFreeIndex": pollNextFreeIndex,
       "powerSupply": powerSupply,
       "netBuilder-mib": netBuilder_mib,
       "lBridgeECS-mib": lBridgeECS_mib,
       "deskMan-mib": deskMan_mib,
       "linkBuilderMSH-mib": linkBuilderMSH_mib,
       "snmpDot3RpMauMgt": snmpDot3RpMauMgt,
       "rpMauBasicGroup": rpMauBasicGroup,
       "rpMauTable": rpMauTable,
       "rpMauEntry": rpMauEntry,
       "rpMauGroupIndex": rpMauGroupIndex,
       "rpMauPortIndex": rpMauPortIndex,
       "rpMauIndex": rpMauIndex,
       "rpMauType": rpMauType,
       "rpMauAdminState": rpMauAdminState,
       "rpMauMediaAvailable": rpMauMediaAvailable,
       "rpMauLostMedias": rpMauLostMedias,
       "rpMauJabberState": rpMauJabberState,
       "rpMauJabbers": rpMauJabbers,
       "ringBuilder": ringBuilder,
       "ringBuilderTable": ringBuilderTable,
       "ringBuilderTableEntry": ringBuilderTableEntry,
       "rbServiceId": rbServiceId,
       "rbRingInMedia": rbRingInMedia,
       "rbRingInMode": rbRingInMode,
       "rbRingInState": rbRingInState,
       "rbRingOutMedia": rbRingOutMedia,
       "rbRingOutMode": rbRingOutMode,
       "rbRingOutState": rbRingOutState,
       "rbMode": rbMode,
       "rbTest": rbTest,
       "rbDRIState": rbDRIState,
       "ringMauPortTable": ringMauPortTable,
       "ringMauPortTableEntry": ringMauPortTableEntry,
       "rbMauServiceId": rbMauServiceId,
       "rbMauSlot": rbMauSlot,
       "rbMauPort": rbMauPort,
       "rbMauMedia": rbMauMedia,
       "rbMauPortAdminState": rbMauPortAdminState,
       "rbMauPortAttachState": rbMauPortAttachState,
       "rbMauPortZDLState": rbMauPortZDLState,
       "rbMauPortDisableReason": rbMauPortDisableReason,
       "ringBuilderMACTable": ringBuilderMACTable,
       "ringBuilderMACTableEntry": ringBuilderMACTableEntry,
       "rbMACServiceId": rbMACServiceId,
       "rbMACinstance": rbMACinstance,
       "rbMACAddress": rbMACAddress,
       "linkBuilderFMS-mib": linkBuilderFMS_mib,
       "linkBuilderFDDI-wghub-mib": linkBuilderFDDI_wghub_mib,
       "linkSwitch-mib": linkSwitch_mib}
)
