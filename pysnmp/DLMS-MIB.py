# SNMP MIB module (DLMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:38 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

swDlmsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 101)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwDlmsNotifications_ObjectIdentity = ObjectIdentity
swDlmsNotifications = _SwDlmsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 0)
)
_SwDlmsObjects_ObjectIdentity = ObjectIdentity
swDlmsObjects = _SwDlmsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1)
)
_SwDlmsGeneralGroup_ObjectIdentity = ObjectIdentity
swDlmsGeneralGroup = _SwDlmsGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 1)
)


class _SwDlmsInstallAc_Type(OctetString):
    """Custom type swDlmsInstallAc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_SwDlmsInstallAc_Type.__name__ = "OctetString"
_SwDlmsInstallAc_Object = MibScalar
swDlmsInstallAc = _SwDlmsInstallAc_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 1, 1),
    _SwDlmsInstallAc_Type()
)
swDlmsInstallAc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDlmsInstallAc.setStatus("current")


class _SwDlmsInstallStackUnitId_Type(Integer32):
    """Custom type swDlmsInstallStackUnitId based on Integer32"""
    defaultValue = 0


_SwDlmsInstallStackUnitId_Object = MibScalar
swDlmsInstallStackUnitId = _SwDlmsInstallStackUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 1, 2),
    _SwDlmsInstallStackUnitId_Type()
)
swDlmsInstallStackUnitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDlmsInstallStackUnitId.setStatus("current")
_SwDlmsLicense_ObjectIdentity = ObjectIdentity
swDlmsLicense = _SwDlmsLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2)
)
_SwDlmsLicenseModelTable_Object = MibTable
swDlmsLicenseModelTable = _SwDlmsLicenseModelTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2, 1)
)
if mibBuilder.loadTexts:
    swDlmsLicenseModelTable.setStatus("current")
_SwDlmsLicenseModelEntry_Object = MibTableRow
swDlmsLicenseModelEntry = _SwDlmsLicenseModelEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2, 1, 1)
)
swDlmsLicenseModelEntry.setIndexNames(
    (0, "DLMS-MIB", "swDlmsLicenseModelName"),
)
if mibBuilder.loadTexts:
    swDlmsLicenseModelEntry.setStatus("current")
_SwDlmsLicenseModelName_Type = DisplayString
_SwDlmsLicenseModelName_Object = MibTableColumn
swDlmsLicenseModelName = _SwDlmsLicenseModelName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2, 1, 1, 1),
    _SwDlmsLicenseModelName_Type()
)
swDlmsLicenseModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDlmsLicenseModelName.setStatus("current")
_SwDlmsLicenseModelRemaining_Type = DisplayString
_SwDlmsLicenseModelRemaining_Object = MibTableColumn
swDlmsLicenseModelRemaining = _SwDlmsLicenseModelRemaining_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2, 1, 1, 2),
    _SwDlmsLicenseModelRemaining_Type()
)
swDlmsLicenseModelRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDlmsLicenseModelRemaining.setStatus("current")
_SwDlmsLicenseAcTable_Object = MibTable
swDlmsLicenseAcTable = _SwDlmsLicenseAcTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2, 2)
)
if mibBuilder.loadTexts:
    swDlmsLicenseAcTable.setStatus("current")
_SwDlmsLicenseAcEntry_Object = MibTableRow
swDlmsLicenseAcEntry = _SwDlmsLicenseAcEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2, 2, 1)
)
swDlmsLicenseAcEntry.setIndexNames(
    (0, "DLMS-MIB", "swDlmsLicenseModelName"),
    (0, "DLMS-MIB", "swDlmsLicenseAc"),
)
if mibBuilder.loadTexts:
    swDlmsLicenseAcEntry.setStatus("current")
_SwDlmsLicenseAc_Type = OctetString
_SwDlmsLicenseAc_Object = MibTableColumn
swDlmsLicenseAc = _SwDlmsLicenseAc_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2, 2, 1, 1),
    _SwDlmsLicenseAc_Type()
)
swDlmsLicenseAc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDlmsLicenseAc.setStatus("current")


class _SwDlmsLicenseAcStatus_Type(Integer32):
    """Custom type swDlmsLicenseAcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("expired", 2))
    )


_SwDlmsLicenseAcStatus_Type.__name__ = "Integer32"
_SwDlmsLicenseAcStatus_Object = MibTableColumn
swDlmsLicenseAcStatus = _SwDlmsLicenseAcStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2, 2, 1, 2),
    _SwDlmsLicenseAcStatus_Type()
)
swDlmsLicenseAcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDlmsLicenseAcStatus.setStatus("current")
_SwDlmsStackLicense_ObjectIdentity = ObjectIdentity
swDlmsStackLicense = _SwDlmsStackLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3)
)
_SwDlmsStackLicenseModelTable_Object = MibTable
swDlmsStackLicenseModelTable = _SwDlmsStackLicenseModelTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 1)
)
if mibBuilder.loadTexts:
    swDlmsStackLicenseModelTable.setStatus("current")
