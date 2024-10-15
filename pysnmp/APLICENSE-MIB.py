# SNMP MIB module (APLICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APLICENSE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:03 2024
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

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

apLicenseModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5)
)
apLicenseModule.setRevisions(
        ("2012-07-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApLicenseMIBObjects_ObjectIdentity = ObjectIdentity
apLicenseMIBObjects = _ApLicenseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1)
)
_ApLicenseTable_Object = MibTable
apLicenseTable = _ApLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    apLicenseTable.setStatus("current")
_ApLicenseEntry_Object = MibTableRow
apLicenseEntry = _ApLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1)
)
apLicenseEntry.setIndexNames(
    (0, "APLICENSE-MIB", "apLicenseIndex"),
)
if mibBuilder.loadTexts:
    apLicenseEntry.setStatus("current")


class _ApLicenseIndex_Type(Integer32):
    """Custom type apLicenseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApLicenseIndex_Type.__name__ = "Integer32"
_ApLicenseIndex_Object = MibTableColumn
apLicenseIndex = _ApLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 1),
    _ApLicenseIndex_Type()
)
apLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apLicenseIndex.setStatus("current")


class _ApLicenseKey_Type(DisplayString):
    """Custom type apLicenseKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApLicenseKey_Type.__name__ = "DisplayString"
_ApLicenseKey_Object = MibTableColumn
apLicenseKey = _ApLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 2),
    _ApLicenseKey_Type()
)
apLicenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseKey.setStatus("current")
_ApLicenseCapacity_Type = Unsigned32
_ApLicenseCapacity_Object = MibTableColumn
apLicenseCapacity = _ApLicenseCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 3),
    _ApLicenseCapacity_Type()
)
apLicenseCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseCapacity.setStatus("current")


class _ApLicenseInstallDate_Type(DisplayString):
    """Custom type apLicenseInstallDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApLicenseInstallDate_Type.__name__ = "DisplayString"
_ApLicenseInstallDate_Object = MibTableColumn
apLicenseInstallDate = _ApLicenseInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 4),
    _ApLicenseInstallDate_Type()
)
apLicenseInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseInstallDate.setStatus("current")


class _ApLicenseBeginDate_Type(DisplayString):
    """Custom type apLicenseBeginDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApLicenseBeginDate_Type.__name__ = "DisplayString"
_ApLicenseBeginDate_Object = MibTableColumn
apLicenseBeginDate = _ApLicenseBeginDate_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 5),
    _ApLicenseBeginDate_Type()
)
apLicenseBeginDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseBeginDate.setStatus("current")


