# SNMP MIB module (HPR-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPR-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:31 2024
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

(SnaControlPointName,) = mibBuilder.importSymbols(
    "APPN-MIB",
    "SnaControlPointName")

(hprCompliances,
 hprGroups,
 hprObjects) = mibBuilder.importSymbols(
    "HPR-MIB",
    "hprCompliances",
    "hprGroups",
    "hprObjects")

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

hprIp = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5)
)
hprIp.setRevisions(
        ("1998-09-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AppnTrafficType(Integer32, TextualConvention):
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
        *(("high", 3),
          ("llcAndFnRoutedNlp", 5),
          ("low", 1),
          ("medium", 2),
          ("network", 4))
    )



class AppnTOSPrecedence(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



# MIB Managed Objects in the order of their OIDs

_HprIpActiveLsTable_Object = MibTable
hprIpActiveLsTable = _HprIpActiveLsTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hprIpActiveLsTable.setStatus("current")
_HprIpActiveLsEntry_Object = MibTableRow
hprIpActiveLsEntry = _HprIpActiveLsEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1)
)
hprIpActiveLsEntry.setIndexNames(
    (0, "HPR-IP-MIB", "hprIpActiveLsLsName"),
    (0, "HPR-IP-MIB", "hprIpActiveLsAppnTrafficType"),
)
if mibBuilder.loadTexts:
    hprIpActiveLsEntry.setStatus("current")


class _HprIpActiveLsLsName_Type(DisplayString):
    """Custom type hprIpActiveLsLsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_HprIpActiveLsLsName_Type.__name__ = "DisplayString"
_HprIpActiveLsLsName_Object = MibTableColumn
hprIpActiveLsLsName = _HprIpActiveLsLsName_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1, 1),
    _HprIpActiveLsLsName_Type()
)
hprIpActiveLsLsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hprIpActiveLsLsName.setStatus("current")
_HprIpActiveLsAppnTrafficType_Type = AppnTrafficType
_HprIpActiveLsAppnTrafficType_Object = MibTableColumn
hprIpActiveLsAppnTrafficType = _HprIpActiveLsAppnTrafficType_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1, 2),
    _HprIpActiveLsAppnTrafficType_Type()
)
hprIpActiveLsAppnTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hprIpActiveLsAppnTrafficType.setStatus("current")
_HprIpActiveLsUdpPackets_Type = Counter32
_HprIpActiveLsUdpPackets_Object = MibTableColumn
hprIpActiveLsUdpPackets = _HprIpActiveLsUdpPackets_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1, 3),
    _HprIpActiveLsUdpPackets_Type()
)
hprIpActiveLsUdpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprIpActiveLsUdpPackets.setStatus("current")
_HprIpAppnPortTable_Object = MibTable
hprIpAppnPortTable = _HprIpAppnPortTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hprIpAppnPortTable.setStatus("current")
_HprIpAppnPortEntry_Object = MibTableRow
hprIpAppnPortEntry = _HprIpAppnPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1)
)
hprIpAppnPortEntry.setIndexNames(
    (0, "HPR-IP-MIB", "hprIpAppnPortName"),
    (0, "HPR-IP-MIB", "hprIpAppnPortAppnTrafficType"),
)
if mibBuilder.loadTexts:
    hprIpAppnPortEntry.setStatus("current")


class _HprIpAppnPortName_Type(DisplayString):
    """Custom type hprIpAppnPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_HprIpAppnPortName_Type.__name__ = "DisplayString"
_HprIpAppnPortName_Object = MibTableColumn
hprIpAppnPortName = _HprIpAppnPortName_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1, 1),
    _HprIpAppnPortName_Type()
)
hprIpAppnPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hprIpAppnPortName.setStatus("current")
_HprIpAppnPortAppnTrafficType_Type = AppnTrafficType
_HprIpAppnPortAppnTrafficType_Object = MibTableColumn
hprIpAppnPortAppnTrafficType = _HprIpAppnPortAppnTrafficType_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1, 2),
    _HprIpAppnPortAppnTrafficType_Type()
)
hprIpAppnPortAppnTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hprIpAppnPortAppnTrafficType.setStatus("current")
_HprIpAppnPortTOSPrecedence_Type = AppnTOSPrecedence
_HprIpAppnPortTOSPrecedence_Object = MibTableColumn
hprIpAppnPortTOSPrecedence = _HprIpAppnPortTOSPrecedence_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1, 3),
    _HprIpAppnPortTOSPrecedence_Type()
)
hprIpAppnPortTOSPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hprIpAppnPortTOSPrecedence.setStatus("current")
_HprIpLsTable_Object = MibTable
hprIpLsTable = _HprIpLsTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3)
)
if mibBuilder.loadTexts:
    hprIpLsTable.setStatus("current")
_HprIpLsEntry_Object = MibTableRow
hprIpLsEntry = _HprIpLsEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1)
)
hprIpLsEntry.setIndexNames(
    (0, "HPR-IP-MIB", "hprIpLsLsName"),
    (0, "HPR-IP-MIB", "hprIpLsAppnTrafficType"),
)
if mibBuilder.loadTexts:
    hprIpLsEntry.setStatus("current")


