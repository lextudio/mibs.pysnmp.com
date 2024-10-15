# SNMP MIB module (CISCO-EPM-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-EPM-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:49 2024
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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoEpmNotificationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 311)
)
ciscoEpmNotificationMIB.setRevisions(
        ("2004-06-07 00:00",
         "2003-08-21 00:00",
         "2002-07-28 14:20")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoEpmNotificationMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoEpmNotificationMIBNotifs = _CiscoEpmNotificationMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 0)
)
_CiscoEpmNotificationMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEpmNotificationMIBObjects = _CiscoEpmNotificationMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1)
)
_CenAlarmData_ObjectIdentity = ObjectIdentity
cenAlarmData = _CenAlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1)
)


class _CenAlarmTableMaxLength_Type(Unsigned32):
    """Custom type cenAlarmTableMaxLength based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CenAlarmTableMaxLength_Type.__name__ = "Unsigned32"
_CenAlarmTableMaxLength_Object = MibScalar
cenAlarmTableMaxLength = _CenAlarmTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 1),
    _CenAlarmTableMaxLength_Type()
)
cenAlarmTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cenAlarmTableMaxLength.setStatus("current")
_CenAlarmTable_Object = MibTable
cenAlarmTable = _CenAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cenAlarmTable.setStatus("current")
_CenAlarmEntry_Object = MibTableRow
cenAlarmEntry = _CenAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1)
)
cenAlarmEntry.setIndexNames(
    (0, "CISCO-EPM-NOTIFICATION-MIB", "cenAlarmIndex"),
)
if mibBuilder.loadTexts:
    cenAlarmEntry.setStatus("current")


class _CenAlarmIndex_Type(Unsigned32):
    """Custom type cenAlarmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CenAlarmIndex_Type.__name__ = "Unsigned32"
_CenAlarmIndex_Object = MibTableColumn
cenAlarmIndex = _CenAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 1),
    _CenAlarmIndex_Type()
)
cenAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cenAlarmIndex.setStatus("current")


class _CenAlarmVersion_Type(SnmpAdminString):
    """Custom type cenAlarmVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CenAlarmVersion_Type.__name__ = "SnmpAdminString"
_CenAlarmVersion_Object = MibTableColumn
cenAlarmVersion = _CenAlarmVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 2),
    _CenAlarmVersion_Type()
)
cenAlarmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmVersion.setStatus("current")
_CenAlarmTimestamp_Type = TimeStamp
_CenAlarmTimestamp_Object = MibTableColumn
cenAlarmTimestamp = _CenAlarmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 3),
    _CenAlarmTimestamp_Type()
)
cenAlarmTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmTimestamp.setStatus("current")
_CenAlarmUpdatedTimestamp_Type = TimeStamp
_CenAlarmUpdatedTimestamp_Object = MibTableColumn
cenAlarmUpdatedTimestamp = _CenAlarmUpdatedTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 4),
    _CenAlarmUpdatedTimestamp_Type()
)
cenAlarmUpdatedTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmUpdatedTimestamp.setStatus("current")


class _CenAlarmInstanceID_Type(SnmpAdminString):
    """Custom type cenAlarmInstanceID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CenAlarmInstanceID_Type.__name__ = "SnmpAdminString"
_CenAlarmInstanceID_Object = MibTableColumn
cenAlarmInstanceID = _CenAlarmInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 5),
    _CenAlarmInstanceID_Type()
)
cenAlarmInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmInstanceID.setStatus("current")


class _CenAlarmStatus_Type(Integer32):
    """Custom type cenAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_CenAlarmStatus_Type.__name__ = "Integer32"
_CenAlarmStatus_Object = MibTableColumn
cenAlarmStatus = _CenAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 6),
    _CenAlarmStatus_Type()
)
cenAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmStatus.setStatus("current")


class _CenAlarmStatusDefinition_Type(SnmpAdminString):
    """Custom type cenAlarmStatusDefinition based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CenAlarmStatusDefinition_Type.__name__ = "SnmpAdminString"
_CenAlarmStatusDefinition_Object = MibTableColumn
cenAlarmStatusDefinition = _CenAlarmStatusDefinition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 7),
    _CenAlarmStatusDefinition_Type()
)
cenAlarmStatusDefinition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmStatusDefinition.setStatus("current")


