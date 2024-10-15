# SNMP MIB module (HM2-LINK-BACKUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-LINK-BACKUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:04 2024
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

(hm2L2RedundancyMibObjects,) = mibBuilder.importSymbols(
    "HM2-L2REDUNDANCY-MIB",
    "hm2L2RedundancyMibObjects")

(HmEnabledStatus,) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hm2LinkBackupMibGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3)
)
hm2LinkBackupMibGroup.setRevisions(
        ("2013-05-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HmLinkBackupStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("blocking", 2),
          ("down", 3),
          ("forwarding", 1),
          ("unknown", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Hm2LinkBackupNotifications_ObjectIdentity = ObjectIdentity
hm2LinkBackupNotifications = _Hm2LinkBackupNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 0)
)
_Hm2LinkBackupObjects_ObjectIdentity = ObjectIdentity
hm2LinkBackupObjects = _Hm2LinkBackupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 1)
)
_Hm2LinkBackupConfiguration_ObjectIdentity = ObjectIdentity
hm2LinkBackupConfiguration = _Hm2LinkBackupConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 1, 1)
)
_Hm2LinkBackupGeneralGroup_ObjectIdentity = ObjectIdentity
hm2LinkBackupGeneralGroup = _Hm2LinkBackupGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 1, 1, 1)
)


class _Hm2LinkBackupAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2LinkBackupAdminStatus based on HmEnabledStatus"""


_Hm2LinkBackupAdminStatus_Object = MibScalar
hm2LinkBackupAdminStatus = _Hm2LinkBackupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 1, 1, 1, 1),
    _Hm2LinkBackupAdminStatus_Type()
)
hm2LinkBackupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LinkBackupAdminStatus.setStatus("current")
_Hm2LinkBackupInterfaceGroup_ObjectIdentity = ObjectIdentity
hm2LinkBackupInterfaceGroup = _Hm2LinkBackupInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 1, 1, 2)
)
_Hm2LinkBackupInterfaceConfigTable_Object = MibTable
hm2LinkBackupInterfaceConfigTable = _Hm2LinkBackupInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hm2LinkBackupInterfaceConfigTable.setStatus("current")
_Hm2LinkBackupInterfaceConfigEntry_Object = MibTableRow
hm2LinkBackupInterfaceConfigEntry = _Hm2LinkBackupInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 1, 1, 2, 1, 1)
)
hm2LinkBackupInterfaceConfigEntry.setIndexNames(
    (0, "HM2-LINK-BACKUP-MIB", "hm2LinkBackupPrimaryInterface"),
    (0, "HM2-LINK-BACKUP-MIB", "hm2LinkBackupBackupInterface"),
)
if mibBuilder.loadTexts:
    hm2LinkBackupInterfaceConfigEntry.setStatus("current")
_Hm2LinkBackupPrimaryInterface_Type = InterfaceIndex
_Hm2LinkBackupPrimaryInterface_Object = MibTableColumn
hm2LinkBackupPrimaryInterface = _Hm2LinkBackupPrimaryInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 1, 1, 2, 1, 1, 1),
    _Hm2LinkBackupPrimaryInterface_Type()
)
hm2LinkBackupPrimaryInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2LinkBackupPrimaryInterface.setStatus("current")
_Hm2LinkBackupBackupInterface_Type = InterfaceIndex
_Hm2LinkBackupBackupInterface_Object = MibTableColumn
hm2LinkBackupBackupInterface = _Hm2LinkBackupBackupInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 1, 1, 2, 1, 1, 2),
    _Hm2LinkBackupBackupInterface_Type()
)
hm2LinkBackupBackupInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2LinkBackupBackupInterface.setStatus("current")


class _Hm2LinkBackupPrimaryInterfaceStatus_Type(HmLinkBackupStatus):
    """Custom type hm2LinkBackupPrimaryInterfaceStatus based on HmLinkBackupStatus"""
    defaultValue = 4


_Hm2LinkBackupPrimaryInterfaceStatus_Object = MibTableColumn
hm2LinkBackupPrimaryInterfaceStatus = _Hm2LinkBackupPrimaryInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 1, 1, 2, 1, 1, 3),
    _Hm2LinkBackupPrimaryInterfaceStatus_Type()
)
hm2LinkBackupPrimaryInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LinkBackupPrimaryInterfaceStatus.setStatus("current")


class _Hm2LinkBackupBackupInterfaceStatus_Type(HmLinkBackupStatus):
    """Custom type hm2LinkBackupBackupInterfaceStatus based on HmLinkBackupStatus"""
    defaultValue = 4


_Hm2LinkBackupBackupInterfaceStatus_Object = MibTableColumn
hm2LinkBackupBackupInterfaceStatus = _Hm2LinkBackupBackupInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 1, 1, 2, 1, 1, 4),
    _Hm2LinkBackupBackupInterfaceStatus_Type()
)
hm2LinkBackupBackupInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LinkBackupBackupInterfaceStatus.setStatus("current")


class _Hm2LinkBackupFailBackEnable_Type(TruthValue):
    """Custom type hm2LinkBackupFailBackEnable based on TruthValue"""


_Hm2LinkBackupFailBackEnable_Object = MibTableColumn
hm2LinkBackupFailBackEnable = _Hm2LinkBackupFailBackEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 1, 1, 2, 1, 1, 5),
    _Hm2LinkBackupFailBackEnable_Type()
)
hm2LinkBackupFailBackEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LinkBackupFailBackEnable.setStatus("current")


class _Hm2LinkBackupFailBackDelay_Type(Integer32):
    """Custom type hm2LinkBackupFailBackDelay based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 3600),
    )