class _HprIpLsLsName_Type(DisplayString):
    """Custom type hprIpLsLsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_HprIpLsLsName_Type.__name__ = "DisplayString"
_HprIpLsLsName_Object = MibTableColumn
hprIpLsLsName = _HprIpLsLsName_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 1),
    _HprIpLsLsName_Type()
)
hprIpLsLsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hprIpLsLsName.setStatus("current")
_HprIpLsAppnTrafficType_Type = AppnTrafficType
_HprIpLsAppnTrafficType_Object = MibTableColumn
hprIpLsAppnTrafficType = _HprIpLsAppnTrafficType_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 2),
    _HprIpLsAppnTrafficType_Type()
)
hprIpLsAppnTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hprIpLsAppnTrafficType.setStatus("current")
_HprIpLsTOSPrecedence_Type = AppnTOSPrecedence
_HprIpLsTOSPrecedence_Object = MibTableColumn
hprIpLsTOSPrecedence = _HprIpLsTOSPrecedence_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 3),
    _HprIpLsTOSPrecedence_Type()
)
hprIpLsTOSPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hprIpLsTOSPrecedence.setStatus("current")
_HprIpLsRowStatus_Type = RowStatus
_HprIpLsRowStatus_Object = MibTableColumn
hprIpLsRowStatus = _HprIpLsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 4),
    _HprIpLsRowStatus_Type()
)
hprIpLsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hprIpLsRowStatus.setStatus("current")
_HprIpCnTable_Object = MibTable
hprIpCnTable = _HprIpCnTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4)
)
if mibBuilder.loadTexts:
    hprIpCnTable.setStatus("current")
_HprIpCnEntry_Object = MibTableRow
hprIpCnEntry = _HprIpCnEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1)
)
hprIpCnEntry.setIndexNames(
    (0, "HPR-IP-MIB", "hprIpCnVrnName"),
    (0, "HPR-IP-MIB", "hprIpCnAppnTrafficType"),
)
if mibBuilder.loadTexts:
    hprIpCnEntry.setStatus("current")
_HprIpCnVrnName_Type = SnaControlPointName
_HprIpCnVrnName_Object = MibTableColumn
hprIpCnVrnName = _HprIpCnVrnName_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 1),
    _HprIpCnVrnName_Type()
)
hprIpCnVrnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hprIpCnVrnName.setStatus("current")
_HprIpCnAppnTrafficType_Type = AppnTrafficType
_HprIpCnAppnTrafficType_Object = MibTableColumn
hprIpCnAppnTrafficType = _HprIpCnAppnTrafficType_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 2),
    _HprIpCnAppnTrafficType_Type()
)
hprIpCnAppnTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hprIpCnAppnTrafficType.setStatus("current")
_HprIpCnTOSPrecedence_Type = AppnTOSPrecedence
_HprIpCnTOSPrecedence_Object = MibTableColumn
hprIpCnTOSPrecedence = _HprIpCnTOSPrecedence_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 3),
    _HprIpCnTOSPrecedence_Type()
)
hprIpCnTOSPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hprIpCnTOSPrecedence.setStatus("current")
_HprIpCnRowStatus_Type = RowStatus
_HprIpCnRowStatus_Object = MibTableColumn
hprIpCnRowStatus = _HprIpCnRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 4),
    _HprIpCnRowStatus_Type()
)
hprIpCnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hprIpCnRowStatus.setStatus("current")

# Managed Objects groups

hprIpMonitoringGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 5)
)
hprIpMonitoringGroup.setObjects(
    ("HPR-IP-MIB", "hprIpActiveLsUdpPackets")
)
if mibBuilder.loadTexts:
    hprIpMonitoringGroup.setStatus("current")

hprIpConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 6)
)
hprIpConfigurationGroup.setObjects(
      *(("HPR-IP-MIB", "hprIpAppnPortTOSPrecedence"),
        ("HPR-IP-MIB", "hprIpLsTOSPrecedence"),
        ("HPR-IP-MIB", "hprIpLsRowStatus"),
        ("HPR-IP-MIB", "hprIpCnTOSPrecedence"),
        ("HPR-IP-MIB", "hprIpCnRowStatus"))
)
if mibBuilder.loadTexts:
    hprIpConfigurationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hprIpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 34, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hprIpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPR-IP-MIB",
    **{"AppnTrafficType": AppnTrafficType,
       "AppnTOSPrecedence": AppnTOSPrecedence,
       "hprIp": hprIp,
       "hprIpActiveLsTable": hprIpActiveLsTable,
       "hprIpActiveLsEntry": hprIpActiveLsEntry,
       "hprIpActiveLsLsName": hprIpActiveLsLsName,
       "hprIpActiveLsAppnTrafficType": hprIpActiveLsAppnTrafficType,
       "hprIpActiveLsUdpPackets": hprIpActiveLsUdpPackets,
       "hprIpAppnPortTable": hprIpAppnPortTable,
       "hprIpAppnPortEntry": hprIpAppnPortEntry,
       "hprIpAppnPortName": hprIpAppnPortName,
       "hprIpAppnPortAppnTrafficType": hprIpAppnPortAppnTrafficType,
       "hprIpAppnPortTOSPrecedence": hprIpAppnPortTOSPrecedence,
       "hprIpLsTable": hprIpLsTable,
       "hprIpLsEntry": hprIpLsEntry,
       "hprIpLsLsName": hprIpLsLsName,
       "hprIpLsAppnTrafficType": hprIpLsAppnTrafficType,
       "hprIpLsTOSPrecedence": hprIpLsTOSPrecedence,
       "hprIpLsRowStatus": hprIpLsRowStatus,
       "hprIpCnTable": hprIpCnTable,
       "hprIpCnEntry": hprIpCnEntry,
       "hprIpCnVrnName": hprIpCnVrnName,
       "hprIpCnAppnTrafficType": hprIpCnAppnTrafficType,
       "hprIpCnTOSPrecedence": hprIpCnTOSPrecedence,
       "hprIpCnRowStatus": hprIpCnRowStatus,
       "hprIpCompliance": hprIpCompliance,
       "hprIpMonitoringGroup": hprIpMonitoringGroup,
       "hprIpConfigurationGroup": hprIpConfigurationGroup}
)
