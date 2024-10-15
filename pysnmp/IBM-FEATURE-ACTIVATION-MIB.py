# SNMP MIB module (IBM-FEATURE-ACTIVATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-FEATURE-ACTIVATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:29 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ibmFeatureActivationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 31)
)
ibmFeatureActivationMIB.setRevisions(
        ("2011-03-30 07:33",
         "2011-02-02 19:49",
         "2010-12-08 18:33")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmArchitecture_ObjectIdentity = ObjectIdentity
ibmArchitecture = _IbmArchitecture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5)
)
_IbmFodNotifications_ObjectIdentity = ObjectIdentity
ibmFodNotifications = _IbmFodNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 0)
)
_IbmFodObjects_ObjectIdentity = ObjectIdentity
ibmFodObjects = _IbmFodObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 1)
)


class _IbmFodAction_Type(Integer32):
    """Custom type ibmFodAction based on Integer32"""
    defaultValue = 4

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
        *(("exportActivationKey", 3),
          ("installActivationKey", 1),
          ("inventoryInstalledActivationKeys", 4),
          ("uninstallActivationKey", 2))
    )


_IbmFodAction_Type.__name__ = "Integer32"
_IbmFodAction_Object = MibScalar
ibmFodAction = _IbmFodAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 1, 1),
    _IbmFodAction_Type()
)
ibmFodAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmFodAction.setStatus("current")


class _IbmFodIndex_Type(Integer32):
    """Custom type ibmFodIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbmFodIndex_Type.__name__ = "Integer32"
_IbmFodIndex_Object = MibScalar
ibmFodIndex = _IbmFodIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 1, 2),
    _IbmFodIndex_Type()
)
ibmFodIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmFodIndex.setStatus("current")


class _IbmFodFileUri_Type(OctetString):
    """Custom type ibmFodFileUri based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_IbmFodFileUri_Type.__name__ = "OctetString"
_IbmFodFileUri_Object = MibScalar
ibmFodFileUri = _IbmFodFileUri_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 1, 3),
    _IbmFodFileUri_Type()
)
ibmFodFileUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmFodFileUri.setStatus("current")


class _IbmFodStatus_Type(Integer32):
    """Custom type ibmFodStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("actionIncompleteDeviceBusy", 14),
          ("communicationFailure", 7),
          ("corruptKeyFile", 4),
          ("fileAlreadyExists", 15),
          ("ftpServerFull", 9),
          ("invalidIndex", 11),
          ("invalideKeyFileTarget", 5),
          ("keyFileNotPresent", 6),
          ("keyStoreFull", 8),
          ("permissionProblem", 16),
          ("preRequisiteKeyActionRequired", 13),
          ("protocolNotSupported", 12),
          ("rebootRequired", 2),
          ("success", 1),
          ("userAuthenticationFailed", 10),
          ("versionMismatch", 3))
    )


_IbmFodStatus_Type.__name__ = "Integer32"
_IbmFodStatus_Object = MibScalar
ibmFodStatus = _IbmFodStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 1, 4),
    _IbmFodStatus_Type()
)
ibmFodStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmFodStatus.setStatus("current")
_IbmFodKeyChangeTime_Type = DateAndTime
_IbmFodKeyChangeTime_Object = MibScalar
ibmFodKeyChangeTime = _IbmFodKeyChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 1, 5),
    _IbmFodKeyChangeTime_Type()
)
ibmFodKeyChangeTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibmFodKeyChangeTime.setStatus("current")


class _IbmFodKeyOldStatus_Type(Integer32):
    """Custom type ibmFodKeyOldStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("keyExpired", 8),
          ("keyFeatureActive", 5),
          ("keyFeatureRequiresBMCReboot", 7),
          ("keyFeatureRequiresHostReboot", 6),
          ("keyInProcessOfValidation", 10),
          ("keyInvalid", 3),
          ("keyUseLimitExceeded", 9),
          ("keyValid", 2),
          ("keyValidElsewhere", 4),
          ("noPreviousStatus", 1))
    )


_IbmFodKeyOldStatus_Type.__name__ = "Integer32"
_IbmFodKeyOldStatus_Object = MibScalar
ibmFodKeyOldStatus = _IbmFodKeyOldStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 1, 6),
    _IbmFodKeyOldStatus_Type()
)
ibmFodKeyOldStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibmFodKeyOldStatus.setStatus("current")


