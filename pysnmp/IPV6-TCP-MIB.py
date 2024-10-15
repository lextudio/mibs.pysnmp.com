# SNMP MIB module (IPV6-TCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPV6-TCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:29 2024
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

(Ipv6Address,
 Ipv6IfIndexOrZero) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6IfIndexOrZero")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 experimental,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "experimental",
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ipv6TcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 86)
)
ipv6TcpMIB.setRevisions(
        ("2017-02-22 00:00",
         "1998-01-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tcp_ObjectIdentity = ObjectIdentity
tcp = _Tcp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 6)
)
_Ipv6TcpConnTable_Object = MibTable
ipv6TcpConnTable = _Ipv6TcpConnTable_Object(
    (1, 3, 6, 1, 2, 1, 6, 16)
)
if mibBuilder.loadTexts:
    ipv6TcpConnTable.setStatus("obsolete")
_Ipv6TcpConnEntry_Object = MibTableRow
ipv6TcpConnEntry = _Ipv6TcpConnEntry_Object(
    (1, 3, 6, 1, 2, 1, 6, 16, 1)
)
ipv6TcpConnEntry.setIndexNames(
    (0, "IPV6-TCP-MIB", "ipv6TcpConnLocalAddress"),
    (0, "IPV6-TCP-MIB", "ipv6TcpConnLocalPort"),
    (0, "IPV6-TCP-MIB", "ipv6TcpConnRemAddress"),
    (0, "IPV6-TCP-MIB", "ipv6TcpConnRemPort"),
    (0, "IPV6-TCP-MIB", "ipv6TcpConnIfIndex"),
)
if mibBuilder.loadTexts:
    ipv6TcpConnEntry.setStatus("obsolete")
_Ipv6TcpConnLocalAddress_Type = Ipv6Address
_Ipv6TcpConnLocalAddress_Object = MibTableColumn
ipv6TcpConnLocalAddress = _Ipv6TcpConnLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 6, 16, 1, 1),
    _Ipv6TcpConnLocalAddress_Type()
)
ipv6TcpConnLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6TcpConnLocalAddress.setStatus("obsolete")


class _Ipv6TcpConnLocalPort_Type(Integer32):
    """Custom type ipv6TcpConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ipv6TcpConnLocalPort_Type.__name__ = "Integer32"
_Ipv6TcpConnLocalPort_Object = MibTableColumn
ipv6TcpConnLocalPort = _Ipv6TcpConnLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 6, 16, 1, 2),
    _Ipv6TcpConnLocalPort_Type()
)
ipv6TcpConnLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6TcpConnLocalPort.setStatus("obsolete")
_Ipv6TcpConnRemAddress_Type = Ipv6Address
_Ipv6TcpConnRemAddress_Object = MibTableColumn
ipv6TcpConnRemAddress = _Ipv6TcpConnRemAddress_Object(
    (1, 3, 6, 1, 2, 1, 6, 16, 1, 3),
    _Ipv6TcpConnRemAddress_Type()
)
ipv6TcpConnRemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6TcpConnRemAddress.setStatus("obsolete")


class _Ipv6TcpConnRemPort_Type(Integer32):
    """Custom type ipv6TcpConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ipv6TcpConnRemPort_Type.__name__ = "Integer32"
_Ipv6TcpConnRemPort_Object = MibTableColumn
ipv6TcpConnRemPort = _Ipv6TcpConnRemPort_Object(
    (1, 3, 6, 1, 2, 1, 6, 16, 1, 4),
    _Ipv6TcpConnRemPort_Type()
)
ipv6TcpConnRemPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6TcpConnRemPort.setStatus("obsolete")
_Ipv6TcpConnIfIndex_Type = Ipv6IfIndexOrZero
_Ipv6TcpConnIfIndex_Object = MibTableColumn
ipv6TcpConnIfIndex = _Ipv6TcpConnIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 6, 16, 1, 5),
    _Ipv6TcpConnIfIndex_Type()
)
ipv6TcpConnIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6TcpConnIfIndex.setStatus("obsolete")


class _Ipv6TcpConnState_Type(Integer32):
    """Custom type ipv6TcpConnState based on Integer32"""
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


_Ipv6TcpConnState_Type.__name__ = "Integer32"
_Ipv6TcpConnState_Object = MibTableColumn
ipv6TcpConnState = _Ipv6TcpConnState_Object(
    (1, 3, 6, 1, 2, 1, 6, 16, 1, 6),
    _Ipv6TcpConnState_Type()
)
ipv6TcpConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6TcpConnState.setStatus("obsolete")
_Ipv6TcpConformance_ObjectIdentity = ObjectIdentity
ipv6TcpConformance = _Ipv6TcpConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 86, 2)
)
_Ipv6TcpCompliances_ObjectIdentity = ObjectIdentity
ipv6TcpCompliances = _Ipv6TcpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 86, 2, 1)
)
_Ipv6TcpGroups_ObjectIdentity = ObjectIdentity
ipv6TcpGroups = _Ipv6TcpGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 86, 2, 2)
)

# Managed Objects groups

ipv6TcpGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 86, 2, 2, 1)
)
ipv6TcpGroup.setObjects(
    ("IPV6-TCP-MIB", "ipv6TcpConnState")
)
if mibBuilder.loadTexts:
    ipv6TcpGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipv6TcpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 86, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipv6TcpCompliance.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPV6-TCP-MIB",
    **{"tcp": tcp,
       "ipv6TcpConnTable": ipv6TcpConnTable,
       "ipv6TcpConnEntry": ipv6TcpConnEntry,
       "ipv6TcpConnLocalAddress": ipv6TcpConnLocalAddress,
       "ipv6TcpConnLocalPort": ipv6TcpConnLocalPort,
       "ipv6TcpConnRemAddress": ipv6TcpConnRemAddress,
       "ipv6TcpConnRemPort": ipv6TcpConnRemPort,
       "ipv6TcpConnIfIndex": ipv6TcpConnIfIndex,
       "ipv6TcpConnState": ipv6TcpConnState,
       "ipv6TcpMIB": ipv6TcpMIB,
       "ipv6TcpConformance": ipv6TcpConformance,
       "ipv6TcpCompliances": ipv6TcpCompliances,
       "ipv6TcpCompliance": ipv6TcpCompliance,
       "ipv6TcpGroups": ipv6TcpGroups,
       "ipv6TcpGroup": ipv6TcpGroup}
)