_Hm2LinkBackupFailBackDelay_Type.__name__ = "Integer32"
_Hm2LinkBackupFailBackDelay_Object = MibTableColumn
hm2LinkBackupFailBackDelay = _Hm2LinkBackupFailBackDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 1, 1, 2, 1, 1, 6),
    _Hm2LinkBackupFailBackDelay_Type()
)
hm2LinkBackupFailBackDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LinkBackupFailBackDelay.setStatus("current")
if mibBuilder.loadTexts:
    hm2LinkBackupFailBackDelay.setUnits("seconds")
_Hm2LinkBackupDescription_Type = SnmpAdminString
_Hm2LinkBackupDescription_Object = MibTableColumn
hm2LinkBackupDescription = _Hm2LinkBackupDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 1, 1, 2, 1, 1, 7),
    _Hm2LinkBackupDescription_Type()
)
hm2LinkBackupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LinkBackupDescription.setStatus("current")
_Hm2LinkBackupRowStatus_Type = RowStatus
_Hm2LinkBackupRowStatus_Object = MibTableColumn
hm2LinkBackupRowStatus = _Hm2LinkBackupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 1, 1, 2, 1, 1, 10),
    _Hm2LinkBackupRowStatus_Type()
)
hm2LinkBackupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LinkBackupRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hm2LinkBackupStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 3, 0, 1)
)
hm2LinkBackupStatusTrap.setObjects(
      *(("HM2-LINK-BACKUP-MIB", "hm2LinkBackupPrimaryInterface"),
        ("HM2-LINK-BACKUP-MIB", "hm2LinkBackupBackupInterface"),
        ("HM2-LINK-BACKUP-MIB", "hm2LinkBackupPrimaryInterfaceStatus"),
        ("HM2-LINK-BACKUP-MIB", "hm2LinkBackupBackupInterfaceStatus"))
)
if mibBuilder.loadTexts:
    hm2LinkBackupStatusTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-LINK-BACKUP-MIB",
    **{"HmLinkBackupStatus": HmLinkBackupStatus,
       "hm2LinkBackupMibGroup": hm2LinkBackupMibGroup,
       "hm2LinkBackupNotifications": hm2LinkBackupNotifications,
       "hm2LinkBackupStatusTrap": hm2LinkBackupStatusTrap,
       "hm2LinkBackupObjects": hm2LinkBackupObjects,
       "hm2LinkBackupConfiguration": hm2LinkBackupConfiguration,
       "hm2LinkBackupGeneralGroup": hm2LinkBackupGeneralGroup,
       "hm2LinkBackupAdminStatus": hm2LinkBackupAdminStatus,
       "hm2LinkBackupInterfaceGroup": hm2LinkBackupInterfaceGroup,
       "hm2LinkBackupInterfaceConfigTable": hm2LinkBackupInterfaceConfigTable,
       "hm2LinkBackupInterfaceConfigEntry": hm2LinkBackupInterfaceConfigEntry,
       "hm2LinkBackupPrimaryInterface": hm2LinkBackupPrimaryInterface,
       "hm2LinkBackupBackupInterface": hm2LinkBackupBackupInterface,
       "hm2LinkBackupPrimaryInterfaceStatus": hm2LinkBackupPrimaryInterfaceStatus,
       "hm2LinkBackupBackupInterfaceStatus": hm2LinkBackupBackupInterfaceStatus,
       "hm2LinkBackupFailBackEnable": hm2LinkBackupFailBackEnable,
       "hm2LinkBackupFailBackDelay": hm2LinkBackupFailBackDelay,
       "hm2LinkBackupDescription": hm2LinkBackupDescription,
       "hm2LinkBackupRowStatus": hm2LinkBackupRowStatus}
)
