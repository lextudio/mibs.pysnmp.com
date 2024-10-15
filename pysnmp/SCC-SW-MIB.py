# SNMP MIB module (SCC-SW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCC-SW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:00 2024
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

(sccMibSw,
 sccSidewinder) = mibBuilder.importSymbols(
    "SCC-MIB",
    "sccMibSw",
    "sccSidewinder")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysDescr,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysUpTime")

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

_SwProxy_ObjectIdentity = ObjectIdentity
swProxy = _SwProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 5)
)
_SwProxyTable_Object = MibTable
swProxyTable = _SwProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    swProxyTable.setStatus("mandatory")
_SwProxyEntry_Object = MibTableRow
swProxyEntry = _SwProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 5, 1, 1)
)
swProxyEntry.setIndexNames(
    (0, "SCC-SW-MIB", "swProxyIndex"),
)
if mibBuilder.loadTexts:
    swProxyEntry.setStatus("mandatory")
_SwProxyIndex_Type = Integer32
_SwProxyIndex_Object = MibTableColumn
swProxyIndex = _SwProxyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 5, 1, 1, 1),
    _SwProxyIndex_Type()
)
swProxyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProxyIndex.setStatus("mandatory")


class _SwProxyName_Type(DisplayString):
    """Custom type swProxyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwProxyName_Type.__name__ = "DisplayString"
_SwProxyName_Object = MibTableColumn
swProxyName = _SwProxyName_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 5, 1, 1, 2),
    _SwProxyName_Type()
)
swProxyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProxyName.setStatus("mandatory")


class _SwProxyAdminStatus_Type(Integer32):
    """Custom type swProxyAdminStatus based on Integer32"""
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


_SwProxyAdminStatus_Type.__name__ = "Integer32"
_SwProxyAdminStatus_Object = MibTableColumn
swProxyAdminStatus = _SwProxyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 5, 1, 1, 3),
    _SwProxyAdminStatus_Type()
)
swProxyAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProxyAdminStatus.setStatus("mandatory")


class _SwProxyOperStatus_Type(Integer32):
    """Custom type swProxyOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_SwProxyOperStatus_Type.__name__ = "Integer32"
_SwProxyOperStatus_Object = MibTableColumn
swProxyOperStatus = _SwProxyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 5, 1, 1, 4),
    _SwProxyOperStatus_Type()
)
swProxyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProxyOperStatus.setStatus("mandatory")
_SwBurb_ObjectIdentity = ObjectIdentity
swBurb = _SwBurb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 6)
)
_SwBurbTotal_Type = Integer32
_SwBurbTotal_Object = MibScalar
swBurbTotal = _SwBurbTotal_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 6, 1),
    _SwBurbTotal_Type()
)
swBurbTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBurbTotal.setStatus("mandatory")
_SwBurbViewTable_Object = MibTable
swBurbViewTable = _SwBurbViewTable_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    swBurbViewTable.setStatus("mandatory")
_SwBurbViewEntry_Object = MibTableRow
swBurbViewEntry = _SwBurbViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 6, 2, 1)
)
swBurbViewEntry.setIndexNames(
    (0, "SCC-SW-MIB", "swBurbIndex"),
)
if mibBuilder.loadTexts:
    swBurbViewEntry.setStatus("mandatory")
_SwBurbIndex_Type = Integer32
_SwBurbIndex_Object = MibTableColumn
swBurbIndex = _SwBurbIndex_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 6, 2, 1, 1),
    _SwBurbIndex_Type()
)
swBurbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBurbIndex.setStatus("mandatory")


