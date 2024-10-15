# SNMP MIB module (QB-QOS-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QB-QOS-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:44 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(qbMibs,) = mibBuilder.importSymbols(
    "QUANTUMBRIDGE-REG",
    "qbMibs")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

qbQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class QbMbitRate(Integer32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_QbQosObjects_ObjectIdentity = ObjectIdentity
qbQosObjects = _QbQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 1)
)
_QbQosIfConfGroup_ObjectIdentity = ObjectIdentity
qbQosIfConfGroup = _QbQosIfConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 1)
)
_QbQosIfConfTableLastUpdate_Type = TimeTicks
_QbQosIfConfTableLastUpdate_Object = MibScalar
qbQosIfConfTableLastUpdate = _QbQosIfConfTableLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 1, 1),
    _QbQosIfConfTableLastUpdate_Type()
)
qbQosIfConfTableLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbQosIfConfTableLastUpdate.setStatus("current")
_QbQosIfConfTable_Object = MibTable
qbQosIfConfTable = _QbQosIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 1, 2)
)
if mibBuilder.loadTexts:
    qbQosIfConfTable.setStatus("current")
_QbQosIfConfEntry_Object = MibTableRow
qbQosIfConfEntry = _QbQosIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 1, 2, 1)
)
qbQosIfConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qbQosIfConfEntry.setStatus("current")


class _QbQosIfConfPolicingAdminStatus_Type(Integer32):
    """Custom type qbQosIfConfPolicingAdminStatus based on Integer32"""
    defaultValue = 2

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


_QbQosIfConfPolicingAdminStatus_Type.__name__ = "Integer32"
_QbQosIfConfPolicingAdminStatus_Object = MibTableColumn
qbQosIfConfPolicingAdminStatus = _QbQosIfConfPolicingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 1, 2, 1, 1),
    _QbQosIfConfPolicingAdminStatus_Type()
)
qbQosIfConfPolicingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbQosIfConfPolicingAdminStatus.setStatus("current")
_QbQosIfStatTable_Object = MibTable
qbQosIfStatTable = _QbQosIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 2)
)
if mibBuilder.loadTexts:
    qbQosIfStatTable.setStatus("current")
_QbQosIfStatEntry_Object = MibTableRow
qbQosIfStatEntry = _QbQosIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 2, 1)
)
qbQosIfStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qbQosIfStatEntry.setStatus("current")
_QbQosIfStatDiscPkts_Type = Counter32
_QbQosIfStatDiscPkts_Object = MibTableColumn
qbQosIfStatDiscPkts = _QbQosIfStatDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 2, 1, 1),
    _QbQosIfStatDiscPkts_Type()
)
qbQosIfStatDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbQosIfStatDiscPkts.setStatus("current")
_QbQosIfStatUpThreshDiscPkts_Type = Counter32
_QbQosIfStatUpThreshDiscPkts_Object = MibTableColumn
qbQosIfStatUpThreshDiscPkts = _QbQosIfStatUpThreshDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 2, 1, 2),
    _QbQosIfStatUpThreshDiscPkts_Type()
)
qbQosIfStatUpThreshDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbQosIfStatUpThreshDiscPkts.setStatus("current")
_QbQosIfStatDownThreshDiscPkts_Type = Counter32
_QbQosIfStatDownThreshDiscPkts_Object = MibTableColumn
qbQosIfStatDownThreshDiscPkts = _QbQosIfStatDownThreshDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 2, 1, 3),
    _QbQosIfStatDownThreshDiscPkts_Type()
)
qbQosIfStatDownThreshDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbQosIfStatDownThreshDiscPkts.setStatus("current")
_QbQosNotifications_ObjectIdentity = ObjectIdentity
qbQosNotifications = _QbQosNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 2)
)
_QbQosNotificationPrefix_ObjectIdentity = ObjectIdentity
qbQosNotificationPrefix = _QbQosNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 2, 0)
)
_QbQosConformance_ObjectIdentity = ObjectIdentity
qbQosConformance = _QbQosConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 3)
)
_QbQosCompliances_ObjectIdentity = ObjectIdentity
qbQosCompliances = _QbQosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 3, 1)
)
_QbQosGroups_ObjectIdentity = ObjectIdentity
qbQosGroups = _QbQosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 3, 2)
)

# Managed Objects groups

qbQosGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 3, 2, 1)
)
qbQosGroupInfo.setObjects(
      *(("QB-QOS-MGMT-MIB", "qbQosIfConfPolicingAdminStatus"),
        ("QB-QOS-MGMT-MIB", "qbQosIfStatDiscPkts"),
        ("QB-QOS-MGMT-MIB", "qbQosIfStatUpThreshDiscPkts"),
        ("QB-QOS-MGMT-MIB", "qbQosIfStatDownThreshDiscPkts"))
)
if mibBuilder.loadTexts:
    qbQosGroupInfo.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qbQosCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4323, 2, 14, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qbQosCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QB-QOS-MGMT-MIB",
    **{"QbMbitRate": QbMbitRate,
       "qbQosMIB": qbQosMIB,
       "qbQosObjects": qbQosObjects,
       "qbQosIfConfGroup": qbQosIfConfGroup,
       "qbQosIfConfTableLastUpdate": qbQosIfConfTableLastUpdate,
       "qbQosIfConfTable": qbQosIfConfTable,
       "qbQosIfConfEntry": qbQosIfConfEntry,
       "qbQosIfConfPolicingAdminStatus": qbQosIfConfPolicingAdminStatus,
       "qbQosIfStatTable": qbQosIfStatTable,
       "qbQosIfStatEntry": qbQosIfStatEntry,
       "qbQosIfStatDiscPkts": qbQosIfStatDiscPkts,
       "qbQosIfStatUpThreshDiscPkts": qbQosIfStatUpThreshDiscPkts,
       "qbQosIfStatDownThreshDiscPkts": qbQosIfStatDownThreshDiscPkts,
       "qbQosNotifications": qbQosNotifications,
       "qbQosNotificationPrefix": qbQosNotificationPrefix,
       "qbQosConformance": qbQosConformance,
       "qbQosCompliances": qbQosCompliances,
       "qbQosCompliance": qbQosCompliance,
       "qbQosGroups": qbQosGroups,
       "qbQosGroupInfo": qbQosGroupInfo}
)
