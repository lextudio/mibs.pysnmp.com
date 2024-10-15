# SNMP MIB module (CISCO-ISNS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ISNS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:11 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoPort,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoIsnsClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 372)
)
ciscoIsnsClientMIB.setRevisions(
        ("2003-11-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIsnsClientMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoIsnsClientMIBNotifications = _CiscoIsnsClientMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 372, 0)
)
_CiscoIsnsClientMIBMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIsnsClientMIBMIBObjects = _CiscoIsnsClientMIBMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 372, 1)
)
_CIsnsClientConfig_ObjectIdentity = ObjectIdentity
cIsnsClientConfig = _CIsnsClientConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 372, 1, 1)
)
_CIsnsClntServerProfileTable_Object = MibTable
cIsnsClntServerProfileTable = _CIsnsClntServerProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 372, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cIsnsClntServerProfileTable.setStatus("current")
_CIsnsClntServerProfileEntry_Object = MibTableRow
cIsnsClntServerProfileEntry = _CIsnsClntServerProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 372, 1, 1, 1, 1)
)
cIsnsClntServerProfileEntry.setIndexNames(
    (0, "CISCO-ISNS-CLIENT-MIB", "cIsnsClntServerProfileName"),
    (0, "CISCO-ISNS-CLIENT-MIB", "cIsnsClntServerIndex"),
)
if mibBuilder.loadTexts:
    cIsnsClntServerProfileEntry.setStatus("current")


class _CIsnsClntServerProfileName_Type(SnmpAdminString):
    """Custom type cIsnsClntServerProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CIsnsClntServerProfileName_Type.__name__ = "SnmpAdminString"
_CIsnsClntServerProfileName_Object = MibTableColumn
cIsnsClntServerProfileName = _CIsnsClntServerProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 372, 1, 1, 1, 1, 1),
    _CIsnsClntServerProfileName_Type()
)
cIsnsClntServerProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsClntServerProfileName.setStatus("current")


class _CIsnsClntServerIndex_Type(Unsigned32):
    """Custom type cIsnsClntServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CIsnsClntServerIndex_Type.__name__ = "Unsigned32"
_CIsnsClntServerIndex_Object = MibTableColumn
cIsnsClntServerIndex = _CIsnsClntServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 372, 1, 1, 1, 1, 2),
    _CIsnsClntServerIndex_Type()
)
cIsnsClntServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIsnsClntServerIndex.setStatus("current")
_CIsnsClntServerProfileAddrType_Type = InetAddressType
_CIsnsClntServerProfileAddrType_Object = MibTableColumn
cIsnsClntServerProfileAddrType = _CIsnsClntServerProfileAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 372, 1, 1, 1, 1, 3),
    _CIsnsClntServerProfileAddrType_Type()
)
cIsnsClntServerProfileAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsClntServerProfileAddrType.setStatus("current")
_CIsnsClntServerProfileAddr_Type = InetAddress
_CIsnsClntServerProfileAddr_Object = MibTableColumn
cIsnsClntServerProfileAddr = _CIsnsClntServerProfileAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 372, 1, 1, 1, 1, 4),
    _CIsnsClntServerProfileAddr_Type()
)
cIsnsClntServerProfileAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsClntServerProfileAddr.setStatus("current")


class _CIsnsClntServerProfilePort_Type(CiscoPort):
    """Custom type cIsnsClntServerProfilePort based on CiscoPort"""
    defaultValue = 3205


_CIsnsClntServerProfilePort_Object = MibTableColumn
cIsnsClntServerProfilePort = _CIsnsClntServerProfilePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 372, 1, 1, 1, 1, 5),
    _CIsnsClntServerProfilePort_Type()
)
cIsnsClntServerProfilePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsClntServerProfilePort.setStatus("current")
_CIsnsClntServerProfileStatus_Type = RowStatus
_CIsnsClntServerProfileStatus_Object = MibTableColumn
cIsnsClntServerProfileStatus = _CIsnsClntServerProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 372, 1, 1, 1, 1, 6),
    _CIsnsClntServerProfileStatus_Type()
)
cIsnsClntServerProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIsnsClntServerProfileStatus.setStatus("current")
_CiscoIsnsClientMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIsnsClientMIBConformance = _CiscoIsnsClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 372, 2)
)
_CiscoiIsnsClientMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoiIsnsClientMIBCompliances = _CiscoiIsnsClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 372, 2, 1)
)
_CiscoIsnsClientMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIsnsClientMIBGroups = _CiscoIsnsClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 372, 2, 2)
)

# Managed Objects groups

cIsnsServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 372, 2, 2, 1)
)
cIsnsServerConfigGroup.setObjects(
      *(("CISCO-ISNS-CLIENT-MIB", "cIsnsClntServerProfileAddrType"),
        ("CISCO-ISNS-CLIENT-MIB", "cIsnsClntServerProfileAddr"),
        ("CISCO-ISNS-CLIENT-MIB", "cIsnsClntServerProfilePort"),
        ("CISCO-ISNS-CLIENT-MIB", "cIsnsClntServerProfileStatus"))
)
if mibBuilder.loadTexts:
    cIsnsServerConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIsnsClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 372, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIsnsClientMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ISNS-CLIENT-MIB",
    **{"ciscoIsnsClientMIB": ciscoIsnsClientMIB,
       "ciscoIsnsClientMIBNotifications": ciscoIsnsClientMIBNotifications,
       "ciscoIsnsClientMIBMIBObjects": ciscoIsnsClientMIBMIBObjects,
       "cIsnsClientConfig": cIsnsClientConfig,
       "cIsnsClntServerProfileTable": cIsnsClntServerProfileTable,
       "cIsnsClntServerProfileEntry": cIsnsClntServerProfileEntry,
       "cIsnsClntServerProfileName": cIsnsClntServerProfileName,
       "cIsnsClntServerIndex": cIsnsClntServerIndex,
       "cIsnsClntServerProfileAddrType": cIsnsClntServerProfileAddrType,
       "cIsnsClntServerProfileAddr": cIsnsClntServerProfileAddr,
       "cIsnsClntServerProfilePort": cIsnsClntServerProfilePort,
       "cIsnsClntServerProfileStatus": cIsnsClntServerProfileStatus,
       "ciscoIsnsClientMIBConformance": ciscoIsnsClientMIBConformance,
       "ciscoiIsnsClientMIBCompliances": ciscoiIsnsClientMIBCompliances,
       "ciscoIsnsClientMIBCompliance": ciscoIsnsClientMIBCompliance,
       "ciscoIsnsClientMIBGroups": ciscoIsnsClientMIBGroups,
       "cIsnsServerConfigGroup": cIsnsServerConfigGroup}
)
