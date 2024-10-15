# SNMP MIB module (WWP-LEOS-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-LDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:55 2024
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

(IndexInteger,) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IndexInteger")

(MplsLdpIdentifier,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLdpIdentifier")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosLdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32)
)
wwpLeosLdpMIB.setRevisions(
        ("2001-04-03 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosLdpMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosLdpMIBObjects = _WwpLeosLdpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1)
)
_WwpLeosLdpObjects_ObjectIdentity = ObjectIdentity
wwpLeosLdpObjects = _WwpLeosLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 1)
)


class _WwpLeosLdpAdminStatus_Type(Integer32):
    """Custom type wwpLeosLdpAdminStatus based on Integer32"""
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


_WwpLeosLdpAdminStatus_Type.__name__ = "Integer32"
_WwpLeosLdpAdminStatus_Object = MibScalar
wwpLeosLdpAdminStatus = _WwpLeosLdpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 1, 1),
    _WwpLeosLdpAdminStatus_Type()
)
wwpLeosLdpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosLdpAdminStatus.setStatus("current")


class _WwpLeosLdpOperStatus_Type(Integer32):
    """Custom type wwpLeosLdpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_WwpLeosLdpOperStatus_Type.__name__ = "Integer32"
_WwpLeosLdpOperStatus_Object = MibScalar
wwpLeosLdpOperStatus = _WwpLeosLdpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 1, 2),
    _WwpLeosLdpOperStatus_Type()
)
wwpLeosLdpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLdpOperStatus.setStatus("current")


class _WwpLeosLdpHelloHoldTime_Type(Unsigned32):
    """Custom type wwpLeosLdpHelloHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosLdpHelloHoldTime_Type.__name__ = "Unsigned32"
_WwpLeosLdpHelloHoldTime_Object = MibScalar
wwpLeosLdpHelloHoldTime = _WwpLeosLdpHelloHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 1, 3),
    _WwpLeosLdpHelloHoldTime_Type()
)
wwpLeosLdpHelloHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosLdpHelloHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosLdpHelloHoldTime.setUnits("seconds")


class _WwpLeosLdpKeepAliveHoldTime_Type(Unsigned32):
    """Custom type wwpLeosLdpKeepAliveHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosLdpKeepAliveHoldTime_Type.__name__ = "Unsigned32"
_WwpLeosLdpKeepAliveHoldTime_Object = MibScalar
wwpLeosLdpKeepAliveHoldTime = _WwpLeosLdpKeepAliveHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 1, 4),
    _WwpLeosLdpKeepAliveHoldTime_Type()
)
wwpLeosLdpKeepAliveHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosLdpKeepAliveHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosLdpKeepAliveHoldTime.setUnits("seconds")
_WwpLeosLdp_ObjectIdentity = ObjectIdentity
wwpLeosLdp = _WwpLeosLdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2)
)
_WwpLeosLdpSessionTable_Object = MibTable
wwpLeosLdpSessionTable = _WwpLeosLdpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpLeosLdpSessionTable.setStatus("current")
_WwpLeosLdpSessionEntry_Object = MibTableRow
wwpLeosLdpSessionEntry = _WwpLeosLdpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 1, 1)
)
wwpLeosLdpSessionEntry.setIndexNames(
    (0, "WWP-LEOS-LDP-MIB", "wwpLeosLdpEntityLdpId"),
    (0, "WWP-LEOS-LDP-MIB", "wwpLeosLdpEntityIndex"),
    (0, "WWP-LEOS-LDP-MIB", "wwpLeosLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    wwpLeosLdpSessionEntry.setStatus("current")
_WwpLeosLdpEntityLdpId_Type = MplsLdpIdentifier
_WwpLeosLdpEntityLdpId_Object = MibTableColumn
wwpLeosLdpEntityLdpId = _WwpLeosLdpEntityLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 1, 1, 1),
    _WwpLeosLdpEntityLdpId_Type()
)
wwpLeosLdpEntityLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLdpEntityLdpId.setStatus("current")
_WwpLeosLdpEntityIndex_Type = IndexInteger
_WwpLeosLdpEntityIndex_Object = MibTableColumn
wwpLeosLdpEntityIndex = _WwpLeosLdpEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 1, 1, 2),
    _WwpLeosLdpEntityIndex_Type()
)
wwpLeosLdpEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLdpEntityIndex.setStatus("current")
_WwpLeosLdpPeerLdpId_Type = MplsLdpIdentifier
_WwpLeosLdpPeerLdpId_Object = MibTableColumn
wwpLeosLdpPeerLdpId = _WwpLeosLdpPeerLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 1, 1, 3),
    _WwpLeosLdpPeerLdpId_Type()
)
wwpLeosLdpPeerLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLdpPeerLdpId.setStatus("current")
_WwpLeosLdpSessionConfiguredHoldTime_Type = Unsigned32
_WwpLeosLdpSessionConfiguredHoldTime_Object = MibTableColumn
wwpLeosLdpSessionConfiguredHoldTime = _WwpLeosLdpSessionConfiguredHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 1, 1, 4),
    _WwpLeosLdpSessionConfiguredHoldTime_Type()
)
wwpLeosLdpSessionConfiguredHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLdpSessionConfiguredHoldTime.setStatus("current")
_WwpLeosLdpSessionPeerHoldTime_Type = Unsigned32
_WwpLeosLdpSessionPeerHoldTime_Object = MibTableColumn
wwpLeosLdpSessionPeerHoldTime = _WwpLeosLdpSessionPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 1, 1, 5),
    _WwpLeosLdpSessionPeerHoldTime_Type()
)
wwpLeosLdpSessionPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLdpSessionPeerHoldTime.setStatus("current")
_WwpLeosLdpSessionHoldTimeInUse_Type = Unsigned32
_WwpLeosLdpSessionHoldTimeInUse_Object = MibTableColumn
wwpLeosLdpSessionHoldTimeInUse = _WwpLeosLdpSessionHoldTimeInUse_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 1, 1, 6),
    _WwpLeosLdpSessionHoldTimeInUse_Type()
)
wwpLeosLdpSessionHoldTimeInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLdpSessionHoldTimeInUse.setStatus("current")
_WwpLeosLdpHelloAdjacencyTable_Object = MibTable
wwpLeosLdpHelloAdjacencyTable = _WwpLeosLdpHelloAdjacencyTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wwpLeosLdpHelloAdjacencyTable.setStatus("current")
_WwpLeosLdpHelloAdjacencyEntry_Object = MibTableRow
wwpLeosLdpHelloAdjacencyEntry = _WwpLeosLdpHelloAdjacencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 2, 1)
)
wwpLeosLdpHelloAdjacencyEntry.setIndexNames(
    (0, "WWP-LEOS-LDP-MIB", "wwpLeosLdpEntityLdpId"),
    (0, "WWP-LEOS-LDP-MIB", "wwpLeosLdpEntityIndex"),
    (0, "WWP-LEOS-LDP-MIB", "wwpLeosLdpPeerLdpId"),
    (0, "WWP-LEOS-LDP-MIB", "wwpLeosLdpHelloAdjacencyIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosLdpHelloAdjacencyEntry.setStatus("current")


class _WwpLeosLdpHelloAdjacencyIndex_Type(Unsigned32):
    """Custom type wwpLeosLdpHelloAdjacencyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WwpLeosLdpHelloAdjacencyIndex_Type.__name__ = "Unsigned32"