_SwDlmsStackLicenseModelEntry_Object = MibTableRow
swDlmsStackLicenseModelEntry = _SwDlmsStackLicenseModelEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 1, 1)
)
swDlmsStackLicenseModelEntry.setIndexNames(
    (0, "DLMS-MIB", "swDlmsStackLicenseModelUnitId"),
    (0, "DLMS-MIB", "swDlmsStackLicenseModelName"),
)
if mibBuilder.loadTexts:
    swDlmsStackLicenseModelEntry.setStatus("current")
_SwDlmsStackLicenseModelUnitId_Type = Integer32
_SwDlmsStackLicenseModelUnitId_Object = MibTableColumn
swDlmsStackLicenseModelUnitId = _SwDlmsStackLicenseModelUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 1, 1, 1),
    _SwDlmsStackLicenseModelUnitId_Type()
)
swDlmsStackLicenseModelUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDlmsStackLicenseModelUnitId.setStatus("current")
_SwDlmsStackLicenseModelName_Type = DisplayString
_SwDlmsStackLicenseModelName_Object = MibTableColumn
swDlmsStackLicenseModelName = _SwDlmsStackLicenseModelName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 1, 1, 2),
    _SwDlmsStackLicenseModelName_Type()
)
swDlmsStackLicenseModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDlmsStackLicenseModelName.setStatus("current")
_SwDlmsStackLicenseModelRemaining_Type = DisplayString
_SwDlmsStackLicenseModelRemaining_Object = MibTableColumn
swDlmsStackLicenseModelRemaining = _SwDlmsStackLicenseModelRemaining_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 1, 1, 3),
    _SwDlmsStackLicenseModelRemaining_Type()
)
swDlmsStackLicenseModelRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDlmsStackLicenseModelRemaining.setStatus("current")
_SwDlmsStackLicenseAcTable_Object = MibTable
swDlmsStackLicenseAcTable = _SwDlmsStackLicenseAcTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 2)
)
if mibBuilder.loadTexts:
    swDlmsStackLicenseAcTable.setStatus("current")
_SwDlmsStackLicenseAcEntry_Object = MibTableRow
swDlmsStackLicenseAcEntry = _SwDlmsStackLicenseAcEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 2, 1)
)
swDlmsStackLicenseAcEntry.setIndexNames(
    (0, "DLMS-MIB", "swDlmsStackLicenseModelUnitId"),
    (0, "DLMS-MIB", "swDlmsStackLicenseModelName"),
    (0, "DLMS-MIB", "swDlmsStackLicenseAc"),
)
if mibBuilder.loadTexts:
    swDlmsStackLicenseAcEntry.setStatus("current")
_SwDlmsStackLicenseAc_Type = OctetString
_SwDlmsStackLicenseAc_Object = MibTableColumn
swDlmsStackLicenseAc = _SwDlmsStackLicenseAc_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 2, 1, 1),
    _SwDlmsStackLicenseAc_Type()
)
swDlmsStackLicenseAc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDlmsStackLicenseAc.setStatus("current")


