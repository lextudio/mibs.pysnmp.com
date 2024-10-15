# SNMP MIB module (WWP-LAYER4-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LAYER4-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:44 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpLayer4FilterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52)
)
wwpLayer4FilterMIB.setRevisions(
        ("2003-04-11 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_WwpLayer4FilterMIBObjects_ObjectIdentity = ObjectIdentity
wwpLayer4FilterMIBObjects = _WwpLayer4FilterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1)
)
_WwpLayer4Filter_ObjectIdentity = ObjectIdentity
wwpLayer4Filter = _WwpLayer4Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1)
)
_WwpMaxLayer4Filters_Type = Unsigned32
_WwpMaxLayer4Filters_Object = MibScalar
wwpMaxLayer4Filters = _WwpMaxLayer4Filters_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 1),
    _WwpMaxLayer4Filters_Type()
)
wwpMaxLayer4Filters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMaxLayer4Filters.setStatus("current")
_WwpNumLayer4Filters_Type = Unsigned32
_WwpNumLayer4Filters_Object = MibScalar
wwpNumLayer4Filters = _WwpNumLayer4Filters_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 2),
    _WwpNumLayer4Filters_Type()
)
wwpNumLayer4Filters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpNumLayer4Filters.setStatus("current")
_WwpLayer4FilterTable_Object = MibTable
wwpLayer4FilterTable = _WwpLayer4FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpLayer4FilterTable.setStatus("current")
_WwpLayer4FilterEntry_Object = MibTableRow
wwpLayer4FilterEntry = _WwpLayer4FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 3, 1)
)
wwpLayer4FilterEntry.setIndexNames(
    (0, "WWP-LAYER4-FILTER-MIB", "wwpLayer4FilterName"),
)
if mibBuilder.loadTexts:
    wwpLayer4FilterEntry.setStatus("current")


class _WwpLayer4FilterName_Type(OctetString):
    """Custom type wwpLayer4FilterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WwpLayer4FilterName_Type.__name__ = "OctetString"
_WwpLayer4FilterName_Object = MibTableColumn
wwpLayer4FilterName = _WwpLayer4FilterName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 3, 1, 1),
    _WwpLayer4FilterName_Type()
)
wwpLayer4FilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLayer4FilterName.setStatus("current")


class _WwpLayer4FilterProtocolNumber_Type(Integer32):
    """Custom type wwpLayer4FilterProtocolNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLayer4FilterProtocolNumber_Type.__name__ = "Integer32"
_WwpLayer4FilterProtocolNumber_Object = MibTableColumn
wwpLayer4FilterProtocolNumber = _WwpLayer4FilterProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 3, 1, 2),
    _WwpLayer4FilterProtocolNumber_Type()
)
wwpLayer4FilterProtocolNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLayer4FilterProtocolNumber.setStatus("current")


class _WwpLayer4FilterSrcPort_Type(Integer32):
    """Custom type wwpLayer4FilterSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLayer4FilterSrcPort_Type.__name__ = "Integer32"
_WwpLayer4FilterSrcPort_Object = MibTableColumn
wwpLayer4FilterSrcPort = _WwpLayer4FilterSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 3, 1, 3),
    _WwpLayer4FilterSrcPort_Type()
)
wwpLayer4FilterSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLayer4FilterSrcPort.setStatus("current")


class _WwpLayer4FilterDstPort_Type(Integer32):
    """Custom type wwpLayer4FilterDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLayer4FilterDstPort_Type.__name__ = "Integer32"
_WwpLayer4FilterDstPort_Object = MibTableColumn
wwpLayer4FilterDstPort = _WwpLayer4FilterDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 3, 1, 4),
    _WwpLayer4FilterDstPort_Type()
)
wwpLayer4FilterDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLayer4FilterDstPort.setStatus("current")
_WwpLayer4FilterStatus_Type = RowStatus
_WwpLayer4FilterStatus_Object = MibTableColumn
wwpLayer4FilterStatus = _WwpLayer4FilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 3, 1, 5),
    _WwpLayer4FilterStatus_Type()
)
wwpLayer4FilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLayer4FilterStatus.setStatus("current")
_WwpLayer4FilterAttachTable_Object = MibTable
wwpLayer4FilterAttachTable = _WwpLayer4FilterAttachTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpLayer4FilterAttachTable.setStatus("current")
_WwpLayer4FilterAttachEntry_Object = MibTableRow
wwpLayer4FilterAttachEntry = _WwpLayer4FilterAttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 4, 1)
)
wwpLayer4FilterAttachEntry.setIndexNames(
    (0, "WWP-LAYER4-FILTER-MIB", "wwpLayer4FilterVid"),
    (0, "WWP-LAYER4-FILTER-MIB", "wwpLayer4FilterName"),
    (0, "WWP-LAYER4-FILTER-MIB", "wwpLayer4FilterAttachType"),
)
if mibBuilder.loadTexts:
    wwpLayer4FilterAttachEntry.setStatus("current")