class _SwBurbViewName_Type(DisplayString):
    """Custom type swBurbViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwBurbViewName_Type.__name__ = "DisplayString"
_SwBurbViewName_Object = MibTableColumn
swBurbViewName = _SwBurbViewName_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 6, 2, 1, 2),
    _SwBurbViewName_Type()
)
swBurbViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBurbViewName.setStatus("mandatory")
_SwBurbedMib2_ObjectIdentity = ObjectIdentity
swBurbedMib2 = _SwBurbedMib2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7)
)
_SwInterfaces_ObjectIdentity = ObjectIdentity
swInterfaces = _SwInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1)
)
_SwIfNumber_Type = Integer32
_SwIfNumber_Object = MibScalar
swIfNumber = _SwIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 1),
    _SwIfNumber_Type()
)
swIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfNumber.setStatus("mandatory")
_SwIfTable_Object = MibTable
swIfTable = _SwIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    swIfTable.setStatus("mandatory")
_SwIfEntry_Object = MibTableRow
swIfEntry = _SwIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1)
)
swIfEntry.setIndexNames(
    (0, "SCC-SW-MIB", "swIfBurbIndex"),
    (0, "SCC-SW-MIB", "swIfIndex"),
)
if mibBuilder.loadTexts:
    swIfEntry.setStatus("mandatory")
_SwIfIndex_Type = Integer32
_SwIfIndex_Object = MibTableColumn
swIfIndex = _SwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 1),
    _SwIfIndex_Type()
)
swIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfIndex.setStatus("mandatory")


class _SwIfDescr_Type(DisplayString):
    """Custom type swIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwIfDescr_Type.__name__ = "DisplayString"
_SwIfDescr_Object = MibTableColumn
swIfDescr = _SwIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 2),
    _SwIfDescr_Type()
)
swIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfDescr.setStatus("mandatory")


class _SwIfType_Type(Integer32):
    """Custom type swIfType based on Integer32"""
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


_SwIfType_Type.__name__ = "Integer32"
_SwIfType_Object = MibTableColumn
swIfType = _SwIfType_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 3),
    _SwIfType_Type()
)
swIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfType.setStatus("mandatory")
_SwIfMtu_Type = Integer32
_SwIfMtu_Object = MibTableColumn
swIfMtu = _SwIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 4),
    _SwIfMtu_Type()
)
swIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfMtu.setStatus("mandatory")
_SwIfSpeed_Type = Gauge32
_SwIfSpeed_Object = MibTableColumn
swIfSpeed = _SwIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 5),
    _SwIfSpeed_Type()
)
swIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfSpeed.setStatus("mandatory")
_SwIfPhysAddress_Type = PhysAddress
_SwIfPhysAddress_Object = MibTableColumn
swIfPhysAddress = _SwIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 6),
    _SwIfPhysAddress_Type()
)
swIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfPhysAddress.setStatus("mandatory")


class _SwIfAdminStatus_Type(Integer32):
    """Custom type swIfAdminStatus based on Integer32"""
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


_SwIfAdminStatus_Type.__name__ = "Integer32"
_SwIfAdminStatus_Object = MibTableColumn
swIfAdminStatus = _SwIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 7),
    _SwIfAdminStatus_Type()
)
swIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIfAdminStatus.setStatus("mandatory")


class _SwIfOperStatus_Type(Integer32):
    """Custom type swIfOperStatus based on Integer32"""
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


