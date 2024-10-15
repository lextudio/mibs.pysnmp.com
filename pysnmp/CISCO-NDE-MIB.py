# SNMP MIB module (CISCO-NDE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NDE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:05 2024
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

ciscoNDEMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 226)
)
ciscoNDEMIB.setRevisions(
        ("2006-03-01 00:00",
         "2005-12-06 00:00",
         "2001-08-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CndeMIBNotifs_ObjectIdentity = ObjectIdentity
cndeMIBNotifs = _CndeMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 226, 0)
)
_CiscoNDEMIBObjects_ObjectIdentity = ObjectIdentity
ciscoNDEMIBObjects = _CiscoNDEMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 226, 1)
)
_CndeCollectorConfiguration_ObjectIdentity = ObjectIdentity
cndeCollectorConfiguration = _CndeCollectorConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1)
)
_CndeMaxCollectors_Type = Unsigned32
_CndeMaxCollectors_Object = MibScalar
cndeMaxCollectors = _CndeMaxCollectors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 1),
    _CndeMaxCollectors_Type()
)
cndeMaxCollectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndeMaxCollectors.setStatus("current")
_CndeCollectorTable_Object = MibTable
cndeCollectorTable = _CndeCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cndeCollectorTable.setStatus("current")
_CndeCollectorEntry_Object = MibTableRow
cndeCollectorEntry = _CndeCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2, 1)
)
cndeCollectorEntry.setIndexNames(
    (0, "CISCO-NDE-MIB", "cndeCollectorAddressType"),
    (0, "CISCO-NDE-MIB", "cndeCollectorAddress"),
    (0, "CISCO-NDE-MIB", "cndeCollectorPort"),
)
if mibBuilder.loadTexts:
    cndeCollectorEntry.setStatus("current")
_CndeCollectorAddressType_Type = InetAddressType
_CndeCollectorAddressType_Object = MibTableColumn
cndeCollectorAddressType = _CndeCollectorAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2, 1, 1),
    _CndeCollectorAddressType_Type()
)
cndeCollectorAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cndeCollectorAddressType.setStatus("current")


class _CndeCollectorAddress_Type(InetAddress):
    """Custom type cndeCollectorAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CndeCollectorAddress_Type.__name__ = "InetAddress"
_CndeCollectorAddress_Object = MibTableColumn
cndeCollectorAddress = _CndeCollectorAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2, 1, 2),
    _CndeCollectorAddress_Type()
)
cndeCollectorAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cndeCollectorAddress.setStatus("current")


class _CndeCollectorPort_Type(Integer32):
    """Custom type cndeCollectorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CndeCollectorPort_Type.__name__ = "Integer32"
_CndeCollectorPort_Object = MibTableColumn
cndeCollectorPort = _CndeCollectorPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2, 1, 3),
    _CndeCollectorPort_Type()
)
cndeCollectorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cndeCollectorPort.setStatus("current")
_CndeCollectorStatus_Type = RowStatus
_CndeCollectorStatus_Object = MibTableColumn
cndeCollectorStatus = _CndeCollectorStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2, 1, 4),
    _CndeCollectorStatus_Type()
)
cndeCollectorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cndeCollectorStatus.setStatus("current")
_CndeMIBNotifications_ObjectIdentity = ObjectIdentity
cndeMIBNotifications = _CndeMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 226, 2)
)
_CndeMIBConformance_ObjectIdentity = ObjectIdentity
cndeMIBConformance = _CndeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 226, 3)
)
_CndeMIBCompliances_ObjectIdentity = ObjectIdentity
cndeMIBCompliances = _CndeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 226, 3, 1)
)
_CndeMIBGroups_ObjectIdentity = ObjectIdentity
cndeMIBGroups = _CndeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 226, 3, 2)
)

# Managed Objects groups

cndeCollectorConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 226, 3, 2, 1)
)
cndeCollectorConfigurationGroup.setObjects(
      *(("CISCO-NDE-MIB", "cndeMaxCollectors"),
        ("CISCO-NDE-MIB", "cndeCollectorStatus"))
)
if mibBuilder.loadTexts:
    cndeCollectorConfigurationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cndeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 226, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cndeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NDE-MIB",
    **{"ciscoNDEMIB": ciscoNDEMIB,
       "cndeMIBNotifs": cndeMIBNotifs,
       "ciscoNDEMIBObjects": ciscoNDEMIBObjects,
       "cndeCollectorConfiguration": cndeCollectorConfiguration,
       "cndeMaxCollectors": cndeMaxCollectors,
       "cndeCollectorTable": cndeCollectorTable,
       "cndeCollectorEntry": cndeCollectorEntry,
       "cndeCollectorAddressType": cndeCollectorAddressType,
       "cndeCollectorAddress": cndeCollectorAddress,
       "cndeCollectorPort": cndeCollectorPort,
       "cndeCollectorStatus": cndeCollectorStatus,
       "cndeMIBNotifications": cndeMIBNotifications,
       "cndeMIBConformance": cndeMIBConformance,
       "cndeMIBCompliances": cndeMIBCompliances,
       "cndeMIBCompliance": cndeMIBCompliance,
       "cndeMIBGroups": cndeMIBGroups,
       "cndeCollectorConfigurationGroup": cndeCollectorConfigurationGroup}
)
