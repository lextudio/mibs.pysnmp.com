# SNMP MIB module (DE1500-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DE1500-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:30 2024
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
 internet,
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
    "internet",
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

_Directory_ObjectIdentity = ObjectIdentity
directory = _Directory_ObjectIdentity(
    (1, 3, 6, 1, 1)
)
_Mib_ObjectIdentity = ObjectIdentity
mib = _Mib_ObjectIdentity(
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
sysLocation.setMaxAccess("read-only")
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
              28)
        )
    )
    namedValues = NamedValues(
        *(("basicISDN", 20),
          ("cept", 19),
          ("ddn-x25", 4),
          ("eon", 25),
          ("ethernet-3Mbit", 26),
          ("ethernet-csmacd", 6),
          ("fddi", 15),
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
          ("slip", 28),
          ("softwareLoopback", 24),
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
_IfPhyAddress_Type = OctetString
_IfPhyAddress_Object = MibScalar
ifPhyAddress = _IfPhyAddress_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 6),
    _IfPhyAddress_Type()
)
ifPhyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhyAddress.setStatus("mandatory")


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
_SnmpInBadTypes_Type = Counter32
_SnmpInBadTypes_Object = MibScalar
snmpInBadTypes = _SnmpInBadTypes_Object(
    (1, 3, 6, 1, 2, 1, 11, 7),
    _SnmpInBadTypes_Type()
)
snmpInBadTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInBadTypes.setStatus("mandatory")
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
_SnmpOutReadOnlys_Type = Counter32
_SnmpOutReadOnlys_Object = MibScalar
snmpOutReadOnlys = _SnmpOutReadOnlys_Object(
    (1, 3, 6, 1, 2, 1, 11, 23),
    _SnmpOutReadOnlys_Type()
)
snmpOutReadOnlys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutReadOnlys.setStatus("mandatory")
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


class _SnmpEnableAuthTraps_Type(Integer32):
    """Custom type snmpEnableAuthTraps based on Integer32"""
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


_SnmpEnableAuthTraps_Type.__name__ = "Integer32"
_SnmpEnableAuthTraps_Object = MibScalar
snmpEnableAuthTraps = _SnmpEnableAuthTraps_Object(
    (1, 3, 6, 1, 2, 1, 11, 30),
    _SnmpEnableAuthTraps_Type()
)
snmpEnableAuthTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpEnableAuthTraps.setStatus("mandatory")
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 3)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_D_link_ObjectIdentity = ObjectIdentity
d_link = _D_link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171)
)
_Hubmib_ObjectIdentity = ObjectIdentity
hubmib = _Hubmib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 2)
)
_BasicGroup_ObjectIdentity = ObjectIdentity
basicGroup = _BasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 2, 1)
)
_BasicHubMIBVersion_Type = DisplayString
_BasicHubMIBVersion_Object = MibScalar
basicHubMIBVersion = _BasicHubMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 1),
    _BasicHubMIBVersion_Type()
)
basicHubMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicHubMIBVersion.setStatus("mandatory")
_BasicHubVender_Type = OctetString
_BasicHubVender_Object = MibScalar
basicHubVender = _BasicHubVender_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 2),
    _BasicHubVender_Type()
)
basicHubVender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicHubVender.setStatus("mandatory")
_BasicHubProduct_Type = OctetString
_BasicHubProduct_Object = MibScalar
basicHubProduct = _BasicHubProduct_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 3),
    _BasicHubProduct_Type()
)
basicHubProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicHubProduct.setStatus("mandatory")
_BasicHubVersion_Type = OctetString
_BasicHubVersion_Object = MibScalar
basicHubVersion = _BasicHubVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 4),
    _BasicHubVersion_Type()
)
basicHubVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicHubVersion.setStatus("mandatory")


class _BasicHubHealthState_Type(Integer32):
    """Custom type basicHubHealthState based on Integer32"""
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
          ("hubFailure", 3),
          ("ok", 2),
          ("other", 1),
          ("portFailure", 5))
    )