_SwIfOperStatus_Type.__name__ = "Integer32"
_SwIfOperStatus_Object = MibTableColumn
swIfOperStatus = _SwIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 8),
    _SwIfOperStatus_Type()
)
swIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfOperStatus.setStatus("mandatory")
_SwIfLastChange_Type = TimeTicks
_SwIfLastChange_Object = MibTableColumn
swIfLastChange = _SwIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 9),
    _SwIfLastChange_Type()
)
swIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfLastChange.setStatus("mandatory")
_SwIfInOctets_Type = Counter32
_SwIfInOctets_Object = MibTableColumn
swIfInOctets = _SwIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 10),
    _SwIfInOctets_Type()
)
swIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfInOctets.setStatus("mandatory")
_SwIfInUcastPkts_Type = Counter32
_SwIfInUcastPkts_Object = MibTableColumn
swIfInUcastPkts = _SwIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 11),
    _SwIfInUcastPkts_Type()
)
swIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfInUcastPkts.setStatus("mandatory")
_SwIfInNUcastPkts_Type = Counter32
_SwIfInNUcastPkts_Object = MibTableColumn
swIfInNUcastPkts = _SwIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 12),
    _SwIfInNUcastPkts_Type()
)
swIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfInNUcastPkts.setStatus("mandatory")
_SwIfInDiscards_Type = Counter32
_SwIfInDiscards_Object = MibTableColumn
swIfInDiscards = _SwIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 13),
    _SwIfInDiscards_Type()
)
swIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfInDiscards.setStatus("mandatory")
_SwIfInErrors_Type = Counter32
_SwIfInErrors_Object = MibTableColumn
swIfInErrors = _SwIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 14),
    _SwIfInErrors_Type()
)
swIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfInErrors.setStatus("mandatory")
_SwIfInUnknownProtos_Type = Counter32
_SwIfInUnknownProtos_Object = MibTableColumn
swIfInUnknownProtos = _SwIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 15),
    _SwIfInUnknownProtos_Type()
)
swIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfInUnknownProtos.setStatus("mandatory")
_SwIfOutOctets_Type = Counter32
_SwIfOutOctets_Object = MibTableColumn
swIfOutOctets = _SwIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 16),
    _SwIfOutOctets_Type()
)
swIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfOutOctets.setStatus("mandatory")
_SwIfOutUcastPkts_Type = Counter32
_SwIfOutUcastPkts_Object = MibTableColumn
swIfOutUcastPkts = _SwIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 17),
    _SwIfOutUcastPkts_Type()
)
swIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfOutUcastPkts.setStatus("mandatory")
_SwIfOutNUcastPkts_Type = Counter32
_SwIfOutNUcastPkts_Object = MibTableColumn
swIfOutNUcastPkts = _SwIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 18),
    _SwIfOutNUcastPkts_Type()
)
swIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfOutNUcastPkts.setStatus("mandatory")
_SwIfOutDiscards_Type = Counter32
_SwIfOutDiscards_Object = MibTableColumn
swIfOutDiscards = _SwIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 19),
    _SwIfOutDiscards_Type()
)
swIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfOutDiscards.setStatus("mandatory")
_SwIfOutErrors_Type = Counter32
_SwIfOutErrors_Object = MibTableColumn
swIfOutErrors = _SwIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 20),
    _SwIfOutErrors_Type()
)
swIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfOutErrors.setStatus("mandatory")
_SwIfOutQLen_Type = Gauge32
_SwIfOutQLen_Object = MibTableColumn
swIfOutQLen = _SwIfOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 21),
    _SwIfOutQLen_Type()
)
swIfOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfOutQLen.setStatus("mandatory")
_SwIfSpecific_Type = ObjectIdentifier
_SwIfSpecific_Object = MibTableColumn
swIfSpecific = _SwIfSpecific_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 22),
    _SwIfSpecific_Type()
)
swIfSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfSpecific.setStatus("mandatory")
_SwIfBurbIndex_Type = Integer32
_SwIfBurbIndex_Object = MibTableColumn
swIfBurbIndex = _SwIfBurbIndex_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 1, 2, 1, 23),
    _SwIfBurbIndex_Type()
)
swIfBurbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIfBurbIndex.setStatus("mandatory")
_SwIp_ObjectIdentity = ObjectIdentity
swIp = _SwIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2)
)
_SwIpAddrTable_Object = MibTable
swIpAddrTable = _SwIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    swIpAddrTable.setStatus("mandatory")
_SwIpAddrEntry_Object = MibTableRow
swIpAddrEntry = _SwIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 1, 1)
)
swIpAddrEntry.setIndexNames(
    (0, "SCC-SW-MIB", "swIpAdEntBurbIndex"),
    (0, "SCC-SW-MIB", "swIpAdEntAddr"),
)
if mibBuilder.loadTexts:
    swIpAddrEntry.setStatus("mandatory")
_SwIpAdEntAddr_Type = IpAddress
_SwIpAdEntAddr_Object = MibTableColumn
swIpAdEntAddr = _SwIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 1, 1, 1),
    _SwIpAdEntAddr_Type()
)
swIpAdEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpAdEntAddr.setStatus("mandatory")
_SwIpAdEntIfIndex_Type = Integer32
_SwIpAdEntIfIndex_Object = MibTableColumn
swIpAdEntIfIndex = _SwIpAdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 1, 1, 2),
    _SwIpAdEntIfIndex_Type()
)
swIpAdEntIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpAdEntIfIndex.setStatus("mandatory")
_SwIpAdEntNetMask_Type = IpAddress
_SwIpAdEntNetMask_Object = MibTableColumn
swIpAdEntNetMask = _SwIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 1, 1, 3),
    _SwIpAdEntNetMask_Type()
)
swIpAdEntNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpAdEntNetMask.setStatus("mandatory")
_SwIpAdEntBcastAddr_Type = Integer32
_SwIpAdEntBcastAddr_Object = MibTableColumn
swIpAdEntBcastAddr = _SwIpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 1, 1, 4),
    _SwIpAdEntBcastAddr_Type()
)
swIpAdEntBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpAdEntBcastAddr.setStatus("mandatory")