_WwpLeosLdpHelloAdjacencyIndex_Object = MibTableColumn
wwpLeosLdpHelloAdjacencyIndex = _WwpLeosLdpHelloAdjacencyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 2, 1, 1),
    _WwpLeosLdpHelloAdjacencyIndex_Type()
)
wwpLeosLdpHelloAdjacencyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLdpHelloAdjacencyIndex.setStatus("current")
_WwpLeosLdpHelloAdjacencyConfiguredHoldTime_Type = Unsigned32
_WwpLeosLdpHelloAdjacencyConfiguredHoldTime_Object = MibTableColumn
wwpLeosLdpHelloAdjacencyConfiguredHoldTime = _WwpLeosLdpHelloAdjacencyConfiguredHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 2, 1, 2),
    _WwpLeosLdpHelloAdjacencyConfiguredHoldTime_Type()
)
wwpLeosLdpHelloAdjacencyConfiguredHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLdpHelloAdjacencyConfiguredHoldTime.setStatus("current")
_WwpLeosLdpHelloAdjacencyPeerHoldTime_Type = Unsigned32
_WwpLeosLdpHelloAdjacencyPeerHoldTime_Object = MibTableColumn
wwpLeosLdpHelloAdjacencyPeerHoldTime = _WwpLeosLdpHelloAdjacencyPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 2, 1, 3),
    _WwpLeosLdpHelloAdjacencyPeerHoldTime_Type()
)
wwpLeosLdpHelloAdjacencyPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLdpHelloAdjacencyPeerHoldTime.setStatus("current")
_WwpLeosLdpIfTable_Object = MibTable
wwpLeosLdpIfTable = _WwpLeosLdpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wwpLeosLdpIfTable.setStatus("current")
_WwpLeosLdpIfEntry_Object = MibTableRow
wwpLeosLdpIfEntry = _WwpLeosLdpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 3, 1)
)
wwpLeosLdpIfEntry.setIndexNames(
    (0, "WWP-LEOS-LDP-MIB", "wwpLeosLdpIfIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosLdpIfEntry.setStatus("current")


class _WwpLeosLdpIfName_Type(DisplayString):
    """Custom type wwpLeosLdpIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WwpLeosLdpIfName_Type.__name__ = "DisplayString"
_WwpLeosLdpIfName_Object = MibTableColumn
wwpLeosLdpIfName = _WwpLeosLdpIfName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 3, 1, 1),
    _WwpLeosLdpIfName_Type()
)
wwpLeosLdpIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLdpIfName.setStatus("current")


class _WwpLeosLdpIfIndex_Type(Integer32):
    """Custom type wwpLeosLdpIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_WwpLeosLdpIfIndex_Type.__name__ = "Integer32"
_WwpLeosLdpIfIndex_Object = MibTableColumn
wwpLeosLdpIfIndex = _WwpLeosLdpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 3, 1, 2),
    _WwpLeosLdpIfIndex_Type()
)
wwpLeosLdpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLdpIfIndex.setStatus("current")
_WwpLeosLdpIfIpAddr_Type = IpAddress
_WwpLeosLdpIfIpAddr_Object = MibTableColumn
wwpLeosLdpIfIpAddr = _WwpLeosLdpIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 3, 1, 3),
    _WwpLeosLdpIfIpAddr_Type()
)
wwpLeosLdpIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLdpIfIpAddr.setStatus("current")