_BasicHubHealthState_Type.__name__ = "Integer32"
_BasicHubHealthState_Object = MibScalar
basicHubHealthState = _BasicHubHealthState_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 5),
    _BasicHubHealthState_Type()
)
basicHubHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicHubHealthState.setStatus("mandatory")
_BasicHubHealthText_Type = DisplayString
_BasicHubHealthText_Object = MibScalar
basicHubHealthText = _BasicHubHealthText_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 6),
    _BasicHubHealthText_Type()
)
basicHubHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicHubHealthText.setStatus("mandatory")
_BasicHubHealthData_Type = OctetString
_BasicHubHealthData_Object = MibScalar
basicHubHealthData = _BasicHubHealthData_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 7),
    _BasicHubHealthData_Type()
)
basicHubHealthData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicHubHealthData.setStatus("mandatory")


class _BasicHubReset_Type(Integer32):
    """Custom type basicHubReset based on Integer32"""
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


_BasicHubReset_Type.__name__ = "Integer32"
_BasicHubReset_Object = MibScalar
basicHubReset = _BasicHubReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 8),
    _BasicHubReset_Type()
)
basicHubReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicHubReset.setStatus("mandatory")


class _BasicHubSelfTest1_Type(Integer32):
    """Custom type basicHubSelfTest1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSelfTest1", 1),
          ("selfTest1", 2))
    )


_BasicHubSelfTest1_Type.__name__ = "Integer32"
_BasicHubSelfTest1_Object = MibScalar
basicHubSelfTest1 = _BasicHubSelfTest1_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 9),
    _BasicHubSelfTest1_Type()
)
basicHubSelfTest1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicHubSelfTest1.setStatus("mandatory")


class _BasicHubSelfTest2_Type(Integer32):
    """Custom type basicHubSelfTest2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSelfTest2", 1),
          ("selfTest2", 2))
    )


_BasicHubSelfTest2_Type.__name__ = "Integer32"
_BasicHubSelfTest2_Object = MibScalar
basicHubSelfTest2 = _BasicHubSelfTest2_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 10),
    _BasicHubSelfTest2_Type()
)
basicHubSelfTest2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicHubSelfTest2.setStatus("mandatory")


class _BasucHubIntrusion_Type(Integer32):
    """Custom type basucHubIntrusion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intrusion", 2),
          ("noIntrusion", 1))
    )


_BasucHubIntrusion_Type.__name__ = "Integer32"
_BasucHubIntrusion_Object = MibScalar
basucHubIntrusion = _BasucHubIntrusion_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 11),
    _BasucHubIntrusion_Type()
)
basucHubIntrusion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basucHubIntrusion.setStatus("mandatory")


class _BasicHubClearStats_Type(Integer32):
    """Custom type basicHubClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearstatsistics", 2),
          ("other", 1))
    )


_BasicHubClearStats_Type.__name__ = "Integer32"
_BasicHubClearStats_Object = MibScalar
basicHubClearStats = _BasicHubClearStats_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 12),
    _BasicHubClearStats_Type()
)
basicHubClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicHubClearStats.setStatus("mandatory")
_BasicHubLed_Type = OctetString
_BasicHubLed_Object = MibScalar
basicHubLed = _BasicHubLed_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 13),
    _BasicHubLed_Type()
)
basicHubLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicHubLed.setStatus("mandatory")
_BasicHubNumofPorts_Type = Integer32
_BasicHubNumofPorts_Object = MibScalar
basicHubNumofPorts = _BasicHubNumofPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 14),
    _BasicHubNumofPorts_Type()
)
basicHubNumofPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicHubNumofPorts.setStatus("mandatory")
_BasicPortTable_Object = MibTable
basicPortTable = _BasicPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 15)
)
if mibBuilder.loadTexts:
    basicPortTable.setStatus("mandatory")
