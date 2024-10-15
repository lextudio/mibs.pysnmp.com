# SNMP MIB module (CISCO-ATM-SERVICE-REGISTRY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-SERVICE-REGISTRY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:59 2024
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

ciscoAtmServiceRegistryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 50)
)
ciscoAtmServiceRegistryMIB.setRevisions(
        ("1996-02-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AtmAddr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(20, 20),
    )



class InterfaceIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAtmServiceRegistryMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmServiceRegistryMIBObjects = _CiscoAtmServiceRegistryMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 50, 1)
)
_AsrSrvcRegTable_Object = MibTable
asrSrvcRegTable = _AsrSrvcRegTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1)
)
if mibBuilder.loadTexts:
    asrSrvcRegTable.setStatus("current")
_AsrSrvcRegEntry_Object = MibTableRow
asrSrvcRegEntry = _AsrSrvcRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1)
)
asrSrvcRegEntry.setIndexNames(
    (0, "CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegPort"),
    (0, "CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegServiceID"),
    (0, "CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegAddressIndex"),
)
if mibBuilder.loadTexts:
    asrSrvcRegEntry.setStatus("current")
_AsrSrvcRegPort_Type = InterfaceIndexOrZero
_AsrSrvcRegPort_Object = MibTableColumn
asrSrvcRegPort = _AsrSrvcRegPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 1),
    _AsrSrvcRegPort_Type()
)
asrSrvcRegPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asrSrvcRegPort.setStatus("current")
_AsrSrvcRegServiceID_Type = ObjectIdentifier
_AsrSrvcRegServiceID_Object = MibTableColumn
asrSrvcRegServiceID = _AsrSrvcRegServiceID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 2),
    _AsrSrvcRegServiceID_Type()
)
asrSrvcRegServiceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asrSrvcRegServiceID.setStatus("current")
_AsrSrvcRegATMAddress_Type = AtmAddr
_AsrSrvcRegATMAddress_Object = MibTableColumn
asrSrvcRegATMAddress = _AsrSrvcRegATMAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 3),
    _AsrSrvcRegATMAddress_Type()
)
asrSrvcRegATMAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    asrSrvcRegATMAddress.setStatus("current")
_AsrSrvcRegAddressIndex_Type = Integer32
_AsrSrvcRegAddressIndex_Object = MibTableColumn
asrSrvcRegAddressIndex = _AsrSrvcRegAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 4),
    _AsrSrvcRegAddressIndex_Type()
)
asrSrvcRegAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asrSrvcRegAddressIndex.setStatus("current")
_AsrSrvcRegParm1_Type = OctetString
_AsrSrvcRegParm1_Object = MibTableColumn
asrSrvcRegParm1 = _AsrSrvcRegParm1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 5),
    _AsrSrvcRegParm1_Type()
)
asrSrvcRegParm1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    asrSrvcRegParm1.setStatus("current")
_AsrSrvcRegRowStatus_Type = RowStatus
_AsrSrvcRegRowStatus_Object = MibTableColumn
asrSrvcRegRowStatus = _AsrSrvcRegRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 6),
    _AsrSrvcRegRowStatus_Type()
)
asrSrvcRegRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    asrSrvcRegRowStatus.setStatus("current")
_AsrSrvcRegMIBConformance_ObjectIdentity = ObjectIdentity
asrSrvcRegMIBConformance = _AsrSrvcRegMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 50, 3)
)
_AsrSrvcRegMIBCompliances_ObjectIdentity = ObjectIdentity
asrSrvcRegMIBCompliances = _AsrSrvcRegMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 1)
)
_AsrSrvcRegMIBGroups_ObjectIdentity = ObjectIdentity
asrSrvcRegMIBGroups = _AsrSrvcRegMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 2)
)

# Managed Objects groups

asrSrvcRegMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 2, 1)
)
asrSrvcRegMIBGroup.setObjects(
      *(("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegATMAddress"),
        ("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegParm1"),
        ("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegRowStatus"))
)
if mibBuilder.loadTexts:
    asrSrvcRegMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

asrSrvcRegMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 1, 1)
)
if mibBuilder.loadTexts:
    asrSrvcRegMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-SERVICE-REGISTRY-MIB",
    **{"AtmAddr": AtmAddr,
       "InterfaceIndexOrZero": InterfaceIndexOrZero,
       "ciscoAtmServiceRegistryMIB": ciscoAtmServiceRegistryMIB,
       "ciscoAtmServiceRegistryMIBObjects": ciscoAtmServiceRegistryMIBObjects,
       "asrSrvcRegTable": asrSrvcRegTable,
       "asrSrvcRegEntry": asrSrvcRegEntry,
       "asrSrvcRegPort": asrSrvcRegPort,
       "asrSrvcRegServiceID": asrSrvcRegServiceID,
       "asrSrvcRegATMAddress": asrSrvcRegATMAddress,
       "asrSrvcRegAddressIndex": asrSrvcRegAddressIndex,
       "asrSrvcRegParm1": asrSrvcRegParm1,
       "asrSrvcRegRowStatus": asrSrvcRegRowStatus,
       "asrSrvcRegMIBConformance": asrSrvcRegMIBConformance,
       "asrSrvcRegMIBCompliances": asrSrvcRegMIBCompliances,
       "asrSrvcRegMIBCompliance": asrSrvcRegMIBCompliance,
       "asrSrvcRegMIBGroups": asrSrvcRegMIBGroups,
       "asrSrvcRegMIBGroup": asrSrvcRegMIBGroup}
)