class _SwDlmsStackLicenseAcStatus_Type(Integer32):
    """Custom type swDlmsStackLicenseAcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("expired", 2))
    )


_SwDlmsStackLicenseAcStatus_Type.__name__ = "Integer32"
_SwDlmsStackLicenseAcStatus_Object = MibTableColumn
swDlmsStackLicenseAcStatus = _SwDlmsStackLicenseAcStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 2, 1, 2),
    _SwDlmsStackLicenseAcStatus_Type()
)
swDlmsStackLicenseAcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDlmsStackLicenseAcStatus.setStatus("current")

# Managed Objects groups


# Notification objects

swDlmsIllegalAc = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 0, 1)
)
swDlmsIllegalAc.setObjects(
    ("DLMS-MIB", "swDlmsInstallAc")
)
if mibBuilder.loadTexts:
    swDlmsIllegalAc.setStatus(
        "current"
    )

swDlmsLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 0, 2)
)
swDlmsLicenseExpired.setObjects(
      *(("DLMS-MIB", "swDlmsLicenseModelName"),
        ("DLMS-MIB", "swDlmsLicenseAc"))
)
if mibBuilder.loadTexts:
    swDlmsLicenseExpired.setStatus(
        "current"
    )

swDlmsLicenseInstallationSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 0, 3)
)
swDlmsLicenseInstallationSuccess.setObjects(
      *(("DLMS-MIB", "swDlmsLicenseModelName"),
        ("DLMS-MIB", "swDlmsInstallAc"))
)
if mibBuilder.loadTexts:
    swDlmsLicenseInstallationSuccess.setStatus(
        "current"
    )

swDlmsLicenseExpiresIn30Days = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 0, 4)
)
swDlmsLicenseExpiresIn30Days.setObjects(
      *(("DLMS-MIB", "swDlmsLicenseModelName"),
        ("DLMS-MIB", "swDlmsInstallAc"))
)
if mibBuilder.loadTexts:
    swDlmsLicenseExpiresIn30Days.setStatus(
        "current"
    )

swDlmsStackLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 0, 21)
)
swDlmsStackLicenseExpired.setObjects(
      *(("DLMS-MIB", "swDlmsStackLicenseModelUnitId"),
        ("DLMS-MIB", "swDlmsStackLicenseModelName"),
        ("DLMS-MIB", "swDlmsStackLicenseAc"))
)
if mibBuilder.loadTexts:
    swDlmsStackLicenseExpired.setStatus(
        "current"
    )

swDlmsStackLicenseInstallationSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 0, 22)
)
swDlmsStackLicenseInstallationSuccess.setObjects(
      *(("DLMS-MIB", "swDlmsStackLicenseModelUnitId"),
        ("DLMS-MIB", "swDlmsStackLicenseModelName"),
        ("DLMS-MIB", "swDlmsInstallAc"))
)
if mibBuilder.loadTexts:
    swDlmsStackLicenseInstallationSuccess.setStatus(
        "current"
    )

swDlmsStackLicenseExpiresIn30Days = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 101, 0, 23)
)
swDlmsStackLicenseExpiresIn30Days.setObjects(
      *(("DLMS-MIB", "swDlmsStackLicenseModelUnitId"),
        ("DLMS-MIB", "swDlmsStackLicenseModelName"),
        ("DLMS-MIB", "swDlmsInstallAc"))
)
if mibBuilder.loadTexts:
    swDlmsStackLicenseExpiresIn30Days.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLMS-MIB",
    **{"swDlmsMIB": swDlmsMIB,
       "swDlmsNotifications": swDlmsNotifications,
       "swDlmsIllegalAc": swDlmsIllegalAc,
       "swDlmsLicenseExpired": swDlmsLicenseExpired,
       "swDlmsLicenseInstallationSuccess": swDlmsLicenseInstallationSuccess,
       "swDlmsLicenseExpiresIn30Days": swDlmsLicenseExpiresIn30Days,
       "swDlmsStackLicenseExpired": swDlmsStackLicenseExpired,
       "swDlmsStackLicenseInstallationSuccess": swDlmsStackLicenseInstallationSuccess,
       "swDlmsStackLicenseExpiresIn30Days": swDlmsStackLicenseExpiresIn30Days,
       "swDlmsObjects": swDlmsObjects,
       "swDlmsGeneralGroup": swDlmsGeneralGroup,
       "swDlmsInstallAc": swDlmsInstallAc,
       "swDlmsInstallStackUnitId": swDlmsInstallStackUnitId,
       "swDlmsLicense": swDlmsLicense,
       "swDlmsLicenseModelTable": swDlmsLicenseModelTable,
       "swDlmsLicenseModelEntry": swDlmsLicenseModelEntry,
       "swDlmsLicenseModelName": swDlmsLicenseModelName,
       "swDlmsLicenseModelRemaining": swDlmsLicenseModelRemaining,
       "swDlmsLicenseAcTable": swDlmsLicenseAcTable,
       "swDlmsLicenseAcEntry": swDlmsLicenseAcEntry,
       "swDlmsLicenseAc": swDlmsLicenseAc,
       "swDlmsLicenseAcStatus": swDlmsLicenseAcStatus,
       "swDlmsStackLicense": swDlmsStackLicense,
       "swDlmsStackLicenseModelTable": swDlmsStackLicenseModelTable,
       "swDlmsStackLicenseModelEntry": swDlmsStackLicenseModelEntry,
       "swDlmsStackLicenseModelUnitId": swDlmsStackLicenseModelUnitId,
       "swDlmsStackLicenseModelName": swDlmsStackLicenseModelName,
       "swDlmsStackLicenseModelRemaining": swDlmsStackLicenseModelRemaining,
       "swDlmsStackLicenseAcTable": swDlmsStackLicenseAcTable,
       "swDlmsStackLicenseAcEntry": swDlmsStackLicenseAcEntry,
       "swDlmsStackLicenseAc": swDlmsStackLicenseAc,
       "swDlmsStackLicenseAcStatus": swDlmsStackLicenseAcStatus}
)