_BasicPortEntry_Object = MibTableRow
basicPortEntry = _BasicPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 15, 1)
)
if mibBuilder.loadTexts:
    basicPortEntry.setStatus("mandatory")
_BasicPortID_Type = Integer32
_BasicPortID_Object = MibTableColumn
basicPortID = _BasicPortID_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 15, 1, 1),
    _BasicPortID_Type()
)
basicPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortID.setStatus("mandatory")


class _BasicPortAdminState_Type(Integer32):
    """Custom type basicPortAdminState based on Integer32"""
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


_BasicPortAdminState_Type.__name__ = "Integer32"
_BasicPortAdminState_Object = MibTableColumn
basicPortAdminState = _BasicPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 15, 1, 2),
    _BasicPortAdminState_Type()
)
basicPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAdminState.setStatus("mandatory")


class _BasicPortAutoPartState_Type(Integer32):
    """Custom type basicPortAutoPartState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoPartitioned", 1),
          ("notAutoPartitioned", 2))
    )


_BasicPortAutoPartState_Type.__name__ = "Integer32"
_BasicPortAutoPartState_Object = MibTableColumn
basicPortAutoPartState = _BasicPortAutoPartState_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 15, 1, 3),
    _BasicPortAutoPartState_Type()
)
basicPortAutoPartState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortAutoPartState.setStatus("mandatory")
_BasicPortName_Type = DisplayString
_BasicPortName_Object = MibTableColumn
basicPortName = _BasicPortName_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 15, 1, 4),
    _BasicPortName_Type()
)
basicPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortName.setStatus("mandatory")


class _BasicPortType_Type(Integer32):
    """Custom type basicPortType based on Integer32"""
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
        *(("other", 1),
          ("tenBASE2", 3),
          ("tenBASE5", 4),
          ("tenBASET", 2))
    )


_BasicPortType_Type.__name__ = "Integer32"
_BasicPortType_Object = MibTableColumn
basicPortType = _BasicPortType_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 15, 1, 5),
    _BasicPortType_Type()
)
basicPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortType.setStatus("mandatory")


class _BasicPortLink_Type(Integer32):
    """Custom type basicPortLink based on Integer32"""
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
          ("other", 1),
          ("up", 3))
    )


_BasicPortLink_Type.__name__ = "Integer32"
_BasicPortLink_Object = MibTableColumn
basicPortLink = _BasicPortLink_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 15, 1, 6),
    _BasicPortLink_Type()
)
basicPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortLink.setStatus("mandatory")


class _BasicPortClearStats_Type(Integer32):
    """Custom type basicPortClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearportstats", 2),
          ("other", 1))
    )


_BasicPortClearStats_Type.__name__ = "Integer32"
_BasicPortClearStats_Object = MibTableColumn
basicPortClearStats = _BasicPortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 1, 15, 1, 7),
    _BasicPortClearStats_Type()
)
basicPortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortClearStats.setStatus("mandatory")
_MonitorGroup_ObjectIdentity = ObjectIdentity
monitorGroup = _MonitorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 2, 2)
)
_MonHubCollisions_Type = Counter32
_MonHubCollisions_Object = MibScalar
monHubCollisions = _MonHubCollisions_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 1),
    _MonHubCollisions_Type()
)
monHubCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monHubCollisions.setStatus("mandatory")
_MonHubBadFrames_Type = Counter32
_MonHubBadFrames_Object = MibScalar
monHubBadFrames = _MonHubBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 2),
    _MonHubBadFrames_Type()
)
monHubBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monHubBadFrames.setStatus("mandatory")
_MonHubReadableOctets_Type = Counter32
_MonHubReadableOctets_Object = MibScalar
monHubReadableOctets = _MonHubReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 3),
    _MonHubReadableOctets_Type()
)
monHubReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monHubReadableOctets.setStatus("mandatory")
_MonHubReadableFrames_Type = Counter32
_MonHubReadableFrames_Object = MibScalar
monHubReadableFrames = _MonHubReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 4),
    _MonHubReadableFrames_Type()
)
monHubReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monHubReadableFrames.setStatus("mandatory")
_MonHubLedFlag_Type = Integer32
_MonHubLedFlag_Object = MibScalar
monHubLedFlag = _MonHubLedFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 5),
    _MonHubLedFlag_Type()
)
monHubLedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monHubLedFlag.setStatus("mandatory")