class _SwIpAdEntReasmMaxSize_Type(Integer32):
    """Custom type swIpAdEntReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwIpAdEntReasmMaxSize_Type.__name__ = "Integer32"
_SwIpAdEntReasmMaxSize_Object = MibTableColumn
swIpAdEntReasmMaxSize = _SwIpAdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 1, 1, 5),
    _SwIpAdEntReasmMaxSize_Type()
)
swIpAdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpAdEntReasmMaxSize.setStatus("mandatory")
_SwIpAdEntBurbIndex_Type = Integer32
_SwIpAdEntBurbIndex_Object = MibTableColumn
swIpAdEntBurbIndex = _SwIpAdEntBurbIndex_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 1, 1, 6),
    _SwIpAdEntBurbIndex_Type()
)
swIpAdEntBurbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpAdEntBurbIndex.setStatus("mandatory")
_SwIpRouteTable_Object = MibTable
swIpRouteTable = _SwIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 2)
)
if mibBuilder.loadTexts:
    swIpRouteTable.setStatus("mandatory")
_SwIpRouteEntry_Object = MibTableRow
swIpRouteEntry = _SwIpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 2, 1)
)
swIpRouteEntry.setIndexNames(
    (0, "SCC-SW-MIB", "swIpRouteBurbIndex"),
    (0, "SCC-SW-MIB", "swIpRouteDest"),
)
if mibBuilder.loadTexts:
    swIpRouteEntry.setStatus("mandatory")
_SwIpRouteDest_Type = IpAddress
_SwIpRouteDest_Object = MibTableColumn
swIpRouteDest = _SwIpRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 2, 1, 1),
    _SwIpRouteDest_Type()
)
swIpRouteDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpRouteDest.setStatus("mandatory")
_SwIpRouteIfIndex_Type = Integer32
_SwIpRouteIfIndex_Object = MibTableColumn
swIpRouteIfIndex = _SwIpRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 2, 1, 2),
    _SwIpRouteIfIndex_Type()
)
swIpRouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpRouteIfIndex.setStatus("mandatory")
_SwIpRouteMetric1_Type = Integer32
_SwIpRouteMetric1_Object = MibTableColumn
swIpRouteMetric1 = _SwIpRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 2, 1, 3),
    _SwIpRouteMetric1_Type()
)
swIpRouteMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpRouteMetric1.setStatus("mandatory")
_SwIpRouteMetric2_Type = Integer32
_SwIpRouteMetric2_Object = MibTableColumn
swIpRouteMetric2 = _SwIpRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 2, 1, 4),
    _SwIpRouteMetric2_Type()
)
swIpRouteMetric2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpRouteMetric2.setStatus("mandatory")
_SwIpRouteMetric3_Type = Integer32
_SwIpRouteMetric3_Object = MibTableColumn
swIpRouteMetric3 = _SwIpRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 2, 1, 5),
    _SwIpRouteMetric3_Type()
)
swIpRouteMetric3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpRouteMetric3.setStatus("mandatory")
_SwIpRouteMetric4_Type = Integer32
_SwIpRouteMetric4_Object = MibTableColumn
swIpRouteMetric4 = _SwIpRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 2, 1, 6),
    _SwIpRouteMetric4_Type()
)
swIpRouteMetric4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpRouteMetric4.setStatus("mandatory")
_SwIpRouteNextHop_Type = IpAddress
_SwIpRouteNextHop_Object = MibTableColumn
swIpRouteNextHop = _SwIpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 2, 1, 7),
    _SwIpRouteNextHop_Type()
)
swIpRouteNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpRouteNextHop.setStatus("mandatory")


class _SwIpRouteType_Type(Integer32):
    """Custom type swIpRouteType based on Integer32"""
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


_SwIpRouteType_Type.__name__ = "Integer32"
_SwIpRouteType_Object = MibTableColumn
swIpRouteType = _SwIpRouteType_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 2, 1, 8),
    _SwIpRouteType_Type()
)
swIpRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpRouteType.setStatus("mandatory")


class _SwIpRouteProto_Type(Integer32):
    """Custom type swIpRouteProto based on Integer32"""
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


_SwIpRouteProto_Type.__name__ = "Integer32"
_SwIpRouteProto_Object = MibTableColumn
swIpRouteProto = _SwIpRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 2, 1, 9),
    _SwIpRouteProto_Type()
)
swIpRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpRouteProto.setStatus("mandatory")
_SwIpRouteAge_Type = Integer32
_SwIpRouteAge_Object = MibTableColumn
swIpRouteAge = _SwIpRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 2, 1, 10),
    _SwIpRouteAge_Type()
)
swIpRouteAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpRouteAge.setStatus("mandatory")
_SwIpRouteMask_Type = IpAddress
_SwIpRouteMask_Object = MibTableColumn
swIpRouteMask = _SwIpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 2, 1, 11),
    _SwIpRouteMask_Type()
)
swIpRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpRouteMask.setStatus("mandatory")
_SwIpRouteMetric5_Type = Integer32
_SwIpRouteMetric5_Object = MibTableColumn
swIpRouteMetric5 = _SwIpRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 2, 1, 12),
    _SwIpRouteMetric5_Type()
)
swIpRouteMetric5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpRouteMetric5.setStatus("mandatory")
_SwIpRouteInfo_Type = ObjectIdentifier
_SwIpRouteInfo_Object = MibTableColumn
swIpRouteInfo = _SwIpRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 2, 1, 13),
    _SwIpRouteInfo_Type()
)
swIpRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpRouteInfo.setStatus("mandatory")
_SwIpRouteBurbIndex_Type = Integer32
_SwIpRouteBurbIndex_Object = MibTableColumn
swIpRouteBurbIndex = _SwIpRouteBurbIndex_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 2, 2, 1, 14),
    _SwIpRouteBurbIndex_Type()
)
swIpRouteBurbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpRouteBurbIndex.setStatus("mandatory")
_SwTcp_ObjectIdentity = ObjectIdentity
swTcp = _SwTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 3)
)
_SwTcpConnTable_Object = MibTable
swTcpConnTable = _SwTcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    swTcpConnTable.setStatus("mandatory")
_SwTcpConnEntry_Object = MibTableRow
swTcpConnEntry = _SwTcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 3, 1, 1)
)
swTcpConnEntry.setIndexNames(
    (0, "SCC-SW-MIB", "swTcpConnBurbIndex"),
    (0, "SCC-SW-MIB", "swTcpConnLocalAddress"),
    (0, "SCC-SW-MIB", "swTcpConnLocalPort"),
    (0, "SCC-SW-MIB", "swTcpConnRemAddress"),
    (0, "SCC-SW-MIB", "swTcpConnRemPort"),
)
if mibBuilder.loadTexts:
    swTcpConnEntry.setStatus("mandatory")


class _SwTcpConnState_Type(Integer32):
    """Custom type swTcpConnState based on Integer32"""
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


_SwTcpConnState_Type.__name__ = "Integer32"
_SwTcpConnState_Object = MibTableColumn
swTcpConnState = _SwTcpConnState_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 3, 1, 1, 1),
    _SwTcpConnState_Type()
)
swTcpConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTcpConnState.setStatus("mandatory")
_SwTcpConnLocalAddress_Type = IpAddress
_SwTcpConnLocalAddress_Object = MibTableColumn
swTcpConnLocalAddress = _SwTcpConnLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 3, 1, 1, 2),
    _SwTcpConnLocalAddress_Type()
)
swTcpConnLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTcpConnLocalAddress.setStatus("mandatory")


class _SwTcpConnLocalPort_Type(Integer32):
    """Custom type swTcpConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwTcpConnLocalPort_Type.__name__ = "Integer32"