class _CenAlarmType_Type(Integer32):
    """Custom type cenAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("direct", 2),
          ("indirect", 3),
          ("mixed", 4),
          ("unknown", 1))
    )


_CenAlarmType_Type.__name__ = "Integer32"
_CenAlarmType_Object = MibTableColumn
cenAlarmType = _CenAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 8),
    _CenAlarmType_Type()
)
cenAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmType.setStatus("current")


class _CenAlarmCategory_Type(Integer32):
    """Custom type cenAlarmCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_CenAlarmCategory_Type.__name__ = "Integer32"
_CenAlarmCategory_Object = MibTableColumn
cenAlarmCategory = _CenAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 9),
    _CenAlarmCategory_Type()
)
cenAlarmCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmCategory.setStatus("current")


class _CenAlarmCategoryDefinition_Type(SnmpAdminString):
    """Custom type cenAlarmCategoryDefinition based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CenAlarmCategoryDefinition_Type.__name__ = "SnmpAdminString"
_CenAlarmCategoryDefinition_Object = MibTableColumn
cenAlarmCategoryDefinition = _CenAlarmCategoryDefinition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 10),
    _CenAlarmCategoryDefinition_Type()
)
cenAlarmCategoryDefinition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmCategoryDefinition.setStatus("current")
_CenAlarmServerAddressType_Type = InetAddressType
_CenAlarmServerAddressType_Object = MibTableColumn
cenAlarmServerAddressType = _CenAlarmServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 11),
    _CenAlarmServerAddressType_Type()
)
cenAlarmServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmServerAddressType.setStatus("current")
_CenAlarmServerAddress_Type = InetAddress
_CenAlarmServerAddress_Object = MibTableColumn
cenAlarmServerAddress = _CenAlarmServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 12),
    _CenAlarmServerAddress_Type()
)
cenAlarmServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmServerAddress.setStatus("current")


class _CenAlarmManagedObjectClass_Type(SnmpAdminString):
    """Custom type cenAlarmManagedObjectClass based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CenAlarmManagedObjectClass_Type.__name__ = "SnmpAdminString"
_CenAlarmManagedObjectClass_Object = MibTableColumn
cenAlarmManagedObjectClass = _CenAlarmManagedObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 13),
    _CenAlarmManagedObjectClass_Type()
)
cenAlarmManagedObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmManagedObjectClass.setStatus("current")
_CenAlarmManagedObjectAddressType_Type = InetAddressType
_CenAlarmManagedObjectAddressType_Object = MibTableColumn
cenAlarmManagedObjectAddressType = _CenAlarmManagedObjectAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 14),
    _CenAlarmManagedObjectAddressType_Type()
)
cenAlarmManagedObjectAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmManagedObjectAddressType.setStatus("current")
_CenAlarmManagedObjectAddress_Type = InetAddress
_CenAlarmManagedObjectAddress_Object = MibTableColumn
cenAlarmManagedObjectAddress = _CenAlarmManagedObjectAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 15),
    _CenAlarmManagedObjectAddress_Type()
)
cenAlarmManagedObjectAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmManagedObjectAddress.setStatus("current")


class _CenAlarmDescription_Type(OctetString):
    """Custom type cenAlarmDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_CenAlarmDescription_Type.__name__ = "OctetString"
_CenAlarmDescription_Object = MibTableColumn
cenAlarmDescription = _CenAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 16),
    _CenAlarmDescription_Type()
)
cenAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmDescription.setStatus("current")


class _CenAlarmSeverity_Type(Integer32):
    """Custom type cenAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CenAlarmSeverity_Type.__name__ = "Integer32"
_CenAlarmSeverity_Object = MibTableColumn
cenAlarmSeverity = _CenAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 17),
    _CenAlarmSeverity_Type()
)
cenAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmSeverity.setStatus("current")


class _CenAlarmSeverityDefinition_Type(SnmpAdminString):
    """Custom type cenAlarmSeverityDefinition based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CenAlarmSeverityDefinition_Type.__name__ = "SnmpAdminString"
_CenAlarmSeverityDefinition_Object = MibTableColumn
cenAlarmSeverityDefinition = _CenAlarmSeverityDefinition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 18),
    _CenAlarmSeverityDefinition_Type()
)
cenAlarmSeverityDefinition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmSeverityDefinition.setStatus("current")


class _CenAlarmTriageValue_Type(Integer32):
    """Custom type cenAlarmTriageValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CenAlarmTriageValue_Type.__name__ = "Integer32"