class _MonHubUtilization_Type(Integer32):
    """Custom type monHubUtilization based on Integer32"""
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
        *(("fifteenPercentage", 5),
          ("fifty-fivePercentage", 11),
          ("finety-ninePercentage", 12),
          ("fivePercentage", 3),
          ("fortyPercentage", 10),
          ("onePercentage", 1),
          ("tenPercentage", 4),
          ("thirty-fivePercentage", 9),
          ("thirtyPercentage", 8),
          ("twenty-fivePercentage", 7),
          ("twentyPercentage", 6),
          ("twoPercentage", 2))
    )


_MonHubUtilization_Type.__name__ = "Integer32"
_MonHubUtilization_Object = MibScalar
monHubUtilization = _MonHubUtilization_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 6),
    _MonHubUtilization_Type()
)
monHubUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monHubUtilization.setStatus("mandatory")
_MonPortTable_Object = MibTable
monPortTable = _MonPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 7)
)
if mibBuilder.loadTexts:
    monPortTable.setStatus("mandatory")
_MonPortEntry_Object = MibTableRow
monPortEntry = _MonPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    monPortEntry.setStatus("mandatory")
_MonPortID_Type = Integer32
_MonPortID_Object = MibTableColumn
monPortID = _MonPortID_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 7, 1, 1),
    _MonPortID_Type()
)
monPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monPortID.setStatus("mandatory")
_MonPortReadableFrames_Type = Counter32
_MonPortReadableFrames_Object = MibTableColumn
monPortReadableFrames = _MonPortReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 7, 1, 2),
    _MonPortReadableFrames_Type()
)
monPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monPortReadableFrames.setStatus("mandatory")
_MonPortReadableOctets_Type = Counter32
_MonPortReadableOctets_Object = MibTableColumn
monPortReadableOctets = _MonPortReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 7, 1, 3),
    _MonPortReadableOctets_Type()
)
monPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monPortReadableOctets.setStatus("mandatory")
_MonPortFcsErrors_Type = Counter32
_MonPortFcsErrors_Object = MibTableColumn
monPortFcsErrors = _MonPortFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 7, 1, 4),
    _MonPortFcsErrors_Type()
)
monPortFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monPortFcsErrors.setStatus("mandatory")
_MonPortAlignmentErrors_Type = Counter32
_MonPortAlignmentErrors_Object = MibTableColumn
monPortAlignmentErrors = _MonPortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 7, 1, 5),
    _MonPortAlignmentErrors_Type()
)
monPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monPortAlignmentErrors.setStatus("mandatory")
_MonPortFrameTooLongs_Type = Counter32
_MonPortFrameTooLongs_Object = MibTableColumn
monPortFrameTooLongs = _MonPortFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 7, 1, 6),
    _MonPortFrameTooLongs_Type()
)
monPortFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monPortFrameTooLongs.setStatus("mandatory")
_MonPortFrameTooShorts_Type = Counter32
_MonPortFrameTooShorts_Object = MibTableColumn
monPortFrameTooShorts = _MonPortFrameTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 7, 1, 7),
    _MonPortFrameTooShorts_Type()
)
monPortFrameTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monPortFrameTooShorts.setStatus("mandatory")
_MonPortRunts_Type = Counter32
_MonPortRunts_Object = MibTableColumn
monPortRunts = _MonPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 7, 1, 8),
    _MonPortRunts_Type()
)
monPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monPortRunts.setStatus("mandatory")
_MonPortCollisions_Type = Counter32
_MonPortCollisions_Object = MibTableColumn
monPortCollisions = _MonPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 7, 1, 9),
    _MonPortCollisions_Type()
)
monPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monPortCollisions.setStatus("mandatory")
_MonPortLateCollisions_Type = Counter32
_MonPortLateCollisions_Object = MibTableColumn
monPortLateCollisions = _MonPortLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 7, 1, 10),
    _MonPortLateCollisions_Type()
)
monPortLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monPortLateCollisions.setStatus("mandatory")
_MonPortDataRateMismatchs_Type = Counter32
_MonPortDataRateMismatchs_Object = MibTableColumn
monPortDataRateMismatchs = _MonPortDataRateMismatchs_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 7, 1, 11),
    _MonPortDataRateMismatchs_Type()
)
monPortDataRateMismatchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monPortDataRateMismatchs.setStatus("mandatory")
_MonPortAutoPartitions_Type = Counter32
_MonPortAutoPartitions_Object = MibTableColumn
monPortAutoPartitions = _MonPortAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 7, 1, 12),
    _MonPortAutoPartitions_Type()
)
monPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monPortAutoPartitions.setStatus("mandatory")
_MonPortBadFrames_Type = Counter32
_MonPortBadFrames_Object = MibTableColumn
monPortBadFrames = _MonPortBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 2, 7, 1, 13),
    _MonPortBadFrames_Type()
)
monPortBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monPortBadFrames.setStatus("mandatory")
_AddrTrackGroup_ObjectIdentity = ObjectIdentity
addrTrackGroup = _AddrTrackGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 2, 3)
)
_AddPortTable_Object = MibTable
addPortTable = _AddPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 3, 1)
)
if mibBuilder.loadTexts:
    addPortTable.setStatus("mandatory")