_SwTcpConnLocalPort_Object = MibTableColumn
swTcpConnLocalPort = _SwTcpConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 3, 1, 1, 3),
    _SwTcpConnLocalPort_Type()
)
swTcpConnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTcpConnLocalPort.setStatus("mandatory")
_SwTcpConnRemAddress_Type = IpAddress
_SwTcpConnRemAddress_Object = MibTableColumn
swTcpConnRemAddress = _SwTcpConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 3, 1, 1, 4),
    _SwTcpConnRemAddress_Type()
)
swTcpConnRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTcpConnRemAddress.setStatus("mandatory")


class _SwTcpConnRemPort_Type(Integer32):
    """Custom type swTcpConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwTcpConnRemPort_Type.__name__ = "Integer32"
_SwTcpConnRemPort_Object = MibTableColumn
swTcpConnRemPort = _SwTcpConnRemPort_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 3, 1, 1, 5),
    _SwTcpConnRemPort_Type()
)
swTcpConnRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTcpConnRemPort.setStatus("mandatory")
_SwTcpConnBurbIndex_Type = Integer32
_SwTcpConnBurbIndex_Object = MibTableColumn
swTcpConnBurbIndex = _SwTcpConnBurbIndex_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 3, 1, 1, 6),
    _SwTcpConnBurbIndex_Type()
)
swTcpConnBurbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTcpConnBurbIndex.setStatus("mandatory")
_SwUdp_ObjectIdentity = ObjectIdentity
swUdp = _SwUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 4)
)
_SwUdpTable_Object = MibTable
swUdpTable = _SwUdpTable_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 4, 1)
)
if mibBuilder.loadTexts:
    swUdpTable.setStatus("mandatory")
_SwUdpEntry_Object = MibTableRow
swUdpEntry = _SwUdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 4, 1, 1)
)
swUdpEntry.setIndexNames(
    (0, "SCC-SW-MIB", "swUdpBurbIndex"),
    (0, "SCC-SW-MIB", "swUdpLocalAddress"),
    (0, "SCC-SW-MIB", "swUdpLocalPort"),
)
if mibBuilder.loadTexts:
    swUdpEntry.setStatus("mandatory")
_SwUdpLocalAddress_Type = IpAddress
_SwUdpLocalAddress_Object = MibTableColumn
swUdpLocalAddress = _SwUdpLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 4, 1, 1, 1),
    _SwUdpLocalAddress_Type()
)
swUdpLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUdpLocalAddress.setStatus("mandatory")


class _SwUdpLocalPort_Type(Integer32):
    """Custom type swUdpLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwUdpLocalPort_Type.__name__ = "Integer32"