class _ApLicenseExpireDate_Type(DisplayString):
    """Custom type apLicenseExpireDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApLicenseExpireDate_Type.__name__ = "DisplayString"
_ApLicenseExpireDate_Object = MibTableColumn
apLicenseExpireDate = _ApLicenseExpireDate_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 6),
    _ApLicenseExpireDate_Type()
)
apLicenseExpireDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseExpireDate.setStatus("current")
_ApLicenseSIPFeature_Type = TruthValue
_ApLicenseSIPFeature_Object = MibTableColumn
apLicenseSIPFeature = _ApLicenseSIPFeature_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 7),
    _ApLicenseSIPFeature_Type()
)
apLicenseSIPFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseSIPFeature.setStatus("current")
_ApLicenseMGCPFeature_Type = TruthValue
_ApLicenseMGCPFeature_Object = MibTableColumn
apLicenseMGCPFeature = _ApLicenseMGCPFeature_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 8),
    _ApLicenseMGCPFeature_Type()
)
apLicenseMGCPFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseMGCPFeature.setStatus("current")
_ApLicenseH323Feature_Type = TruthValue
_ApLicenseH323Feature_Object = MibTableColumn
apLicenseH323Feature = _ApLicenseH323Feature_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 9),
    _ApLicenseH323Feature_Type()
)
apLicenseH323Feature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseH323Feature.setStatus("current")
_ApLicenseIWFFeature_Type = TruthValue
_ApLicenseIWFFeature_Object = MibTableColumn
apLicenseIWFFeature = _ApLicenseIWFFeature_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 10),
    _ApLicenseIWFFeature_Type()
)
apLicenseIWFFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseIWFFeature.setStatus("current")
_ApLicenseQOSFeature_Type = TruthValue
_ApLicenseQOSFeature_Object = MibTableColumn
apLicenseQOSFeature = _ApLicenseQOSFeature_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 11),
    _ApLicenseQOSFeature_Type()
)
apLicenseQOSFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseQOSFeature.setStatus("current")
_ApLicenseACPFeature_Type = TruthValue
_ApLicenseACPFeature_Object = MibTableColumn
apLicenseACPFeature = _ApLicenseACPFeature_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 12),
    _ApLicenseACPFeature_Type()
)
apLicenseACPFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseACPFeature.setStatus("current")
_ApLicenseLPFeature_Type = TruthValue
_ApLicenseLPFeature_Object = MibTableColumn
apLicenseLPFeature = _ApLicenseLPFeature_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 13),
    _ApLicenseLPFeature_Type()
)
apLicenseLPFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseLPFeature.setStatus("current")
_ApLicenseSAGFeature_Type = TruthValue
_ApLicenseSAGFeature_Object = MibTableColumn
apLicenseSAGFeature = _ApLicenseSAGFeature_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 14),
    _ApLicenseSAGFeature_Type()
)
apLicenseSAGFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseSAGFeature.setStatus("current")
_ApLicenseACCTFeature_Type = TruthValue
_ApLicenseACCTFeature_Object = MibTableColumn
apLicenseACCTFeature = _ApLicenseACCTFeature_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 15),
    _ApLicenseACCTFeature_Type()
)
apLicenseACCTFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseACCTFeature.setStatus("current")
_ApLicenseHAFeature_Type = TruthValue
_ApLicenseHAFeature_Object = MibTableColumn
apLicenseHAFeature = _ApLicenseHAFeature_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 16),
    _ApLicenseHAFeature_Type()
)
apLicenseHAFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseHAFeature.setStatus("current")
_ApLicensePACFeature_Type = TruthValue
_ApLicensePACFeature_Object = MibTableColumn
apLicensePACFeature = _ApLicensePACFeature_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 17),
    _ApLicensePACFeature_Type()
)
apLicensePACFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicensePACFeature.setStatus("current")
_ApLicenseIKEFeature_Type = TruthValue
_ApLicenseIKEFeature_Object = MibTableColumn
apLicenseIKEFeature = _ApLicenseIKEFeature_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 18),
    _ApLicenseIKEFeature_Type()
)
apLicenseIKEFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseIKEFeature.setStatus("current")
_ApLicenseIPsecTunCap_Type = Unsigned32
_ApLicenseIPsecTunCap_Object = MibTableColumn
apLicenseIPsecTunCap = _ApLicenseIPsecTunCap_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 19),
    _ApLicenseIPsecTunCap_Type()
)
apLicenseIPsecTunCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseIPsecTunCap.setStatus("current")
_ApLicenseAuthFeature_Type = TruthValue
_ApLicenseAuthFeature_Object = MibTableColumn
apLicenseAuthFeature = _ApLicenseAuthFeature_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 20),
    _ApLicenseAuthFeature_Type()
)
apLicenseAuthFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseAuthFeature.setStatus("current")
_ApLicenseDatabaseRegFeature_Type = TruthValue
_ApLicenseDatabaseRegFeature_Object = MibTableColumn
apLicenseDatabaseRegFeature = _ApLicenseDatabaseRegFeature_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 21),
    _ApLicenseDatabaseRegFeature_Type()
)
apLicenseDatabaseRegFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseDatabaseRegFeature.setStatus("current")
_ApLicenseDatabaseRegCap_Type = Unsigned32
_ApLicenseDatabaseRegCap_Object = MibTableColumn
apLicenseDatabaseRegCap = _ApLicenseDatabaseRegCap_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 22),
    _ApLicenseDatabaseRegCap_Type()
)
apLicenseDatabaseRegCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseDatabaseRegCap.setStatus("current")
_ApLicenseSLBEndpointCap_Type = Unsigned32
_ApLicenseSLBEndpointCap_Object = MibTableColumn
apLicenseSLBEndpointCap = _ApLicenseSLBEndpointCap_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 1, 1, 1, 23),
    _ApLicenseSLBEndpointCap_Type()
)
apLicenseSLBEndpointCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLicenseSLBEndpointCap.setStatus("current")
_ApLicenseNotificationObjects_ObjectIdentity = ObjectIdentity
apLicenseNotificationObjects = _ApLicenseNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 2)
)


class _ApLicenseExpirationWarningAcliIndex_Type(Integer32):
    """Custom type apLicenseExpirationWarningAcliIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApLicenseExpirationWarningAcliIndex_Type.__name__ = "Integer32"
_ApLicenseExpirationWarningAcliIndex_Object = MibScalar
apLicenseExpirationWarningAcliIndex = _ApLicenseExpirationWarningAcliIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 2, 1),
    _ApLicenseExpirationWarningAcliIndex_Type()
)
apLicenseExpirationWarningAcliIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apLicenseExpirationWarningAcliIndex.setStatus("current")


