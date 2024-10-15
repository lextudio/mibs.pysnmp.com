# SNMP MIB module (DHCPCLIENT-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DHCPCLIENT-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:02 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(switch,) = mibBuilder.importSymbols(
    "QUANTA-SWITCH-MIB",
    "switch")

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

dhcpClientPrivate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 100)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Agentdhcp4ClientLeaseParameters_ObjectIdentity = ObjectIdentity
agentdhcp4ClientLeaseParameters = _Agentdhcp4ClientLeaseParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 100, 1)
)
_Agentdhcp4ClientLeaseParametersTable_Object = MibTable
agentdhcp4ClientLeaseParametersTable = _Agentdhcp4ClientLeaseParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1)
)
if mibBuilder.loadTexts:
    agentdhcp4ClientLeaseParametersTable.setStatus("current")
_Agentdhcp4ClientLeaseParametersEntry_Object = MibTableRow
agentdhcp4ClientLeaseParametersEntry = _Agentdhcp4ClientLeaseParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1)
)
agentdhcp4ClientLeaseParametersEntry.setIndexNames(
    (0, "DHCPCLIENT-PRIVATE-MIB", "agentdhcp4ClientInterfaceIndex"),
)
if mibBuilder.loadTexts:
    agentdhcp4ClientLeaseParametersEntry.setStatus("current")
_Agentdhcp4ClientInterfaceIndex_Type = InterfaceIndex
_Agentdhcp4ClientInterfaceIndex_Object = MibTableColumn
agentdhcp4ClientInterfaceIndex = _Agentdhcp4ClientInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 1),
    _Agentdhcp4ClientInterfaceIndex_Type()
)
agentdhcp4ClientInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentdhcp4ClientInterfaceIndex.setStatus("current")
_Agentdhcp4ClientIpAddress_Type = IpAddress
_Agentdhcp4ClientIpAddress_Object = MibTableColumn
agentdhcp4ClientIpAddress = _Agentdhcp4ClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 2),
    _Agentdhcp4ClientIpAddress_Type()
)
agentdhcp4ClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentdhcp4ClientIpAddress.setStatus("current")
_Agentdhcp4ClientSubnetMask_Type = IpAddress
_Agentdhcp4ClientSubnetMask_Object = MibTableColumn
agentdhcp4ClientSubnetMask = _Agentdhcp4ClientSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 3),
    _Agentdhcp4ClientSubnetMask_Type()
)
agentdhcp4ClientSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentdhcp4ClientSubnetMask.setStatus("current")
_Agentdhcp4ClientDhcpServerAddress_Type = IpAddress
_Agentdhcp4ClientDhcpServerAddress_Object = MibTableColumn
agentdhcp4ClientDhcpServerAddress = _Agentdhcp4ClientDhcpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 4),
    _Agentdhcp4ClientDhcpServerAddress_Type()
)
agentdhcp4ClientDhcpServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentdhcp4ClientDhcpServerAddress.setStatus("current")


class _Agentdhcp4ClientState_Type(Integer32):
    """Custom type agentdhcp4ClientState based on Integer32"""
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
        *(("bootp-fallback", 10),
          ("bound", 5),
          ("do-release", 13),
          ("failed", 12),
          ("init", 1),
          ("not-bound", 11),
          ("rebind-recv", 9),
          ("rebinding", 8),
          ("renew-recv", 7),
          ("renewing", 6),
          ("request-recv", 4),
          ("requesting", 3),
          ("selecting", 2))
    )


_Agentdhcp4ClientState_Type.__name__ = "Integer32"
_Agentdhcp4ClientState_Object = MibTableColumn
agentdhcp4ClientState = _Agentdhcp4ClientState_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 5),
    _Agentdhcp4ClientState_Type()
)
agentdhcp4ClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentdhcp4ClientState.setStatus("current")
_Agentdhcp4ClientTransactionID_Type = DisplayString
_Agentdhcp4ClientTransactionID_Object = MibTableColumn
agentdhcp4ClientTransactionID = _Agentdhcp4ClientTransactionID_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 6),
    _Agentdhcp4ClientTransactionID_Type()
)
agentdhcp4ClientTransactionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentdhcp4ClientTransactionID.setStatus("current")
_Agentdhcp4ClientLeaseTime_Type = TimeTicks
_Agentdhcp4ClientLeaseTime_Object = MibTableColumn
agentdhcp4ClientLeaseTime = _Agentdhcp4ClientLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 7),
    _Agentdhcp4ClientLeaseTime_Type()
)
agentdhcp4ClientLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentdhcp4ClientLeaseTime.setStatus("current")
_Agentdhcp4ClientRenewTime_Type = TimeTicks
_Agentdhcp4ClientRenewTime_Object = MibTableColumn
agentdhcp4ClientRenewTime = _Agentdhcp4ClientRenewTime_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 8),
    _Agentdhcp4ClientRenewTime_Type()
)
agentdhcp4ClientRenewTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentdhcp4ClientRenewTime.setStatus("current")
_Agentdhcp4ClientRebindTime_Type = TimeTicks
_Agentdhcp4ClientRebindTime_Object = MibTableColumn
agentdhcp4ClientRebindTime = _Agentdhcp4ClientRebindTime_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 9),
    _Agentdhcp4ClientRebindTime_Type()
)
agentdhcp4ClientRebindTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentdhcp4ClientRebindTime.setStatus("current")
_Agentdhcp4ClientRetryCount_Type = Counter32
_Agentdhcp4ClientRetryCount_Object = MibTableColumn
agentdhcp4ClientRetryCount = _Agentdhcp4ClientRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 100, 1, 1, 1, 10),
    _Agentdhcp4ClientRetryCount_Type()
)
agentdhcp4ClientRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentdhcp4ClientRetryCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DHCPCLIENT-PRIVATE-MIB",
    **{"dhcpClientPrivate": dhcpClientPrivate,
       "agentdhcp4ClientLeaseParameters": agentdhcp4ClientLeaseParameters,
       "agentdhcp4ClientLeaseParametersTable": agentdhcp4ClientLeaseParametersTable,
       "agentdhcp4ClientLeaseParametersEntry": agentdhcp4ClientLeaseParametersEntry,
       "agentdhcp4ClientInterfaceIndex": agentdhcp4ClientInterfaceIndex,
       "agentdhcp4ClientIpAddress": agentdhcp4ClientIpAddress,
       "agentdhcp4ClientSubnetMask": agentdhcp4ClientSubnetMask,
       "agentdhcp4ClientDhcpServerAddress": agentdhcp4ClientDhcpServerAddress,
       "agentdhcp4ClientState": agentdhcp4ClientState,
       "agentdhcp4ClientTransactionID": agentdhcp4ClientTransactionID,
       "agentdhcp4ClientLeaseTime": agentdhcp4ClientLeaseTime,
       "agentdhcp4ClientRenewTime": agentdhcp4ClientRenewTime,
       "agentdhcp4ClientRebindTime": agentdhcp4ClientRebindTime,
       "agentdhcp4ClientRetryCount": agentdhcp4ClientRetryCount}
)
