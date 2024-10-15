# SNMP MIB module (CISCO-ITP-SP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-SP2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:37 2024
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

(CItpTcAclId,) = mibBuilder.importSymbols(
    "CISCO-ITP-TC-MIB",
    "CItpTcAclId")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoItpSp2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 248)
)
ciscoItpSp2MIB.setRevisions(
        ("2002-09-16 00:00",
         "2002-02-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CisTcQosClass(Unsigned32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoItpSp2MIBNotifications_ObjectIdentity = ObjectIdentity
ciscoItpSp2MIBNotifications = _CiscoItpSp2MIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 0)
)
_CiscoItpSp2MIBObjects_ObjectIdentity = ObjectIdentity
ciscoItpSp2MIBObjects = _CiscoItpSp2MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1)
)
_CisEvents_ObjectIdentity = ObjectIdentity
cisEvents = _CisEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 1)
)
_CisEventSummryLoggedEvents_Type = Counter32
_CisEventSummryLoggedEvents_Object = MibScalar
cisEventSummryLoggedEvents = _CisEventSummryLoggedEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 1, 1),
    _CisEventSummryLoggedEvents_Type()
)
cisEventSummryLoggedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisEventSummryLoggedEvents.setStatus("deprecated")
_CisEventSummryDroppedEvents_Type = Counter32
_CisEventSummryDroppedEvents_Object = MibScalar
cisEventSummryDroppedEvents = _CisEventSummryDroppedEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 1, 2),
    _CisEventSummryDroppedEvents_Type()
)
cisEventSummryDroppedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisEventSummryDroppedEvents.setStatus("deprecated")


class _CisEventHistoryMaxEntries_Type(Unsigned32):
    """Custom type cisEventHistoryMaxEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CisEventHistoryMaxEntries_Type.__name__ = "Unsigned32"
_CisEventHistoryMaxEntries_Object = MibScalar
cisEventHistoryMaxEntries = _CisEventHistoryMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 1, 3),
    _CisEventHistoryMaxEntries_Type()
)
cisEventHistoryMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisEventHistoryMaxEntries.setStatus("deprecated")


class _CisEventHistoryTableEntAllowed_Type(Unsigned32):
    """Custom type cisEventHistoryTableEntAllowed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CisEventHistoryTableEntAllowed_Type.__name__ = "Unsigned32"
_CisEventHistoryTableEntAllowed_Object = MibScalar
cisEventHistoryTableEntAllowed = _CisEventHistoryTableEntAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 1, 4),
    _CisEventHistoryTableEntAllowed_Type()
)
cisEventHistoryTableEntAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisEventHistoryTableEntAllowed.setStatus("deprecated")
_CisEventHistoryTable_Object = MibTable
cisEventHistoryTable = _CisEventHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cisEventHistoryTable.setStatus("deprecated")
_CisEventHistoryTableEntry_Object = MibTableRow
cisEventHistoryTableEntry = _CisEventHistoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 1, 5, 1)
)
cisEventHistoryTableEntry.setIndexNames(
    (0, "CISCO-ITP-SP2-MIB", "cisEventHistoryIndex"),
)
if mibBuilder.loadTexts:
    cisEventHistoryTableEntry.setStatus("deprecated")


class _CisEventHistoryIndex_Type(Unsigned32):
    """Custom type cisEventHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CisEventHistoryIndex_Type.__name__ = "Unsigned32"
_CisEventHistoryIndex_Object = MibTableColumn
cisEventHistoryIndex = _CisEventHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 1, 5, 1, 1),
    _CisEventHistoryIndex_Type()
)
cisEventHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisEventHistoryIndex.setStatus("deprecated")


class _CisEventHistoryDescr_Type(SnmpAdminString):
    """Custom type cisEventHistoryDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CisEventHistoryDescr_Type.__name__ = "SnmpAdminString"
_CisEventHistoryDescr_Object = MibTableColumn
cisEventHistoryDescr = _CisEventHistoryDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 1, 5, 1, 2),
    _CisEventHistoryDescr_Type()
)
cisEventHistoryDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisEventHistoryDescr.setStatus("deprecated")
_CisQos_ObjectIdentity = ObjectIdentity
cisQos = _CisQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 2)
)
_CisQosTable_Object = MibTable
cisQosTable = _CisQosTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cisQosTable.setStatus("deprecated")
_CisQosTableEntry_Object = MibTableRow
cisQosTableEntry = _CisQosTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 2, 1, 1)
)
cisQosTableEntry.setIndexNames(
    (0, "CISCO-ITP-SP2-MIB", "cisQosClass"),
)
if mibBuilder.loadTexts:
    cisQosTableEntry.setStatus("deprecated")
_CisQosClass_Type = CisTcQosClass
_CisQosClass_Object = MibTableColumn
cisQosClass = _CisQosClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 2, 1, 1, 1),
    _CisQosClass_Type()
)
cisQosClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisQosClass.setStatus("deprecated")


class _CisQosType_Type(Integer32):
    """Custom type cisQosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipDscp", 2),
          ("ipPrecedence", 1))
    )


_CisQosType_Type.__name__ = "Integer32"
_CisQosType_Object = MibTableColumn
cisQosType = _CisQosType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 2, 1, 1, 2),
    _CisQosType_Type()
)
cisQosType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisQosType.setStatus("deprecated")


class _CisQosPrecedenceValue_Type(Integer32):
    """Custom type cisQosPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_CisQosPrecedenceValue_Type.__name__ = "Integer32"
