# SNMP MIB module (HP-ICF-OOBM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-OOBM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:53 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(snmpTargetAddrEntry,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "snmpTargetAddrEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfOobmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58)
)
hpicfOobmMIB.setRevisions(
        ("2010-03-26 00:00",
         "2009-02-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpicfOobmServerIndex(Integer32, TextualConvention):
    status = "current"
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
        *(("http", 4),
          ("snmp", 5),
          ("ssh", 2),
          ("telnet", 1),
          ("tftp", 3))
    )



class HpicfOobmServerState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("data", 2),
          ("oobm", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfOobmNotifications_ObjectIdentity = ObjectIdentity
hpicfOobmNotifications = _HpicfOobmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 0)
)
_HpicfOobmObjects_ObjectIdentity = ObjectIdentity
hpicfOobmObjects = _HpicfOobmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1)
)
_HpicfOobmScalars_ObjectIdentity = ObjectIdentity
hpicfOobmScalars = _HpicfOobmScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 1)
)


class _HpicfOobmStatus_Type(Integer32):
    """Custom type hpicfOobmStatus based on Integer32"""
    defaultValue = 1

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


_HpicfOobmStatus_Type.__name__ = "Integer32"
_HpicfOobmStatus_Object = MibScalar
hpicfOobmStatus = _HpicfOobmStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 1, 1),
    _HpicfOobmStatus_Type()
)
hpicfOobmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOobmStatus.setStatus("current")
_HpicfOobmServers_ObjectIdentity = ObjectIdentity
hpicfOobmServers = _HpicfOobmServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 2)
)
_HpicfOobmServerTable_Object = MibTable
hpicfOobmServerTable = _HpicfOobmServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfOobmServerTable.setStatus("current")
_HpicfOobmServerEntry_Object = MibTableRow
hpicfOobmServerEntry = _HpicfOobmServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 2, 1, 1)
)
hpicfOobmServerEntry.setIndexNames(
    (0, "HP-ICF-OOBM-MIB", "hpicfOobmServerType"),
)
if mibBuilder.loadTexts:
    hpicfOobmServerEntry.setStatus("current")
_HpicfOobmServerType_Type = HpicfOobmServerIndex
_HpicfOobmServerType_Object = MibTableColumn
hpicfOobmServerType = _HpicfOobmServerType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 2, 1, 1, 1),
    _HpicfOobmServerType_Type()
)
hpicfOobmServerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOobmServerType.setStatus("current")
_HpicfOobmServerListenMode_Type = HpicfOobmServerState
_HpicfOobmServerListenMode_Object = MibTableColumn
hpicfOobmServerListenMode = _HpicfOobmServerListenMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 2, 1, 1, 2),
    _HpicfOobmServerListenMode_Type()
)
hpicfOobmServerListenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOobmServerListenMode.setStatus("current")
_HpicfOobmSnmpTargetAddrIsOobm_ObjectIdentity = ObjectIdentity
hpicfOobmSnmpTargetAddrIsOobm = _HpicfOobmSnmpTargetAddrIsOobm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 3)
)
_HpicfSnmpTargetAddrIsOobmTable_Object = MibTable
hpicfSnmpTargetAddrIsOobmTable = _HpicfSnmpTargetAddrIsOobmTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfSnmpTargetAddrIsOobmTable.setStatus("current")
_HpicfSnmpTargetAddrIsOobmEntry_Object = MibTableRow
hpicfSnmpTargetAddrIsOobmEntry = _HpicfSnmpTargetAddrIsOobmEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfSnmpTargetAddrIsOobmEntry.setStatus("current")


class _HpicfSnmpTargetAddrIsOobm_Type(TruthValue):
    """Custom type hpicfSnmpTargetAddrIsOobm based on TruthValue"""