class _WwpLeosLdpIfAdminStatus_Type(Integer32):
    """Custom type wwpLeosLdpIfAdminStatus based on Integer32"""
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


_WwpLeosLdpIfAdminStatus_Type.__name__ = "Integer32"
_WwpLeosLdpIfAdminStatus_Object = MibTableColumn
wwpLeosLdpIfAdminStatus = _WwpLeosLdpIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 3, 1, 4),
    _WwpLeosLdpIfAdminStatus_Type()
)
wwpLeosLdpIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosLdpIfAdminStatus.setStatus("current")


class _WwpLeosLdpIfOperStatus_Type(Integer32):
    """Custom type wwpLeosLdpIfOperStatus based on Integer32"""
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


_WwpLeosLdpIfOperStatus_Type.__name__ = "Integer32"
_WwpLeosLdpIfOperStatus_Object = MibTableColumn
wwpLeosLdpIfOperStatus = _WwpLeosLdpIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 32, 1, 2, 3, 1, 5),
    _WwpLeosLdpIfOperStatus_Type()
)
wwpLeosLdpIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLdpIfOperStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-LDP-MIB",
    **{"wwpLeosLdpMIB": wwpLeosLdpMIB,
       "wwpLeosLdpMIBObjects": wwpLeosLdpMIBObjects,
       "wwpLeosLdpObjects": wwpLeosLdpObjects,
       "wwpLeosLdpAdminStatus": wwpLeosLdpAdminStatus,
       "wwpLeosLdpOperStatus": wwpLeosLdpOperStatus,
       "wwpLeosLdpHelloHoldTime": wwpLeosLdpHelloHoldTime,
       "wwpLeosLdpKeepAliveHoldTime": wwpLeosLdpKeepAliveHoldTime,
       "wwpLeosLdp": wwpLeosLdp,
       "wwpLeosLdpSessionTable": wwpLeosLdpSessionTable,
       "wwpLeosLdpSessionEntry": wwpLeosLdpSessionEntry,
       "wwpLeosLdpEntityLdpId": wwpLeosLdpEntityLdpId,
       "wwpLeosLdpEntityIndex": wwpLeosLdpEntityIndex,
       "wwpLeosLdpPeerLdpId": wwpLeosLdpPeerLdpId,
       "wwpLeosLdpSessionConfiguredHoldTime": wwpLeosLdpSessionConfiguredHoldTime,
       "wwpLeosLdpSessionPeerHoldTime": wwpLeosLdpSessionPeerHoldTime,
       "wwpLeosLdpSessionHoldTimeInUse": wwpLeosLdpSessionHoldTimeInUse,
       "wwpLeosLdpHelloAdjacencyTable": wwpLeosLdpHelloAdjacencyTable,
       "wwpLeosLdpHelloAdjacencyEntry": wwpLeosLdpHelloAdjacencyEntry,
       "wwpLeosLdpHelloAdjacencyIndex": wwpLeosLdpHelloAdjacencyIndex,
       "wwpLeosLdpHelloAdjacencyConfiguredHoldTime": wwpLeosLdpHelloAdjacencyConfiguredHoldTime,
       "wwpLeosLdpHelloAdjacencyPeerHoldTime": wwpLeosLdpHelloAdjacencyPeerHoldTime,
       "wwpLeosLdpIfTable": wwpLeosLdpIfTable,
       "wwpLeosLdpIfEntry": wwpLeosLdpIfEntry,
       "wwpLeosLdpIfName": wwpLeosLdpIfName,
       "wwpLeosLdpIfIndex": wwpLeosLdpIfIndex,
       "wwpLeosLdpIfIpAddr": wwpLeosLdpIfIpAddr,
       "wwpLeosLdpIfAdminStatus": wwpLeosLdpIfAdminStatus,
       "wwpLeosLdpIfOperStatus": wwpLeosLdpIfOperStatus}
)