_CisQosPrecedenceValue_Object = MibTableColumn
cisQosPrecedenceValue = _CisQosPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 2, 1, 1, 3),
    _CisQosPrecedenceValue_Type()
)
cisQosPrecedenceValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisQosPrecedenceValue.setStatus("deprecated")


class _CisQosIpDscp_Type(Integer32):
    """Custom type cisQosIpDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_CisQosIpDscp_Type.__name__ = "Integer32"
_CisQosIpDscp_Object = MibTableColumn
cisQosIpDscp = _CisQosIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 2, 1, 1, 4),
    _CisQosIpDscp_Type()
)
cisQosIpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisQosIpDscp.setStatus("deprecated")


class _CisQosAclId_Type(CItpTcAclId):
    """Custom type cisQosAclId based on CItpTcAclId"""
    defaultValue = 0


_CisQosAclId_Object = MibTableColumn
cisQosAclId = _CisQosAclId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 2, 1, 1, 5),
    _CisQosAclId_Type()
)
cisQosAclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisQosAclId.setStatus("deprecated")
_CisQosRowStatus_Type = RowStatus
_CisQosRowStatus_Object = MibTableColumn
cisQosRowStatus = _CisQosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 1, 2, 1, 1, 6),
    _CisQosRowStatus_Type()
)
cisQosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cisQosRowStatus.setStatus("deprecated")
_CiscoItpSp2MIBConformance_ObjectIdentity = ObjectIdentity
ciscoItpSp2MIBConformance = _CiscoItpSp2MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 2)
)
_CiscoItpSp2MIBCompliances_ObjectIdentity = ObjectIdentity
ciscoItpSp2MIBCompliances = _CiscoItpSp2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 2, 1)
)
_CiscoItpSp2MIBGroups_ObjectIdentity = ObjectIdentity
ciscoItpSp2MIBGroups = _CiscoItpSp2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 2, 2)
)

# Managed Objects groups

ciscoItpSp2EventsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 2, 2, 1)
)
ciscoItpSp2EventsGroup.setObjects(
      *(("CISCO-ITP-SP2-MIB", "cisEventSummryLoggedEvents"),
        ("CISCO-ITP-SP2-MIB", "cisEventSummryDroppedEvents"),
        ("CISCO-ITP-SP2-MIB", "cisEventHistoryMaxEntries"),
        ("CISCO-ITP-SP2-MIB", "cisEventHistoryTableEntAllowed"),
        ("CISCO-ITP-SP2-MIB", "cisEventHistoryDescr"))
)
if mibBuilder.loadTexts:
    ciscoItpSp2EventsGroup.setStatus("deprecated")

ciscoItpSp2QosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 2, 2, 2)
)
ciscoItpSp2QosGroup.setObjects(
      *(("CISCO-ITP-SP2-MIB", "cisQosType"),
        ("CISCO-ITP-SP2-MIB", "cisQosPrecedenceValue"),
        ("CISCO-ITP-SP2-MIB", "cisQosIpDscp"),
        ("CISCO-ITP-SP2-MIB", "cisQosAclId"),
        ("CISCO-ITP-SP2-MIB", "cisQosRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoItpSp2QosGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoItpSp2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 248, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoItpSp2MIBCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-SP2-MIB",
    **{"CisTcQosClass": CisTcQosClass,
       "ciscoItpSp2MIB": ciscoItpSp2MIB,
       "ciscoItpSp2MIBNotifications": ciscoItpSp2MIBNotifications,
       "ciscoItpSp2MIBObjects": ciscoItpSp2MIBObjects,
       "cisEvents": cisEvents,
       "cisEventSummryLoggedEvents": cisEventSummryLoggedEvents,
       "cisEventSummryDroppedEvents": cisEventSummryDroppedEvents,
       "cisEventHistoryMaxEntries": cisEventHistoryMaxEntries,
       "cisEventHistoryTableEntAllowed": cisEventHistoryTableEntAllowed,
       "cisEventHistoryTable": cisEventHistoryTable,
       "cisEventHistoryTableEntry": cisEventHistoryTableEntry,
       "cisEventHistoryIndex": cisEventHistoryIndex,
       "cisEventHistoryDescr": cisEventHistoryDescr,
       "cisQos": cisQos,
       "cisQosTable": cisQosTable,
       "cisQosTableEntry": cisQosTableEntry,
       "cisQosClass": cisQosClass,
       "cisQosType": cisQosType,
       "cisQosPrecedenceValue": cisQosPrecedenceValue,
       "cisQosIpDscp": cisQosIpDscp,
       "cisQosAclId": cisQosAclId,
       "cisQosRowStatus": cisQosRowStatus,
       "ciscoItpSp2MIBConformance": ciscoItpSp2MIBConformance,
       "ciscoItpSp2MIBCompliances": ciscoItpSp2MIBCompliances,
       "ciscoItpSp2MIBCompliance": ciscoItpSp2MIBCompliance,
       "ciscoItpSp2MIBGroups": ciscoItpSp2MIBGroups,
       "ciscoItpSp2EventsGroup": ciscoItpSp2EventsGroup,
       "ciscoItpSp2QosGroup": ciscoItpSp2QosGroup}
)