_HpicfSnmpTargetAddrIsOobm_Object = MibTableColumn
hpicfSnmpTargetAddrIsOobm = _HpicfSnmpTargetAddrIsOobm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 3, 1, 1, 1),
    _HpicfSnmpTargetAddrIsOobm_Type()
)
hpicfSnmpTargetAddrIsOobm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSnmpTargetAddrIsOobm.setStatus("current")
_HpicfOobmDefGateway_ObjectIdentity = ObjectIdentity
hpicfOobmDefGateway = _HpicfOobmDefGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 4)
)
_HpicfOobmDefGatewayTable_Object = MibTable
hpicfOobmDefGatewayTable = _HpicfOobmDefGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpicfOobmDefGatewayTable.setStatus("current")
_HpicfOobmDefGatewayEntry_Object = MibTableRow
hpicfOobmDefGatewayEntry = _HpicfOobmDefGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 4, 1, 1)
)
hpicfOobmDefGatewayEntry.setIndexNames(
    (0, "HP-ICF-OOBM-MIB", "hpicfOobmDefGatewayType"),
)
if mibBuilder.loadTexts:
    hpicfOobmDefGatewayEntry.setStatus("current")
_HpicfOobmDefGatewayType_Type = InetAddressType
_HpicfOobmDefGatewayType_Object = MibTableColumn
hpicfOobmDefGatewayType = _HpicfOobmDefGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 4, 1, 1, 1),
    _HpicfOobmDefGatewayType_Type()
)
hpicfOobmDefGatewayType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOobmDefGatewayType.setStatus("current")
_HpicfOobmDefGatewayAddr_Type = InetAddress
_HpicfOobmDefGatewayAddr_Object = MibTableColumn
hpicfOobmDefGatewayAddr = _HpicfOobmDefGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 4, 1, 1, 2),
    _HpicfOobmDefGatewayAddr_Type()
)
hpicfOobmDefGatewayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOobmDefGatewayAddr.setStatus("current")
_HpicfOobmStackMembers_ObjectIdentity = ObjectIdentity
hpicfOobmStackMembers = _HpicfOobmStackMembers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 5)
)
_HpicfOobmMemberDefGatewayTable_Object = MibTable
hpicfOobmMemberDefGatewayTable = _HpicfOobmMemberDefGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 5, 3)
)
if mibBuilder.loadTexts:
    hpicfOobmMemberDefGatewayTable.setStatus("current")
_HpicfOobmMemberDefGatewayEntry_Object = MibTableRow
hpicfOobmMemberDefGatewayEntry = _HpicfOobmMemberDefGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 5, 3, 1)
)
hpicfOobmMemberDefGatewayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HP-ICF-OOBM-MIB", "hpicfOobmMemberDefGatewayType"),
)
if mibBuilder.loadTexts:
    hpicfOobmMemberDefGatewayEntry.setStatus("current")
_HpicfOobmMemberDefGatewayType_Type = InetAddressType
_HpicfOobmMemberDefGatewayType_Object = MibTableColumn
hpicfOobmMemberDefGatewayType = _HpicfOobmMemberDefGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 5, 3, 1, 1),
    _HpicfOobmMemberDefGatewayType_Type()
)
hpicfOobmMemberDefGatewayType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOobmMemberDefGatewayType.setStatus("current")
_HpicfOobmMemberDefGatewayAddr_Type = InetAddress
_HpicfOobmMemberDefGatewayAddr_Object = MibTableColumn
hpicfOobmMemberDefGatewayAddr = _HpicfOobmMemberDefGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 5, 3, 1, 2),
    _HpicfOobmMemberDefGatewayAddr_Type()
)
hpicfOobmMemberDefGatewayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOobmMemberDefGatewayAddr.setStatus("current")
_HpicfOobmConformance_ObjectIdentity = ObjectIdentity
hpicfOobmConformance = _HpicfOobmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3)
)
_HpicfOobmCompliance_ObjectIdentity = ObjectIdentity
hpicfOobmCompliance = _HpicfOobmCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 1)
)
_HpicfOobmGroups_ObjectIdentity = ObjectIdentity
hpicfOobmGroups = _HpicfOobmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2)
)
snmpTargetAddrEntry.registerAugmentions(
    ("HP-ICF-OOBM-MIB",
     "hpicfSnmpTargetAddrIsOobmEntry")
)
hpicfSnmpTargetAddrIsOobmEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())

# Managed Objects groups

hpicfOobmScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2, 1)
)
hpicfOobmScalarsGroup.setObjects(
    ("HP-ICF-OOBM-MIB", "hpicfOobmStatus")
)
if mibBuilder.loadTexts:
    hpicfOobmScalarsGroup.setStatus("current")

hpicfOobmServersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2, 2)
)
hpicfOobmServersGroup.setObjects(
    ("HP-ICF-OOBM-MIB", "hpicfOobmServerListenMode")
)
if mibBuilder.loadTexts:
    hpicfOobmServersGroup.setStatus("current")

hpicfSnmpTargetAddrIsOobmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2, 3)
)
hpicfSnmpTargetAddrIsOobmGroup.setObjects(
    ("HP-ICF-OOBM-MIB", "hpicfSnmpTargetAddrIsOobm")
)
if mibBuilder.loadTexts:
    hpicfSnmpTargetAddrIsOobmGroup.setStatus("current")

hpicfOobmDefGatewayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2, 4)
)
hpicfOobmDefGatewayGroup.setObjects(
    ("HP-ICF-OOBM-MIB", "hpicfOobmDefGatewayAddr")
)
if mibBuilder.loadTexts:
    hpicfOobmDefGatewayGroup.setStatus("current")

hpicfOobmMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2, 5)
)
hpicfOobmMemberGroup.setObjects(
    ("HP-ICF-OOBM-MIB", "hpicfOobmMemberDefGatewayAddr")
)
if mibBuilder.loadTexts:
    hpicfOobmMemberGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfOobmMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfOobmMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-OOBM-MIB",
    **{"HpicfOobmServerIndex": HpicfOobmServerIndex,
       "HpicfOobmServerState": HpicfOobmServerState,
       "hpicfOobmMIB": hpicfOobmMIB,
       "hpicfOobmNotifications": hpicfOobmNotifications,
       "hpicfOobmObjects": hpicfOobmObjects,
       "hpicfOobmScalars": hpicfOobmScalars,
       "hpicfOobmStatus": hpicfOobmStatus,
       "hpicfOobmServers": hpicfOobmServers,
       "hpicfOobmServerTable": hpicfOobmServerTable,
       "hpicfOobmServerEntry": hpicfOobmServerEntry,
       "hpicfOobmServerType": hpicfOobmServerType,
       "hpicfOobmServerListenMode": hpicfOobmServerListenMode,
       "hpicfOobmSnmpTargetAddrIsOobm": hpicfOobmSnmpTargetAddrIsOobm,
       "hpicfSnmpTargetAddrIsOobmTable": hpicfSnmpTargetAddrIsOobmTable,
       "hpicfSnmpTargetAddrIsOobmEntry": hpicfSnmpTargetAddrIsOobmEntry,
       "hpicfSnmpTargetAddrIsOobm": hpicfSnmpTargetAddrIsOobm,
       "hpicfOobmDefGateway": hpicfOobmDefGateway,
       "hpicfOobmDefGatewayTable": hpicfOobmDefGatewayTable,
       "hpicfOobmDefGatewayEntry": hpicfOobmDefGatewayEntry,
       "hpicfOobmDefGatewayType": hpicfOobmDefGatewayType,
       "hpicfOobmDefGatewayAddr": hpicfOobmDefGatewayAddr,
       "hpicfOobmStackMembers": hpicfOobmStackMembers,
       "hpicfOobmMemberDefGatewayTable": hpicfOobmMemberDefGatewayTable,
       "hpicfOobmMemberDefGatewayEntry": hpicfOobmMemberDefGatewayEntry,
       "hpicfOobmMemberDefGatewayType": hpicfOobmMemberDefGatewayType,
       "hpicfOobmMemberDefGatewayAddr": hpicfOobmMemberDefGatewayAddr,
       "hpicfOobmConformance": hpicfOobmConformance,
       "hpicfOobmCompliance": hpicfOobmCompliance,
       "hpicfOobmMibCompliance": hpicfOobmMibCompliance,
       "hpicfOobmGroups": hpicfOobmGroups,
       "hpicfOobmScalarsGroup": hpicfOobmScalarsGroup,
       "hpicfOobmServersGroup": hpicfOobmServersGroup,
       "hpicfSnmpTargetAddrIsOobmGroup": hpicfSnmpTargetAddrIsOobmGroup,
       "hpicfOobmDefGatewayGroup": hpicfOobmDefGatewayGroup,
       "hpicfOobmMemberGroup": hpicfOobmMemberGroup}
)