_AddPortEntry_Object = MibTableRow
addPortEntry = _AddPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    addPortEntry.setStatus("mandatory")
_AddPortID_Type = Integer32
_AddPortID_Object = MibTableColumn
addPortID = _AddPortID_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 3, 1, 1, 1),
    _AddPortID_Type()
)
addPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addPortID.setStatus("mandatory")


class _AddPortLastSourceAddress_Type(OctetString):
    """Custom type addPortLastSourceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AddPortLastSourceAddress_Type.__name__ = "OctetString"
_AddPortLastSourceAddress_Object = MibTableColumn
addPortLastSourceAddress = _AddPortLastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 3, 1, 1, 2),
    _AddPortLastSourceAddress_Type()
)
addPortLastSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addPortLastSourceAddress.setStatus("mandatory")
_AddPortSourceAddrChanges_Type = Counter32
_AddPortSourceAddrChanges_Object = MibTableColumn
addPortSourceAddrChanges = _AddPortSourceAddrChanges_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 3, 1, 1, 3),
    _AddPortSourceAddrChanges_Type()
)
addPortSourceAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addPortSourceAddrChanges.setStatus("mandatory")


class _AddPortAuthorized_Type(Integer32):
    """Custom type addPortAuthorized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 2),
          ("unauthorized", 1))
    )