class _IbmFodKeyNewStatus_Type(Integer32):
    """Custom type ibmFodKeyNewStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("keyExpired", 8),
          ("keyFeatureActive", 5),
          ("keyFeatureRequiresBMCReboot", 7),
          ("keyFeatureRequiresHostReboot", 6),
          ("keyInProcessOfValidation", 10),
          ("keyInvalid", 3),
          ("keyRemoved", 1),
          ("keyReplaced", 11),
          ("keyUseLimitExceeded", 9),
          ("keyValid", 2),
          ("keyValidElsewhere", 4))
    )


_IbmFodKeyNewStatus_Type.__name__ = "Integer32"
_IbmFodKeyNewStatus_Object = MibScalar
ibmFodKeyNewStatus = _IbmFodKeyNewStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 1, 7),
    _IbmFodKeyNewStatus_Type()
)
ibmFodKeyNewStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibmFodKeyNewStatus.setStatus("current")
_IbmFodKeyUpdateData_Type = DisplayString
_IbmFodKeyUpdateData_Object = MibScalar
ibmFodKeyUpdateData = _IbmFodKeyUpdateData_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 1, 8),
    _IbmFodKeyUpdateData_Type()
)
ibmFodKeyUpdateData.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ibmFodKeyUpdateData.setStatus("current")
_IbmFodConformance_ObjectIdentity = ObjectIdentity
ibmFodConformance = _IbmFodConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 2)
)
_IbmFeatureActivationCompliances_ObjectIdentity = ObjectIdentity
ibmFeatureActivationCompliances = _IbmFeatureActivationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 2, 1)
)
_IbmFeatureActivationGroups_ObjectIdentity = ObjectIdentity
ibmFeatureActivationGroups = _IbmFeatureActivationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 2, 2)
)

# Managed Objects groups

ibmFeatureActivationBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 2, 2, 1)
)
ibmFeatureActivationBaseGroup.setObjects(
      *(("IBM-FEATURE-ACTIVATION-MIB", "ibmFodAction"),
        ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodIndex"),
        ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodFileUri"),
        ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodStatus"),
        ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodKeyChangeTime"),
        ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodKeyOldStatus"),
        ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodKeyNewStatus"),
        ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodKeyUpdateData"))
)
if mibBuilder.loadTexts:
    ibmFeatureActivationBaseGroup.setStatus("current")


# Notification objects

ibmFodActivationChangeAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 0, 1)
)
ibmFodActivationChangeAlert.setObjects(
      *(("IBM-FEATURE-ACTIVATION-MIB", "ibmFodIndex"),
        ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodKeyChangeTime"),
        ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodKeyOldStatus"),
        ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodKeyNewStatus"),
        ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodKeyUpdateData"))
)
if mibBuilder.loadTexts:
    ibmFodActivationChangeAlert.setStatus(
        "current"
    )


# Notifications groups

ibmFeatureActivationNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 2, 2, 2)
)
ibmFeatureActivationNotifGroup.setObjects(
    ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodActivationChangeAlert")
)
if mibBuilder.loadTexts:
    ibmFeatureActivationNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ibmFeatureActivationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2, 5, 31, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ibmFeatureActivationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-FEATURE-ACTIVATION-MIB",
    **{"ibm": ibm,
       "ibmArchitecture": ibmArchitecture,
       "ibmFeatureActivationMIB": ibmFeatureActivationMIB,
       "ibmFodNotifications": ibmFodNotifications,
       "ibmFodActivationChangeAlert": ibmFodActivationChangeAlert,
       "ibmFodObjects": ibmFodObjects,
       "ibmFodAction": ibmFodAction,
       "ibmFodIndex": ibmFodIndex,
       "ibmFodFileUri": ibmFodFileUri,
       "ibmFodStatus": ibmFodStatus,
       "ibmFodKeyChangeTime": ibmFodKeyChangeTime,
       "ibmFodKeyOldStatus": ibmFodKeyOldStatus,
       "ibmFodKeyNewStatus": ibmFodKeyNewStatus,
       "ibmFodKeyUpdateData": ibmFodKeyUpdateData,
       "ibmFodConformance": ibmFodConformance,
       "ibmFeatureActivationCompliances": ibmFeatureActivationCompliances,
       "ibmFeatureActivationCompliance": ibmFeatureActivationCompliance,
       "ibmFeatureActivationGroups": ibmFeatureActivationGroups,
       "ibmFeatureActivationBaseGroup": ibmFeatureActivationBaseGroup,
       "ibmFeatureActivationNotifGroup": ibmFeatureActivationNotifGroup}
)