_SwUdpLocalPort_Object = MibTableColumn
swUdpLocalPort = _SwUdpLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 4, 1, 1, 2),
    _SwUdpLocalPort_Type()
)
swUdpLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUdpLocalPort.setStatus("mandatory")
_SwUdpBurbIndex_Type = Integer32
_SwUdpBurbIndex_Object = MibTableColumn
swUdpBurbIndex = _SwUdpBurbIndex_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 7, 4, 1, 1, 3),
    _SwUdpBurbIndex_Type()
)
swUdpBurbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUdpBurbIndex.setStatus("mandatory")
_SwTrap_ObjectIdentity = ObjectIdentity
swTrap = _SwTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 10)
)
_SccAuthenFailSrcIp_Type = IpAddress
_SccAuthenFailSrcIp_Object = MibScalar
sccAuthenFailSrcIp = _SccAuthenFailSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 10, 1),
    _SccAuthenFailSrcIp_Type()
)
sccAuthenFailSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccAuthenFailSrcIp.setStatus("mandatory")
_SccAuthenFailSrcCommName_Type = OctetString
_SccAuthenFailSrcCommName_Object = MibScalar
sccAuthenFailSrcCommName = _SccAuthenFailSrcCommName_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 10, 2),
    _SccAuthenFailSrcCommName_Type()
)
sccAuthenFailSrcCommName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccAuthenFailSrcCommName.setStatus("mandatory")


class _SwUser_Type(DisplayString):
    """Custom type swUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwUser_Type.__name__ = "DisplayString"
_SwUser_Object = MibScalar
swUser = _SwUser_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 10, 3),
    _SwUser_Type()
)
swUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUser.setStatus("mandatory")


class _SwSRoleUser_Type(DisplayString):
    """Custom type swSRoleUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwSRoleUser_Type.__name__ = "DisplayString"
