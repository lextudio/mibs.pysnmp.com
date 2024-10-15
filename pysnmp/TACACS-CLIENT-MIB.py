# SNMP MIB module (TACACS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TACACS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:51 2024
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

(fastPath,) = mibBuilder.importSymbols(
    "EdgeSwitch-REF-MIB",
    "fastPath")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

agentTacacsClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 18)
)
agentTacacsClientMIB.setRevisions(
        ("2011-12-14 00:00",
         "2011-01-26 00:00",
         "2007-05-23 00:00",
         "2005-08-17 00:44")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentTacacsClientObjects_ObjectIdentity = ObjectIdentity
agentTacacsClientObjects = _AgentTacacsClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 18, 1)
)
_AgentTacacsGlobalConfigGroup_ObjectIdentity = ObjectIdentity
agentTacacsGlobalConfigGroup = _AgentTacacsGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 18, 1, 1)
)


class _AgentTacacsGlobalTimeout_Type(Unsigned32):
    """Custom type agentTacacsGlobalTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AgentTacacsGlobalTimeout_Type.__name__ = "Unsigned32"
_AgentTacacsGlobalTimeout_Object = MibScalar
agentTacacsGlobalTimeout = _AgentTacacsGlobalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 18, 1, 1, 1),
    _AgentTacacsGlobalTimeout_Type()
)
agentTacacsGlobalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTacacsGlobalTimeout.setStatus("current")


class _AgentTacacsGlobalKey_Type(OctetString):
    """Custom type agentTacacsGlobalKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgentTacacsGlobalKey_Type.__name__ = "OctetString"
_AgentTacacsGlobalKey_Object = MibScalar
agentTacacsGlobalKey = _AgentTacacsGlobalKey_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 18, 1, 1, 2),
    _AgentTacacsGlobalKey_Type()
)
agentTacacsGlobalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTacacsGlobalKey.setStatus("current")
_AgentTacacsSourceInterface_Type = InterfaceIndexOrZero
_AgentTacacsSourceInterface_Object = MibScalar
agentTacacsSourceInterface = _AgentTacacsSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 18, 1, 1, 3),
    _AgentTacacsSourceInterface_Type()
)
agentTacacsSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTacacsSourceInterface.setStatus("current")
_AgentTacacsServerTable_Object = MibTable
agentTacacsServerTable = _AgentTacacsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 18, 1, 2)
)
if mibBuilder.loadTexts:
    agentTacacsServerTable.setStatus("current")
_AgentTacacsServerEntry_Object = MibTableRow
agentTacacsServerEntry = _AgentTacacsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 18, 1, 2, 1)
)
agentTacacsServerEntry.setIndexNames(
    (0, "TACACS-CLIENT-MIB", "agentTacacsServerIpAddress"),
)
if mibBuilder.loadTexts:
    agentTacacsServerEntry.setStatus("current")
_AgentTacacsServerIpAddress_Type = InetAddress
_AgentTacacsServerIpAddress_Object = MibTableColumn
agentTacacsServerIpAddress = _AgentTacacsServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 18, 1, 2, 1, 1),
    _AgentTacacsServerIpAddress_Type()
)
agentTacacsServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentTacacsServerIpAddress.setStatus("current")


class _AgentTacacsPortNumber_Type(Unsigned32):
    """Custom type agentTacacsPortNumber based on Unsigned32"""
    defaultValue = 49

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentTacacsPortNumber_Type.__name__ = "Unsigned32"
_AgentTacacsPortNumber_Object = MibTableColumn
agentTacacsPortNumber = _AgentTacacsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 18, 1, 2, 1, 2),
    _AgentTacacsPortNumber_Type()
)
agentTacacsPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTacacsPortNumber.setStatus("current")


class _AgentTacacsTimeOut_Type(Unsigned32):
    """Custom type agentTacacsTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AgentTacacsTimeOut_Type.__name__ = "Unsigned32"
_AgentTacacsTimeOut_Object = MibTableColumn
agentTacacsTimeOut = _AgentTacacsTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 18, 1, 2, 1, 3),
    _AgentTacacsTimeOut_Type()
)
agentTacacsTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTacacsTimeOut.setStatus("current")


class _AgentTacacsKey_Type(OctetString):
    """Custom type agentTacacsKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgentTacacsKey_Type.__name__ = "OctetString"
_AgentTacacsKey_Object = MibTableColumn
agentTacacsKey = _AgentTacacsKey_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 18, 1, 2, 1, 4),
    _AgentTacacsKey_Type()
)
agentTacacsKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTacacsKey.setStatus("current")


class _AgentTacacsPriority_Type(Unsigned32):
    """Custom type agentTacacsPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentTacacsPriority_Type.__name__ = "Unsigned32"
_AgentTacacsPriority_Object = MibTableColumn
agentTacacsPriority = _AgentTacacsPriority_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 18, 1, 2, 1, 5),
    _AgentTacacsPriority_Type()
)
agentTacacsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTacacsPriority.setStatus("current")
_AgentTacacsServerStatus_Type = RowStatus
_AgentTacacsServerStatus_Object = MibTableColumn
agentTacacsServerStatus = _AgentTacacsServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 18, 1, 2, 1, 6),
    _AgentTacacsServerStatus_Type()
)
agentTacacsServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTacacsServerStatus.setStatus("current")
_AgentTacacsServerIpAddrType_Type = InetAddressType
_AgentTacacsServerIpAddrType_Object = MibTableColumn
agentTacacsServerIpAddrType = _AgentTacacsServerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 18, 1, 2, 1, 7),
    _AgentTacacsServerIpAddrType_Type()
)
agentTacacsServerIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTacacsServerIpAddrType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TACACS-CLIENT-MIB",
    **{"agentTacacsClientMIB": agentTacacsClientMIB,
       "agentTacacsClientObjects": agentTacacsClientObjects,
       "agentTacacsGlobalConfigGroup": agentTacacsGlobalConfigGroup,
       "agentTacacsGlobalTimeout": agentTacacsGlobalTimeout,
       "agentTacacsGlobalKey": agentTacacsGlobalKey,
       "agentTacacsSourceInterface": agentTacacsSourceInterface,
       "agentTacacsServerTable": agentTacacsServerTable,
       "agentTacacsServerEntry": agentTacacsServerEntry,
       "agentTacacsServerIpAddress": agentTacacsServerIpAddress,
       "agentTacacsPortNumber": agentTacacsPortNumber,
       "agentTacacsTimeOut": agentTacacsTimeOut,
       "agentTacacsKey": agentTacacsKey,
       "agentTacacsPriority": agentTacacsPriority,
       "agentTacacsServerStatus": agentTacacsServerStatus,
       "agentTacacsServerIpAddrType": agentTacacsServerIpAddrType}
)
