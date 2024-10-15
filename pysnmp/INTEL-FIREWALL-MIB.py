# SNMP MIB module (INTEL-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-FIREWALL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:41 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Firewall_ObjectIdentity = ObjectIdentity
firewall = _Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 54)
)
_FirewallInfo_ObjectIdentity = ObjectIdentity
firewallInfo = _FirewallInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 54, 1)
)
_FirewallSessionTable_Object = MibTable
firewallSessionTable = _FirewallSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 54, 1, 1)
)
if mibBuilder.loadTexts:
    firewallSessionTable.setStatus("mandatory")
_FirewallSessionEntry_Object = MibTableRow
firewallSessionEntry = _FirewallSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 54, 1, 1, 1)
)
firewallSessionEntry.setIndexNames(
    (0, "INTEL-FIREWALL-MIB", "firewallSessionIpIfIndex"),
    (0, "INTEL-FIREWALL-MIB", "firewallSessionDirection"),
    (0, "INTEL-FIREWALL-MIB", "firewallSessionNumber"),
)
if mibBuilder.loadTexts:
    firewallSessionEntry.setStatus("mandatory")
_FirewallSessionIpIfIndex_Type = Integer32
_FirewallSessionIpIfIndex_Object = MibTableColumn
firewallSessionIpIfIndex = _FirewallSessionIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 54, 1, 1, 1, 1),
    _FirewallSessionIpIfIndex_Type()
)
firewallSessionIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSessionIpIfIndex.setStatus("mandatory")


class _FirewallSessionDirection_Type(Integer32):
    """Custom type firewallSessionDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_FirewallSessionDirection_Type.__name__ = "Integer32"
_FirewallSessionDirection_Object = MibTableColumn
firewallSessionDirection = _FirewallSessionDirection_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 54, 1, 1, 1, 2),
    _FirewallSessionDirection_Type()
)
firewallSessionDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSessionDirection.setStatus("mandatory")
_FirewallSessionNumber_Type = Integer32
_FirewallSessionNumber_Object = MibTableColumn
firewallSessionNumber = _FirewallSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 54, 1, 1, 1, 3),
    _FirewallSessionNumber_Type()
)
firewallSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSessionNumber.setStatus("mandatory")
_FirewallSessionSourceAddr_Type = IpAddress
_FirewallSessionSourceAddr_Object = MibTableColumn
firewallSessionSourceAddr = _FirewallSessionSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 54, 1, 1, 1, 4),
    _FirewallSessionSourceAddr_Type()
)
firewallSessionSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSessionSourceAddr.setStatus("mandatory")
_FirewallSessionSourcePortOrSeq_Type = Counter32
_FirewallSessionSourcePortOrSeq_Object = MibTableColumn
firewallSessionSourcePortOrSeq = _FirewallSessionSourcePortOrSeq_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 54, 1, 1, 1, 5),
    _FirewallSessionSourcePortOrSeq_Type()
)
firewallSessionSourcePortOrSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSessionSourcePortOrSeq.setStatus("mandatory")
_FirewallSessionDestAddr_Type = IpAddress
_FirewallSessionDestAddr_Object = MibTableColumn
firewallSessionDestAddr = _FirewallSessionDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 54, 1, 1, 1, 6),
    _FirewallSessionDestAddr_Type()
)
firewallSessionDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSessionDestAddr.setStatus("mandatory")
_FirewallSessionDestPortOrSeq_Type = Counter32
_FirewallSessionDestPortOrSeq_Object = MibTableColumn
firewallSessionDestPortOrSeq = _FirewallSessionDestPortOrSeq_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 54, 1, 1, 1, 7),
    _FirewallSessionDestPortOrSeq_Type()
)
firewallSessionDestPortOrSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSessionDestPortOrSeq.setStatus("mandatory")


class _FirewallSessionProtocol_Type(Integer32):
    """Custom type firewallSessionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("tcp", 6),
          ("udp", 17))
    )


_FirewallSessionProtocol_Type.__name__ = "Integer32"
_FirewallSessionProtocol_Object = MibTableColumn
firewallSessionProtocol = _FirewallSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 54, 1, 1, 1, 8),
    _FirewallSessionProtocol_Type()
)
firewallSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSessionProtocol.setStatus("mandatory")


class _FirewallSessionState_Type(Integer32):
    """Custom type firewallSessionState based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("cantbeadded", 8),
          ("closewait", 6),
          ("denied", 11),
          ("established", 1),
          ("finwaitone", 4),
          ("finwaittwo", 5),
          ("portterminated", 16),
          ("reused", 9),
          ("sendsyninsidewaitforacksyn", 3),
          ("synreceived", 2),
          ("terminated", 7),
          ("timedout", 10))
    )


_FirewallSessionState_Type.__name__ = "Integer32"
_FirewallSessionState_Object = MibTableColumn
firewallSessionState = _FirewallSessionState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 54, 1, 1, 1, 9),
    _FirewallSessionState_Type()
)
firewallSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSessionState.setStatus("mandatory")
_FirewallSessionLastUpdate_Type = Integer32
_FirewallSessionLastUpdate_Object = MibTableColumn
firewallSessionLastUpdate = _FirewallSessionLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 54, 1, 1, 1, 10),
    _FirewallSessionLastUpdate_Type()
)
firewallSessionLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSessionLastUpdate.setStatus("mandatory")


class _FirewallSessionPacked1_Type(OctetString):
    """Custom type firewallSessionPacked1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )


_FirewallSessionPacked1_Type.__name__ = "OctetString"
_FirewallSessionPacked1_Object = MibTableColumn
firewallSessionPacked1 = _FirewallSessionPacked1_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 54, 1, 1, 1, 11),
    _FirewallSessionPacked1_Type()
)
firewallSessionPacked1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSessionPacked1.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-FIREWALL-MIB",
    **{"firewall": firewall,
       "firewallInfo": firewallInfo,
       "firewallSessionTable": firewallSessionTable,
       "firewallSessionEntry": firewallSessionEntry,
       "firewallSessionIpIfIndex": firewallSessionIpIfIndex,
       "firewallSessionDirection": firewallSessionDirection,
       "firewallSessionNumber": firewallSessionNumber,
       "firewallSessionSourceAddr": firewallSessionSourceAddr,
       "firewallSessionSourcePortOrSeq": firewallSessionSourcePortOrSeq,
       "firewallSessionDestAddr": firewallSessionDestAddr,
       "firewallSessionDestPortOrSeq": firewallSessionDestPortOrSeq,
       "firewallSessionProtocol": firewallSessionProtocol,
       "firewallSessionState": firewallSessionState,
       "firewallSessionLastUpdate": firewallSessionLastUpdate,
       "firewallSessionPacked1": firewallSessionPacked1}
)