_SwSRoleUser_Object = MibScalar
swSRoleUser = _SwSRoleUser_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 10, 4),
    _SwSRoleUser_Type()
)
swSRoleUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSRoleUser.setStatus("mandatory")


class _SwSRoleName_Type(DisplayString):
    """Custom type swSRoleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwSRoleName_Type.__name__ = "DisplayString"
_SwSRoleName_Object = MibScalar
swSRoleName = _SwSRoleName_Object(
    (1, 3, 6, 1, 4, 1, 1573, 3, 1, 10, 5),
    _SwSRoleName_Type()
)
swSRoleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSRoleName.setStatus("mandatory")

# Managed Objects groups


# Notification objects

swColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1573, 2, 1, 0, 0)
)
swColdStart.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysUpTime"))
)
if mibBuilder.loadTexts:
    swColdStart.setStatus(
        ""
    )

swAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1573, 2, 1, 0, 4)
)
swAuthenticationFailure.setObjects(
      *(("SCC-SW-MIB", "sccAuthenFailSrcIp"),
        ("SCC-SW-MIB", "sccAuthenFailSrcCommName"))
)
if mibBuilder.loadTexts:
    swAuthenticationFailure.setStatus(
        ""
    )

swNetTrafficThresholds = NotificationType(
    (1, 3, 6, 1, 4, 1, 1573, 2, 1, 0, 201)
)
if mibBuilder.loadTexts:
    swNetTrafficThresholds.setStatus(
        ""
    )

swAttackAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1573, 2, 1, 0, 202)
)
if mibBuilder.loadTexts:
    swAttackAttempt.setStatus(
        ""
    )

swTeViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1573, 2, 1, 0, 203)
)
if mibBuilder.loadTexts:
    swTeViolation.setStatus(
        ""
    )

swAclThresholds = NotificationType(
    (1, 3, 6, 1, 4, 1, 1573, 2, 1, 0, 204)
)
if mibBuilder.loadTexts:
    swAclThresholds.setStatus(
        ""
    )

swBadProxyAuth = NotificationType(
    (1, 3, 6, 1, 4, 1, 1573, 2, 1, 0, 205)
)
if mibBuilder.loadTexts:
    swBadProxyAuth.setStatus(
        ""
    )

swNetProbeAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1573, 2, 1, 0, 206)
)
if mibBuilder.loadTexts:
    swNetProbeAttempt.setStatus(
        ""
    )

swMailFilterFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1573, 2, 1, 0, 207)
)
if mibBuilder.loadTexts:
    swMailFilterFailure.setStatus(
        ""
    )

swIPSECFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1573, 2, 1, 0, 208)
)
if mibBuilder.loadTexts:
    swIPSECFailure.setStatus(
        ""
    )

swFAILOVEREvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1573, 2, 1, 0, 209)
)
if mibBuilder.loadTexts:
    swFAILOVEREvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCC-SW-MIB",
    **{"swColdStart": swColdStart,
       "swAuthenticationFailure": swAuthenticationFailure,
       "swNetTrafficThresholds": swNetTrafficThresholds,
       "swAttackAttempt": swAttackAttempt,
       "swTeViolation": swTeViolation,
       "swAclThresholds": swAclThresholds,
       "swBadProxyAuth": swBadProxyAuth,
       "swNetProbeAttempt": swNetProbeAttempt,
       "swMailFilterFailure": swMailFilterFailure,
       "swIPSECFailure": swIPSECFailure,
       "swFAILOVEREvent": swFAILOVEREvent,
       "swProxy": swProxy,
       "swProxyTable": swProxyTable,
       "swProxyEntry": swProxyEntry,
       "swProxyIndex": swProxyIndex,
       "swProxyName": swProxyName,
       "swProxyAdminStatus": swProxyAdminStatus,
       "swProxyOperStatus": swProxyOperStatus,
       "swBurb": swBurb,
       "swBurbTotal": swBurbTotal,
       "swBurbViewTable": swBurbViewTable,
       "swBurbViewEntry": swBurbViewEntry,
       "swBurbIndex": swBurbIndex,
       "swBurbViewName": swBurbViewName,
       "swBurbedMib2": swBurbedMib2,
       "swInterfaces": swInterfaces,
       "swIfNumber": swIfNumber,
       "swIfTable": swIfTable,
       "swIfEntry": swIfEntry,
       "swIfIndex": swIfIndex,
       "swIfDescr": swIfDescr,
       "swIfType": swIfType,
       "swIfMtu": swIfMtu,
       "swIfSpeed": swIfSpeed,
       "swIfPhysAddress": swIfPhysAddress,
       "swIfAdminStatus": swIfAdminStatus,
       "swIfOperStatus": swIfOperStatus,
       "swIfLastChange": swIfLastChange,
       "swIfInOctets": swIfInOctets,
       "swIfInUcastPkts": swIfInUcastPkts,
       "swIfInNUcastPkts": swIfInNUcastPkts,
       "swIfInDiscards": swIfInDiscards,
       "swIfInErrors": swIfInErrors,
       "swIfInUnknownProtos": swIfInUnknownProtos,
       "swIfOutOctets": swIfOutOctets,
       "swIfOutUcastPkts": swIfOutUcastPkts,
       "swIfOutNUcastPkts": swIfOutNUcastPkts,
       "swIfOutDiscards": swIfOutDiscards,
       "swIfOutErrors": swIfOutErrors,
       "swIfOutQLen": swIfOutQLen,
       "swIfSpecific": swIfSpecific,
       "swIfBurbIndex": swIfBurbIndex,
       "swIp": swIp,
       "swIpAddrTable": swIpAddrTable,
       "swIpAddrEntry": swIpAddrEntry,
       "swIpAdEntAddr": swIpAdEntAddr,
       "swIpAdEntIfIndex": swIpAdEntIfIndex,
       "swIpAdEntNetMask": swIpAdEntNetMask,
       "swIpAdEntBcastAddr": swIpAdEntBcastAddr,
       "swIpAdEntReasmMaxSize": swIpAdEntReasmMaxSize,
       "swIpAdEntBurbIndex": swIpAdEntBurbIndex,
       "swIpRouteTable": swIpRouteTable,
       "swIpRouteEntry": swIpRouteEntry,
       "swIpRouteDest": swIpRouteDest,
       "swIpRouteIfIndex": swIpRouteIfIndex,
       "swIpRouteMetric1": swIpRouteMetric1,
       "swIpRouteMetric2": swIpRouteMetric2,
       "swIpRouteMetric3": swIpRouteMetric3,
       "swIpRouteMetric4": swIpRouteMetric4,
       "swIpRouteNextHop": swIpRouteNextHop,
       "swIpRouteType": swIpRouteType,
       "swIpRouteProto": swIpRouteProto,
       "swIpRouteAge": swIpRouteAge,
       "swIpRouteMask": swIpRouteMask,
       "swIpRouteMetric5": swIpRouteMetric5,
       "swIpRouteInfo": swIpRouteInfo,
       "swIpRouteBurbIndex": swIpRouteBurbIndex,
       "swTcp": swTcp,
       "swTcpConnTable": swTcpConnTable,
       "swTcpConnEntry": swTcpConnEntry,
       "swTcpConnState": swTcpConnState,
       "swTcpConnLocalAddress": swTcpConnLocalAddress,
       "swTcpConnLocalPort": swTcpConnLocalPort,
       "swTcpConnRemAddress": swTcpConnRemAddress,
       "swTcpConnRemPort": swTcpConnRemPort,
       "swTcpConnBurbIndex": swTcpConnBurbIndex,
       "swUdp": swUdp,
       "swUdpTable": swUdpTable,
       "swUdpEntry": swUdpEntry,
       "swUdpLocalAddress": swUdpLocalAddress,
       "swUdpLocalPort": swUdpLocalPort,
       "swUdpBurbIndex": swUdpBurbIndex,
       "swTrap": swTrap,
       "sccAuthenFailSrcIp": sccAuthenFailSrcIp,
       "sccAuthenFailSrcCommName": sccAuthenFailSrcCommName,
       "swUser": swUser,
       "swSRoleUser": swSRoleUser,
       "swSRoleName": swSRoleName}
)