_CenAlarmTriageValue_Object = MibTableColumn
cenAlarmTriageValue = _CenAlarmTriageValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 19),
    _CenAlarmTriageValue_Type()
)
cenAlarmTriageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmTriageValue.setStatus("current")


class _CenEventIDList_Type(OctetString):
    """Custom type cenEventIDList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_CenEventIDList_Type.__name__ = "OctetString"
_CenEventIDList_Object = MibTableColumn
cenEventIDList = _CenEventIDList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 20),
    _CenEventIDList_Type()
)
cenEventIDList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenEventIDList.setStatus("current")


class _CenUserMessage1_Type(SnmpAdminString):
    """Custom type cenUserMessage1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CenUserMessage1_Type.__name__ = "SnmpAdminString"
_CenUserMessage1_Object = MibTableColumn
cenUserMessage1 = _CenUserMessage1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 21),
    _CenUserMessage1_Type()
)
cenUserMessage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenUserMessage1.setStatus("current")


class _CenUserMessage2_Type(SnmpAdminString):
    """Custom type cenUserMessage2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CenUserMessage2_Type.__name__ = "SnmpAdminString"
_CenUserMessage2_Object = MibTableColumn
cenUserMessage2 = _CenUserMessage2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 22),
    _CenUserMessage2_Type()
)
cenUserMessage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenUserMessage2.setStatus("current")


class _CenUserMessage3_Type(SnmpAdminString):
    """Custom type cenUserMessage3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CenUserMessage3_Type.__name__ = "SnmpAdminString"
_CenUserMessage3_Object = MibTableColumn
cenUserMessage3 = _CenUserMessage3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 23),
    _CenUserMessage3_Type()
)
cenUserMessage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenUserMessage3.setStatus("current")


class _CenAlarmMode_Type(Integer32):
    """Custom type cenAlarmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("event", 3),
          ("unknown", 1))
    )


_CenAlarmMode_Type.__name__ = "Integer32"
_CenAlarmMode_Object = MibTableColumn
cenAlarmMode = _CenAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 24),
    _CenAlarmMode_Type()
)
cenAlarmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlarmMode.setStatus("current")


class _CenPartitionNumber_Type(Unsigned32):
    """Custom type cenPartitionNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CenPartitionNumber_Type.__name__ = "Unsigned32"
_CenPartitionNumber_Object = MibTableColumn
cenPartitionNumber = _CenPartitionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 25),
    _CenPartitionNumber_Type()
)
cenPartitionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenPartitionNumber.setStatus("current")


class _CenPartitionName_Type(SnmpAdminString):
    """Custom type cenPartitionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CenPartitionName_Type.__name__ = "SnmpAdminString"
_CenPartitionName_Object = MibTableColumn
cenPartitionName = _CenPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 26),
    _CenPartitionName_Type()
)
cenPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenPartitionName.setStatus("current")


class _CenCustomerIdentification_Type(SnmpAdminString):
    """Custom type cenCustomerIdentification based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CenCustomerIdentification_Type.__name__ = "SnmpAdminString"
_CenCustomerIdentification_Object = MibTableColumn
cenCustomerIdentification = _CenCustomerIdentification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 27),
    _CenCustomerIdentification_Type()
)
cenCustomerIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenCustomerIdentification.setStatus("current")


class _CenCustomerRevision_Type(SnmpAdminString):
    """Custom type cenCustomerRevision based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CenCustomerRevision_Type.__name__ = "SnmpAdminString"
_CenCustomerRevision_Object = MibTableColumn
cenCustomerRevision = _CenCustomerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 28),
    _CenCustomerRevision_Type()
)
cenCustomerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenCustomerRevision.setStatus("current")


class _CenAlertID_Type(SnmpAdminString):
    """Custom type cenAlertID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CenAlertID_Type.__name__ = "SnmpAdminString"