class _ApLicenseExpirationWarningSnmpIndex_Type(Integer32):
    """Custom type apLicenseExpirationWarningSnmpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApLicenseExpirationWarningSnmpIndex_Type.__name__ = "Integer32"
_ApLicenseExpirationWarningSnmpIndex_Object = MibScalar
apLicenseExpirationWarningSnmpIndex = _ApLicenseExpirationWarningSnmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 2, 2),
    _ApLicenseExpirationWarningSnmpIndex_Type()
)
apLicenseExpirationWarningSnmpIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apLicenseExpirationWarningSnmpIndex.setStatus("current")


class _ApLicenseExpirationWarningKey_Type(DisplayString):
    """Custom type apLicenseExpirationWarningKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApLicenseExpirationWarningKey_Type.__name__ = "DisplayString"
_ApLicenseExpirationWarningKey_Object = MibScalar
apLicenseExpirationWarningKey = _ApLicenseExpirationWarningKey_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 2, 3),
    _ApLicenseExpirationWarningKey_Type()
)
apLicenseExpirationWarningKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apLicenseExpirationWarningKey.setStatus("current")
_ApLicenseExpirationWarningDays_Type = Unsigned32
_ApLicenseExpirationWarningDays_Object = MibScalar
apLicenseExpirationWarningDays = _ApLicenseExpirationWarningDays_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 2, 4),
    _ApLicenseExpirationWarningDays_Type()
)
apLicenseExpirationWarningDays.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apLicenseExpirationWarningDays.setStatus("current")
_ApLicenseNotificationPrefix_ObjectIdentity = ObjectIdentity
apLicenseNotificationPrefix = _ApLicenseNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 3)
)
_ApLicenseNotifications_ObjectIdentity = ObjectIdentity
apLicenseNotifications = _ApLicenseNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 3, 0)
)
_ApLicenseConformance_ObjectIdentity = ObjectIdentity
apLicenseConformance = _ApLicenseConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 4)
)
_ApLicenseCompliances_ObjectIdentity = ObjectIdentity
apLicenseCompliances = _ApLicenseCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 4, 1)
)
_ApLicenseGroups_ObjectIdentity = ObjectIdentity
apLicenseGroups = _ApLicenseGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 4, 2)
)
_ApLicenseNotificationsGroups_ObjectIdentity = ObjectIdentity
apLicenseNotificationsGroups = _ApLicenseNotificationsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 4, 3)
)

# Managed Objects groups

apLicenseObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 4, 2, 1)
)
apLicenseObjectsGroup.setObjects(
      *(("APLICENSE-MIB", "apLicenseKey"),
        ("APLICENSE-MIB", "apLicenseCapacity"),
        ("APLICENSE-MIB", "apLicenseInstallDate"),
        ("APLICENSE-MIB", "apLicenseBeginDate"),
        ("APLICENSE-MIB", "apLicenseExpireDate"),
        ("APLICENSE-MIB", "apLicenseSIPFeature"),
        ("APLICENSE-MIB", "apLicenseMGCPFeature"),
        ("APLICENSE-MIB", "apLicenseH323Feature"),
        ("APLICENSE-MIB", "apLicenseIWFFeature"),
        ("APLICENSE-MIB", "apLicenseQOSFeature"),
        ("APLICENSE-MIB", "apLicenseACPFeature"),
        ("APLICENSE-MIB", "apLicenseLPFeature"),
        ("APLICENSE-MIB", "apLicenseSAGFeature"),
        ("APLICENSE-MIB", "apLicenseACCTFeature"),
        ("APLICENSE-MIB", "apLicenseHAFeature"),
        ("APLICENSE-MIB", "apLicensePACFeature"),
        ("APLICENSE-MIB", "apLicenseIKEFeature"),
        ("APLICENSE-MIB", "apLicenseIPsecTunCap"),
        ("APLICENSE-MIB", "apLicenseSLBEndpointCap"))
)
if mibBuilder.loadTexts:
    apLicenseObjectsGroup.setStatus("current")

apLicenseDatabaseRegGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 4, 2, 2)
)
apLicenseDatabaseRegGroup.setObjects(
      *(("APLICENSE-MIB", "apLicenseAuthFeature"),
        ("APLICENSE-MIB", "apLicenseDatabaseRegFeature"),
        ("APLICENSE-MIB", "apLicenseDatabaseRegCap"))
)
if mibBuilder.loadTexts:
    apLicenseDatabaseRegGroup.setStatus("current")


# Notification objects

apLicenseApproachingCapacityNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 3, 0, 1)
)
if mibBuilder.loadTexts:
    apLicenseApproachingCapacityNotification.setStatus(
        "current"
    )

apLicenseNotApproachingCapacityNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 3, 0, 2)
)
if mibBuilder.loadTexts:
    apLicenseNotApproachingCapacityNotification.setStatus(
        "current"
    )

apLicenseExpirationWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 3, 0, 3)
)
apLicenseExpirationWarningNotification.setObjects(
      *(("APLICENSE-MIB", "apLicenseExpirationWarningAcliIndex"),
        ("APLICENSE-MIB", "apLicenseExpirationWarningSnmpIndex"),
        ("APLICENSE-MIB", "apLicenseExpirationWarningKey"),
        ("APLICENSE-MIB", "apLicenseExpirationWarningDays"))
)
if mibBuilder.loadTexts:
    apLicenseExpirationWarningNotification.setStatus(
        "current"
    )


# Notifications groups

apLicenseNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 4, 3, 1)
)
apLicenseNotificationsGroup.setObjects(
      *(("APLICENSE-MIB", "apLicenseApproachingCapacityNotification"),
        ("APLICENSE-MIB", "apLicenseNotApproachingCapacityNotification"))
)
if mibBuilder.loadTexts:
    apLicenseNotificationsGroup.setStatus(
        "current"
    )

apLicenseExpirationNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 5, 4, 3, 2)
)
apLicenseExpirationNotificationsGroup.setObjects(
    ("APLICENSE-MIB", "apLicenseExpirationWarningNotification")
)
if mibBuilder.loadTexts:
    apLicenseExpirationNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APLICENSE-MIB",
    **{"apLicenseModule": apLicenseModule,
       "apLicenseMIBObjects": apLicenseMIBObjects,
       "apLicenseTable": apLicenseTable,
       "apLicenseEntry": apLicenseEntry,
       "apLicenseIndex": apLicenseIndex,
       "apLicenseKey": apLicenseKey,
       "apLicenseCapacity": apLicenseCapacity,
       "apLicenseInstallDate": apLicenseInstallDate,
       "apLicenseBeginDate": apLicenseBeginDate,
       "apLicenseExpireDate": apLicenseExpireDate,
       "apLicenseSIPFeature": apLicenseSIPFeature,
       "apLicenseMGCPFeature": apLicenseMGCPFeature,
       "apLicenseH323Feature": apLicenseH323Feature,
       "apLicenseIWFFeature": apLicenseIWFFeature,
       "apLicenseQOSFeature": apLicenseQOSFeature,
       "apLicenseACPFeature": apLicenseACPFeature,
       "apLicenseLPFeature": apLicenseLPFeature,
       "apLicenseSAGFeature": apLicenseSAGFeature,
       "apLicenseACCTFeature": apLicenseACCTFeature,
       "apLicenseHAFeature": apLicenseHAFeature,
       "apLicensePACFeature": apLicensePACFeature,
       "apLicenseIKEFeature": apLicenseIKEFeature,
       "apLicenseIPsecTunCap": apLicenseIPsecTunCap,
       "apLicenseAuthFeature": apLicenseAuthFeature,
       "apLicenseDatabaseRegFeature": apLicenseDatabaseRegFeature,
       "apLicenseDatabaseRegCap": apLicenseDatabaseRegCap,
       "apLicenseSLBEndpointCap": apLicenseSLBEndpointCap,
       "apLicenseNotificationObjects": apLicenseNotificationObjects,
       "apLicenseExpirationWarningAcliIndex": apLicenseExpirationWarningAcliIndex,
       "apLicenseExpirationWarningSnmpIndex": apLicenseExpirationWarningSnmpIndex,
       "apLicenseExpirationWarningKey": apLicenseExpirationWarningKey,
       "apLicenseExpirationWarningDays": apLicenseExpirationWarningDays,
       "apLicenseNotificationPrefix": apLicenseNotificationPrefix,
       "apLicenseNotifications": apLicenseNotifications,
       "apLicenseApproachingCapacityNotification": apLicenseApproachingCapacityNotification,
       "apLicenseNotApproachingCapacityNotification": apLicenseNotApproachingCapacityNotification,
       "apLicenseExpirationWarningNotification": apLicenseExpirationWarningNotification,
       "apLicenseConformance": apLicenseConformance,
       "apLicenseCompliances": apLicenseCompliances,
       "apLicenseGroups": apLicenseGroups,
       "apLicenseObjectsGroup": apLicenseObjectsGroup,
       "apLicenseDatabaseRegGroup": apLicenseDatabaseRegGroup,
       "apLicenseNotificationsGroups": apLicenseNotificationsGroups,
       "apLicenseNotificationsGroup": apLicenseNotificationsGroup,
       "apLicenseExpirationNotificationsGroup": apLicenseExpirationNotificationsGroup}
)