class _WwpLayer4FilterVid_Type(Integer32):
    """Custom type wwpLayer4FilterVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WwpLayer4FilterVid_Type.__name__ = "Integer32"
_WwpLayer4FilterVid_Object = MibTableColumn
wwpLayer4FilterVid = _WwpLayer4FilterVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 4, 1, 1),
    _WwpLayer4FilterVid_Type()
)
wwpLayer4FilterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLayer4FilterVid.setStatus("current")


class _WwpLayer4FilterAttachType_Type(Integer32):
    """Custom type wwpLayer4FilterAttachType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("deny", 1))
    )


_WwpLayer4FilterAttachType_Type.__name__ = "Integer32"
_WwpLayer4FilterAttachType_Object = MibTableColumn
wwpLayer4FilterAttachType = _WwpLayer4FilterAttachType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 4, 1, 2),
    _WwpLayer4FilterAttachType_Type()
)
wwpLayer4FilterAttachType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLayer4FilterAttachType.setStatus("current")
_WwpLayer4FilterPortList_Type = PortList
_WwpLayer4FilterPortList_Object = MibTableColumn
wwpLayer4FilterPortList = _WwpLayer4FilterPortList_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 4, 1, 3),
    _WwpLayer4FilterPortList_Type()
)
wwpLayer4FilterPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLayer4FilterPortList.setStatus("current")


class _WwpLayer4FilterCounterId_Type(Integer32):
    """Custom type wwpLayer4FilterCounterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WwpLayer4FilterCounterId_Type.__name__ = "Integer32"
_WwpLayer4FilterCounterId_Object = MibTableColumn
wwpLayer4FilterCounterId = _WwpLayer4FilterCounterId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 4, 1, 4),
    _WwpLayer4FilterCounterId_Type()
)
wwpLayer4FilterCounterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLayer4FilterCounterId.setStatus("current")
_WwpLayer4FilterCount_Type = Counter32
_WwpLayer4FilterCount_Object = MibTableColumn
wwpLayer4FilterCount = _WwpLayer4FilterCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 4, 1, 5),
    _WwpLayer4FilterCount_Type()
)
wwpLayer4FilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLayer4FilterCount.setStatus("current")
_WwpLayer4FilterAttachStatus_Type = RowStatus
_WwpLayer4FilterAttachStatus_Object = MibTableColumn
wwpLayer4FilterAttachStatus = _WwpLayer4FilterAttachStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 4, 1, 6),
    _WwpLayer4FilterAttachStatus_Type()
)
wwpLayer4FilterAttachStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLayer4FilterAttachStatus.setStatus("current")
_WwpLayer4FilterMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLayer4FilterMIBNotificationPrefix = _WwpLayer4FilterMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 2)
)
_WwpLayer4FilterMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLayer4FilterMIBNotifications = _WwpLayer4FilterMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 2, 0)
)
_WwpLayer4FilterMIBConformance_ObjectIdentity = ObjectIdentity
wwpLayer4FilterMIBConformance = _WwpLayer4FilterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 3)
)
_WwpLayer4FilterMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLayer4FilterMIBCompliances = _WwpLayer4FilterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 3, 1)
)
_WwpLayer4FilterMIBGroups_ObjectIdentity = ObjectIdentity
wwpLayer4FilterMIBGroups = _WwpLayer4FilterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 52, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LAYER4-FILTER-MIB",
    **{"PortList": PortList,
       "wwpLayer4FilterMIB": wwpLayer4FilterMIB,
       "wwpLayer4FilterMIBObjects": wwpLayer4FilterMIBObjects,
       "wwpLayer4Filter": wwpLayer4Filter,
       "wwpMaxLayer4Filters": wwpMaxLayer4Filters,
       "wwpNumLayer4Filters": wwpNumLayer4Filters,
       "wwpLayer4FilterTable": wwpLayer4FilterTable,
       "wwpLayer4FilterEntry": wwpLayer4FilterEntry,
       "wwpLayer4FilterName": wwpLayer4FilterName,
       "wwpLayer4FilterProtocolNumber": wwpLayer4FilterProtocolNumber,
       "wwpLayer4FilterSrcPort": wwpLayer4FilterSrcPort,
       "wwpLayer4FilterDstPort": wwpLayer4FilterDstPort,
       "wwpLayer4FilterStatus": wwpLayer4FilterStatus,
       "wwpLayer4FilterAttachTable": wwpLayer4FilterAttachTable,
       "wwpLayer4FilterAttachEntry": wwpLayer4FilterAttachEntry,
       "wwpLayer4FilterVid": wwpLayer4FilterVid,
       "wwpLayer4FilterAttachType": wwpLayer4FilterAttachType,
       "wwpLayer4FilterPortList": wwpLayer4FilterPortList,
       "wwpLayer4FilterCounterId": wwpLayer4FilterCounterId,
       "wwpLayer4FilterCount": wwpLayer4FilterCount,
       "wwpLayer4FilterAttachStatus": wwpLayer4FilterAttachStatus,
       "wwpLayer4FilterMIBNotificationPrefix": wwpLayer4FilterMIBNotificationPrefix,
       "wwpLayer4FilterMIBNotifications": wwpLayer4FilterMIBNotifications,
       "wwpLayer4FilterMIBConformance": wwpLayer4FilterMIBConformance,
       "wwpLayer4FilterMIBCompliances": wwpLayer4FilterMIBCompliances,
       "wwpLayer4FilterMIBGroups": wwpLayer4FilterMIBGroups}
)