_CenAlertID_Object = MibTableColumn
cenAlertID = _CenAlertID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 1, 1, 2, 1, 29),
    _CenAlertID_Type()
)
cenAlertID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cenAlertID.setStatus("current")
_CiscoEpmNotificationMIBConform_ObjectIdentity = ObjectIdentity
ciscoEpmNotificationMIBConform = _CiscoEpmNotificationMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 2)
)
_CiscoEpmNotificationMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEpmNotificationMIBCompliances = _CiscoEpmNotificationMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 2, 1)
)
_CiscoEpmNotificationMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEpmNotificationMIBGroups = _CiscoEpmNotificationMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 2, 2)
)

# Managed Objects groups

ciscoEpmNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 2, 2, 2)
)
ciscoEpmNotificationObjectsGroup.setObjects(
      *(("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmVersion"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmTimestamp"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmUpdatedTimestamp"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmInstanceID"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmStatus"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmStatusDefinition"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmType"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmCategory"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmCategoryDefinition"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmServerAddressType"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmServerAddress"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmManagedObjectClass"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmManagedObjectAddressType"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmManagedObjectAddress"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmDescription"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmSeverity"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmSeverityDefinition"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmTriageValue"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenEventIDList"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenUserMessage1"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenUserMessage2"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenUserMessage3"))
)
if mibBuilder.loadTexts:
    ciscoEpmNotificationObjectsGroup.setStatus("deprecated")

ciscoEpmAlarmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 2, 2, 3)
)
ciscoEpmAlarmConfigGroup.setObjects(
    ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmTableMaxLength")
)
if mibBuilder.loadTexts:
    ciscoEpmAlarmConfigGroup.setStatus("current")

ciscoEpmNotificationObjectsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 2, 2, 5)
)
ciscoEpmNotificationObjectsGroupRev1.setObjects(
      *(("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmVersion"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmTimestamp"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmUpdatedTimestamp"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmInstanceID"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmStatus"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmStatusDefinition"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmType"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmCategory"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmCategoryDefinition"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmServerAddressType"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmServerAddress"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmManagedObjectClass"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmManagedObjectAddressType"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmManagedObjectAddress"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmDescription"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmSeverity"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmSeverityDefinition"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmTriageValue"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenEventIDList"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenUserMessage1"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenUserMessage2"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenUserMessage3"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmMode"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenPartitionNumber"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenPartitionName"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenCustomerIdentification"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenCustomerRevision"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlertID"))
)
if mibBuilder.loadTexts:
    ciscoEpmNotificationObjectsGroupRev1.setStatus("current")


# Notification objects

ciscoEpmNotificationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 0, 1)
)
ciscoEpmNotificationAlarm.setObjects(
      *(("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmVersion"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmTimestamp"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmUpdatedTimestamp"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmInstanceID"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmStatus"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmStatusDefinition"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmType"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmCategory"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmCategoryDefinition"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmServerAddressType"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmServerAddress"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmManagedObjectClass"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmManagedObjectAddressType"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmManagedObjectAddress"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmDescription"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmSeverity"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmSeverityDefinition"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmTriageValue"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenEventIDList"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenUserMessage1"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenUserMessage2"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenUserMessage3"))
)
if mibBuilder.loadTexts:
    ciscoEpmNotificationAlarm.setStatus(
        "deprecated"
    )

ciscoEpmNotificationAlarmRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 0, 2)
)
ciscoEpmNotificationAlarmRev1.setObjects(
      *(("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmVersion"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmTimestamp"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmUpdatedTimestamp"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmInstanceID"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmStatus"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmStatusDefinition"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmType"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmCategory"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmCategoryDefinition"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmServerAddressType"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmServerAddress"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmManagedObjectClass"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmManagedObjectAddressType"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmManagedObjectAddress"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmDescription"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmSeverity"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmSeverityDefinition"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmTriageValue"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenEventIDList"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenUserMessage1"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenUserMessage2"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenUserMessage3"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlarmMode"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenPartitionNumber"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenPartitionName"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenCustomerIdentification"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenCustomerRevision"),
        ("CISCO-EPM-NOTIFICATION-MIB", "cenAlertID"))
)
if mibBuilder.loadTexts:
    ciscoEpmNotificationAlarmRev1.setStatus(
        "current"
    )


# Notifications groups

ciscoEpmNotificationAlarmGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 2, 2, 1)
)
ciscoEpmNotificationAlarmGroup.setObjects(
    ("CISCO-EPM-NOTIFICATION-MIB", "ciscoEpmNotificationAlarm")
)
if mibBuilder.loadTexts:
    ciscoEpmNotificationAlarmGroup.setStatus(
        "deprecated"
    )

ciscoEpmNotificationAlarmGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 2, 2, 4)
)
ciscoEpmNotificationAlarmGroupRev1.setObjects(
    ("CISCO-EPM-NOTIFICATION-MIB", "ciscoEpmNotificationAlarmRev1")
)
if mibBuilder.loadTexts:
    ciscoEpmNotificationAlarmGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoEpmNotificationMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEpmNotificationMIBCompliance.setStatus(
        "deprecated"
    )

ciscoEpmNotificationMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 311, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoEpmNotificationMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-EPM-NOTIFICATION-MIB",
    **{"ciscoEpmNotificationMIB": ciscoEpmNotificationMIB,
       "ciscoEpmNotificationMIBNotifs": ciscoEpmNotificationMIBNotifs,
       "ciscoEpmNotificationAlarm": ciscoEpmNotificationAlarm,
       "ciscoEpmNotificationAlarmRev1": ciscoEpmNotificationAlarmRev1,
       "ciscoEpmNotificationMIBObjects": ciscoEpmNotificationMIBObjects,
       "cenAlarmData": cenAlarmData,
       "cenAlarmTableMaxLength": cenAlarmTableMaxLength,
       "cenAlarmTable": cenAlarmTable,
       "cenAlarmEntry": cenAlarmEntry,
       "cenAlarmIndex": cenAlarmIndex,
       "cenAlarmVersion": cenAlarmVersion,
       "cenAlarmTimestamp": cenAlarmTimestamp,
       "cenAlarmUpdatedTimestamp": cenAlarmUpdatedTimestamp,
       "cenAlarmInstanceID": cenAlarmInstanceID,
       "cenAlarmStatus": cenAlarmStatus,
       "cenAlarmStatusDefinition": cenAlarmStatusDefinition,
       "cenAlarmType": cenAlarmType,
       "cenAlarmCategory": cenAlarmCategory,
       "cenAlarmCategoryDefinition": cenAlarmCategoryDefinition,
       "cenAlarmServerAddressType": cenAlarmServerAddressType,
       "cenAlarmServerAddress": cenAlarmServerAddress,
       "cenAlarmManagedObjectClass": cenAlarmManagedObjectClass,
       "cenAlarmManagedObjectAddressType": cenAlarmManagedObjectAddressType,
       "cenAlarmManagedObjectAddress": cenAlarmManagedObjectAddress,
       "cenAlarmDescription": cenAlarmDescription,
       "cenAlarmSeverity": cenAlarmSeverity,
       "cenAlarmSeverityDefinition": cenAlarmSeverityDefinition,
       "cenAlarmTriageValue": cenAlarmTriageValue,
       "cenEventIDList": cenEventIDList,
       "cenUserMessage1": cenUserMessage1,
       "cenUserMessage2": cenUserMessage2,
       "cenUserMessage3": cenUserMessage3,
       "cenAlarmMode": cenAlarmMode,
       "cenPartitionNumber": cenPartitionNumber,
       "cenPartitionName": cenPartitionName,
       "cenCustomerIdentification": cenCustomerIdentification,
       "cenCustomerRevision": cenCustomerRevision,
       "cenAlertID": cenAlertID,
       "ciscoEpmNotificationMIBConform": ciscoEpmNotificationMIBConform,
       "ciscoEpmNotificationMIBCompliances": ciscoEpmNotificationMIBCompliances,
       "ciscoEpmNotificationMIBCompliance": ciscoEpmNotificationMIBCompliance,
       "ciscoEpmNotificationMIBComplianceRev1": ciscoEpmNotificationMIBComplianceRev1,
       "ciscoEpmNotificationMIBGroups": ciscoEpmNotificationMIBGroups,
       "ciscoEpmNotificationAlarmGroup": ciscoEpmNotificationAlarmGroup,
       "ciscoEpmNotificationObjectsGroup": ciscoEpmNotificationObjectsGroup,
       "ciscoEpmAlarmConfigGroup": ciscoEpmAlarmConfigGroup,
       "ciscoEpmNotificationAlarmGroupRev1": ciscoEpmNotificationAlarmGroupRev1,
       "ciscoEpmNotificationObjectsGroupRev1": ciscoEpmNotificationObjectsGroupRev1}
)