_AddPortAuthorized_Type.__name__ = "Integer32"
_AddPortAuthorized_Object = MibTableColumn
addPortAuthorized = _AddPortAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 171, 2, 3, 1, 1, 4),
    _AddPortAuthorized_Type()
)
addPortAuthorized.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addPortAuthorized.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DE1500-MIB",
    **{"directory": directory,
       "mib": mib,
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
       "ifPhyAddress": ifPhyAddress,
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
       "udp": udp,
       "udpInDatagrams": udpInDatagrams,
       "udpNoPorts": udpNoPorts,
       "udpInErrors": udpInErrors,
       "udpOutDatagrams": udpOutDatagrams,
       "udpTable": udpTable,
       "udpEntry": udpEntry,
       "udpLocalAddress": udpLocalAddress,
       "udpLocalPort": udpLocalPort,
       "snmp": snmp,
       "snmpInPkts": snmpInPkts,
       "snmpOutPkts": snmpOutPkts,
       "snmpInBadVersions": snmpInBadVersions,
       "snmpInBadCommunityNames": snmpInBadCommunityNames,
       "snmpInBadCommunityUses": snmpInBadCommunityUses,
       "snmpInASNParseErrs": snmpInASNParseErrs,
       "snmpInBadTypes": snmpInBadTypes,
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
       "snmpOutReadOnlys": snmpOutReadOnlys,
       "snmpOutGenErrs": snmpOutGenErrs,
       "snmpOutGetRequests": snmpOutGetRequests,
       "snmpOutGetNexts": snmpOutGetNexts,
       "snmpOutSetRequests": snmpOutSetRequests,
       "snmpOutGetResponses": snmpOutGetResponses,
       "snmpOutTraps": snmpOutTraps,
       "snmpEnableAuthTraps": snmpEnableAuthTraps,
       "experimental": experimental,
       "private": private,
       "enterprises": enterprises,
       "d-link": d_link,
       "hubmib": hubmib,
       "basicGroup": basicGroup,
       "basicHubMIBVersion": basicHubMIBVersion,
       "basicHubVender": basicHubVender,
       "basicHubProduct": basicHubProduct,
       "basicHubVersion": basicHubVersion,
       "basicHubHealthState": basicHubHealthState,
       "basicHubHealthText": basicHubHealthText,
       "basicHubHealthData": basicHubHealthData,
       "basicHubReset": basicHubReset,
       "basicHubSelfTest1": basicHubSelfTest1,
       "basicHubSelfTest2": basicHubSelfTest2,
       "basucHubIntrusion": basucHubIntrusion,
       "basicHubClearStats": basicHubClearStats,
       "basicHubLed": basicHubLed,
       "basicHubNumofPorts": basicHubNumofPorts,
       "basicPortTable": basicPortTable,
       "basicPortEntry": basicPortEntry,
       "basicPortID": basicPortID,
       "basicPortAdminState": basicPortAdminState,
       "basicPortAutoPartState": basicPortAutoPartState,
       "basicPortName": basicPortName,
       "basicPortType": basicPortType,
       "basicPortLink": basicPortLink,
       "basicPortClearStats": basicPortClearStats,
       "monitorGroup": monitorGroup,
       "monHubCollisions": monHubCollisions,
       "monHubBadFrames": monHubBadFrames,
       "monHubReadableOctets": monHubReadableOctets,
       "monHubReadableFrames": monHubReadableFrames,
       "monHubLedFlag": monHubLedFlag,
       "monHubUtilization": monHubUtilization,
       "monPortTable": monPortTable,
       "monPortEntry": monPortEntry,
       "monPortID": monPortID,
       "monPortReadableFrames": monPortReadableFrames,
       "monPortReadableOctets": monPortReadableOctets,
       "monPortFcsErrors": monPortFcsErrors,
       "monPortAlignmentErrors": monPortAlignmentErrors,
       "monPortFrameTooLongs": monPortFrameTooLongs,
       "monPortFrameTooShorts": monPortFrameTooShorts,
       "monPortRunts": monPortRunts,
       "monPortCollisions": monPortCollisions,
       "monPortLateCollisions": monPortLateCollisions,
       "monPortDataRateMismatchs": monPortDataRateMismatchs,
       "monPortAutoPartitions": monPortAutoPartitions,
       "monPortBadFrames": monPortBadFrames,
       "addrTrackGroup": addrTrackGroup,
       "addPortTable": addPortTable,
       "addPortEntry": addPortEntry,
       "addPortID": addPortID,
       "addPortLastSourceAddress": addPortLastSourceAddress,
       "addPortSourceAddrChanges": addPortSourceAddrChanges,
       "addPortAuthorized": addPortAuthorized}
)
