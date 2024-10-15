# SNMP MIB module (ORiNOCO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ORiNOCO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:40 2024
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

orinoco = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )



class InterfaceBitmask(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ObjStatus(Integer32, TextualConvention):
    status = "current"
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



class WEPKeyType(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class ObjStatusActive(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("deleted", 3),
          ("inactive", 2))
    )



class DisplayString80(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class DisplayString55(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 55),
    )



class DisplayString32(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



# MIB Managed Objects in the order of their OIDs

_Agere_ObjectIdentity = ObjectIdentity
agere = _Agere_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898)
)
_OrinocoObjects_ObjectIdentity = ObjectIdentity
orinocoObjects = _OrinocoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1)
)
_OrinocoSys_ObjectIdentity = ObjectIdentity
orinocoSys = _OrinocoSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1)
)
_OrinocoSysInvMgmt_ObjectIdentity = ObjectIdentity
orinocoSysInvMgmt = _OrinocoSysInvMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1)
)
_OriSystemInvMgmtComponentTable_Object = MibTable
oriSystemInvMgmtComponentTable = _OriSystemInvMgmtComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    oriSystemInvMgmtComponentTable.setStatus("current")
_OriSystemInvMgmtComponentTableEntry_Object = MibTableRow
oriSystemInvMgmtComponentTableEntry = _OriSystemInvMgmtComponentTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 1, 1)
)
oriSystemInvMgmtComponentTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriSystemInvMgmtTableComponentIndex"),
)
if mibBuilder.loadTexts:
    oriSystemInvMgmtComponentTableEntry.setStatus("current")
_OriSystemInvMgmtTableComponentIndex_Type = Integer32
_OriSystemInvMgmtTableComponentIndex_Object = MibTableColumn
oriSystemInvMgmtTableComponentIndex = _OriSystemInvMgmtTableComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 1, 1, 1),
    _OriSystemInvMgmtTableComponentIndex_Type()
)
oriSystemInvMgmtTableComponentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemInvMgmtTableComponentIndex.setStatus("current")
_OriSystemInvMgmtTableComponentSerialNumber_Type = DisplayString
_OriSystemInvMgmtTableComponentSerialNumber_Object = MibTableColumn
oriSystemInvMgmtTableComponentSerialNumber = _OriSystemInvMgmtTableComponentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 1, 1, 2),
    _OriSystemInvMgmtTableComponentSerialNumber_Type()
)
oriSystemInvMgmtTableComponentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemInvMgmtTableComponentSerialNumber.setStatus("current")
_OriSystemInvMgmtTableComponentName_Type = DisplayString
_OriSystemInvMgmtTableComponentName_Object = MibTableColumn
oriSystemInvMgmtTableComponentName = _OriSystemInvMgmtTableComponentName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 1, 1, 3),
    _OriSystemInvMgmtTableComponentName_Type()
)
oriSystemInvMgmtTableComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemInvMgmtTableComponentName.setStatus("current")
_OriSystemInvMgmtTableComponentId_Type = Integer32
_OriSystemInvMgmtTableComponentId_Object = MibTableColumn
oriSystemInvMgmtTableComponentId = _OriSystemInvMgmtTableComponentId_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 1, 1, 4),
    _OriSystemInvMgmtTableComponentId_Type()
)
oriSystemInvMgmtTableComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemInvMgmtTableComponentId.setStatus("current")
_OriSystemInvMgmtTableComponentVariant_Type = Integer32
_OriSystemInvMgmtTableComponentVariant_Object = MibTableColumn
oriSystemInvMgmtTableComponentVariant = _OriSystemInvMgmtTableComponentVariant_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 1, 1, 5),
    _OriSystemInvMgmtTableComponentVariant_Type()
)
oriSystemInvMgmtTableComponentVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemInvMgmtTableComponentVariant.setStatus("current")
_OriSystemInvMgmtTableComponentReleaseVersion_Type = Integer32
_OriSystemInvMgmtTableComponentReleaseVersion_Object = MibTableColumn
oriSystemInvMgmtTableComponentReleaseVersion = _OriSystemInvMgmtTableComponentReleaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 1, 1, 6),
    _OriSystemInvMgmtTableComponentReleaseVersion_Type()
)
oriSystemInvMgmtTableComponentReleaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemInvMgmtTableComponentReleaseVersion.setStatus("current")
_OriSystemInvMgmtTableComponentMajorVersion_Type = Integer32
_OriSystemInvMgmtTableComponentMajorVersion_Object = MibTableColumn
oriSystemInvMgmtTableComponentMajorVersion = _OriSystemInvMgmtTableComponentMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 1, 1, 7),
    _OriSystemInvMgmtTableComponentMajorVersion_Type()
)
oriSystemInvMgmtTableComponentMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemInvMgmtTableComponentMajorVersion.setStatus("current")
_OriSystemInvMgmtTableComponentMinorVersion_Type = Integer32
_OriSystemInvMgmtTableComponentMinorVersion_Object = MibTableColumn
oriSystemInvMgmtTableComponentMinorVersion = _OriSystemInvMgmtTableComponentMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 1, 1, 8),
    _OriSystemInvMgmtTableComponentMinorVersion_Type()
)
oriSystemInvMgmtTableComponentMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemInvMgmtTableComponentMinorVersion.setStatus("current")
_OriSystemInvMgmtTableComponentIfTable_Object = MibTable
oriSystemInvMgmtTableComponentIfTable = _OriSystemInvMgmtTableComponentIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    oriSystemInvMgmtTableComponentIfTable.setStatus("deprecated")
_OriSystemInvMgmtTableComponentIfTableEntry_Object = MibTableRow
oriSystemInvMgmtTableComponentIfTableEntry = _OriSystemInvMgmtTableComponentIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 2, 1)
)
oriSystemInvMgmtTableComponentIfTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriSystemInvMgmtTableComponentIndex"),
    (0, "ORiNOCO-MIB", "oriSystemInvMgmtInterfaceTableIndex"),
)
if mibBuilder.loadTexts:
    oriSystemInvMgmtTableComponentIfTableEntry.setStatus("deprecated")
_OriSystemInvMgmtInterfaceTableIndex_Type = Integer32
_OriSystemInvMgmtInterfaceTableIndex_Object = MibTableColumn
oriSystemInvMgmtInterfaceTableIndex = _OriSystemInvMgmtInterfaceTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 2, 1, 1),
    _OriSystemInvMgmtInterfaceTableIndex_Type()
)
oriSystemInvMgmtInterfaceTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemInvMgmtInterfaceTableIndex.setStatus("deprecated")
_OriSystemInvMgmtInterfaceId_Type = Integer32
_OriSystemInvMgmtInterfaceId_Object = MibTableColumn
oriSystemInvMgmtInterfaceId = _OriSystemInvMgmtInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 2, 1, 2),
    _OriSystemInvMgmtInterfaceId_Type()
)
oriSystemInvMgmtInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemInvMgmtInterfaceId.setStatus("deprecated")


class _OriSystemInvMgmtInterfaceRole_Type(Integer32):
    """Custom type oriSystemInvMgmtInterfaceRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("actor", 1),
          ("supplier", 2))
    )


_OriSystemInvMgmtInterfaceRole_Type.__name__ = "Integer32"
_OriSystemInvMgmtInterfaceRole_Object = MibTableColumn
oriSystemInvMgmtInterfaceRole = _OriSystemInvMgmtInterfaceRole_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 2, 1, 3),
    _OriSystemInvMgmtInterfaceRole_Type()
)
oriSystemInvMgmtInterfaceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemInvMgmtInterfaceRole.setStatus("deprecated")
_OriSystemInvMgmtInterfaceVariant_Type = Integer32
_OriSystemInvMgmtInterfaceVariant_Object = MibTableColumn
oriSystemInvMgmtInterfaceVariant = _OriSystemInvMgmtInterfaceVariant_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 2, 1, 4),
    _OriSystemInvMgmtInterfaceVariant_Type()
)
oriSystemInvMgmtInterfaceVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemInvMgmtInterfaceVariant.setStatus("deprecated")
_OriSystemInvMgmtInterfaceBottomNumber_Type = Integer32
_OriSystemInvMgmtInterfaceBottomNumber_Object = MibTableColumn
oriSystemInvMgmtInterfaceBottomNumber = _OriSystemInvMgmtInterfaceBottomNumber_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 2, 1, 5),
    _OriSystemInvMgmtInterfaceBottomNumber_Type()
)
oriSystemInvMgmtInterfaceBottomNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemInvMgmtInterfaceBottomNumber.setStatus("deprecated")
_OriSystemInvMgmtInterfaceTopNumber_Type = Integer32
_OriSystemInvMgmtInterfaceTopNumber_Object = MibTableColumn
oriSystemInvMgmtInterfaceTopNumber = _OriSystemInvMgmtInterfaceTopNumber_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 1, 2, 1, 6),
    _OriSystemInvMgmtInterfaceTopNumber_Type()
)
oriSystemInvMgmtInterfaceTopNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemInvMgmtInterfaceTopNumber.setStatus("deprecated")
_OriSystemReboot_Type = Integer32
_OriSystemReboot_Object = MibScalar
oriSystemReboot = _OriSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 4),
    _OriSystemReboot_Type()
)
oriSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSystemReboot.setStatus("current")
_OriSystemContactEmail_Type = DisplayString
_OriSystemContactEmail_Object = MibScalar
oriSystemContactEmail = _OriSystemContactEmail_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 5),
    _OriSystemContactEmail_Type()
)
oriSystemContactEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSystemContactEmail.setStatus("current")
_OriSystemContactPhoneNumber_Type = DisplayString
_OriSystemContactPhoneNumber_Object = MibScalar
oriSystemContactPhoneNumber = _OriSystemContactPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 6),
    _OriSystemContactPhoneNumber_Type()
)
oriSystemContactPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSystemContactPhoneNumber.setStatus("current")
_OriSystemFlashUpdate_Type = Integer32
_OriSystemFlashUpdate_Object = MibScalar
oriSystemFlashUpdate = _OriSystemFlashUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 7),
    _OriSystemFlashUpdate_Type()
)
oriSystemFlashUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSystemFlashUpdate.setStatus("current")
_OriSystemFlashBackupInterval_Type = Integer32
_OriSystemFlashBackupInterval_Object = MibScalar
oriSystemFlashBackupInterval = _OriSystemFlashBackupInterval_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 8),
    _OriSystemFlashBackupInterval_Type()
)
oriSystemFlashBackupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSystemFlashBackupInterval.setStatus("current")


class _OriSystemEmergencyResetToDefault_Type(Integer32):
    """Custom type oriSystemEmergencyResetToDefault based on Integer32"""
    defaultValue = 0


_OriSystemEmergencyResetToDefault_Object = MibScalar
oriSystemEmergencyResetToDefault = _OriSystemEmergencyResetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 9),
    _OriSystemEmergencyResetToDefault_Type()
)
oriSystemEmergencyResetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSystemEmergencyResetToDefault.setStatus("current")


class _OriSystemMode_Type(Integer32):
    """Custom type oriSystemMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("gateway", 2))
    )


_OriSystemMode_Type.__name__ = "Integer32"
_OriSystemMode_Object = MibScalar
oriSystemMode = _OriSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 10),
    _OriSystemMode_Type()
)
oriSystemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSystemMode.setStatus("current")
_OriSystemEventLogTable_Object = MibTable
oriSystemEventLogTable = _OriSystemEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 11)
)
if mibBuilder.loadTexts:
    oriSystemEventLogTable.setStatus("current")
_OriSystemEventLogTableEntry_Object = MibTableRow
oriSystemEventLogTableEntry = _OriSystemEventLogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 11, 1)
)
oriSystemEventLogTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriSystemEventLogMessage"),
)
if mibBuilder.loadTexts:
    oriSystemEventLogTableEntry.setStatus("current")
_OriSystemEventLogMessage_Type = DisplayString
_OriSystemEventLogMessage_Object = MibTableColumn
oriSystemEventLogMessage = _OriSystemEventLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 11, 1, 1),
    _OriSystemEventLogMessage_Type()
)
oriSystemEventLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemEventLogMessage.setStatus("current")


class _OriSystemEventLogTableReset_Type(Integer32):
    """Custom type oriSystemEventLogTableReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_OriSystemEventLogTableReset_Type.__name__ = "Integer32"
_OriSystemEventLogTableReset_Object = MibScalar
oriSystemEventLogTableReset = _OriSystemEventLogTableReset_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 12),
    _OriSystemEventLogTableReset_Type()
)
oriSystemEventLogTableReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSystemEventLogTableReset.setStatus("current")
_OriSystemEventLogMask_Type = Integer32
_OriSystemEventLogMask_Object = MibScalar
oriSystemEventLogMask = _OriSystemEventLogMask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 13),
    _OriSystemEventLogMask_Type()
)
oriSystemEventLogMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSystemEventLogMask.setStatus("current")
_OriSystemAccessUserName_Type = DisplayString
_OriSystemAccessUserName_Object = MibScalar
oriSystemAccessUserName = _OriSystemAccessUserName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 14),
    _OriSystemAccessUserName_Type()
)
oriSystemAccessUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSystemAccessUserName.setStatus("current")
_OriSystemAccessPassword_Type = DisplayString
_OriSystemAccessPassword_Object = MibScalar
oriSystemAccessPassword = _OriSystemAccessPassword_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 15),
    _OriSystemAccessPassword_Type()
)
oriSystemAccessPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSystemAccessPassword.setStatus("current")


class _OriSystemAccessLoginTimeout_Type(Integer32):
    """Custom type oriSystemAccessLoginTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OriSystemAccessLoginTimeout_Type.__name__ = "Integer32"
_OriSystemAccessLoginTimeout_Object = MibScalar
oriSystemAccessLoginTimeout = _OriSystemAccessLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 16),
    _OriSystemAccessLoginTimeout_Type()
)
oriSystemAccessLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSystemAccessLoginTimeout.setStatus("current")


class _OriSystemAccessIdleTimeout_Type(Integer32):
    """Custom type oriSystemAccessIdleTimeout based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 36000),
    )


_OriSystemAccessIdleTimeout_Type.__name__ = "Integer32"
_OriSystemAccessIdleTimeout_Object = MibScalar
oriSystemAccessIdleTimeout = _OriSystemAccessIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 17),
    _OriSystemAccessIdleTimeout_Type()
)
oriSystemAccessIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSystemAccessIdleTimeout.setStatus("current")
_OriSystemEventLogNumberOfMessages_Type = Integer32
_OriSystemEventLogNumberOfMessages_Object = MibScalar
oriSystemEventLogNumberOfMessages = _OriSystemEventLogNumberOfMessages_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 18),
    _OriSystemEventLogNumberOfMessages_Type()
)
oriSystemEventLogNumberOfMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemEventLogNumberOfMessages.setStatus("current")
_OrinocoSysFeature_ObjectIdentity = ObjectIdentity
orinocoSysFeature = _OrinocoSysFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 19)
)
_OriSystemFeatureTable_Object = MibTable
oriSystemFeatureTable = _OriSystemFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 19, 1)
)
if mibBuilder.loadTexts:
    oriSystemFeatureTable.setStatus("current")
_OriSystemFeatureTableEntry_Object = MibTableRow
oriSystemFeatureTableEntry = _OriSystemFeatureTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 19, 1, 1)
)
oriSystemFeatureTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriSystemFeatureTableCode"),
)
if mibBuilder.loadTexts:
    oriSystemFeatureTableEntry.setStatus("current")


class _OriSystemFeatureTableCode_Type(Integer32):
    """Custom type oriSystemFeatureTableCode based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("aOLNATGateway", 32),
          ("acctRADIUS", 25),
          ("authRADIUS", 24),
          ("bandwidthADSL", 5),
          ("bandwidthCable", 6),
          ("bandwidthPhone", 7),
          ("bandwidthTurboCell", 4),
          ("bandwidthWDS", 2),
          ("bandwidthWORPDown", 37),
          ("bandwidthWORPUp", 3),
          ("bandwidthWiFi", 1),
          ("dHCPRelayAgent", 21),
          ("dHCPServer", 20),
          ("dNSRedirect", 31),
          ("disableSecWifiIf", 38),
          ("filterIP", 27),
          ("filteringStatic", 23),
          ("hereUare", 33),
          ("iAPP", 30),
          ("ieee802dot1x", 28),
          ("initialProductType", 39),
          ("linkIntegrity", 19),
          ("managementHTTP", 13),
          ("maxLinksWDS", 9),
          ("maxPPPoESessions", 12),
          ("maxStationsTurboCell", 11),
          ("maxStationsWORP", 10),
          ("maxStationsWiFi", 8),
          ("nse", 29),
          ("proxyARP", 22),
          ("remoteLinkTest", 14),
          ("routingOSPF", 17),
          ("routingRIP", 16),
          ("routingStatic", 15),
          ("satMaxUsers", 36),
          ("spanningTreeProtocol", 18),
          ("spectralink", 34),
          ("throttlingRADIUS", 26),
          ("vLANTagging", 35))
    )


_OriSystemFeatureTableCode_Type.__name__ = "Integer32"
_OriSystemFeatureTableCode_Object = MibTableColumn
oriSystemFeatureTableCode = _OriSystemFeatureTableCode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 19, 1, 1, 1),
    _OriSystemFeatureTableCode_Type()
)
oriSystemFeatureTableCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemFeatureTableCode.setStatus("current")
_OriSystemFeatureTableSupported_Type = Integer32
_OriSystemFeatureTableSupported_Object = MibTableColumn
oriSystemFeatureTableSupported = _OriSystemFeatureTableSupported_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 19, 1, 1, 2),
    _OriSystemFeatureTableSupported_Type()
)
oriSystemFeatureTableSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemFeatureTableSupported.setStatus("current")
_OriSystemFeatureTableLicensed_Type = Integer32
_OriSystemFeatureTableLicensed_Object = MibTableColumn
oriSystemFeatureTableLicensed = _OriSystemFeatureTableLicensed_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 19, 1, 1, 3),
    _OriSystemFeatureTableLicensed_Type()
)
oriSystemFeatureTableLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemFeatureTableLicensed.setStatus("current")
_OriSystemFeatureTableDescription_Type = DisplayString
_OriSystemFeatureTableDescription_Object = MibTableColumn
oriSystemFeatureTableDescription = _OriSystemFeatureTableDescription_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 19, 1, 1, 4),
    _OriSystemFeatureTableDescription_Type()
)
oriSystemFeatureTableDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemFeatureTableDescription.setStatus("current")


class _OriSystemAccessMaxSessions_Type(Integer32):
    """Custom type oriSystemAccessMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_OriSystemAccessMaxSessions_Type.__name__ = "Integer32"
_OriSystemAccessMaxSessions_Object = MibScalar
oriSystemAccessMaxSessions = _OriSystemAccessMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 20),
    _OriSystemAccessMaxSessions_Type()
)
oriSystemAccessMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemAccessMaxSessions.setStatus("current")
_OrinocoSyslog_ObjectIdentity = ObjectIdentity
orinocoSyslog = _OrinocoSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 21)
)


class _OriSyslogStatus_Type(Integer32):
    """Custom type oriSyslogStatus based on Integer32"""
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


_OriSyslogStatus_Type.__name__ = "Integer32"
_OriSyslogStatus_Object = MibScalar
oriSyslogStatus = _OriSyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 21, 1),
    _OriSyslogStatus_Type()
)
oriSyslogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSyslogStatus.setStatus("current")
_OriSyslogPort_Type = Integer32
_OriSyslogPort_Object = MibScalar
oriSyslogPort = _OriSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 21, 2),
    _OriSyslogPort_Type()
)
oriSyslogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSyslogPort.setStatus("current")


class _OriSyslogPriority_Type(Integer32):
    """Custom type oriSyslogPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_OriSyslogPriority_Type.__name__ = "Integer32"
_OriSyslogPriority_Object = MibScalar
oriSyslogPriority = _OriSyslogPriority_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 21, 3),
    _OriSyslogPriority_Type()
)
oriSyslogPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSyslogPriority.setStatus("current")


class _OriSyslogHeartbeatStatus_Type(Integer32):
    """Custom type oriSyslogHeartbeatStatus based on Integer32"""
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


_OriSyslogHeartbeatStatus_Type.__name__ = "Integer32"
_OriSyslogHeartbeatStatus_Object = MibScalar
oriSyslogHeartbeatStatus = _OriSyslogHeartbeatStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 21, 4),
    _OriSyslogHeartbeatStatus_Type()
)
oriSyslogHeartbeatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSyslogHeartbeatStatus.setStatus("current")


class _OriSyslogHeartbeatInterval_Type(Integer32):
    """Custom type oriSyslogHeartbeatInterval based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_OriSyslogHeartbeatInterval_Type.__name__ = "Integer32"
_OriSyslogHeartbeatInterval_Object = MibScalar
oriSyslogHeartbeatInterval = _OriSyslogHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 21, 5),
    _OriSyslogHeartbeatInterval_Type()
)
oriSyslogHeartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSyslogHeartbeatInterval.setStatus("current")
_OriSyslogHostTable_Object = MibTable
oriSyslogHostTable = _OriSyslogHostTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 21, 6)
)
if mibBuilder.loadTexts:
    oriSyslogHostTable.setStatus("current")
_OriSyslogHostTableEntry_Object = MibTableRow
oriSyslogHostTableEntry = _OriSyslogHostTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 21, 6, 1)
)
oriSyslogHostTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriSyslogHostTableIndex"),
)
if mibBuilder.loadTexts:
    oriSyslogHostTableEntry.setStatus("current")


class _OriSyslogHostTableIndex_Type(Integer32):
    """Custom type oriSyslogHostTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_OriSyslogHostTableIndex_Type.__name__ = "Integer32"
_OriSyslogHostTableIndex_Object = MibTableColumn
oriSyslogHostTableIndex = _OriSyslogHostTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 21, 6, 1, 1),
    _OriSyslogHostTableIndex_Type()
)
oriSyslogHostTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSyslogHostTableIndex.setStatus("current")
_OriSyslogHostIPAddress_Type = IpAddress
_OriSyslogHostIPAddress_Object = MibTableColumn
oriSyslogHostIPAddress = _OriSyslogHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 21, 6, 1, 2),
    _OriSyslogHostIPAddress_Type()
)
oriSyslogHostIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSyslogHostIPAddress.setStatus("current")
_OriSyslogHostComment_Type = DisplayString
_OriSyslogHostComment_Object = MibTableColumn
oriSyslogHostComment = _OriSyslogHostComment_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 21, 6, 1, 3),
    _OriSyslogHostComment_Type()
)
oriSyslogHostComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSyslogHostComment.setStatus("current")


class _OriSyslogHostTableEntryStatus_Type(Integer32):
    """Custom type oriSyslogHostTableEntryStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriSyslogHostTableEntryStatus_Type.__name__ = "Integer32"
_OriSyslogHostTableEntryStatus_Object = MibTableColumn
oriSyslogHostTableEntryStatus = _OriSyslogHostTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 21, 6, 1, 4),
    _OriSyslogHostTableEntryStatus_Type()
)
oriSyslogHostTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSyslogHostTableEntryStatus.setStatus("current")
_OriSystemCountryCode_Type = DisplayString
_OriSystemCountryCode_Object = MibScalar
oriSystemCountryCode = _OriSystemCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 22),
    _OriSystemCountryCode_Type()
)
oriSystemCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSystemCountryCode.setStatus("current")
_OrinocoTempLog_ObjectIdentity = ObjectIdentity
orinocoTempLog = _OrinocoTempLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 23)
)


class _OriUnitTemp_Type(Integer32):
    """Custom type oriUnitTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 60),
    )


_OriUnitTemp_Type.__name__ = "Integer32"
_OriUnitTemp_Object = MibScalar
oriUnitTemp = _OriUnitTemp_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 23, 1),
    _OriUnitTemp_Type()
)
oriUnitTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriUnitTemp.setStatus("current")


class _OriTempLoggingInterval_Type(Integer32):
    """Custom type oriTempLoggingInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_OriTempLoggingInterval_Type.__name__ = "Integer32"
_OriTempLoggingInterval_Object = MibScalar
oriTempLoggingInterval = _OriTempLoggingInterval_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 23, 2),
    _OriTempLoggingInterval_Type()
)
oriTempLoggingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTempLoggingInterval.setStatus("current")
_OriTempLogTable_Object = MibTable
oriTempLogTable = _OriTempLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 23, 3)
)
if mibBuilder.loadTexts:
    oriTempLogTable.setStatus("current")
_OriTempLogTableEntry_Object = MibTableRow
oriTempLogTableEntry = _OriTempLogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 23, 3, 1)
)
oriTempLogTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriTempLogMessage"),
)
if mibBuilder.loadTexts:
    oriTempLogTableEntry.setStatus("current")
_OriTempLogMessage_Type = DisplayString55
_OriTempLogMessage_Object = MibTableColumn
oriTempLogMessage = _OriTempLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 23, 3, 1, 1),
    _OriTempLogMessage_Type()
)
oriTempLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTempLogMessage.setStatus("current")


class _OriTempLogTableReset_Type(Integer32):
    """Custom type oriTempLogTableReset based on Integer32"""
    defaultValue = 0


_OriTempLogTableReset_Object = MibScalar
oriTempLogTableReset = _OriTempLogTableReset_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 23, 4),
    _OriTempLogTableReset_Type()
)
oriTempLogTableReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTempLogTableReset.setStatus("current")


class _OriSystemHwType_Type(Integer32):
    """Custom type oriSystemHwType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indoor", 1),
          ("outdoor", 2))
    )


_OriSystemHwType_Type.__name__ = "Integer32"
_OriSystemHwType_Object = MibScalar
oriSystemHwType = _OriSystemHwType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 1, 24),
    _OriSystemHwType_Type()
)
oriSystemHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSystemHwType.setStatus("current")
_OrinocoIf_ObjectIdentity = ObjectIdentity
orinocoIf = _OrinocoIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2)
)
_OrinocoWirelessIf_ObjectIdentity = ObjectIdentity
orinocoWirelessIf = _OrinocoWirelessIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1)
)
_OriWirelessIfPropertiesTable_Object = MibTable
oriWirelessIfPropertiesTable = _OriWirelessIfPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    oriWirelessIfPropertiesTable.setStatus("current")
_OriWirelessIfPropertiesEntry_Object = MibTableRow
oriWirelessIfPropertiesEntry = _OriWirelessIfPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1)
)
oriWirelessIfPropertiesEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriWirelessIfPropertiesIndex"),
)
if mibBuilder.loadTexts:
    oriWirelessIfPropertiesEntry.setStatus("current")
_OriWirelessIfPropertiesIndex_Type = Integer32
_OriWirelessIfPropertiesIndex_Object = MibTableColumn
oriWirelessIfPropertiesIndex = _OriWirelessIfPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 1),
    _OriWirelessIfPropertiesIndex_Type()
)
oriWirelessIfPropertiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWirelessIfPropertiesIndex.setStatus("current")


class _OriWirelessIfNetworkName_Type(DisplayString):
    """Custom type oriWirelessIfNetworkName based on DisplayString"""
    defaultValue = OctetString("My Wireless Network")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OriWirelessIfNetworkName_Type.__name__ = "DisplayString"
_OriWirelessIfNetworkName_Object = MibTableColumn
oriWirelessIfNetworkName = _OriWirelessIfNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 2),
    _OriWirelessIfNetworkName_Type()
)
oriWirelessIfNetworkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfNetworkName.setStatus("current")


class _OriWirelessIfMediumReservation_Type(Integer32):
    """Custom type oriWirelessIfMediumReservation based on Integer32"""
    defaultValue = 2347

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_OriWirelessIfMediumReservation_Type.__name__ = "Integer32"
_OriWirelessIfMediumReservation_Object = MibTableColumn
oriWirelessIfMediumReservation = _OriWirelessIfMediumReservation_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 3),
    _OriWirelessIfMediumReservation_Type()
)
oriWirelessIfMediumReservation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfMediumReservation.setStatus("current")


class _OriWirelessIfInterferenceRobustness_Type(Integer32):
    """Custom type oriWirelessIfInterferenceRobustness based on Integer32"""
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


_OriWirelessIfInterferenceRobustness_Type.__name__ = "Integer32"
_OriWirelessIfInterferenceRobustness_Object = MibTableColumn
oriWirelessIfInterferenceRobustness = _OriWirelessIfInterferenceRobustness_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 4),
    _OriWirelessIfInterferenceRobustness_Type()
)
oriWirelessIfInterferenceRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfInterferenceRobustness.setStatus("current")


class _OriWirelessIfDTIMPeriod_Type(Integer32):
    """Custom type oriWirelessIfDTIMPeriod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OriWirelessIfDTIMPeriod_Type.__name__ = "Integer32"
_OriWirelessIfDTIMPeriod_Object = MibTableColumn
oriWirelessIfDTIMPeriod = _OriWirelessIfDTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 5),
    _OriWirelessIfDTIMPeriod_Type()
)
oriWirelessIfDTIMPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfDTIMPeriod.setStatus("current")


class _OriWirelessIfChannel_Type(Integer32):
    """Custom type oriWirelessIfChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_OriWirelessIfChannel_Type.__name__ = "Integer32"
_OriWirelessIfChannel_Object = MibTableColumn
oriWirelessIfChannel = _OriWirelessIfChannel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 6),
    _OriWirelessIfChannel_Type()
)
oriWirelessIfChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfChannel.setStatus("current")


class _OriWirelessIfDistancebetweenAPs_Type(Integer32):
    """Custom type oriWirelessIfDistancebetweenAPs based on Integer32"""
    defaultValue = 1

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
        *(("large", 1),
          ("medium", 2),
          ("microcell", 5),
          ("minicell", 4),
          ("small", 3))
    )


_OriWirelessIfDistancebetweenAPs_Type.__name__ = "Integer32"
_OriWirelessIfDistancebetweenAPs_Object = MibTableColumn
oriWirelessIfDistancebetweenAPs = _OriWirelessIfDistancebetweenAPs_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 7),
    _OriWirelessIfDistancebetweenAPs_Type()
)
oriWirelessIfDistancebetweenAPs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfDistancebetweenAPs.setStatus("current")


class _OriWirelessIfMulticastRate_Type(Integer32):
    """Custom type oriWirelessIfMulticastRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OriWirelessIfMulticastRate_Type.__name__ = "Integer32"
_OriWirelessIfMulticastRate_Object = MibTableColumn
oriWirelessIfMulticastRate = _OriWirelessIfMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 8),
    _OriWirelessIfMulticastRate_Type()
)
oriWirelessIfMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfMulticastRate.setStatus("current")


class _OriWirelessIfClosedSystem_Type(Integer32):
    """Custom type oriWirelessIfClosedSystem based on Integer32"""
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


_OriWirelessIfClosedSystem_Type.__name__ = "Integer32"
_OriWirelessIfClosedSystem_Object = MibTableColumn
oriWirelessIfClosedSystem = _OriWirelessIfClosedSystem_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 9),
    _OriWirelessIfClosedSystem_Type()
)
oriWirelessIfClosedSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfClosedSystem.setStatus("current")
_OriWirelessIfAllowedSupportedDataRates_Type = OctetString
_OriWirelessIfAllowedSupportedDataRates_Object = MibTableColumn
oriWirelessIfAllowedSupportedDataRates = _OriWirelessIfAllowedSupportedDataRates_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 10),
    _OriWirelessIfAllowedSupportedDataRates_Type()
)
oriWirelessIfAllowedSupportedDataRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWirelessIfAllowedSupportedDataRates.setStatus("current")
_OriWirelessIfRegulatoryDomainList_Type = OctetString
_OriWirelessIfRegulatoryDomainList_Object = MibTableColumn
oriWirelessIfRegulatoryDomainList = _OriWirelessIfRegulatoryDomainList_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 11),
    _OriWirelessIfRegulatoryDomainList_Type()
)
oriWirelessIfRegulatoryDomainList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWirelessIfRegulatoryDomainList.setStatus("current")
_OriWirelessIfAllowedChannels_Type = OctetString
_OriWirelessIfAllowedChannels_Object = MibTableColumn
oriWirelessIfAllowedChannels = _OriWirelessIfAllowedChannels_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 12),
    _OriWirelessIfAllowedChannels_Type()
)
oriWirelessIfAllowedChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWirelessIfAllowedChannels.setStatus("current")
_OriWirelessIfMACAddress_Type = PhysAddress
_OriWirelessIfMACAddress_Object = MibTableColumn
oriWirelessIfMACAddress = _OriWirelessIfMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 13),
    _OriWirelessIfMACAddress_Type()
)
oriWirelessIfMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWirelessIfMACAddress.setStatus("deprecated")


class _OriWirelessIfLoadBalancing_Type(Integer32):
    """Custom type oriWirelessIfLoadBalancing based on Integer32"""
    defaultValue = 1

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


_OriWirelessIfLoadBalancing_Type.__name__ = "Integer32"
_OriWirelessIfLoadBalancing_Object = MibTableColumn
oriWirelessIfLoadBalancing = _OriWirelessIfLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 14),
    _OriWirelessIfLoadBalancing_Type()
)
oriWirelessIfLoadBalancing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfLoadBalancing.setStatus("current")


class _OriWirelessIfMediumDensityDistribution_Type(Integer32):
    """Custom type oriWirelessIfMediumDensityDistribution based on Integer32"""
    defaultValue = 1

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


_OriWirelessIfMediumDensityDistribution_Type.__name__ = "Integer32"
_OriWirelessIfMediumDensityDistribution_Object = MibTableColumn
oriWirelessIfMediumDensityDistribution = _OriWirelessIfMediumDensityDistribution_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 15),
    _OriWirelessIfMediumDensityDistribution_Type()
)
oriWirelessIfMediumDensityDistribution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfMediumDensityDistribution.setStatus("current")


class _OriWirelessIfTxRate_Type(Integer32):
    """Custom type oriWirelessIfTxRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OriWirelessIfTxRate_Type.__name__ = "Integer32"
_OriWirelessIfTxRate_Object = MibTableColumn
oriWirelessIfTxRate = _OriWirelessIfTxRate_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 16),
    _OriWirelessIfTxRate_Type()
)
oriWirelessIfTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfTxRate.setStatus("current")


class _OriWirelessIfAutoChannelSelectStatus_Type(Integer32):
    """Custom type oriWirelessIfAutoChannelSelectStatus based on Integer32"""
    defaultValue = 1

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


_OriWirelessIfAutoChannelSelectStatus_Type.__name__ = "Integer32"
_OriWirelessIfAutoChannelSelectStatus_Object = MibTableColumn
oriWirelessIfAutoChannelSelectStatus = _OriWirelessIfAutoChannelSelectStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 17),
    _OriWirelessIfAutoChannelSelectStatus_Type()
)
oriWirelessIfAutoChannelSelectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfAutoChannelSelectStatus.setStatus("current")
_OriWirelessIfBandwidthLimitIn_Type = Gauge32
_OriWirelessIfBandwidthLimitIn_Object = MibTableColumn
oriWirelessIfBandwidthLimitIn = _OriWirelessIfBandwidthLimitIn_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 18),
    _OriWirelessIfBandwidthLimitIn_Type()
)
oriWirelessIfBandwidthLimitIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfBandwidthLimitIn.setStatus("current")
_OriWirelessIfBandwidthLimitOut_Type = Gauge32
_OriWirelessIfBandwidthLimitOut_Object = MibTableColumn
oriWirelessIfBandwidthLimitOut = _OriWirelessIfBandwidthLimitOut_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 19),
    _OriWirelessIfBandwidthLimitOut_Type()
)
oriWirelessIfBandwidthLimitOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfBandwidthLimitOut.setStatus("current")
_OriWirelessIfTurboModeStatus_Type = ObjStatus
_OriWirelessIfTurboModeStatus_Object = MibTableColumn
oriWirelessIfTurboModeStatus = _OriWirelessIfTurboModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 20),
    _OriWirelessIfTurboModeStatus_Type()
)
oriWirelessIfTurboModeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfTurboModeStatus.setStatus("current")
_OriWirelessIfSupportedOperationalModes_Type = DisplayString
_OriWirelessIfSupportedOperationalModes_Object = MibTableColumn
oriWirelessIfSupportedOperationalModes = _OriWirelessIfSupportedOperationalModes_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 21),
    _OriWirelessIfSupportedOperationalModes_Type()
)
oriWirelessIfSupportedOperationalModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWirelessIfSupportedOperationalModes.setStatus("current")


class _OriWirelessIfOperationalMode_Type(Integer32):
    """Custom type oriWirelessIfOperationalMode based on Integer32"""
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
        *(("dot11a-only", 4),
          ("dot11b-only", 1),
          ("dot11bg", 3),
          ("dot11g-only", 2),
          ("dot11g-wifi", 5))
    )


_OriWirelessIfOperationalMode_Type.__name__ = "Integer32"
_OriWirelessIfOperationalMode_Object = MibTableColumn
oriWirelessIfOperationalMode = _OriWirelessIfOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 22),
    _OriWirelessIfOperationalMode_Type()
)
oriWirelessIfOperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfOperationalMode.setStatus("current")
_OriWirelessIfPreambleType_Type = DisplayString
_OriWirelessIfPreambleType_Object = MibTableColumn
oriWirelessIfPreambleType = _OriWirelessIfPreambleType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 23),
    _OriWirelessIfPreambleType_Type()
)
oriWirelessIfPreambleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWirelessIfPreambleType.setStatus("current")
_OriWirelessIfProtectionMechanismStatus_Type = ObjStatus
_OriWirelessIfProtectionMechanismStatus_Object = MibTableColumn
oriWirelessIfProtectionMechanismStatus = _OriWirelessIfProtectionMechanismStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 24),
    _OriWirelessIfProtectionMechanismStatus_Type()
)
oriWirelessIfProtectionMechanismStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWirelessIfProtectionMechanismStatus.setStatus("current")
_OriWirelessIfSupportedMulticastRates_Type = DisplayString
_OriWirelessIfSupportedMulticastRates_Object = MibTableColumn
oriWirelessIfSupportedMulticastRates = _OriWirelessIfSupportedMulticastRates_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 25),
    _OriWirelessIfSupportedMulticastRates_Type()
)
oriWirelessIfSupportedMulticastRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWirelessIfSupportedMulticastRates.setStatus("current")


class _OriWirelessIfCapabilities_Type(OctetString):
    """Custom type oriWirelessIfCapabilities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_OriWirelessIfCapabilities_Type.__name__ = "OctetString"
_OriWirelessIfCapabilities_Object = MibTableColumn
oriWirelessIfCapabilities = _OriWirelessIfCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 26),
    _OriWirelessIfCapabilities_Type()
)
oriWirelessIfCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWirelessIfCapabilities.setStatus("current")


class _OriWirelessIfLBTxTimeThreshold_Type(Integer32):
    """Custom type oriWirelessIfLBTxTimeThreshold based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_OriWirelessIfLBTxTimeThreshold_Type.__name__ = "Integer32"
_OriWirelessIfLBTxTimeThreshold_Object = MibTableColumn
oriWirelessIfLBTxTimeThreshold = _OriWirelessIfLBTxTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 27),
    _OriWirelessIfLBTxTimeThreshold_Type()
)
oriWirelessIfLBTxTimeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfLBTxTimeThreshold.setStatus("current")


class _OriWirelessIfLBAdjAPTimeDiffThreshold_Type(Integer32):
    """Custom type oriWirelessIfLBAdjAPTimeDiffThreshold based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_OriWirelessIfLBAdjAPTimeDiffThreshold_Type.__name__ = "Integer32"
_OriWirelessIfLBAdjAPTimeDiffThreshold_Object = MibTableColumn
oriWirelessIfLBAdjAPTimeDiffThreshold = _OriWirelessIfLBAdjAPTimeDiffThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 28),
    _OriWirelessIfLBAdjAPTimeDiffThreshold_Type()
)
oriWirelessIfLBAdjAPTimeDiffThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfLBAdjAPTimeDiffThreshold.setStatus("current")


class _OriWirelessIfACSFrequencyBandScan_Type(Integer32):
    """Custom type oriWirelessIfACSFrequencyBandScan based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OriWirelessIfACSFrequencyBandScan_Type.__name__ = "Integer32"
_OriWirelessIfACSFrequencyBandScan_Object = MibTableColumn
oriWirelessIfACSFrequencyBandScan = _OriWirelessIfACSFrequencyBandScan_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 29),
    _OriWirelessIfACSFrequencyBandScan_Type()
)
oriWirelessIfACSFrequencyBandScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfACSFrequencyBandScan.setStatus("current")


class _OriWirelessIfSecurityPerSSIDStatus_Type(ObjStatus):
    """Custom type oriWirelessIfSecurityPerSSIDStatus based on ObjStatus"""


_OriWirelessIfSecurityPerSSIDStatus_Object = MibTableColumn
oriWirelessIfSecurityPerSSIDStatus = _OriWirelessIfSecurityPerSSIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 30),
    _OriWirelessIfSecurityPerSSIDStatus_Type()
)
oriWirelessIfSecurityPerSSIDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfSecurityPerSSIDStatus.setStatus("current")


class _OriWirelessIfDFSStatus_Type(ObjStatus):
    """Custom type oriWirelessIfDFSStatus based on ObjStatus"""


_OriWirelessIfDFSStatus_Object = MibTableColumn
oriWirelessIfDFSStatus = _OriWirelessIfDFSStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 31),
    _OriWirelessIfDFSStatus_Type()
)
oriWirelessIfDFSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfDFSStatus.setStatus("current")


class _OriWirelessIfAntenna_Type(Integer32):
    """Custom type oriWirelessIfAntenna based on Integer32"""
    defaultValue = 1

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
        *(("controllable", 3),
          ("disabled", 4),
          ("external", 1),
          ("internal", 2))
    )


_OriWirelessIfAntenna_Type.__name__ = "Integer32"
_OriWirelessIfAntenna_Object = MibTableColumn
oriWirelessIfAntenna = _OriWirelessIfAntenna_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 32),
    _OriWirelessIfAntenna_Type()
)
oriWirelessIfAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfAntenna.setStatus("deprecated")


class _OriWirelessIfTPCMode_Type(Integer32):
    """Custom type oriWirelessIfTPCMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(18, 18),
    )


_OriWirelessIfTPCMode_Type.__name__ = "Integer32"
_OriWirelessIfTPCMode_Object = MibTableColumn
oriWirelessIfTPCMode = _OriWirelessIfTPCMode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 33),
    _OriWirelessIfTPCMode_Type()
)
oriWirelessIfTPCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfTPCMode.setStatus("current")


class _OriWirelessIfSuperModeStatus_Type(ObjStatus):
    """Custom type oriWirelessIfSuperModeStatus based on ObjStatus"""


_OriWirelessIfSuperModeStatus_Object = MibTableColumn
oriWirelessIfSuperModeStatus = _OriWirelessIfSuperModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 34),
    _OriWirelessIfSuperModeStatus_Type()
)
oriWirelessIfSuperModeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfSuperModeStatus.setStatus("current")


class _OriWirelessIfWSSStatus_Type(Integer32):
    """Custom type oriWirelessIfWSSStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_OriWirelessIfWSSStatus_Type.__name__ = "Integer32"
_OriWirelessIfWSSStatus_Object = MibTableColumn
oriWirelessIfWSSStatus = _OriWirelessIfWSSStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 35),
    _OriWirelessIfWSSStatus_Type()
)
oriWirelessIfWSSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfWSSStatus.setStatus("current")
_OriWirelessIfSupportedAuthenticationModes_Type = DisplayString
_OriWirelessIfSupportedAuthenticationModes_Object = MibTableColumn
oriWirelessIfSupportedAuthenticationModes = _OriWirelessIfSupportedAuthenticationModes_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 36),
    _OriWirelessIfSupportedAuthenticationModes_Type()
)
oriWirelessIfSupportedAuthenticationModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWirelessIfSupportedAuthenticationModes.setStatus("current")
_OriWirelessIfSupportedCipherModes_Type = DisplayString
_OriWirelessIfSupportedCipherModes_Object = MibTableColumn
oriWirelessIfSupportedCipherModes = _OriWirelessIfSupportedCipherModes_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 37),
    _OriWirelessIfSupportedCipherModes_Type()
)
oriWirelessIfSupportedCipherModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWirelessIfSupportedCipherModes.setStatus("current")


class _OriWirelessIfQoSStatus_Type(ObjStatus):
    """Custom type oriWirelessIfQoSStatus based on ObjStatus"""


_OriWirelessIfQoSStatus_Object = MibTableColumn
oriWirelessIfQoSStatus = _OriWirelessIfQoSStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 38),
    _OriWirelessIfQoSStatus_Type()
)
oriWirelessIfQoSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfQoSStatus.setStatus("current")


class _OriWirelessIfQoSMaxMediumThreshold_Type(Integer32):
    """Custom type oriWirelessIfQoSMaxMediumThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 90),
    )


_OriWirelessIfQoSMaxMediumThreshold_Type.__name__ = "Integer32"
_OriWirelessIfQoSMaxMediumThreshold_Object = MibTableColumn
oriWirelessIfQoSMaxMediumThreshold = _OriWirelessIfQoSMaxMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 39),
    _OriWirelessIfQoSMaxMediumThreshold_Type()
)
oriWirelessIfQoSMaxMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfQoSMaxMediumThreshold.setStatus("current")


class _OriWirelessIfAntennaGain_Type(Integer32):
    """Custom type oriWirelessIfAntennaGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35),
    )


_OriWirelessIfAntennaGain_Type.__name__ = "Integer32"
_OriWirelessIfAntennaGain_Object = MibTableColumn
oriWirelessIfAntennaGain = _OriWirelessIfAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 1, 1, 40),
    _OriWirelessIfAntennaGain_Type()
)
oriWirelessIfAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfAntennaGain.setStatus("current")
_OriWirelessIfSecurityTable_Object = MibTable
oriWirelessIfSecurityTable = _OriWirelessIfSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    oriWirelessIfSecurityTable.setStatus("current")
_OriWirelessIfSecurityEntry_Object = MibTableRow
oriWirelessIfSecurityEntry = _OriWirelessIfSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 2, 1)
)
oriWirelessIfSecurityEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriWirelessIfSecurityIndex"),
)
if mibBuilder.loadTexts:
    oriWirelessIfSecurityEntry.setStatus("current")
_OriWirelessIfSecurityIndex_Type = Integer32
_OriWirelessIfSecurityIndex_Object = MibTableColumn
oriWirelessIfSecurityIndex = _OriWirelessIfSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 2, 1, 1),
    _OriWirelessIfSecurityIndex_Type()
)
oriWirelessIfSecurityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWirelessIfSecurityIndex.setStatus("current")


class _OriWirelessIfEncryptionOptions_Type(Integer32):
    """Custom type oriWirelessIfEncryptionOptions based on Integer32"""
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
        *(("aes", 4),
          ("none", 1),
          ("rcFour128", 3),
          ("wep", 2))
    )


_OriWirelessIfEncryptionOptions_Type.__name__ = "Integer32"
_OriWirelessIfEncryptionOptions_Object = MibTableColumn
oriWirelessIfEncryptionOptions = _OriWirelessIfEncryptionOptions_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 2, 1, 2),
    _OriWirelessIfEncryptionOptions_Type()
)
oriWirelessIfEncryptionOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfEncryptionOptions.setStatus("current")


class _OriWirelessIfEncryptionStatus_Type(Integer32):
    """Custom type oriWirelessIfEncryptionStatus based on Integer32"""
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


_OriWirelessIfEncryptionStatus_Type.__name__ = "Integer32"
_OriWirelessIfEncryptionStatus_Object = MibTableColumn
oriWirelessIfEncryptionStatus = _OriWirelessIfEncryptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 2, 1, 3),
    _OriWirelessIfEncryptionStatus_Type()
)
oriWirelessIfEncryptionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfEncryptionStatus.setStatus("deprecated")
_OriWirelessIfEncryptionKey1_Type = DisplayString
_OriWirelessIfEncryptionKey1_Object = MibTableColumn
oriWirelessIfEncryptionKey1 = _OriWirelessIfEncryptionKey1_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 2, 1, 4),
    _OriWirelessIfEncryptionKey1_Type()
)
oriWirelessIfEncryptionKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfEncryptionKey1.setStatus("current")
_OriWirelessIfEncryptionKey2_Type = DisplayString
_OriWirelessIfEncryptionKey2_Object = MibTableColumn
oriWirelessIfEncryptionKey2 = _OriWirelessIfEncryptionKey2_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 2, 1, 5),
    _OriWirelessIfEncryptionKey2_Type()
)
oriWirelessIfEncryptionKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfEncryptionKey2.setStatus("current")
_OriWirelessIfEncryptionKey3_Type = DisplayString
_OriWirelessIfEncryptionKey3_Object = MibTableColumn
oriWirelessIfEncryptionKey3 = _OriWirelessIfEncryptionKey3_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 2, 1, 6),
    _OriWirelessIfEncryptionKey3_Type()
)
oriWirelessIfEncryptionKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfEncryptionKey3.setStatus("current")
_OriWirelessIfEncryptionKey4_Type = DisplayString
_OriWirelessIfEncryptionKey4_Object = MibTableColumn
oriWirelessIfEncryptionKey4 = _OriWirelessIfEncryptionKey4_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 2, 1, 7),
    _OriWirelessIfEncryptionKey4_Type()
)
oriWirelessIfEncryptionKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfEncryptionKey4.setStatus("current")


class _OriWirelessIfEncryptionTxKey_Type(Integer32):
    """Custom type oriWirelessIfEncryptionTxKey based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_OriWirelessIfEncryptionTxKey_Type.__name__ = "Integer32"
_OriWirelessIfEncryptionTxKey_Object = MibTableColumn
oriWirelessIfEncryptionTxKey = _OriWirelessIfEncryptionTxKey_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 2, 1, 8),
    _OriWirelessIfEncryptionTxKey_Type()
)
oriWirelessIfEncryptionTxKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfEncryptionTxKey.setStatus("current")


class _OriWirelessIfDenyNonEncryptedData_Type(Integer32):
    """Custom type oriWirelessIfDenyNonEncryptedData based on Integer32"""
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


_OriWirelessIfDenyNonEncryptedData_Type.__name__ = "Integer32"
_OriWirelessIfDenyNonEncryptedData_Object = MibTableColumn
oriWirelessIfDenyNonEncryptedData = _OriWirelessIfDenyNonEncryptedData_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 2, 1, 9),
    _OriWirelessIfDenyNonEncryptedData_Type()
)
oriWirelessIfDenyNonEncryptedData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfDenyNonEncryptedData.setStatus("current")
_OriWirelessIfProfileCode_Type = Integer32
_OriWirelessIfProfileCode_Object = MibTableColumn
oriWirelessIfProfileCode = _OriWirelessIfProfileCode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 2, 1, 10),
    _OriWirelessIfProfileCode_Type()
)
oriWirelessIfProfileCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWirelessIfProfileCode.setStatus("current")
_OriWirelessIfSSIDTable_Object = MibTable
oriWirelessIfSSIDTable = _OriWirelessIfSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTable.setStatus("current")
_OriWirelessIfSSIDTableEntry_Object = MibTableRow
oriWirelessIfSSIDTableEntry = _OriWirelessIfSSIDTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1)
)
oriWirelessIfSSIDTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ORiNOCO-MIB", "oriWirelessIfSSIDTableIndex"),
)
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableEntry.setStatus("current")


class _OriWirelessIfSSIDTableIndex_Type(Integer32):
    """Custom type oriWirelessIfSSIDTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OriWirelessIfSSIDTableIndex_Type.__name__ = "Integer32"
_OriWirelessIfSSIDTableIndex_Object = MibTableColumn
oriWirelessIfSSIDTableIndex = _OriWirelessIfSSIDTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 1),
    _OriWirelessIfSSIDTableIndex_Type()
)
oriWirelessIfSSIDTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableIndex.setStatus("current")


class _OriWirelessIfSSIDTableSSID_Type(DisplayString):
    """Custom type oriWirelessIfSSIDTableSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OriWirelessIfSSIDTableSSID_Type.__name__ = "DisplayString"
_OriWirelessIfSSIDTableSSID_Object = MibTableColumn
oriWirelessIfSSIDTableSSID = _OriWirelessIfSSIDTableSSID_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 2),
    _OriWirelessIfSSIDTableSSID_Type()
)
oriWirelessIfSSIDTableSSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableSSID.setStatus("current")


class _OriWirelessIfSSIDTableVLANID_Type(VlanId):
    """Custom type oriWirelessIfSSIDTableVLANID based on VlanId"""
    defaultValue = -1


_OriWirelessIfSSIDTableVLANID_Object = MibTableColumn
oriWirelessIfSSIDTableVLANID = _OriWirelessIfSSIDTableVLANID_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 3),
    _OriWirelessIfSSIDTableVLANID_Type()
)
oriWirelessIfSSIDTableVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableVLANID.setStatus("current")
_OriWirelessIfSSIDTableStatus_Type = RowStatus
_OriWirelessIfSSIDTableStatus_Object = MibTableColumn
oriWirelessIfSSIDTableStatus = _OriWirelessIfSSIDTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 4),
    _OriWirelessIfSSIDTableStatus_Type()
)
oriWirelessIfSSIDTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableStatus.setStatus("current")


class _OriWirelessIfSSIDTableSecurityMode_Type(Integer32):
    """Custom type oriWirelessIfSSIDTableSecurityMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 2),
          ("mixed", 3),
          ("none", 1),
          ("wep", 6),
          ("wpa", 4),
          ("wpa-psk", 5))
    )


_OriWirelessIfSSIDTableSecurityMode_Type.__name__ = "Integer32"
_OriWirelessIfSSIDTableSecurityMode_Object = MibTableColumn
oriWirelessIfSSIDTableSecurityMode = _OriWirelessIfSSIDTableSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 5),
    _OriWirelessIfSSIDTableSecurityMode_Type()
)
oriWirelessIfSSIDTableSecurityMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableSecurityMode.setStatus("deprecated")


class _OriWirelessIfSSIDTableBroadcastSSID_Type(ObjStatus):
    """Custom type oriWirelessIfSSIDTableBroadcastSSID based on ObjStatus"""


_OriWirelessIfSSIDTableBroadcastSSID_Object = MibTableColumn
oriWirelessIfSSIDTableBroadcastSSID = _OriWirelessIfSSIDTableBroadcastSSID_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 6),
    _OriWirelessIfSSIDTableBroadcastSSID_Type()
)
oriWirelessIfSSIDTableBroadcastSSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableBroadcastSSID.setStatus("current")


class _OriWirelessIfSSIDTableClosedSystem_Type(ObjStatus):
    """Custom type oriWirelessIfSSIDTableClosedSystem based on ObjStatus"""


_OriWirelessIfSSIDTableClosedSystem_Object = MibTableColumn
oriWirelessIfSSIDTableClosedSystem = _OriWirelessIfSSIDTableClosedSystem_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 7),
    _OriWirelessIfSSIDTableClosedSystem_Type()
)
oriWirelessIfSSIDTableClosedSystem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableClosedSystem.setStatus("current")
_OriWirelessIfSSIDTableSupportedSecurityModes_Type = DisplayString
_OriWirelessIfSSIDTableSupportedSecurityModes_Object = MibTableColumn
oriWirelessIfSSIDTableSupportedSecurityModes = _OriWirelessIfSSIDTableSupportedSecurityModes_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 8),
    _OriWirelessIfSSIDTableSupportedSecurityModes_Type()
)
oriWirelessIfSSIDTableSupportedSecurityModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableSupportedSecurityModes.setStatus("deprecated")
_OriWirelessIfSSIDTableEncryptionKey0_Type = WEPKeyType
_OriWirelessIfSSIDTableEncryptionKey0_Object = MibTableColumn
oriWirelessIfSSIDTableEncryptionKey0 = _OriWirelessIfSSIDTableEncryptionKey0_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 9),
    _OriWirelessIfSSIDTableEncryptionKey0_Type()
)
oriWirelessIfSSIDTableEncryptionKey0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableEncryptionKey0.setStatus("deprecated")
_OriWirelessIfSSIDTableEncryptionKey1_Type = WEPKeyType
_OriWirelessIfSSIDTableEncryptionKey1_Object = MibTableColumn
oriWirelessIfSSIDTableEncryptionKey1 = _OriWirelessIfSSIDTableEncryptionKey1_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 10),
    _OriWirelessIfSSIDTableEncryptionKey1_Type()
)
oriWirelessIfSSIDTableEncryptionKey1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableEncryptionKey1.setStatus("deprecated")
_OriWirelessIfSSIDTableEncryptionKey2_Type = WEPKeyType
_OriWirelessIfSSIDTableEncryptionKey2_Object = MibTableColumn
oriWirelessIfSSIDTableEncryptionKey2 = _OriWirelessIfSSIDTableEncryptionKey2_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 11),
    _OriWirelessIfSSIDTableEncryptionKey2_Type()
)
oriWirelessIfSSIDTableEncryptionKey2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableEncryptionKey2.setStatus("deprecated")
_OriWirelessIfSSIDTableEncryptionKey3_Type = WEPKeyType
_OriWirelessIfSSIDTableEncryptionKey3_Object = MibTableColumn
oriWirelessIfSSIDTableEncryptionKey3 = _OriWirelessIfSSIDTableEncryptionKey3_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 12),
    _OriWirelessIfSSIDTableEncryptionKey3_Type()
)
oriWirelessIfSSIDTableEncryptionKey3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableEncryptionKey3.setStatus("deprecated")


class _OriWirelessIfSSIDTableEncryptionTxKey_Type(Integer32):
    """Custom type oriWirelessIfSSIDTableEncryptionTxKey based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_OriWirelessIfSSIDTableEncryptionTxKey_Type.__name__ = "Integer32"
_OriWirelessIfSSIDTableEncryptionTxKey_Object = MibTableColumn
oriWirelessIfSSIDTableEncryptionTxKey = _OriWirelessIfSSIDTableEncryptionTxKey_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 13),
    _OriWirelessIfSSIDTableEncryptionTxKey_Type()
)
oriWirelessIfSSIDTableEncryptionTxKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableEncryptionTxKey.setStatus("deprecated")


class _OriWirelessIfSSIDTableEncryptionKeyLength_Type(Integer32):
    """Custom type oriWirelessIfSSIDTableEncryptionKeyLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneHundredFiftyTwoBits", 3),
          ("oneHundredTwentyEightBits", 2),
          ("sixtyFourBits", 1))
    )


_OriWirelessIfSSIDTableEncryptionKeyLength_Type.__name__ = "Integer32"
_OriWirelessIfSSIDTableEncryptionKeyLength_Object = MibTableColumn
oriWirelessIfSSIDTableEncryptionKeyLength = _OriWirelessIfSSIDTableEncryptionKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 14),
    _OriWirelessIfSSIDTableEncryptionKeyLength_Type()
)
oriWirelessIfSSIDTableEncryptionKeyLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableEncryptionKeyLength.setStatus("deprecated")


class _OriWirelessIfSSIDTableRekeyingInterval_Type(Integer32):
    """Custom type oriWirelessIfSSIDTableRekeyingInterval based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 65535),
    )


_OriWirelessIfSSIDTableRekeyingInterval_Type.__name__ = "Integer32"
_OriWirelessIfSSIDTableRekeyingInterval_Object = MibTableColumn
oriWirelessIfSSIDTableRekeyingInterval = _OriWirelessIfSSIDTableRekeyingInterval_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 15),
    _OriWirelessIfSSIDTableRekeyingInterval_Type()
)
oriWirelessIfSSIDTableRekeyingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableRekeyingInterval.setStatus("current")


class _OriWirelessIfSSIDTablePSKValue_Type(OctetString):
    """Custom type oriWirelessIfSSIDTablePSKValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_OriWirelessIfSSIDTablePSKValue_Type.__name__ = "OctetString"
_OriWirelessIfSSIDTablePSKValue_Object = MibTableColumn
oriWirelessIfSSIDTablePSKValue = _OriWirelessIfSSIDTablePSKValue_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 16),
    _OriWirelessIfSSIDTablePSKValue_Type()
)
oriWirelessIfSSIDTablePSKValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTablePSKValue.setStatus("deprecated")
_OriWirelessIfSSIDTablePSKPassPhrase_Type = DisplayString
_OriWirelessIfSSIDTablePSKPassPhrase_Object = MibTableColumn
oriWirelessIfSSIDTablePSKPassPhrase = _OriWirelessIfSSIDTablePSKPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 17),
    _OriWirelessIfSSIDTablePSKPassPhrase_Type()
)
oriWirelessIfSSIDTablePSKPassPhrase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTablePSKPassPhrase.setStatus("deprecated")


class _OriWirelessIfSSIDTableDenyNonEncryptedData_Type(ObjStatus):
    """Custom type oriWirelessIfSSIDTableDenyNonEncryptedData based on ObjStatus"""


_OriWirelessIfSSIDTableDenyNonEncryptedData_Object = MibTableColumn
oriWirelessIfSSIDTableDenyNonEncryptedData = _OriWirelessIfSSIDTableDenyNonEncryptedData_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 18),
    _OriWirelessIfSSIDTableDenyNonEncryptedData_Type()
)
oriWirelessIfSSIDTableDenyNonEncryptedData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableDenyNonEncryptedData.setStatus("deprecated")


class _OriWirelessIfSSIDTableSSIDAuthorizationStatus_Type(ObjStatus):
    """Custom type oriWirelessIfSSIDTableSSIDAuthorizationStatus based on ObjStatus"""


_OriWirelessIfSSIDTableSSIDAuthorizationStatus_Object = MibTableColumn
oriWirelessIfSSIDTableSSIDAuthorizationStatus = _OriWirelessIfSSIDTableSSIDAuthorizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 19),
    _OriWirelessIfSSIDTableSSIDAuthorizationStatus_Type()
)
oriWirelessIfSSIDTableSSIDAuthorizationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableSSIDAuthorizationStatus.setStatus("current")


class _OriWirelessIfSSIDTableMACAccessControl_Type(ObjStatus):
    """Custom type oriWirelessIfSSIDTableMACAccessControl based on ObjStatus"""


_OriWirelessIfSSIDTableMACAccessControl_Object = MibTableColumn
oriWirelessIfSSIDTableMACAccessControl = _OriWirelessIfSSIDTableMACAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 20),
    _OriWirelessIfSSIDTableMACAccessControl_Type()
)
oriWirelessIfSSIDTableMACAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableMACAccessControl.setStatus("current")


class _OriWirelessIfSSIDTableRADIUSMACAccessControl_Type(ObjStatus):
    """Custom type oriWirelessIfSSIDTableRADIUSMACAccessControl based on ObjStatus"""


_OriWirelessIfSSIDTableRADIUSMACAccessControl_Object = MibTableColumn
oriWirelessIfSSIDTableRADIUSMACAccessControl = _OriWirelessIfSSIDTableRADIUSMACAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 21),
    _OriWirelessIfSSIDTableRADIUSMACAccessControl_Type()
)
oriWirelessIfSSIDTableRADIUSMACAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableRADIUSMACAccessControl.setStatus("current")
_OriWirelessIfSSIDTableSecurityProfile_Type = Integer32
_OriWirelessIfSSIDTableSecurityProfile_Object = MibTableColumn
oriWirelessIfSSIDTableSecurityProfile = _OriWirelessIfSSIDTableSecurityProfile_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 22),
    _OriWirelessIfSSIDTableSecurityProfile_Type()
)
oriWirelessIfSSIDTableSecurityProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableSecurityProfile.setStatus("current")
_OriWirelessIfSSIDTableRADIUSDot1xProfile_Type = DisplayString
_OriWirelessIfSSIDTableRADIUSDot1xProfile_Object = MibTableColumn
oriWirelessIfSSIDTableRADIUSDot1xProfile = _OriWirelessIfSSIDTableRADIUSDot1xProfile_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 23),
    _OriWirelessIfSSIDTableRADIUSDot1xProfile_Type()
)
oriWirelessIfSSIDTableRADIUSDot1xProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableRADIUSDot1xProfile.setStatus("current")
_OriWirelessIfSSIDTableRADIUSMACAuthProfile_Type = DisplayString
_OriWirelessIfSSIDTableRADIUSMACAuthProfile_Object = MibTableColumn
oriWirelessIfSSIDTableRADIUSMACAuthProfile = _OriWirelessIfSSIDTableRADIUSMACAuthProfile_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 24),
    _OriWirelessIfSSIDTableRADIUSMACAuthProfile_Type()
)
oriWirelessIfSSIDTableRADIUSMACAuthProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableRADIUSMACAuthProfile.setStatus("current")


class _OriWirelessIfSSIDTableRADIUSAccountingStatus_Type(ObjStatus):
    """Custom type oriWirelessIfSSIDTableRADIUSAccountingStatus based on ObjStatus"""


_OriWirelessIfSSIDTableRADIUSAccountingStatus_Object = MibTableColumn
oriWirelessIfSSIDTableRADIUSAccountingStatus = _OriWirelessIfSSIDTableRADIUSAccountingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 25),
    _OriWirelessIfSSIDTableRADIUSAccountingStatus_Type()
)
oriWirelessIfSSIDTableRADIUSAccountingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableRADIUSAccountingStatus.setStatus("current")
_OriWirelessIfSSIDTableRADIUSAccountingProfile_Type = DisplayString
_OriWirelessIfSSIDTableRADIUSAccountingProfile_Object = MibTableColumn
oriWirelessIfSSIDTableRADIUSAccountingProfile = _OriWirelessIfSSIDTableRADIUSAccountingProfile_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 26),
    _OriWirelessIfSSIDTableRADIUSAccountingProfile_Type()
)
oriWirelessIfSSIDTableRADIUSAccountingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableRADIUSAccountingProfile.setStatus("current")
_OriWirelessIfSSIDTableQoSPolicy_Type = Integer32
_OriWirelessIfSSIDTableQoSPolicy_Object = MibTableColumn
oriWirelessIfSSIDTableQoSPolicy = _OriWirelessIfSSIDTableQoSPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 3, 1, 27),
    _OriWirelessIfSSIDTableQoSPolicy_Type()
)
oriWirelessIfSSIDTableQoSPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriWirelessIfSSIDTableQoSPolicy.setStatus("current")


class _OriWirelessIfTxPowerControl_Type(ObjStatus):
    """Custom type oriWirelessIfTxPowerControl based on ObjStatus"""


_OriWirelessIfTxPowerControl_Object = MibScalar
oriWirelessIfTxPowerControl = _OriWirelessIfTxPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 1, 4),
    _OriWirelessIfTxPowerControl_Type()
)
oriWirelessIfTxPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfTxPowerControl.setStatus("current")
_OrinocoEthernetIf_ObjectIdentity = ObjectIdentity
orinocoEthernetIf = _OrinocoEthernetIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 2)
)
_OriEthernetIfConfigTable_Object = MibTable
oriEthernetIfConfigTable = _OriEthernetIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    oriEthernetIfConfigTable.setStatus("current")
_OriEthernetIfConfigTableEntry_Object = MibTableRow
oriEthernetIfConfigTableEntry = _OriEthernetIfConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 2, 1, 1)
)
oriEthernetIfConfigTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriEthernetIfConfigTableIndex"),
)
if mibBuilder.loadTexts:
    oriEthernetIfConfigTableEntry.setStatus("current")
_OriEthernetIfConfigTableIndex_Type = Integer32
_OriEthernetIfConfigTableIndex_Object = MibTableColumn
oriEthernetIfConfigTableIndex = _OriEthernetIfConfigTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 2, 1, 1, 1),
    _OriEthernetIfConfigTableIndex_Type()
)
oriEthernetIfConfigTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriEthernetIfConfigTableIndex.setStatus("current")


class _OriEthernetIfConfigSettings_Type(Integer32):
    """Custom type oriEthernetIfConfigSettings based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("autoSpeedAutoDuplex", 7),
          ("autoSpeedHalfDuplex", 6),
          ("onehundredMegabitPerSecAutoDuplex", 8),
          ("onehundredMegabitPerSecFullDuplex", 5),
          ("onehundredMegabitPerSecHalfDuplex", 4),
          ("tenMegabitPerSecAutoDuplex", 3),
          ("tenMegabitPerSecFullDuplex", 2),
          ("tenMegabitPerSecHalfDuplex", 1))
    )


_OriEthernetIfConfigSettings_Type.__name__ = "Integer32"
_OriEthernetIfConfigSettings_Object = MibTableColumn
oriEthernetIfConfigSettings = _OriEthernetIfConfigSettings_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 2, 1, 1, 2),
    _OriEthernetIfConfigSettings_Type()
)
oriEthernetIfConfigSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriEthernetIfConfigSettings.setStatus("current")
_OriEthernetIfConfigBandwidthLimitIn_Type = Gauge32
_OriEthernetIfConfigBandwidthLimitIn_Object = MibTableColumn
oriEthernetIfConfigBandwidthLimitIn = _OriEthernetIfConfigBandwidthLimitIn_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 2, 1, 1, 3),
    _OriEthernetIfConfigBandwidthLimitIn_Type()
)
oriEthernetIfConfigBandwidthLimitIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriEthernetIfConfigBandwidthLimitIn.setStatus("current")
_OriEthernetIfConfigBandwidthLimitOut_Type = Gauge32
_OriEthernetIfConfigBandwidthLimitOut_Object = MibTableColumn
oriEthernetIfConfigBandwidthLimitOut = _OriEthernetIfConfigBandwidthLimitOut_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 2, 1, 1, 4),
    _OriEthernetIfConfigBandwidthLimitOut_Type()
)
oriEthernetIfConfigBandwidthLimitOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriEthernetIfConfigBandwidthLimitOut.setStatus("current")
_OriIfWANInterfaceMACAddress_Type = PhysAddress
_OriIfWANInterfaceMACAddress_Object = MibScalar
oriIfWANInterfaceMACAddress = _OriIfWANInterfaceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 4),
    _OriIfWANInterfaceMACAddress_Type()
)
oriIfWANInterfaceMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIfWANInterfaceMACAddress.setStatus("current")
_OrinocoWORPIf_ObjectIdentity = ObjectIdentity
orinocoWORPIf = _OrinocoWORPIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5)
)
_OriWORPIfConfigTable_Object = MibTable
oriWORPIfConfigTable = _OriWORPIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    oriWORPIfConfigTable.setStatus("current")
_OriWORPIfConfigTableEntry_Object = MibTableRow
oriWORPIfConfigTableEntry = _OriWORPIfConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 1, 1)
)
oriWORPIfConfigTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oriWORPIfConfigTableEntry.setStatus("current")


class _OriWORPIfConfigTableMode_Type(Integer32):
    """Custom type oriWORPIfConfigTableMode based on Integer32"""
    defaultValue = 1

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
        *(("ap", 2),
          ("base", 3),
          ("disabled", 1),
          ("satellite", 4))
    )


_OriWORPIfConfigTableMode_Type.__name__ = "Integer32"
_OriWORPIfConfigTableMode_Object = MibTableColumn
oriWORPIfConfigTableMode = _OriWORPIfConfigTableMode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 1, 1, 1),
    _OriWORPIfConfigTableMode_Type()
)
oriWORPIfConfigTableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfConfigTableMode.setStatus("current")
_OriWORPIfConfigTableBaseStationName_Type = DisplayString
_OriWORPIfConfigTableBaseStationName_Object = MibTableColumn
oriWORPIfConfigTableBaseStationName = _OriWORPIfConfigTableBaseStationName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 1, 1, 2),
    _OriWORPIfConfigTableBaseStationName_Type()
)
oriWORPIfConfigTableBaseStationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfConfigTableBaseStationName.setStatus("current")
_OriWORPIfConfigTableMaxSatellites_Type = Integer32
_OriWORPIfConfigTableMaxSatellites_Object = MibTableColumn
oriWORPIfConfigTableMaxSatellites = _OriWORPIfConfigTableMaxSatellites_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 1, 1, 3),
    _OriWORPIfConfigTableMaxSatellites_Type()
)
oriWORPIfConfigTableMaxSatellites.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfConfigTableMaxSatellites.setStatus("current")


class _OriWORPIfConfigTableRegistrationTimeout_Type(Integer32):
    """Custom type oriWORPIfConfigTableRegistrationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_OriWORPIfConfigTableRegistrationTimeout_Type.__name__ = "Integer32"
_OriWORPIfConfigTableRegistrationTimeout_Object = MibTableColumn
oriWORPIfConfigTableRegistrationTimeout = _OriWORPIfConfigTableRegistrationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 1, 1, 4),
    _OriWORPIfConfigTableRegistrationTimeout_Type()
)
oriWORPIfConfigTableRegistrationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfConfigTableRegistrationTimeout.setStatus("current")


class _OriWORPIfConfigTableRetries_Type(Integer32):
    """Custom type oriWORPIfConfigTableRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_OriWORPIfConfigTableRetries_Type.__name__ = "Integer32"
_OriWORPIfConfigTableRetries_Object = MibTableColumn
oriWORPIfConfigTableRetries = _OriWORPIfConfigTableRetries_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 1, 1, 5),
    _OriWORPIfConfigTableRetries_Type()
)
oriWORPIfConfigTableRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfConfigTableRetries.setStatus("current")
_OriWORPIfConfigTableNetworkSecret_Type = DisplayString
_OriWORPIfConfigTableNetworkSecret_Object = MibTableColumn
oriWORPIfConfigTableNetworkSecret = _OriWORPIfConfigTableNetworkSecret_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 1, 1, 6),
    _OriWORPIfConfigTableNetworkSecret_Type()
)
oriWORPIfConfigTableNetworkSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfConfigTableNetworkSecret.setStatus("current")


class _OriWORPIfConfigTableNoSleepMode_Type(ObjStatus):
    """Custom type oriWORPIfConfigTableNoSleepMode based on ObjStatus"""


_OriWORPIfConfigTableNoSleepMode_Object = MibTableColumn
oriWORPIfConfigTableNoSleepMode = _OriWORPIfConfigTableNoSleepMode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 1, 1, 7),
    _OriWORPIfConfigTableNoSleepMode_Type()
)
oriWORPIfConfigTableNoSleepMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfConfigTableNoSleepMode.setStatus("current")
_OriWORPIfStatTable_Object = MibTable
oriWORPIfStatTable = _OriWORPIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    oriWORPIfStatTable.setStatus("current")
_OriWORPIfStatTableEntry_Object = MibTableRow
oriWORPIfStatTableEntry = _OriWORPIfStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1)
)
oriWORPIfStatTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oriWORPIfStatTableEntry.setStatus("current")
_OriWORPIfStatTableRemotePartners_Type = Counter32
_OriWORPIfStatTableRemotePartners_Object = MibTableColumn
oriWORPIfStatTableRemotePartners = _OriWORPIfStatTableRemotePartners_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 1),
    _OriWORPIfStatTableRemotePartners_Type()
)
oriWORPIfStatTableRemotePartners.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableRemotePartners.setStatus("current")


class _OriWORPIfStatTableAverageLocalSignal_Type(Integer32):
    """Custom type oriWORPIfStatTableAverageLocalSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_OriWORPIfStatTableAverageLocalSignal_Type.__name__ = "Integer32"
_OriWORPIfStatTableAverageLocalSignal_Object = MibTableColumn
oriWORPIfStatTableAverageLocalSignal = _OriWORPIfStatTableAverageLocalSignal_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 2),
    _OriWORPIfStatTableAverageLocalSignal_Type()
)
oriWORPIfStatTableAverageLocalSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableAverageLocalSignal.setStatus("current")


class _OriWORPIfStatTableAverageLocalNoise_Type(Integer32):
    """Custom type oriWORPIfStatTableAverageLocalNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_OriWORPIfStatTableAverageLocalNoise_Type.__name__ = "Integer32"
_OriWORPIfStatTableAverageLocalNoise_Object = MibTableColumn
oriWORPIfStatTableAverageLocalNoise = _OriWORPIfStatTableAverageLocalNoise_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 3),
    _OriWORPIfStatTableAverageLocalNoise_Type()
)
oriWORPIfStatTableAverageLocalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableAverageLocalNoise.setStatus("current")


class _OriWORPIfStatTableAverageRemoteSignal_Type(Integer32):
    """Custom type oriWORPIfStatTableAverageRemoteSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_OriWORPIfStatTableAverageRemoteSignal_Type.__name__ = "Integer32"
_OriWORPIfStatTableAverageRemoteSignal_Object = MibTableColumn
oriWORPIfStatTableAverageRemoteSignal = _OriWORPIfStatTableAverageRemoteSignal_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 4),
    _OriWORPIfStatTableAverageRemoteSignal_Type()
)
oriWORPIfStatTableAverageRemoteSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableAverageRemoteSignal.setStatus("current")


class _OriWORPIfStatTableAverageRemoteNoise_Type(Integer32):
    """Custom type oriWORPIfStatTableAverageRemoteNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_OriWORPIfStatTableAverageRemoteNoise_Type.__name__ = "Integer32"
_OriWORPIfStatTableAverageRemoteNoise_Object = MibTableColumn
oriWORPIfStatTableAverageRemoteNoise = _OriWORPIfStatTableAverageRemoteNoise_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 5),
    _OriWORPIfStatTableAverageRemoteNoise_Type()
)
oriWORPIfStatTableAverageRemoteNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableAverageRemoteNoise.setStatus("current")
_OriWORPIfStatTableBaseStationAnnounces_Type = Counter32
_OriWORPIfStatTableBaseStationAnnounces_Object = MibTableColumn
oriWORPIfStatTableBaseStationAnnounces = _OriWORPIfStatTableBaseStationAnnounces_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 6),
    _OriWORPIfStatTableBaseStationAnnounces_Type()
)
oriWORPIfStatTableBaseStationAnnounces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableBaseStationAnnounces.setStatus("current")
_OriWORPIfStatTableRegistrationRequests_Type = Counter32
_OriWORPIfStatTableRegistrationRequests_Object = MibTableColumn
oriWORPIfStatTableRegistrationRequests = _OriWORPIfStatTableRegistrationRequests_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 7),
    _OriWORPIfStatTableRegistrationRequests_Type()
)
oriWORPIfStatTableRegistrationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableRegistrationRequests.setStatus("current")
_OriWORPIfStatTableRegistrationRejects_Type = Counter32
_OriWORPIfStatTableRegistrationRejects_Object = MibTableColumn
oriWORPIfStatTableRegistrationRejects = _OriWORPIfStatTableRegistrationRejects_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 8),
    _OriWORPIfStatTableRegistrationRejects_Type()
)
oriWORPIfStatTableRegistrationRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableRegistrationRejects.setStatus("current")
_OriWORPIfStatTableAuthenticationRequests_Type = Counter32
_OriWORPIfStatTableAuthenticationRequests_Object = MibTableColumn
oriWORPIfStatTableAuthenticationRequests = _OriWORPIfStatTableAuthenticationRequests_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 9),
    _OriWORPIfStatTableAuthenticationRequests_Type()
)
oriWORPIfStatTableAuthenticationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableAuthenticationRequests.setStatus("current")
_OriWORPIfStatTableAuthenticationConfirms_Type = Counter32
_OriWORPIfStatTableAuthenticationConfirms_Object = MibTableColumn
oriWORPIfStatTableAuthenticationConfirms = _OriWORPIfStatTableAuthenticationConfirms_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 10),
    _OriWORPIfStatTableAuthenticationConfirms_Type()
)
oriWORPIfStatTableAuthenticationConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableAuthenticationConfirms.setStatus("current")
_OriWORPIfStatTableRegistrationAttempts_Type = Counter32
_OriWORPIfStatTableRegistrationAttempts_Object = MibTableColumn
oriWORPIfStatTableRegistrationAttempts = _OriWORPIfStatTableRegistrationAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 11),
    _OriWORPIfStatTableRegistrationAttempts_Type()
)
oriWORPIfStatTableRegistrationAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableRegistrationAttempts.setStatus("current")
_OriWORPIfStatTableRegistrationIncompletes_Type = Counter32
_OriWORPIfStatTableRegistrationIncompletes_Object = MibTableColumn
oriWORPIfStatTableRegistrationIncompletes = _OriWORPIfStatTableRegistrationIncompletes_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 12),
    _OriWORPIfStatTableRegistrationIncompletes_Type()
)
oriWORPIfStatTableRegistrationIncompletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableRegistrationIncompletes.setStatus("current")
_OriWORPIfStatTableRegistrationTimeouts_Type = Counter32
_OriWORPIfStatTableRegistrationTimeouts_Object = MibTableColumn
oriWORPIfStatTableRegistrationTimeouts = _OriWORPIfStatTableRegistrationTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 13),
    _OriWORPIfStatTableRegistrationTimeouts_Type()
)
oriWORPIfStatTableRegistrationTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableRegistrationTimeouts.setStatus("current")


class _OriWORPIfStatTableRegistrationLastReason_Type(Integer32):
    """Custom type oriWORPIfStatTableRegistrationLastReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("incorrectParameter", 3),
          ("lowQuality", 6),
          ("noMoreAllowed", 2),
          ("none", 1),
          ("roaming", 4),
          ("timeout", 5))
    )


_OriWORPIfStatTableRegistrationLastReason_Type.__name__ = "Integer32"
_OriWORPIfStatTableRegistrationLastReason_Object = MibTableColumn
oriWORPIfStatTableRegistrationLastReason = _OriWORPIfStatTableRegistrationLastReason_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 14),
    _OriWORPIfStatTableRegistrationLastReason_Type()
)
oriWORPIfStatTableRegistrationLastReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableRegistrationLastReason.setStatus("current")
_OriWORPIfStatTablePollData_Type = Counter32
_OriWORPIfStatTablePollData_Object = MibTableColumn
oriWORPIfStatTablePollData = _OriWORPIfStatTablePollData_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 15),
    _OriWORPIfStatTablePollData_Type()
)
oriWORPIfStatTablePollData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTablePollData.setStatus("current")
_OriWORPIfStatTablePollNoData_Type = Counter32
_OriWORPIfStatTablePollNoData_Object = MibTableColumn
oriWORPIfStatTablePollNoData = _OriWORPIfStatTablePollNoData_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 16),
    _OriWORPIfStatTablePollNoData_Type()
)
oriWORPIfStatTablePollNoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTablePollNoData.setStatus("current")
_OriWORPIfStatTableReplyData_Type = Counter32
_OriWORPIfStatTableReplyData_Object = MibTableColumn
oriWORPIfStatTableReplyData = _OriWORPIfStatTableReplyData_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 17),
    _OriWORPIfStatTableReplyData_Type()
)
oriWORPIfStatTableReplyData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableReplyData.setStatus("current")
_OriWORPIfStatTableReplyMoreData_Type = Counter32
_OriWORPIfStatTableReplyMoreData_Object = MibTableColumn
oriWORPIfStatTableReplyMoreData = _OriWORPIfStatTableReplyMoreData_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 18),
    _OriWORPIfStatTableReplyMoreData_Type()
)
oriWORPIfStatTableReplyMoreData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableReplyMoreData.setStatus("current")
_OriWORPIfStatTableReplyNoData_Type = Counter32
_OriWORPIfStatTableReplyNoData_Object = MibTableColumn
oriWORPIfStatTableReplyNoData = _OriWORPIfStatTableReplyNoData_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 19),
    _OriWORPIfStatTableReplyNoData_Type()
)
oriWORPIfStatTableReplyNoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableReplyNoData.setStatus("current")
_OriWORPIfStatTableRequestForService_Type = Counter32
_OriWORPIfStatTableRequestForService_Object = MibTableColumn
oriWORPIfStatTableRequestForService = _OriWORPIfStatTableRequestForService_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 20),
    _OriWORPIfStatTableRequestForService_Type()
)
oriWORPIfStatTableRequestForService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableRequestForService.setStatus("current")
_OriWORPIfStatTableSendSuccess_Type = Counter32
_OriWORPIfStatTableSendSuccess_Object = MibTableColumn
oriWORPIfStatTableSendSuccess = _OriWORPIfStatTableSendSuccess_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 21),
    _OriWORPIfStatTableSendSuccess_Type()
)
oriWORPIfStatTableSendSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableSendSuccess.setStatus("current")
_OriWORPIfStatTableSendRetries_Type = Counter32
_OriWORPIfStatTableSendRetries_Object = MibTableColumn
oriWORPIfStatTableSendRetries = _OriWORPIfStatTableSendRetries_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 22),
    _OriWORPIfStatTableSendRetries_Type()
)
oriWORPIfStatTableSendRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableSendRetries.setStatus("current")
_OriWORPIfStatTableSendFailures_Type = Counter32
_OriWORPIfStatTableSendFailures_Object = MibTableColumn
oriWORPIfStatTableSendFailures = _OriWORPIfStatTableSendFailures_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 23),
    _OriWORPIfStatTableSendFailures_Type()
)
oriWORPIfStatTableSendFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableSendFailures.setStatus("current")
_OriWORPIfStatTableReceiveSuccess_Type = Counter32
_OriWORPIfStatTableReceiveSuccess_Object = MibTableColumn
oriWORPIfStatTableReceiveSuccess = _OriWORPIfStatTableReceiveSuccess_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 24),
    _OriWORPIfStatTableReceiveSuccess_Type()
)
oriWORPIfStatTableReceiveSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableReceiveSuccess.setStatus("current")
_OriWORPIfStatTableReceiveRetries_Type = Counter32
_OriWORPIfStatTableReceiveRetries_Object = MibTableColumn
oriWORPIfStatTableReceiveRetries = _OriWORPIfStatTableReceiveRetries_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 25),
    _OriWORPIfStatTableReceiveRetries_Type()
)
oriWORPIfStatTableReceiveRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableReceiveRetries.setStatus("current")
_OriWORPIfStatTableReceiveFailures_Type = Counter32
_OriWORPIfStatTableReceiveFailures_Object = MibTableColumn
oriWORPIfStatTableReceiveFailures = _OriWORPIfStatTableReceiveFailures_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 26),
    _OriWORPIfStatTableReceiveFailures_Type()
)
oriWORPIfStatTableReceiveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTableReceiveFailures.setStatus("current")
_OriWORPIfStatTablePollNoReplies_Type = Counter32
_OriWORPIfStatTablePollNoReplies_Object = MibTableColumn
oriWORPIfStatTablePollNoReplies = _OriWORPIfStatTablePollNoReplies_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 2, 1, 27),
    _OriWORPIfStatTablePollNoReplies_Type()
)
oriWORPIfStatTablePollNoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfStatTablePollNoReplies.setStatus("current")
_OrinocoWORPIfSat_ObjectIdentity = ObjectIdentity
orinocoWORPIfSat = _OrinocoWORPIfSat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3)
)
_OrinocoWORPIfSatConfig_ObjectIdentity = ObjectIdentity
orinocoWORPIfSatConfig = _OrinocoWORPIfSatConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 1)
)


class _OriWORPIfSatConfigStatus_Type(Integer32):
    """Custom type oriWORPIfSatConfigStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_OriWORPIfSatConfigStatus_Type.__name__ = "Integer32"
_OriWORPIfSatConfigStatus_Object = MibScalar
oriWORPIfSatConfigStatus = _OriWORPIfSatConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 1, 1),
    _OriWORPIfSatConfigStatus_Type()
)
oriWORPIfSatConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfSatConfigStatus.setStatus("current")
_OriWORPIfSatConfigTable_Object = MibTable
oriWORPIfSatConfigTable = _OriWORPIfSatConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 1, 2)
)
if mibBuilder.loadTexts:
    oriWORPIfSatConfigTable.setStatus("current")
_OriWORPIfSatConfigTableEntry_Object = MibTableRow
oriWORPIfSatConfigTableEntry = _OriWORPIfSatConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 1, 2, 1)
)
oriWORPIfSatConfigTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriWORPIfSatConfigTableIndex"),
)
if mibBuilder.loadTexts:
    oriWORPIfSatConfigTableEntry.setStatus("current")
_OriWORPIfSatConfigTableIndex_Type = Integer32
_OriWORPIfSatConfigTableIndex_Object = MibTableColumn
oriWORPIfSatConfigTableIndex = _OriWORPIfSatConfigTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 1, 2, 1, 1),
    _OriWORPIfSatConfigTableIndex_Type()
)
oriWORPIfSatConfigTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatConfigTableIndex.setStatus("current")


class _OriWORPIfSatConfigTableEntryStatus_Type(Integer32):
    """Custom type oriWORPIfSatConfigTableEntryStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriWORPIfSatConfigTableEntryStatus_Type.__name__ = "Integer32"
_OriWORPIfSatConfigTableEntryStatus_Object = MibTableColumn
oriWORPIfSatConfigTableEntryStatus = _OriWORPIfSatConfigTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 1, 2, 1, 2),
    _OriWORPIfSatConfigTableEntryStatus_Type()
)
oriWORPIfSatConfigTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfSatConfigTableEntryStatus.setStatus("current")
_OriWORPIfSatConfigTableMacAddress_Type = MacAddress
_OriWORPIfSatConfigTableMacAddress_Object = MibTableColumn
oriWORPIfSatConfigTableMacAddress = _OriWORPIfSatConfigTableMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 1, 2, 1, 3),
    _OriWORPIfSatConfigTableMacAddress_Type()
)
oriWORPIfSatConfigTableMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfSatConfigTableMacAddress.setStatus("current")
_OriWORPIfSatConfigTableMinimumBandwidthLimitDownlink_Type = Gauge32
_OriWORPIfSatConfigTableMinimumBandwidthLimitDownlink_Object = MibTableColumn
oriWORPIfSatConfigTableMinimumBandwidthLimitDownlink = _OriWORPIfSatConfigTableMinimumBandwidthLimitDownlink_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 1, 2, 1, 4),
    _OriWORPIfSatConfigTableMinimumBandwidthLimitDownlink_Type()
)
oriWORPIfSatConfigTableMinimumBandwidthLimitDownlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfSatConfigTableMinimumBandwidthLimitDownlink.setStatus("current")
_OriWORPIfSatConfigTableMaximumBandwidthLimitDownlink_Type = Gauge32
_OriWORPIfSatConfigTableMaximumBandwidthLimitDownlink_Object = MibTableColumn
oriWORPIfSatConfigTableMaximumBandwidthLimitDownlink = _OriWORPIfSatConfigTableMaximumBandwidthLimitDownlink_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 1, 2, 1, 5),
    _OriWORPIfSatConfigTableMaximumBandwidthLimitDownlink_Type()
)
oriWORPIfSatConfigTableMaximumBandwidthLimitDownlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfSatConfigTableMaximumBandwidthLimitDownlink.setStatus("current")
_OriWORPIfSatConfigTableMinimumBandwidthLimitUplink_Type = Gauge32
_OriWORPIfSatConfigTableMinimumBandwidthLimitUplink_Object = MibTableColumn
oriWORPIfSatConfigTableMinimumBandwidthLimitUplink = _OriWORPIfSatConfigTableMinimumBandwidthLimitUplink_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 1, 2, 1, 6),
    _OriWORPIfSatConfigTableMinimumBandwidthLimitUplink_Type()
)
oriWORPIfSatConfigTableMinimumBandwidthLimitUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfSatConfigTableMinimumBandwidthLimitUplink.setStatus("current")
_OriWORPIfSatConfigTableMaximumBandwidthLimitUplink_Type = Gauge32
_OriWORPIfSatConfigTableMaximumBandwidthLimitUplink_Object = MibTableColumn
oriWORPIfSatConfigTableMaximumBandwidthLimitUplink = _OriWORPIfSatConfigTableMaximumBandwidthLimitUplink_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 1, 2, 1, 7),
    _OriWORPIfSatConfigTableMaximumBandwidthLimitUplink_Type()
)
oriWORPIfSatConfigTableMaximumBandwidthLimitUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfSatConfigTableMaximumBandwidthLimitUplink.setStatus("current")
_OriWORPIfSatConfigTableComment_Type = DisplayString
_OriWORPIfSatConfigTableComment_Object = MibTableColumn
oriWORPIfSatConfigTableComment = _OriWORPIfSatConfigTableComment_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 1, 2, 1, 8),
    _OriWORPIfSatConfigTableComment_Type()
)
oriWORPIfSatConfigTableComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfSatConfigTableComment.setStatus("current")
_OrinocoWORPIfSatStat_ObjectIdentity = ObjectIdentity
orinocoWORPIfSatStat = _OrinocoWORPIfSatStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2)
)
_OriWORPIfSatStatTable_Object = MibTable
oriWORPIfSatStatTable = _OriWORPIfSatStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    oriWORPIfSatStatTable.setStatus("current")
_OriWORPIfSatStatTableEntry_Object = MibTableRow
oriWORPIfSatStatTableEntry = _OriWORPIfSatStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1)
)
oriWORPIfSatStatTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriStationStatTableIndex"),
)
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableEntry.setStatus("current")
_OriWORPIfSatStatTableIndex_Type = Integer32
_OriWORPIfSatStatTableIndex_Object = MibTableColumn
oriWORPIfSatStatTableIndex = _OriWORPIfSatStatTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 1),
    _OriWORPIfSatStatTableIndex_Type()
)
oriWORPIfSatStatTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableIndex.setStatus("current")
_OriWORPIfSatStatTableMacAddress_Type = MacAddress
_OriWORPIfSatStatTableMacAddress_Object = MibTableColumn
oriWORPIfSatStatTableMacAddress = _OriWORPIfSatStatTableMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 2),
    _OriWORPIfSatStatTableMacAddress_Type()
)
oriWORPIfSatStatTableMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableMacAddress.setStatus("current")


class _OriWORPIfSatStatTableAverageLocalSignal_Type(Integer32):
    """Custom type oriWORPIfSatStatTableAverageLocalSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_OriWORPIfSatStatTableAverageLocalSignal_Type.__name__ = "Integer32"
_OriWORPIfSatStatTableAverageLocalSignal_Object = MibTableColumn
oriWORPIfSatStatTableAverageLocalSignal = _OriWORPIfSatStatTableAverageLocalSignal_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 3),
    _OriWORPIfSatStatTableAverageLocalSignal_Type()
)
oriWORPIfSatStatTableAverageLocalSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableAverageLocalSignal.setStatus("current")


class _OriWORPIfSatStatTableAverageLocalNoise_Type(Integer32):
    """Custom type oriWORPIfSatStatTableAverageLocalNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_OriWORPIfSatStatTableAverageLocalNoise_Type.__name__ = "Integer32"
_OriWORPIfSatStatTableAverageLocalNoise_Object = MibTableColumn
oriWORPIfSatStatTableAverageLocalNoise = _OriWORPIfSatStatTableAverageLocalNoise_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 4),
    _OriWORPIfSatStatTableAverageLocalNoise_Type()
)
oriWORPIfSatStatTableAverageLocalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableAverageLocalNoise.setStatus("current")


class _OriWORPIfSatStatTableAverageRemoteSignal_Type(Integer32):
    """Custom type oriWORPIfSatStatTableAverageRemoteSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_OriWORPIfSatStatTableAverageRemoteSignal_Type.__name__ = "Integer32"
_OriWORPIfSatStatTableAverageRemoteSignal_Object = MibTableColumn
oriWORPIfSatStatTableAverageRemoteSignal = _OriWORPIfSatStatTableAverageRemoteSignal_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 5),
    _OriWORPIfSatStatTableAverageRemoteSignal_Type()
)
oriWORPIfSatStatTableAverageRemoteSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableAverageRemoteSignal.setStatus("current")


class _OriWORPIfSatStatTableAverageRemoteNoise_Type(Integer32):
    """Custom type oriWORPIfSatStatTableAverageRemoteNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_OriWORPIfSatStatTableAverageRemoteNoise_Type.__name__ = "Integer32"
_OriWORPIfSatStatTableAverageRemoteNoise_Object = MibTableColumn
oriWORPIfSatStatTableAverageRemoteNoise = _OriWORPIfSatStatTableAverageRemoteNoise_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 6),
    _OriWORPIfSatStatTableAverageRemoteNoise_Type()
)
oriWORPIfSatStatTableAverageRemoteNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableAverageRemoteNoise.setStatus("current")
_OriWORPIfSatStatTablePollData_Type = Counter32
_OriWORPIfSatStatTablePollData_Object = MibTableColumn
oriWORPIfSatStatTablePollData = _OriWORPIfSatStatTablePollData_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 7),
    _OriWORPIfSatStatTablePollData_Type()
)
oriWORPIfSatStatTablePollData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTablePollData.setStatus("current")
_OriWORPIfSatStatTablePollNoData_Type = Counter32
_OriWORPIfSatStatTablePollNoData_Object = MibTableColumn
oriWORPIfSatStatTablePollNoData = _OriWORPIfSatStatTablePollNoData_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 8),
    _OriWORPIfSatStatTablePollNoData_Type()
)
oriWORPIfSatStatTablePollNoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTablePollNoData.setStatus("current")
_OriWORPIfSatStatTableReplyData_Type = Counter32
_OriWORPIfSatStatTableReplyData_Object = MibTableColumn
oriWORPIfSatStatTableReplyData = _OriWORPIfSatStatTableReplyData_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 9),
    _OriWORPIfSatStatTableReplyData_Type()
)
oriWORPIfSatStatTableReplyData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableReplyData.setStatus("current")
_OriWORPIfSatStatTableReplyNoData_Type = Counter32
_OriWORPIfSatStatTableReplyNoData_Object = MibTableColumn
oriWORPIfSatStatTableReplyNoData = _OriWORPIfSatStatTableReplyNoData_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 10),
    _OriWORPIfSatStatTableReplyNoData_Type()
)
oriWORPIfSatStatTableReplyNoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableReplyNoData.setStatus("current")
_OriWORPIfSatStatTableRequestForService_Type = Counter32
_OriWORPIfSatStatTableRequestForService_Object = MibTableColumn
oriWORPIfSatStatTableRequestForService = _OriWORPIfSatStatTableRequestForService_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 11),
    _OriWORPIfSatStatTableRequestForService_Type()
)
oriWORPIfSatStatTableRequestForService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableRequestForService.setStatus("current")
_OriWORPIfSatStatTableSendSuccess_Type = Counter32
_OriWORPIfSatStatTableSendSuccess_Object = MibTableColumn
oriWORPIfSatStatTableSendSuccess = _OriWORPIfSatStatTableSendSuccess_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 12),
    _OriWORPIfSatStatTableSendSuccess_Type()
)
oriWORPIfSatStatTableSendSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableSendSuccess.setStatus("current")
_OriWORPIfSatStatTableSendRetries_Type = Counter32
_OriWORPIfSatStatTableSendRetries_Object = MibTableColumn
oriWORPIfSatStatTableSendRetries = _OriWORPIfSatStatTableSendRetries_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 13),
    _OriWORPIfSatStatTableSendRetries_Type()
)
oriWORPIfSatStatTableSendRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableSendRetries.setStatus("current")
_OriWORPIfSatStatTableSendFailures_Type = Counter32
_OriWORPIfSatStatTableSendFailures_Object = MibTableColumn
oriWORPIfSatStatTableSendFailures = _OriWORPIfSatStatTableSendFailures_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 14),
    _OriWORPIfSatStatTableSendFailures_Type()
)
oriWORPIfSatStatTableSendFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableSendFailures.setStatus("current")
_OriWORPIfSatStatTableReceiveSuccess_Type = Counter32
_OriWORPIfSatStatTableReceiveSuccess_Object = MibTableColumn
oriWORPIfSatStatTableReceiveSuccess = _OriWORPIfSatStatTableReceiveSuccess_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 15),
    _OriWORPIfSatStatTableReceiveSuccess_Type()
)
oriWORPIfSatStatTableReceiveSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableReceiveSuccess.setStatus("current")
_OriWORPIfSatStatTableReceiveRetries_Type = Counter32
_OriWORPIfSatStatTableReceiveRetries_Object = MibTableColumn
oriWORPIfSatStatTableReceiveRetries = _OriWORPIfSatStatTableReceiveRetries_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 16),
    _OriWORPIfSatStatTableReceiveRetries_Type()
)
oriWORPIfSatStatTableReceiveRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableReceiveRetries.setStatus("current")
_OriWORPIfSatStatTableReceiveFailures_Type = Counter32
_OriWORPIfSatStatTableReceiveFailures_Object = MibTableColumn
oriWORPIfSatStatTableReceiveFailures = _OriWORPIfSatStatTableReceiveFailures_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 17),
    _OriWORPIfSatStatTableReceiveFailures_Type()
)
oriWORPIfSatStatTableReceiveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableReceiveFailures.setStatus("current")
_OriWORPIfSatStatTablePollNoReplies_Type = Counter32
_OriWORPIfSatStatTablePollNoReplies_Object = MibTableColumn
oriWORPIfSatStatTablePollNoReplies = _OriWORPIfSatStatTablePollNoReplies_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 18),
    _OriWORPIfSatStatTablePollNoReplies_Type()
)
oriWORPIfSatStatTablePollNoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTablePollNoReplies.setStatus("current")
_OriWORPIfSatStatTableLocalTxRate_Type = Integer32
_OriWORPIfSatStatTableLocalTxRate_Object = MibTableColumn
oriWORPIfSatStatTableLocalTxRate = _OriWORPIfSatStatTableLocalTxRate_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 19),
    _OriWORPIfSatStatTableLocalTxRate_Type()
)
oriWORPIfSatStatTableLocalTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableLocalTxRate.setStatus("current")
_OriWORPIfSatStatTableRemoteTxRate_Type = Integer32
_OriWORPIfSatStatTableRemoteTxRate_Object = MibTableColumn
oriWORPIfSatStatTableRemoteTxRate = _OriWORPIfSatStatTableRemoteTxRate_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 3, 2, 1, 1, 20),
    _OriWORPIfSatStatTableRemoteTxRate_Type()
)
oriWORPIfSatStatTableRemoteTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSatStatTableRemoteTxRate.setStatus("current")
_OrinocoWORPIfSiteSurvey_ObjectIdentity = ObjectIdentity
orinocoWORPIfSiteSurvey = _OrinocoWORPIfSiteSurvey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 4)
)


class _OriWORPIfSiteSurveyOperation_Type(Integer32):
    """Custom type oriWORPIfSiteSurveyOperation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("test", 3))
    )


_OriWORPIfSiteSurveyOperation_Type.__name__ = "Integer32"
_OriWORPIfSiteSurveyOperation_Object = MibScalar
oriWORPIfSiteSurveyOperation = _OriWORPIfSiteSurveyOperation_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 4, 1),
    _OriWORPIfSiteSurveyOperation_Type()
)
oriWORPIfSiteSurveyOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfSiteSurveyOperation.setStatus("current")
_OriWORPIfSiteSurveyTable_Object = MibTable
oriWORPIfSiteSurveyTable = _OriWORPIfSiteSurveyTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 4, 2)
)
if mibBuilder.loadTexts:
    oriWORPIfSiteSurveyTable.setStatus("current")
_OriWORPIfSiteSurveySignalQualityTableEntry_Object = MibTableRow
oriWORPIfSiteSurveySignalQualityTableEntry = _OriWORPIfSiteSurveySignalQualityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 4, 2, 1)
)
oriWORPIfSiteSurveySignalQualityTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriWORPIfSiteSurveyTableIndex"),
)
if mibBuilder.loadTexts:
    oriWORPIfSiteSurveySignalQualityTableEntry.setStatus("current")
_OriWORPIfSiteSurveyTableIndex_Type = Integer32
_OriWORPIfSiteSurveyTableIndex_Object = MibTableColumn
oriWORPIfSiteSurveyTableIndex = _OriWORPIfSiteSurveyTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 4, 2, 1, 1),
    _OriWORPIfSiteSurveyTableIndex_Type()
)
oriWORPIfSiteSurveyTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSiteSurveyTableIndex.setStatus("current")
_OriWORPIfSiteSurveyBaseMACAddress_Type = PhysAddress
_OriWORPIfSiteSurveyBaseMACAddress_Object = MibTableColumn
oriWORPIfSiteSurveyBaseMACAddress = _OriWORPIfSiteSurveyBaseMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 4, 2, 1, 2),
    _OriWORPIfSiteSurveyBaseMACAddress_Type()
)
oriWORPIfSiteSurveyBaseMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSiteSurveyBaseMACAddress.setStatus("current")
_OriWORPIfSiteSurveyBaseName_Type = DisplayString
_OriWORPIfSiteSurveyBaseName_Object = MibTableColumn
oriWORPIfSiteSurveyBaseName = _OriWORPIfSiteSurveyBaseName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 4, 2, 1, 3),
    _OriWORPIfSiteSurveyBaseName_Type()
)
oriWORPIfSiteSurveyBaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSiteSurveyBaseName.setStatus("current")
_OriWORPIfSiteSurveyMaxSatAllowed_Type = Integer32
_OriWORPIfSiteSurveyMaxSatAllowed_Object = MibTableColumn
oriWORPIfSiteSurveyMaxSatAllowed = _OriWORPIfSiteSurveyMaxSatAllowed_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 4, 2, 1, 4),
    _OriWORPIfSiteSurveyMaxSatAllowed_Type()
)
oriWORPIfSiteSurveyMaxSatAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSiteSurveyMaxSatAllowed.setStatus("current")
_OriWORPIfSiteSurveyNumSatRegistered_Type = Integer32
_OriWORPIfSiteSurveyNumSatRegistered_Object = MibTableColumn
oriWORPIfSiteSurveyNumSatRegistered = _OriWORPIfSiteSurveyNumSatRegistered_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 4, 2, 1, 5),
    _OriWORPIfSiteSurveyNumSatRegistered_Type()
)
oriWORPIfSiteSurveyNumSatRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSiteSurveyNumSatRegistered.setStatus("current")
_OriWORPIfSiteSurveyCurrentSatRegistered_Type = Integer32
_OriWORPIfSiteSurveyCurrentSatRegistered_Object = MibTableColumn
oriWORPIfSiteSurveyCurrentSatRegistered = _OriWORPIfSiteSurveyCurrentSatRegistered_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 4, 2, 1, 6),
    _OriWORPIfSiteSurveyCurrentSatRegistered_Type()
)
oriWORPIfSiteSurveyCurrentSatRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSiteSurveyCurrentSatRegistered.setStatus("current")
_OriWORPIfSiteSurveyLocalSignalLevel_Type = Integer32
_OriWORPIfSiteSurveyLocalSignalLevel_Object = MibTableColumn
oriWORPIfSiteSurveyLocalSignalLevel = _OriWORPIfSiteSurveyLocalSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 4, 2, 1, 7),
    _OriWORPIfSiteSurveyLocalSignalLevel_Type()
)
oriWORPIfSiteSurveyLocalSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSiteSurveyLocalSignalLevel.setStatus("current")
_OriWORPIfSiteSurveyLocalNoiseLevel_Type = Integer32
_OriWORPIfSiteSurveyLocalNoiseLevel_Object = MibTableColumn
oriWORPIfSiteSurveyLocalNoiseLevel = _OriWORPIfSiteSurveyLocalNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 4, 2, 1, 8),
    _OriWORPIfSiteSurveyLocalNoiseLevel_Type()
)
oriWORPIfSiteSurveyLocalNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSiteSurveyLocalNoiseLevel.setStatus("current")
_OriWORPIfSiteSurveyLocalSNR_Type = Integer32
_OriWORPIfSiteSurveyLocalSNR_Object = MibTableColumn
oriWORPIfSiteSurveyLocalSNR = _OriWORPIfSiteSurveyLocalSNR_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 4, 2, 1, 9),
    _OriWORPIfSiteSurveyLocalSNR_Type()
)
oriWORPIfSiteSurveyLocalSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSiteSurveyLocalSNR.setStatus("current")
_OriWORPIfSiteSurveyRemoteSignalLevel_Type = Integer32
_OriWORPIfSiteSurveyRemoteSignalLevel_Object = MibTableColumn
oriWORPIfSiteSurveyRemoteSignalLevel = _OriWORPIfSiteSurveyRemoteSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 4, 2, 1, 10),
    _OriWORPIfSiteSurveyRemoteSignalLevel_Type()
)
oriWORPIfSiteSurveyRemoteSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSiteSurveyRemoteSignalLevel.setStatus("current")
_OriWORPIfSiteSurveyRemoteNoiseLevel_Type = Integer32
_OriWORPIfSiteSurveyRemoteNoiseLevel_Object = MibTableColumn
oriWORPIfSiteSurveyRemoteNoiseLevel = _OriWORPIfSiteSurveyRemoteNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 4, 2, 1, 11),
    _OriWORPIfSiteSurveyRemoteNoiseLevel_Type()
)
oriWORPIfSiteSurveyRemoteNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSiteSurveyRemoteNoiseLevel.setStatus("current")
_OriWORPIfSiteSurveyRemoteSNR_Type = Integer32
_OriWORPIfSiteSurveyRemoteSNR_Object = MibTableColumn
oriWORPIfSiteSurveyRemoteSNR = _OriWORPIfSiteSurveyRemoteSNR_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 4, 2, 1, 12),
    _OriWORPIfSiteSurveyRemoteSNR_Type()
)
oriWORPIfSiteSurveyRemoteSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWORPIfSiteSurveyRemoteSNR.setStatus("current")
_OrinocoWORPIfRoaming_ObjectIdentity = ObjectIdentity
orinocoWORPIfRoaming = _OrinocoWORPIfRoaming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 5)
)
_OriWORPIfRoamingStatus_Type = ObjStatus
_OriWORPIfRoamingStatus_Object = MibScalar
oriWORPIfRoamingStatus = _OriWORPIfRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 5, 1),
    _OriWORPIfRoamingStatus_Type()
)
oriWORPIfRoamingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfRoamingStatus.setStatus("current")


class _OriWORPIfRoamingSlowScanThreshold_Type(Integer32):
    """Custom type oriWORPIfRoamingSlowScanThreshold based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_OriWORPIfRoamingSlowScanThreshold_Type.__name__ = "Integer32"
_OriWORPIfRoamingSlowScanThreshold_Object = MibScalar
oriWORPIfRoamingSlowScanThreshold = _OriWORPIfRoamingSlowScanThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 5, 2),
    _OriWORPIfRoamingSlowScanThreshold_Type()
)
oriWORPIfRoamingSlowScanThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfRoamingSlowScanThreshold.setStatus("current")


class _OriWORPIfRoamingFastScanThreshold_Type(Integer32):
    """Custom type oriWORPIfRoamingFastScanThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_OriWORPIfRoamingFastScanThreshold_Type.__name__ = "Integer32"
_OriWORPIfRoamingFastScanThreshold_Object = MibScalar
oriWORPIfRoamingFastScanThreshold = _OriWORPIfRoamingFastScanThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 5, 3),
    _OriWORPIfRoamingFastScanThreshold_Type()
)
oriWORPIfRoamingFastScanThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfRoamingFastScanThreshold.setStatus("current")


class _OriWORPIfRoamingThreshold_Type(Integer32):
    """Custom type oriWORPIfRoamingThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_OriWORPIfRoamingThreshold_Type.__name__ = "Integer32"
_OriWORPIfRoamingThreshold_Object = MibScalar
oriWORPIfRoamingThreshold = _OriWORPIfRoamingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 5, 4),
    _OriWORPIfRoamingThreshold_Type()
)
oriWORPIfRoamingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfRoamingThreshold.setStatus("current")


class _OriWORPIfRoamingSlowScanPercentThreshold_Type(Integer32):
    """Custom type oriWORPIfRoamingSlowScanPercentThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OriWORPIfRoamingSlowScanPercentThreshold_Type.__name__ = "Integer32"
_OriWORPIfRoamingSlowScanPercentThreshold_Object = MibScalar
oriWORPIfRoamingSlowScanPercentThreshold = _OriWORPIfRoamingSlowScanPercentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 5, 5),
    _OriWORPIfRoamingSlowScanPercentThreshold_Type()
)
oriWORPIfRoamingSlowScanPercentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfRoamingSlowScanPercentThreshold.setStatus("current")


class _OriWORPIfRoamingFastScanPercentThreshold_Type(Integer32):
    """Custom type oriWORPIfRoamingFastScanPercentThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OriWORPIfRoamingFastScanPercentThreshold_Type.__name__ = "Integer32"
_OriWORPIfRoamingFastScanPercentThreshold_Object = MibScalar
oriWORPIfRoamingFastScanPercentThreshold = _OriWORPIfRoamingFastScanPercentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 5, 6),
    _OriWORPIfRoamingFastScanPercentThreshold_Type()
)
oriWORPIfRoamingFastScanPercentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfRoamingFastScanPercentThreshold.setStatus("current")
_OrinocoWORPIfDDRS_ObjectIdentity = ObjectIdentity
orinocoWORPIfDDRS = _OrinocoWORPIfDDRS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6)
)


class _OriWORPIfDDRSStatus_Type(ObjStatus):
    """Custom type oriWORPIfDDRSStatus based on ObjStatus"""


_OriWORPIfDDRSStatus_Object = MibScalar
oriWORPIfDDRSStatus = _OriWORPIfDDRSStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 1),
    _OriWORPIfDDRSStatus_Type()
)
oriWORPIfDDRSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSStatus.setStatus("current")


class _OriWORPIfDDRSDefDataRate_Type(Integer32):
    """Custom type oriWORPIfDDRSDefDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 108),
    )


_OriWORPIfDDRSDefDataRate_Type.__name__ = "Integer32"
_OriWORPIfDDRSDefDataRate_Object = MibScalar
oriWORPIfDDRSDefDataRate = _OriWORPIfDDRSDefDataRate_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 2),
    _OriWORPIfDDRSDefDataRate_Type()
)
oriWORPIfDDRSDefDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSDefDataRate.setStatus("current")


class _OriWORPIfDDRSMaxDataRate_Type(Integer32):
    """Custom type oriWORPIfDDRSMaxDataRate based on Integer32"""
    defaultValue = 36

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 108),
    )


_OriWORPIfDDRSMaxDataRate_Type.__name__ = "Integer32"
_OriWORPIfDDRSMaxDataRate_Object = MibScalar
oriWORPIfDDRSMaxDataRate = _OriWORPIfDDRSMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 3),
    _OriWORPIfDDRSMaxDataRate_Type()
)
oriWORPIfDDRSMaxDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMaxDataRate.setStatus("current")


class _OriWORPIfDDRSMinReqSNRdot11an6Mbps_Type(Integer32):
    """Custom type oriWORPIfDDRSMinReqSNRdot11an6Mbps based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSMinReqSNRdot11an6Mbps_Type.__name__ = "Integer32"
_OriWORPIfDDRSMinReqSNRdot11an6Mbps_Object = MibScalar
oriWORPIfDDRSMinReqSNRdot11an6Mbps = _OriWORPIfDDRSMinReqSNRdot11an6Mbps_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 4),
    _OriWORPIfDDRSMinReqSNRdot11an6Mbps_Type()
)
oriWORPIfDDRSMinReqSNRdot11an6Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMinReqSNRdot11an6Mbps.setStatus("current")


class _OriWORPIfDDRSMinReqSNRdot11an9Mbps_Type(Integer32):
    """Custom type oriWORPIfDDRSMinReqSNRdot11an9Mbps based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSMinReqSNRdot11an9Mbps_Type.__name__ = "Integer32"
_OriWORPIfDDRSMinReqSNRdot11an9Mbps_Object = MibScalar
oriWORPIfDDRSMinReqSNRdot11an9Mbps = _OriWORPIfDDRSMinReqSNRdot11an9Mbps_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 5),
    _OriWORPIfDDRSMinReqSNRdot11an9Mbps_Type()
)
oriWORPIfDDRSMinReqSNRdot11an9Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMinReqSNRdot11an9Mbps.setStatus("current")


class _OriWORPIfDDRSMinReqSNRdot11an12Mbps_Type(Integer32):
    """Custom type oriWORPIfDDRSMinReqSNRdot11an12Mbps based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSMinReqSNRdot11an12Mbps_Type.__name__ = "Integer32"
_OriWORPIfDDRSMinReqSNRdot11an12Mbps_Object = MibScalar
oriWORPIfDDRSMinReqSNRdot11an12Mbps = _OriWORPIfDDRSMinReqSNRdot11an12Mbps_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 6),
    _OriWORPIfDDRSMinReqSNRdot11an12Mbps_Type()
)
oriWORPIfDDRSMinReqSNRdot11an12Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMinReqSNRdot11an12Mbps.setStatus("current")


class _OriWORPIfDDRSMinReqSNRdot11an18Mbps_Type(Integer32):
    """Custom type oriWORPIfDDRSMinReqSNRdot11an18Mbps based on Integer32"""
    defaultValue = 11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSMinReqSNRdot11an18Mbps_Type.__name__ = "Integer32"
_OriWORPIfDDRSMinReqSNRdot11an18Mbps_Object = MibScalar
oriWORPIfDDRSMinReqSNRdot11an18Mbps = _OriWORPIfDDRSMinReqSNRdot11an18Mbps_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 7),
    _OriWORPIfDDRSMinReqSNRdot11an18Mbps_Type()
)
oriWORPIfDDRSMinReqSNRdot11an18Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMinReqSNRdot11an18Mbps.setStatus("current")


class _OriWORPIfDDRSMinReqSNRdot11an24Mbps_Type(Integer32):
    """Custom type oriWORPIfDDRSMinReqSNRdot11an24Mbps based on Integer32"""
    defaultValue = 14

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSMinReqSNRdot11an24Mbps_Type.__name__ = "Integer32"
_OriWORPIfDDRSMinReqSNRdot11an24Mbps_Object = MibScalar
oriWORPIfDDRSMinReqSNRdot11an24Mbps = _OriWORPIfDDRSMinReqSNRdot11an24Mbps_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 8),
    _OriWORPIfDDRSMinReqSNRdot11an24Mbps_Type()
)
oriWORPIfDDRSMinReqSNRdot11an24Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMinReqSNRdot11an24Mbps.setStatus("current")


class _OriWORPIfDDRSMinReqSNRdot11an36Mbps_Type(Integer32):
    """Custom type oriWORPIfDDRSMinReqSNRdot11an36Mbps based on Integer32"""
    defaultValue = 18

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSMinReqSNRdot11an36Mbps_Type.__name__ = "Integer32"
_OriWORPIfDDRSMinReqSNRdot11an36Mbps_Object = MibScalar
oriWORPIfDDRSMinReqSNRdot11an36Mbps = _OriWORPIfDDRSMinReqSNRdot11an36Mbps_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 9),
    _OriWORPIfDDRSMinReqSNRdot11an36Mbps_Type()
)
oriWORPIfDDRSMinReqSNRdot11an36Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMinReqSNRdot11an36Mbps.setStatus("current")


class _OriWORPIfDDRSMinReqSNRdot11an48Mbps_Type(Integer32):
    """Custom type oriWORPIfDDRSMinReqSNRdot11an48Mbps based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSMinReqSNRdot11an48Mbps_Type.__name__ = "Integer32"
_OriWORPIfDDRSMinReqSNRdot11an48Mbps_Object = MibScalar
oriWORPIfDDRSMinReqSNRdot11an48Mbps = _OriWORPIfDDRSMinReqSNRdot11an48Mbps_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 10),
    _OriWORPIfDDRSMinReqSNRdot11an48Mbps_Type()
)
oriWORPIfDDRSMinReqSNRdot11an48Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMinReqSNRdot11an48Mbps.setStatus("current")


class _OriWORPIfDDRSMinReqSNRdot11an54Mbps_Type(Integer32):
    """Custom type oriWORPIfDDRSMinReqSNRdot11an54Mbps based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSMinReqSNRdot11an54Mbps_Type.__name__ = "Integer32"
_OriWORPIfDDRSMinReqSNRdot11an54Mbps_Object = MibScalar
oriWORPIfDDRSMinReqSNRdot11an54Mbps = _OriWORPIfDDRSMinReqSNRdot11an54Mbps_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 11),
    _OriWORPIfDDRSMinReqSNRdot11an54Mbps_Type()
)
oriWORPIfDDRSMinReqSNRdot11an54Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMinReqSNRdot11an54Mbps.setStatus("current")


class _OriWORPIfDDRSMinReqSNRdot11at12Mbps_Type(Integer32):
    """Custom type oriWORPIfDDRSMinReqSNRdot11at12Mbps based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSMinReqSNRdot11at12Mbps_Type.__name__ = "Integer32"
_OriWORPIfDDRSMinReqSNRdot11at12Mbps_Object = MibScalar
oriWORPIfDDRSMinReqSNRdot11at12Mbps = _OriWORPIfDDRSMinReqSNRdot11at12Mbps_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 12),
    _OriWORPIfDDRSMinReqSNRdot11at12Mbps_Type()
)
oriWORPIfDDRSMinReqSNRdot11at12Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMinReqSNRdot11at12Mbps.setStatus("current")


class _OriWORPIfDDRSMinReqSNRdot11at18Mbps_Type(Integer32):
    """Custom type oriWORPIfDDRSMinReqSNRdot11at18Mbps based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSMinReqSNRdot11at18Mbps_Type.__name__ = "Integer32"
_OriWORPIfDDRSMinReqSNRdot11at18Mbps_Object = MibScalar
oriWORPIfDDRSMinReqSNRdot11at18Mbps = _OriWORPIfDDRSMinReqSNRdot11at18Mbps_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 13),
    _OriWORPIfDDRSMinReqSNRdot11at18Mbps_Type()
)
oriWORPIfDDRSMinReqSNRdot11at18Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMinReqSNRdot11at18Mbps.setStatus("current")


class _OriWORPIfDDRSMinReqSNRdot11at24Mbps_Type(Integer32):
    """Custom type oriWORPIfDDRSMinReqSNRdot11at24Mbps based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSMinReqSNRdot11at24Mbps_Type.__name__ = "Integer32"
_OriWORPIfDDRSMinReqSNRdot11at24Mbps_Object = MibScalar
oriWORPIfDDRSMinReqSNRdot11at24Mbps = _OriWORPIfDDRSMinReqSNRdot11at24Mbps_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 14),
    _OriWORPIfDDRSMinReqSNRdot11at24Mbps_Type()
)
oriWORPIfDDRSMinReqSNRdot11at24Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMinReqSNRdot11at24Mbps.setStatus("current")


class _OriWORPIfDDRSMinReqSNRdot11at36Mbps_Type(Integer32):
    """Custom type oriWORPIfDDRSMinReqSNRdot11at36Mbps based on Integer32"""
    defaultValue = 11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSMinReqSNRdot11at36Mbps_Type.__name__ = "Integer32"
_OriWORPIfDDRSMinReqSNRdot11at36Mbps_Object = MibScalar
oriWORPIfDDRSMinReqSNRdot11at36Mbps = _OriWORPIfDDRSMinReqSNRdot11at36Mbps_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 15),
    _OriWORPIfDDRSMinReqSNRdot11at36Mbps_Type()
)
oriWORPIfDDRSMinReqSNRdot11at36Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMinReqSNRdot11at36Mbps.setStatus("current")


class _OriWORPIfDDRSMinReqSNRdot11at48Mbps_Type(Integer32):
    """Custom type oriWORPIfDDRSMinReqSNRdot11at48Mbps based on Integer32"""
    defaultValue = 14

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSMinReqSNRdot11at48Mbps_Type.__name__ = "Integer32"
_OriWORPIfDDRSMinReqSNRdot11at48Mbps_Object = MibScalar
oriWORPIfDDRSMinReqSNRdot11at48Mbps = _OriWORPIfDDRSMinReqSNRdot11at48Mbps_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 16),
    _OriWORPIfDDRSMinReqSNRdot11at48Mbps_Type()
)
oriWORPIfDDRSMinReqSNRdot11at48Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMinReqSNRdot11at48Mbps.setStatus("current")


class _OriWORPIfDDRSMinReqSNRdot11at72Mbps_Type(Integer32):
    """Custom type oriWORPIfDDRSMinReqSNRdot11at72Mbps based on Integer32"""
    defaultValue = 18

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSMinReqSNRdot11at72Mbps_Type.__name__ = "Integer32"
_OriWORPIfDDRSMinReqSNRdot11at72Mbps_Object = MibScalar
oriWORPIfDDRSMinReqSNRdot11at72Mbps = _OriWORPIfDDRSMinReqSNRdot11at72Mbps_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 17),
    _OriWORPIfDDRSMinReqSNRdot11at72Mbps_Type()
)
oriWORPIfDDRSMinReqSNRdot11at72Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMinReqSNRdot11at72Mbps.setStatus("current")


class _OriWORPIfDDRSMinReqSNRdot11at96Mbps_Type(Integer32):
    """Custom type oriWORPIfDDRSMinReqSNRdot11at96Mbps based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSMinReqSNRdot11at96Mbps_Type.__name__ = "Integer32"
_OriWORPIfDDRSMinReqSNRdot11at96Mbps_Object = MibScalar
oriWORPIfDDRSMinReqSNRdot11at96Mbps = _OriWORPIfDDRSMinReqSNRdot11at96Mbps_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 18),
    _OriWORPIfDDRSMinReqSNRdot11at96Mbps_Type()
)
oriWORPIfDDRSMinReqSNRdot11at96Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMinReqSNRdot11at96Mbps.setStatus("current")


class _OriWORPIfDDRSMinReqSNRdot11at108Mbps_Type(Integer32):
    """Custom type oriWORPIfDDRSMinReqSNRdot11at108Mbps based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSMinReqSNRdot11at108Mbps_Type.__name__ = "Integer32"
_OriWORPIfDDRSMinReqSNRdot11at108Mbps_Object = MibScalar
oriWORPIfDDRSMinReqSNRdot11at108Mbps = _OriWORPIfDDRSMinReqSNRdot11at108Mbps_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 19),
    _OriWORPIfDDRSMinReqSNRdot11at108Mbps_Type()
)
oriWORPIfDDRSMinReqSNRdot11at108Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSMinReqSNRdot11at108Mbps.setStatus("current")


class _OriWORPIfDDRSDataRateIncAvgSNRThreshold_Type(Integer32):
    """Custom type oriWORPIfDDRSDataRateIncAvgSNRThreshold based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSDataRateIncAvgSNRThreshold_Type.__name__ = "Integer32"
_OriWORPIfDDRSDataRateIncAvgSNRThreshold_Object = MibScalar
oriWORPIfDDRSDataRateIncAvgSNRThreshold = _OriWORPIfDDRSDataRateIncAvgSNRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 20),
    _OriWORPIfDDRSDataRateIncAvgSNRThreshold_Type()
)
oriWORPIfDDRSDataRateIncAvgSNRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSDataRateIncAvgSNRThreshold.setStatus("current")


class _OriWORPIfDDRSDataRateIncReqSNRThreshold_Type(Integer32):
    """Custom type oriWORPIfDDRSDataRateIncReqSNRThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSDataRateIncReqSNRThreshold_Type.__name__ = "Integer32"
_OriWORPIfDDRSDataRateIncReqSNRThreshold_Object = MibScalar
oriWORPIfDDRSDataRateIncReqSNRThreshold = _OriWORPIfDDRSDataRateIncReqSNRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 21),
    _OriWORPIfDDRSDataRateIncReqSNRThreshold_Type()
)
oriWORPIfDDRSDataRateIncReqSNRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSDataRateIncReqSNRThreshold.setStatus("current")


class _OriWORPIfDDRSDataRateDecReqSNRThreshold_Type(Integer32):
    """Custom type oriWORPIfDDRSDataRateDecReqSNRThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_OriWORPIfDDRSDataRateDecReqSNRThreshold_Type.__name__ = "Integer32"
_OriWORPIfDDRSDataRateDecReqSNRThreshold_Object = MibScalar
oriWORPIfDDRSDataRateDecReqSNRThreshold = _OriWORPIfDDRSDataRateDecReqSNRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 22),
    _OriWORPIfDDRSDataRateDecReqSNRThreshold_Type()
)
oriWORPIfDDRSDataRateDecReqSNRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSDataRateDecReqSNRThreshold.setStatus("current")


class _OriWORPIfDDRSDataRateIncPercentThreshold_Type(Integer32):
    """Custom type oriWORPIfDDRSDataRateIncPercentThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OriWORPIfDDRSDataRateIncPercentThreshold_Type.__name__ = "Integer32"
_OriWORPIfDDRSDataRateIncPercentThreshold_Object = MibScalar
oriWORPIfDDRSDataRateIncPercentThreshold = _OriWORPIfDDRSDataRateIncPercentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 23),
    _OriWORPIfDDRSDataRateIncPercentThreshold_Type()
)
oriWORPIfDDRSDataRateIncPercentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSDataRateIncPercentThreshold.setStatus("current")


class _OriWORPIfDDRSDataRateDecPercentThreshold_Type(Integer32):
    """Custom type oriWORPIfDDRSDataRateDecPercentThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OriWORPIfDDRSDataRateDecPercentThreshold_Type.__name__ = "Integer32"
_OriWORPIfDDRSDataRateDecPercentThreshold_Object = MibScalar
oriWORPIfDDRSDataRateDecPercentThreshold = _OriWORPIfDDRSDataRateDecPercentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 6, 24),
    _OriWORPIfDDRSDataRateDecPercentThreshold_Type()
)
oriWORPIfDDRSDataRateDecPercentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPIfDDRSDataRateDecPercentThreshold.setStatus("current")
_OrinocoWORPIfBSU_ObjectIdentity = ObjectIdentity
orinocoWORPIfBSU = _OrinocoWORPIfBSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 7)
)
_OrinocoWORPIfBSUStat_ObjectIdentity = ObjectIdentity
orinocoWORPIfBSUStat = _OrinocoWORPIfBSUStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 7, 1)
)
_OrinocoWORPIfBSUStatMACAddress_Type = MacAddress
_OrinocoWORPIfBSUStatMACAddress_Object = MibScalar
orinocoWORPIfBSUStatMACAddress = _OrinocoWORPIfBSUStatMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 7, 1, 1),
    _OrinocoWORPIfBSUStatMACAddress_Type()
)
orinocoWORPIfBSUStatMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orinocoWORPIfBSUStatMACAddress.setStatus("current")
_OrinocoWORPIfBSUStatLocalTxRate_Type = Integer32
_OrinocoWORPIfBSUStatLocalTxRate_Object = MibScalar
orinocoWORPIfBSUStatLocalTxRate = _OrinocoWORPIfBSUStatLocalTxRate_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 7, 1, 2),
    _OrinocoWORPIfBSUStatLocalTxRate_Type()
)
orinocoWORPIfBSUStatLocalTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orinocoWORPIfBSUStatLocalTxRate.setStatus("current")
_OrinocoWORPIfBSUStatRemoteTxRate_Type = Integer32
_OrinocoWORPIfBSUStatRemoteTxRate_Object = MibScalar
orinocoWORPIfBSUStatRemoteTxRate = _OrinocoWORPIfBSUStatRemoteTxRate_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 7, 1, 3),
    _OrinocoWORPIfBSUStatRemoteTxRate_Type()
)
orinocoWORPIfBSUStatRemoteTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orinocoWORPIfBSUStatRemoteTxRate.setStatus("current")


class _OrinocoWORPIfBSUStatAverageLocalSignal_Type(Integer32):
    """Custom type orinocoWORPIfBSUStatAverageLocalSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_OrinocoWORPIfBSUStatAverageLocalSignal_Type.__name__ = "Integer32"
_OrinocoWORPIfBSUStatAverageLocalSignal_Object = MibScalar
orinocoWORPIfBSUStatAverageLocalSignal = _OrinocoWORPIfBSUStatAverageLocalSignal_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 7, 1, 4),
    _OrinocoWORPIfBSUStatAverageLocalSignal_Type()
)
orinocoWORPIfBSUStatAverageLocalSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orinocoWORPIfBSUStatAverageLocalSignal.setStatus("current")


class _OrinocoWORPIfBSUStatAverageLocalNoise_Type(Integer32):
    """Custom type orinocoWORPIfBSUStatAverageLocalNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_OrinocoWORPIfBSUStatAverageLocalNoise_Type.__name__ = "Integer32"
_OrinocoWORPIfBSUStatAverageLocalNoise_Object = MibScalar
orinocoWORPIfBSUStatAverageLocalNoise = _OrinocoWORPIfBSUStatAverageLocalNoise_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 7, 1, 5),
    _OrinocoWORPIfBSUStatAverageLocalNoise_Type()
)
orinocoWORPIfBSUStatAverageLocalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orinocoWORPIfBSUStatAverageLocalNoise.setStatus("current")


class _OrinocoWORPIfBSUStatAverageRemoteSignal_Type(Integer32):
    """Custom type orinocoWORPIfBSUStatAverageRemoteSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_OrinocoWORPIfBSUStatAverageRemoteSignal_Type.__name__ = "Integer32"
_OrinocoWORPIfBSUStatAverageRemoteSignal_Object = MibScalar
orinocoWORPIfBSUStatAverageRemoteSignal = _OrinocoWORPIfBSUStatAverageRemoteSignal_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 7, 1, 6),
    _OrinocoWORPIfBSUStatAverageRemoteSignal_Type()
)
orinocoWORPIfBSUStatAverageRemoteSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orinocoWORPIfBSUStatAverageRemoteSignal.setStatus("current")


class _OrinocoWORPIfBSUStatAverageRemoteNoise_Type(Integer32):
    """Custom type orinocoWORPIfBSUStatAverageRemoteNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_OrinocoWORPIfBSUStatAverageRemoteNoise_Type.__name__ = "Integer32"
_OrinocoWORPIfBSUStatAverageRemoteNoise_Object = MibScalar
orinocoWORPIfBSUStatAverageRemoteNoise = _OrinocoWORPIfBSUStatAverageRemoteNoise_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 2, 5, 7, 1, 7),
    _OrinocoWORPIfBSUStatAverageRemoteNoise_Type()
)
orinocoWORPIfBSUStatAverageRemoteNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orinocoWORPIfBSUStatAverageRemoteNoise.setStatus("current")
_OrinocoNet_ObjectIdentity = ObjectIdentity
orinocoNet = _OrinocoNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 3)
)
_OrinocoNetIP_ObjectIdentity = ObjectIdentity
orinocoNetIP = _OrinocoNetIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 3, 1)
)
_OriNetworkIPConfigTable_Object = MibTable
oriNetworkIPConfigTable = _OriNetworkIPConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    oriNetworkIPConfigTable.setStatus("current")
_OriNetworkIPConfigTableEntry_Object = MibTableRow
oriNetworkIPConfigTableEntry = _OriNetworkIPConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 3, 1, 1, 1)
)
oriNetworkIPConfigTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriNetworkIPConfigTableIndex"),
)
if mibBuilder.loadTexts:
    oriNetworkIPConfigTableEntry.setStatus("current")
_OriNetworkIPConfigTableIndex_Type = Integer32
_OriNetworkIPConfigTableIndex_Object = MibTableColumn
oriNetworkIPConfigTableIndex = _OriNetworkIPConfigTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 3, 1, 1, 1, 1),
    _OriNetworkIPConfigTableIndex_Type()
)
oriNetworkIPConfigTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriNetworkIPConfigTableIndex.setStatus("current")
_OriNetworkIPConfigIPAddress_Type = IpAddress
_OriNetworkIPConfigIPAddress_Object = MibTableColumn
oriNetworkIPConfigIPAddress = _OriNetworkIPConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 3, 1, 1, 1, 2),
    _OriNetworkIPConfigIPAddress_Type()
)
oriNetworkIPConfigIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriNetworkIPConfigIPAddress.setStatus("current")
_OriNetworkIPConfigSubnetMask_Type = IpAddress
_OriNetworkIPConfigSubnetMask_Object = MibTableColumn
oriNetworkIPConfigSubnetMask = _OriNetworkIPConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 3, 1, 1, 1, 3),
    _OriNetworkIPConfigSubnetMask_Type()
)
oriNetworkIPConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriNetworkIPConfigSubnetMask.setStatus("current")
_OriNetworkIPDefaultRouterIPAddress_Type = IpAddress
_OriNetworkIPDefaultRouterIPAddress_Object = MibScalar
oriNetworkIPDefaultRouterIPAddress = _OriNetworkIPDefaultRouterIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 3, 1, 3),
    _OriNetworkIPDefaultRouterIPAddress_Type()
)
oriNetworkIPDefaultRouterIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriNetworkIPDefaultRouterIPAddress.setStatus("current")


class _OriNetworkIPDefaultTTL_Type(Integer32):
    """Custom type oriNetworkIPDefaultTTL based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OriNetworkIPDefaultTTL_Type.__name__ = "Integer32"
_OriNetworkIPDefaultTTL_Object = MibScalar
oriNetworkIPDefaultTTL = _OriNetworkIPDefaultTTL_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 3, 1, 4),
    _OriNetworkIPDefaultTTL_Type()
)
oriNetworkIPDefaultTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriNetworkIPDefaultTTL.setStatus("current")


class _OriNetworkIPAddressType_Type(Integer32):
    """Custom type oriNetworkIPAddressType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_OriNetworkIPAddressType_Type.__name__ = "Integer32"
_OriNetworkIPAddressType_Object = MibScalar
oriNetworkIPAddressType = _OriNetworkIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 3, 1, 5),
    _OriNetworkIPAddressType_Type()
)
oriNetworkIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriNetworkIPAddressType.setStatus("current")
_OrinocoSNMP_ObjectIdentity = ObjectIdentity
orinocoSNMP = _OrinocoSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4)
)


class _OriSNMPReadPassword_Type(DisplayString):
    """Custom type oriSNMPReadPassword based on DisplayString"""
    defaultValue = OctetString("public")


_OriSNMPReadPassword_Object = MibScalar
oriSNMPReadPassword = _OriSNMPReadPassword_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 1),
    _OriSNMPReadPassword_Type()
)
oriSNMPReadPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPReadPassword.setStatus("current")


class _OriSNMPReadWritePassword_Type(DisplayString):
    """Custom type oriSNMPReadWritePassword based on DisplayString"""
    defaultValue = OctetString("public")


_OriSNMPReadWritePassword_Object = MibScalar
oriSNMPReadWritePassword = _OriSNMPReadWritePassword_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 2),
    _OriSNMPReadWritePassword_Type()
)
oriSNMPReadWritePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPReadWritePassword.setStatus("current")
_OriSNMPAuthorizedManagerCount_Type = Counter32
_OriSNMPAuthorizedManagerCount_Object = MibScalar
oriSNMPAuthorizedManagerCount = _OriSNMPAuthorizedManagerCount_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 3),
    _OriSNMPAuthorizedManagerCount_Type()
)
oriSNMPAuthorizedManagerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSNMPAuthorizedManagerCount.setStatus("current")
_OriSNMPAccessTable_Object = MibTable
oriSNMPAccessTable = _OriSNMPAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    oriSNMPAccessTable.setStatus("current")
_OriSNMPAccessTableEntry_Object = MibTableRow
oriSNMPAccessTableEntry = _OriSNMPAccessTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 4, 1)
)
oriSNMPAccessTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriSNMPAccessTableIndex"),
)
if mibBuilder.loadTexts:
    oriSNMPAccessTableEntry.setStatus("current")


class _OriSNMPAccessTableIndex_Type(Integer32):
    """Custom type oriSNMPAccessTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_OriSNMPAccessTableIndex_Type.__name__ = "Integer32"
_OriSNMPAccessTableIndex_Object = MibTableColumn
oriSNMPAccessTableIndex = _OriSNMPAccessTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 4, 1, 1),
    _OriSNMPAccessTableIndex_Type()
)
oriSNMPAccessTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSNMPAccessTableIndex.setStatus("current")
_OriSNMPAccessTableIPAddress_Type = IpAddress
_OriSNMPAccessTableIPAddress_Object = MibTableColumn
oriSNMPAccessTableIPAddress = _OriSNMPAccessTableIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 4, 1, 2),
    _OriSNMPAccessTableIPAddress_Type()
)
oriSNMPAccessTableIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPAccessTableIPAddress.setStatus("current")
_OriSNMPAccessTableIPMask_Type = IpAddress
_OriSNMPAccessTableIPMask_Object = MibTableColumn
oriSNMPAccessTableIPMask = _OriSNMPAccessTableIPMask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 4, 1, 3),
    _OriSNMPAccessTableIPMask_Type()
)
oriSNMPAccessTableIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPAccessTableIPMask.setStatus("current")
_OriSNMPAccessTableInterfaceBitmask_Type = InterfaceBitmask
_OriSNMPAccessTableInterfaceBitmask_Object = MibTableColumn
oriSNMPAccessTableInterfaceBitmask = _OriSNMPAccessTableInterfaceBitmask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 4, 1, 4),
    _OriSNMPAccessTableInterfaceBitmask_Type()
)
oriSNMPAccessTableInterfaceBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPAccessTableInterfaceBitmask.setStatus("current")
_OriSNMPAccessTableComment_Type = DisplayString
_OriSNMPAccessTableComment_Object = MibTableColumn
oriSNMPAccessTableComment = _OriSNMPAccessTableComment_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 4, 1, 5),
    _OriSNMPAccessTableComment_Type()
)
oriSNMPAccessTableComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPAccessTableComment.setStatus("current")


class _OriSNMPAccessTableEntryStatus_Type(Integer32):
    """Custom type oriSNMPAccessTableEntryStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriSNMPAccessTableEntryStatus_Type.__name__ = "Integer32"
_OriSNMPAccessTableEntryStatus_Object = MibTableColumn
oriSNMPAccessTableEntryStatus = _OriSNMPAccessTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 4, 1, 6),
    _OriSNMPAccessTableEntryStatus_Type()
)
oriSNMPAccessTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPAccessTableEntryStatus.setStatus("current")
_OriSNMPTrapHostTable_Object = MibTable
oriSNMPTrapHostTable = _OriSNMPTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    oriSNMPTrapHostTable.setStatus("current")
_OriSNMPTrapHostTableEntry_Object = MibTableRow
oriSNMPTrapHostTableEntry = _OriSNMPTrapHostTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 5, 1)
)
oriSNMPTrapHostTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriSNMPTrapHostTableIndex"),
)
if mibBuilder.loadTexts:
    oriSNMPTrapHostTableEntry.setStatus("current")


class _OriSNMPTrapHostTableIndex_Type(Integer32):
    """Custom type oriSNMPTrapHostTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_OriSNMPTrapHostTableIndex_Type.__name__ = "Integer32"
_OriSNMPTrapHostTableIndex_Object = MibTableColumn
oriSNMPTrapHostTableIndex = _OriSNMPTrapHostTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 5, 1, 1),
    _OriSNMPTrapHostTableIndex_Type()
)
oriSNMPTrapHostTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSNMPTrapHostTableIndex.setStatus("current")
_OriSNMPTrapHostTableIPAddress_Type = IpAddress
_OriSNMPTrapHostTableIPAddress_Object = MibTableColumn
oriSNMPTrapHostTableIPAddress = _OriSNMPTrapHostTableIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 5, 1, 2),
    _OriSNMPTrapHostTableIPAddress_Type()
)
oriSNMPTrapHostTableIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPTrapHostTableIPAddress.setStatus("current")
_OriSNMPTrapHostTablePassword_Type = DisplayString
_OriSNMPTrapHostTablePassword_Object = MibTableColumn
oriSNMPTrapHostTablePassword = _OriSNMPTrapHostTablePassword_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 5, 1, 3),
    _OriSNMPTrapHostTablePassword_Type()
)
oriSNMPTrapHostTablePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPTrapHostTablePassword.setStatus("current")
_OriSNMPTrapHostTableComment_Type = DisplayString
_OriSNMPTrapHostTableComment_Object = MibTableColumn
oriSNMPTrapHostTableComment = _OriSNMPTrapHostTableComment_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 5, 1, 4),
    _OriSNMPTrapHostTableComment_Type()
)
oriSNMPTrapHostTableComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPTrapHostTableComment.setStatus("current")


class _OriSNMPTrapHostTableEntryStatus_Type(Integer32):
    """Custom type oriSNMPTrapHostTableEntryStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriSNMPTrapHostTableEntryStatus_Type.__name__ = "Integer32"
_OriSNMPTrapHostTableEntryStatus_Object = MibTableColumn
oriSNMPTrapHostTableEntryStatus = _OriSNMPTrapHostTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 5, 1, 5),
    _OriSNMPTrapHostTableEntryStatus_Type()
)
oriSNMPTrapHostTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPTrapHostTableEntryStatus.setStatus("current")
_OriSNMPInterfaceBitmask_Type = InterfaceBitmask
_OriSNMPInterfaceBitmask_Object = MibScalar
oriSNMPInterfaceBitmask = _OriSNMPInterfaceBitmask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 7),
    _OriSNMPInterfaceBitmask_Type()
)
oriSNMPInterfaceBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPInterfaceBitmask.setStatus("current")
_OriSNMPErrorMessage_Type = DisplayString
_OriSNMPErrorMessage_Object = MibScalar
oriSNMPErrorMessage = _OriSNMPErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 8),
    _OriSNMPErrorMessage_Type()
)
oriSNMPErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSNMPErrorMessage.setStatus("current")


class _OriSNMPAccessTableStatus_Type(Integer32):
    """Custom type oriSNMPAccessTableStatus based on Integer32"""
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


_OriSNMPAccessTableStatus_Type.__name__ = "Integer32"
_OriSNMPAccessTableStatus_Object = MibScalar
oriSNMPAccessTableStatus = _OriSNMPAccessTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 9),
    _OriSNMPAccessTableStatus_Type()
)
oriSNMPAccessTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPAccessTableStatus.setStatus("current")


class _OriSNMPTrapType_Type(Integer32):
    """Custom type oriSNMPTrapType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmp-v1", 1),
          ("snmp-v2c", 2))
    )


_OriSNMPTrapType_Type.__name__ = "Integer32"
_OriSNMPTrapType_Object = MibScalar
oriSNMPTrapType = _OriSNMPTrapType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 10),
    _OriSNMPTrapType_Type()
)
oriSNMPTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPTrapType.setStatus("current")


class _OriSNMPSecureManagementStatus_Type(Integer32):
    """Custom type oriSNMPSecureManagementStatus based on Integer32"""
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


_OriSNMPSecureManagementStatus_Type.__name__ = "Integer32"
_OriSNMPSecureManagementStatus_Object = MibScalar
oriSNMPSecureManagementStatus = _OriSNMPSecureManagementStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 11),
    _OriSNMPSecureManagementStatus_Type()
)
oriSNMPSecureManagementStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPSecureManagementStatus.setStatus("current")


class _OriSNMPV3AuthPassword_Type(DisplayString):
    """Custom type oriSNMPV3AuthPassword based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 32),
    )


_OriSNMPV3AuthPassword_Type.__name__ = "DisplayString"
_OriSNMPV3AuthPassword_Object = MibScalar
oriSNMPV3AuthPassword = _OriSNMPV3AuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 12),
    _OriSNMPV3AuthPassword_Type()
)
oriSNMPV3AuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPV3AuthPassword.setStatus("current")


class _OriSNMPV3PrivPassword_Type(DisplayString):
    """Custom type oriSNMPV3PrivPassword based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 32),
    )


_OriSNMPV3PrivPassword_Type.__name__ = "DisplayString"
_OriSNMPV3PrivPassword_Object = MibScalar
oriSNMPV3PrivPassword = _OriSNMPV3PrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 4, 13),
    _OriSNMPV3PrivPassword_Type()
)
oriSNMPV3PrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNMPV3PrivPassword.setStatus("current")
_OrinocoFiltering_ObjectIdentity = ObjectIdentity
orinocoFiltering = _OrinocoFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5)
)
_OrinocoProtocolFilter_ObjectIdentity = ObjectIdentity
orinocoProtocolFilter = _OrinocoProtocolFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 1)
)


class _OriProtocolFilterOperationType_Type(Integer32):
    """Custom type oriProtocolFilterOperationType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("passthru", 1))
    )


_OriProtocolFilterOperationType_Type.__name__ = "Integer32"
_OriProtocolFilterOperationType_Object = MibScalar
oriProtocolFilterOperationType = _OriProtocolFilterOperationType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 1, 1),
    _OriProtocolFilterOperationType_Type()
)
oriProtocolFilterOperationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriProtocolFilterOperationType.setStatus("current")
_OriProtocolFilterTable_Object = MibTable
oriProtocolFilterTable = _OriProtocolFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    oriProtocolFilterTable.setStatus("current")
_OriProtocolFilterTableEntry_Object = MibTableRow
oriProtocolFilterTableEntry = _OriProtocolFilterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 1, 2, 1)
)
oriProtocolFilterTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriProtocolFilterTableIndex"),
)
if mibBuilder.loadTexts:
    oriProtocolFilterTableEntry.setStatus("current")


class _OriProtocolFilterTableIndex_Type(Integer32):
    """Custom type oriProtocolFilterTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_OriProtocolFilterTableIndex_Type.__name__ = "Integer32"
_OriProtocolFilterTableIndex_Object = MibTableColumn
oriProtocolFilterTableIndex = _OriProtocolFilterTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 1, 2, 1, 1),
    _OriProtocolFilterTableIndex_Type()
)
oriProtocolFilterTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriProtocolFilterTableIndex.setStatus("current")


class _OriProtocolFilterProtocol_Type(OctetString):
    """Custom type oriProtocolFilterProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_OriProtocolFilterProtocol_Type.__name__ = "OctetString"
_OriProtocolFilterProtocol_Object = MibTableColumn
oriProtocolFilterProtocol = _OriProtocolFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 1, 2, 1, 2),
    _OriProtocolFilterProtocol_Type()
)
oriProtocolFilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriProtocolFilterProtocol.setStatus("current")
_OriProtocolFilterProtocolComment_Type = DisplayString
_OriProtocolFilterProtocolComment_Object = MibTableColumn
oriProtocolFilterProtocolComment = _OriProtocolFilterProtocolComment_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 1, 2, 1, 3),
    _OriProtocolFilterProtocolComment_Type()
)
oriProtocolFilterProtocolComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriProtocolFilterProtocolComment.setStatus("current")


class _OriProtocolFilterTableEntryStatus_Type(Integer32):
    """Custom type oriProtocolFilterTableEntryStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriProtocolFilterTableEntryStatus_Type.__name__ = "Integer32"
_OriProtocolFilterTableEntryStatus_Object = MibTableColumn
oriProtocolFilterTableEntryStatus = _OriProtocolFilterTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 1, 2, 1, 4),
    _OriProtocolFilterTableEntryStatus_Type()
)
oriProtocolFilterTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriProtocolFilterTableEntryStatus.setStatus("current")
_OriProtocolFilterTableInterfaceBitmask_Type = InterfaceBitmask
_OriProtocolFilterTableInterfaceBitmask_Object = MibTableColumn
oriProtocolFilterTableInterfaceBitmask = _OriProtocolFilterTableInterfaceBitmask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 1, 2, 1, 5),
    _OriProtocolFilterTableInterfaceBitmask_Type()
)
oriProtocolFilterTableInterfaceBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriProtocolFilterTableInterfaceBitmask.setStatus("current")
_OriProtocolFilterProtocolString_Type = DisplayString
_OriProtocolFilterProtocolString_Object = MibTableColumn
oriProtocolFilterProtocolString = _OriProtocolFilterProtocolString_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 1, 2, 1, 6),
    _OriProtocolFilterProtocolString_Type()
)
oriProtocolFilterProtocolString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriProtocolFilterProtocolString.setStatus("current")
_OriProtocolFilterInterfaceBitmask_Type = InterfaceBitmask
_OriProtocolFilterInterfaceBitmask_Object = MibScalar
oriProtocolFilterInterfaceBitmask = _OriProtocolFilterInterfaceBitmask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 1, 3),
    _OriProtocolFilterInterfaceBitmask_Type()
)
oriProtocolFilterInterfaceBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriProtocolFilterInterfaceBitmask.setStatus("current")
_OrinocoAccessControl_ObjectIdentity = ObjectIdentity
orinocoAccessControl = _OrinocoAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 2)
)


class _OriAccessControlStatus_Type(Integer32):
    """Custom type oriAccessControlStatus based on Integer32"""
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


_OriAccessControlStatus_Type.__name__ = "Integer32"
_OriAccessControlStatus_Object = MibScalar
oriAccessControlStatus = _OriAccessControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 2, 1),
    _OriAccessControlStatus_Type()
)
oriAccessControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriAccessControlStatus.setStatus("current")


class _OriAccessControlOperationType_Type(Integer32):
    """Custom type oriAccessControlOperationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("passthru", 1))
    )


_OriAccessControlOperationType_Type.__name__ = "Integer32"
_OriAccessControlOperationType_Object = MibScalar
oriAccessControlOperationType = _OriAccessControlOperationType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 2, 2),
    _OriAccessControlOperationType_Type()
)
oriAccessControlOperationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriAccessControlOperationType.setStatus("current")
_OriAccessControlTable_Object = MibTable
oriAccessControlTable = _OriAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    oriAccessControlTable.setStatus("current")
_OriAccessControlEntry_Object = MibTableRow
oriAccessControlEntry = _OriAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 2, 3, 1)
)
oriAccessControlEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriAccessControlTableIndex"),
)
if mibBuilder.loadTexts:
    oriAccessControlEntry.setStatus("current")


class _OriAccessControlTableIndex_Type(Integer32):
    """Custom type oriAccessControlTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_OriAccessControlTableIndex_Type.__name__ = "Integer32"
_OriAccessControlTableIndex_Object = MibTableColumn
oriAccessControlTableIndex = _OriAccessControlTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 2, 3, 1, 1),
    _OriAccessControlTableIndex_Type()
)
oriAccessControlTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriAccessControlTableIndex.setStatus("current")
_OriAccessControlTableMACAddress_Type = PhysAddress
_OriAccessControlTableMACAddress_Object = MibTableColumn
oriAccessControlTableMACAddress = _OriAccessControlTableMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 2, 3, 1, 2),
    _OriAccessControlTableMACAddress_Type()
)
oriAccessControlTableMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriAccessControlTableMACAddress.setStatus("current")
_OriAccessControlTableComment_Type = DisplayString
_OriAccessControlTableComment_Object = MibTableColumn
oriAccessControlTableComment = _OriAccessControlTableComment_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 2, 3, 1, 3),
    _OriAccessControlTableComment_Type()
)
oriAccessControlTableComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriAccessControlTableComment.setStatus("current")


class _OriAccessControlTableEntryStatus_Type(Integer32):
    """Custom type oriAccessControlTableEntryStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriAccessControlTableEntryStatus_Type.__name__ = "Integer32"
_OriAccessControlTableEntryStatus_Object = MibTableColumn
oriAccessControlTableEntryStatus = _OriAccessControlTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 2, 3, 1, 4),
    _OriAccessControlTableEntryStatus_Type()
)
oriAccessControlTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriAccessControlTableEntryStatus.setStatus("current")
_OrinocoStaticMACAddressFilter_ObjectIdentity = ObjectIdentity
orinocoStaticMACAddressFilter = _OrinocoStaticMACAddressFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 3)
)
_OriStaticMACAddressFilterTable_Object = MibTable
oriStaticMACAddressFilterTable = _OriStaticMACAddressFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    oriStaticMACAddressFilterTable.setStatus("current")
_OriStaticMACAddressFilterEntry_Object = MibTableRow
oriStaticMACAddressFilterEntry = _OriStaticMACAddressFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 3, 1, 1)
)
oriStaticMACAddressFilterEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriStaticMACAddressFilterTableIndex"),
)
if mibBuilder.loadTexts:
    oriStaticMACAddressFilterEntry.setStatus("current")


class _OriStaticMACAddressFilterTableIndex_Type(Integer32):
    """Custom type oriStaticMACAddressFilterTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_OriStaticMACAddressFilterTableIndex_Type.__name__ = "Integer32"
_OriStaticMACAddressFilterTableIndex_Object = MibTableColumn
oriStaticMACAddressFilterTableIndex = _OriStaticMACAddressFilterTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 3, 1, 1, 1),
    _OriStaticMACAddressFilterTableIndex_Type()
)
oriStaticMACAddressFilterTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStaticMACAddressFilterTableIndex.setStatus("current")
_OriStaticMACAddressFilterWiredAddress_Type = PhysAddress
_OriStaticMACAddressFilterWiredAddress_Object = MibTableColumn
oriStaticMACAddressFilterWiredAddress = _OriStaticMACAddressFilterWiredAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 3, 1, 1, 2),
    _OriStaticMACAddressFilterWiredAddress_Type()
)
oriStaticMACAddressFilterWiredAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriStaticMACAddressFilterWiredAddress.setStatus("current")
_OriStaticMACAddressFilterWiredMask_Type = PhysAddress
_OriStaticMACAddressFilterWiredMask_Object = MibTableColumn
oriStaticMACAddressFilterWiredMask = _OriStaticMACAddressFilterWiredMask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 3, 1, 1, 3),
    _OriStaticMACAddressFilterWiredMask_Type()
)
oriStaticMACAddressFilterWiredMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriStaticMACAddressFilterWiredMask.setStatus("current")
_OriStaticMACAddressFilterWirelessAddress_Type = PhysAddress
_OriStaticMACAddressFilterWirelessAddress_Object = MibTableColumn
oriStaticMACAddressFilterWirelessAddress = _OriStaticMACAddressFilterWirelessAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 3, 1, 1, 4),
    _OriStaticMACAddressFilterWirelessAddress_Type()
)
oriStaticMACAddressFilterWirelessAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriStaticMACAddressFilterWirelessAddress.setStatus("current")
_OriStaticMACAddressFilterWirelessMask_Type = PhysAddress
_OriStaticMACAddressFilterWirelessMask_Object = MibTableColumn
oriStaticMACAddressFilterWirelessMask = _OriStaticMACAddressFilterWirelessMask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 3, 1, 1, 5),
    _OriStaticMACAddressFilterWirelessMask_Type()
)
oriStaticMACAddressFilterWirelessMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriStaticMACAddressFilterWirelessMask.setStatus("current")


class _OriStaticMACAddressFilterTableEntryStatus_Type(Integer32):
    """Custom type oriStaticMACAddressFilterTableEntryStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriStaticMACAddressFilterTableEntryStatus_Type.__name__ = "Integer32"
_OriStaticMACAddressFilterTableEntryStatus_Object = MibTableColumn
oriStaticMACAddressFilterTableEntryStatus = _OriStaticMACAddressFilterTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 3, 1, 1, 6),
    _OriStaticMACAddressFilterTableEntryStatus_Type()
)
oriStaticMACAddressFilterTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriStaticMACAddressFilterTableEntryStatus.setStatus("current")
_OriStaticMACAddressFilterComment_Type = DisplayString
_OriStaticMACAddressFilterComment_Object = MibTableColumn
oriStaticMACAddressFilterComment = _OriStaticMACAddressFilterComment_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 3, 1, 1, 7),
    _OriStaticMACAddressFilterComment_Type()
)
oriStaticMACAddressFilterComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriStaticMACAddressFilterComment.setStatus("current")
_OrinocoStormThreshold_ObjectIdentity = ObjectIdentity
orinocoStormThreshold = _OrinocoStormThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 4)
)


class _OriBroadcastAddressThreshold_Type(Integer32):
    """Custom type oriBroadcastAddressThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OriBroadcastAddressThreshold_Type.__name__ = "Integer32"
_OriBroadcastAddressThreshold_Object = MibScalar
oriBroadcastAddressThreshold = _OriBroadcastAddressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 4, 1),
    _OriBroadcastAddressThreshold_Type()
)
oriBroadcastAddressThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriBroadcastAddressThreshold.setStatus("current")


class _OriMulticastAddressThreshold_Type(Integer32):
    """Custom type oriMulticastAddressThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OriMulticastAddressThreshold_Type.__name__ = "Integer32"
_OriMulticastAddressThreshold_Object = MibScalar
oriMulticastAddressThreshold = _OriMulticastAddressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 4, 2),
    _OriMulticastAddressThreshold_Type()
)
oriMulticastAddressThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriMulticastAddressThreshold.setStatus("current")
_OriStormThresholdTable_Object = MibTable
oriStormThresholdTable = _OriStormThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 4, 3)
)
if mibBuilder.loadTexts:
    oriStormThresholdTable.setStatus("current")
_OriStormThresholdTableEntry_Object = MibTableRow
oriStormThresholdTableEntry = _OriStormThresholdTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 4, 3, 1)
)
oriStormThresholdTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oriStormThresholdTableEntry.setStatus("current")


class _OriStormThresholdIfBroadcast_Type(Integer32):
    """Custom type oriStormThresholdIfBroadcast based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_OriStormThresholdIfBroadcast_Type.__name__ = "Integer32"
_OriStormThresholdIfBroadcast_Object = MibTableColumn
oriStormThresholdIfBroadcast = _OriStormThresholdIfBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 4, 3, 1, 1),
    _OriStormThresholdIfBroadcast_Type()
)
oriStormThresholdIfBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriStormThresholdIfBroadcast.setStatus("current")


class _OriStormThresholdIfMulticast_Type(Integer32):
    """Custom type oriStormThresholdIfMulticast based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_OriStormThresholdIfMulticast_Type.__name__ = "Integer32"
_OriStormThresholdIfMulticast_Object = MibTableColumn
oriStormThresholdIfMulticast = _OriStormThresholdIfMulticast_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 4, 3, 1, 2),
    _OriStormThresholdIfMulticast_Type()
)
oriStormThresholdIfMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriStormThresholdIfMulticast.setStatus("current")
_OrinocoPortFilter_ObjectIdentity = ObjectIdentity
orinocoPortFilter = _OrinocoPortFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 5)
)


class _OriPortFilterStatus_Type(Integer32):
    """Custom type oriPortFilterStatus based on Integer32"""
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


_OriPortFilterStatus_Type.__name__ = "Integer32"
_OriPortFilterStatus_Object = MibScalar
oriPortFilterStatus = _OriPortFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 5, 1),
    _OriPortFilterStatus_Type()
)
oriPortFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPortFilterStatus.setStatus("current")


class _OriPortFilterOperationType_Type(Integer32):
    """Custom type oriPortFilterOperationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("passthru", 1))
    )


_OriPortFilterOperationType_Type.__name__ = "Integer32"
_OriPortFilterOperationType_Object = MibScalar
oriPortFilterOperationType = _OriPortFilterOperationType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 5, 2),
    _OriPortFilterOperationType_Type()
)
oriPortFilterOperationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPortFilterOperationType.setStatus("current")
_OriPortFilterTable_Object = MibTable
oriPortFilterTable = _OriPortFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 5, 3)
)
if mibBuilder.loadTexts:
    oriPortFilterTable.setStatus("current")
_OriPortFilterTableEntry_Object = MibTableRow
oriPortFilterTableEntry = _OriPortFilterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 5, 3, 1)
)
oriPortFilterTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriPortFilterTableEntryIndex"),
)
if mibBuilder.loadTexts:
    oriPortFilterTableEntry.setStatus("current")


class _OriPortFilterTableEntryIndex_Type(Integer32):
    """Custom type oriPortFilterTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_OriPortFilterTableEntryIndex_Type.__name__ = "Integer32"
_OriPortFilterTableEntryIndex_Object = MibTableColumn
oriPortFilterTableEntryIndex = _OriPortFilterTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 5, 3, 1, 1),
    _OriPortFilterTableEntryIndex_Type()
)
oriPortFilterTableEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriPortFilterTableEntryIndex.setStatus("current")
_OriPortFilterTableEntryPort_Type = Integer32
_OriPortFilterTableEntryPort_Object = MibTableColumn
oriPortFilterTableEntryPort = _OriPortFilterTableEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 5, 3, 1, 2),
    _OriPortFilterTableEntryPort_Type()
)
oriPortFilterTableEntryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPortFilterTableEntryPort.setStatus("current")


class _OriPortFilterTableEntryPortType_Type(Integer32):
    """Custom type oriPortFilterTableEntryPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_OriPortFilterTableEntryPortType_Type.__name__ = "Integer32"
_OriPortFilterTableEntryPortType_Object = MibTableColumn
oriPortFilterTableEntryPortType = _OriPortFilterTableEntryPortType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 5, 3, 1, 3),
    _OriPortFilterTableEntryPortType_Type()
)
oriPortFilterTableEntryPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPortFilterTableEntryPortType.setStatus("current")
_OriPortFilterTableEntryInterfaceBitmask_Type = InterfaceBitmask
_OriPortFilterTableEntryInterfaceBitmask_Object = MibTableColumn
oriPortFilterTableEntryInterfaceBitmask = _OriPortFilterTableEntryInterfaceBitmask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 5, 3, 1, 4),
    _OriPortFilterTableEntryInterfaceBitmask_Type()
)
oriPortFilterTableEntryInterfaceBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPortFilterTableEntryInterfaceBitmask.setStatus("current")
_OriPortFilterTableEntryComment_Type = DisplayString
_OriPortFilterTableEntryComment_Object = MibTableColumn
oriPortFilterTableEntryComment = _OriPortFilterTableEntryComment_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 5, 3, 1, 5),
    _OriPortFilterTableEntryComment_Type()
)
oriPortFilterTableEntryComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPortFilterTableEntryComment.setStatus("current")


class _OriPortFilterTableEntryStatus_Type(Integer32):
    """Custom type oriPortFilterTableEntryStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriPortFilterTableEntryStatus_Type.__name__ = "Integer32"
_OriPortFilterTableEntryStatus_Object = MibTableColumn
oriPortFilterTableEntryStatus = _OriPortFilterTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 5, 3, 1, 6),
    _OriPortFilterTableEntryStatus_Type()
)
oriPortFilterTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPortFilterTableEntryStatus.setStatus("current")
_OrinocoAdvancedFiltering_ObjectIdentity = ObjectIdentity
orinocoAdvancedFiltering = _OrinocoAdvancedFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 6)
)
_OriBroadcastFilteringTable_Object = MibTable
oriBroadcastFilteringTable = _OriBroadcastFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 6, 1)
)
if mibBuilder.loadTexts:
    oriBroadcastFilteringTable.setStatus("current")
_OriBroadcastFilteringTableEntry_Object = MibTableRow
oriBroadcastFilteringTableEntry = _OriBroadcastFilteringTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 6, 1, 1)
)
oriBroadcastFilteringTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriBroadcastFilteringTableIndex"),
)
if mibBuilder.loadTexts:
    oriBroadcastFilteringTableEntry.setStatus("current")


class _OriBroadcastFilteringTableIndex_Type(Integer32):
    """Custom type oriBroadcastFilteringTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_OriBroadcastFilteringTableIndex_Type.__name__ = "Integer32"
_OriBroadcastFilteringTableIndex_Object = MibTableColumn
oriBroadcastFilteringTableIndex = _OriBroadcastFilteringTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 6, 1, 1, 1),
    _OriBroadcastFilteringTableIndex_Type()
)
oriBroadcastFilteringTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriBroadcastFilteringTableIndex.setStatus("current")
_OriBroadcastFilteringProtocolName_Type = DisplayString
_OriBroadcastFilteringProtocolName_Object = MibTableColumn
oriBroadcastFilteringProtocolName = _OriBroadcastFilteringProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 6, 1, 1, 2),
    _OriBroadcastFilteringProtocolName_Type()
)
oriBroadcastFilteringProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriBroadcastFilteringProtocolName.setStatus("current")


class _OriBroadcastFilteringDirection_Type(Integer32):
    """Custom type oriBroadcastFilteringDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ethernetToWireless", 1),
          ("wirelessToEthernet", 2))
    )


_OriBroadcastFilteringDirection_Type.__name__ = "Integer32"
_OriBroadcastFilteringDirection_Object = MibTableColumn
oriBroadcastFilteringDirection = _OriBroadcastFilteringDirection_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 6, 1, 1, 3),
    _OriBroadcastFilteringDirection_Type()
)
oriBroadcastFilteringDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriBroadcastFilteringDirection.setStatus("current")


class _OriBroadcastFilteringTableEntryStatus_Type(Integer32):
    """Custom type oriBroadcastFilteringTableEntryStatus based on Integer32"""
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


_OriBroadcastFilteringTableEntryStatus_Type.__name__ = "Integer32"
_OriBroadcastFilteringTableEntryStatus_Object = MibTableColumn
oriBroadcastFilteringTableEntryStatus = _OriBroadcastFilteringTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 6, 1, 1, 4),
    _OriBroadcastFilteringTableEntryStatus_Type()
)
oriBroadcastFilteringTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriBroadcastFilteringTableEntryStatus.setStatus("current")
_OrinocoPacketForwarding_ObjectIdentity = ObjectIdentity
orinocoPacketForwarding = _OrinocoPacketForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 7)
)


class _OriPacketForwardingStatus_Type(Integer32):
    """Custom type oriPacketForwardingStatus based on Integer32"""
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


_OriPacketForwardingStatus_Type.__name__ = "Integer32"
_OriPacketForwardingStatus_Object = MibScalar
oriPacketForwardingStatus = _OriPacketForwardingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 7, 1),
    _OriPacketForwardingStatus_Type()
)
oriPacketForwardingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPacketForwardingStatus.setStatus("current")
_OriPacketForwardingMACAddress_Type = MacAddress
_OriPacketForwardingMACAddress_Object = MibScalar
oriPacketForwardingMACAddress = _OriPacketForwardingMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 7, 2),
    _OriPacketForwardingMACAddress_Type()
)
oriPacketForwardingMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPacketForwardingMACAddress.setStatus("current")


class _OriPacketForwardingInterface_Type(Integer32):
    """Custom type oriPacketForwardingInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_OriPacketForwardingInterface_Type.__name__ = "Integer32"
_OriPacketForwardingInterface_Object = MibScalar
oriPacketForwardingInterface = _OriPacketForwardingInterface_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 7, 3),
    _OriPacketForwardingInterface_Type()
)
oriPacketForwardingInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPacketForwardingInterface.setStatus("current")
_OrinocoIBSSTraffic_ObjectIdentity = ObjectIdentity
orinocoIBSSTraffic = _OrinocoIBSSTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 8)
)


class _OriIBSSTrafficOperation_Type(Integer32):
    """Custom type oriIBSSTrafficOperation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("passthru", 1))
    )


_OriIBSSTrafficOperation_Type.__name__ = "Integer32"
_OriIBSSTrafficOperation_Object = MibScalar
oriIBSSTrafficOperation = _OriIBSSTrafficOperation_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 8, 1),
    _OriIBSSTrafficOperation_Type()
)
oriIBSSTrafficOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIBSSTrafficOperation.setStatus("current")
_OrinocoIntraCellBlocking_ObjectIdentity = ObjectIdentity
orinocoIntraCellBlocking = _OrinocoIntraCellBlocking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9)
)


class _OriIntraCellBlockingStatus_Type(ObjStatus):
    """Custom type oriIntraCellBlockingStatus based on ObjStatus"""


_OriIntraCellBlockingStatus_Object = MibScalar
oriIntraCellBlockingStatus = _OriIntraCellBlockingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 1),
    _OriIntraCellBlockingStatus_Type()
)
oriIntraCellBlockingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingStatus.setStatus("current")
_OriIntraCellBlockingMACTable_Object = MibTable
oriIntraCellBlockingMACTable = _OriIntraCellBlockingMACTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2)
)
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTable.setStatus("current")
_OriIntraCellBlockingMACTableEntry_Object = MibTableRow
oriIntraCellBlockingMACTableEntry = _OriIntraCellBlockingMACTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1)
)
oriIntraCellBlockingMACTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriIntraCellBlockingMACTableIndex"),
)
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableEntry.setStatus("current")


class _OriIntraCellBlockingMACTableIndex_Type(Integer32):
    """Custom type oriIntraCellBlockingMACTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_OriIntraCellBlockingMACTableIndex_Type.__name__ = "Integer32"
_OriIntraCellBlockingMACTableIndex_Object = MibTableColumn
oriIntraCellBlockingMACTableIndex = _OriIntraCellBlockingMACTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 1),
    _OriIntraCellBlockingMACTableIndex_Type()
)
oriIntraCellBlockingMACTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableIndex.setStatus("current")
_OriIntraCellBlockingMACTableMACAddress_Type = PhysAddress
_OriIntraCellBlockingMACTableMACAddress_Object = MibTableColumn
oriIntraCellBlockingMACTableMACAddress = _OriIntraCellBlockingMACTableMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 2),
    _OriIntraCellBlockingMACTableMACAddress_Type()
)
oriIntraCellBlockingMACTableMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableMACAddress.setStatus("current")


class _OriIntraCellBlockingMACTableGroupID1_Type(ObjStatusActive):
    """Custom type oriIntraCellBlockingMACTableGroupID1 based on ObjStatusActive"""


_OriIntraCellBlockingMACTableGroupID1_Object = MibTableColumn
oriIntraCellBlockingMACTableGroupID1 = _OriIntraCellBlockingMACTableGroupID1_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 3),
    _OriIntraCellBlockingMACTableGroupID1_Type()
)
oriIntraCellBlockingMACTableGroupID1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableGroupID1.setStatus("current")


class _OriIntraCellBlockingMACTableGroupID2_Type(ObjStatusActive):
    """Custom type oriIntraCellBlockingMACTableGroupID2 based on ObjStatusActive"""


_OriIntraCellBlockingMACTableGroupID2_Object = MibTableColumn
oriIntraCellBlockingMACTableGroupID2 = _OriIntraCellBlockingMACTableGroupID2_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 4),
    _OriIntraCellBlockingMACTableGroupID2_Type()
)
oriIntraCellBlockingMACTableGroupID2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableGroupID2.setStatus("current")


class _OriIntraCellBlockingMACTableGroupID3_Type(ObjStatusActive):
    """Custom type oriIntraCellBlockingMACTableGroupID3 based on ObjStatusActive"""


_OriIntraCellBlockingMACTableGroupID3_Object = MibTableColumn
oriIntraCellBlockingMACTableGroupID3 = _OriIntraCellBlockingMACTableGroupID3_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 5),
    _OriIntraCellBlockingMACTableGroupID3_Type()
)
oriIntraCellBlockingMACTableGroupID3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableGroupID3.setStatus("current")


class _OriIntraCellBlockingMACTableGroupID4_Type(ObjStatusActive):
    """Custom type oriIntraCellBlockingMACTableGroupID4 based on ObjStatusActive"""


_OriIntraCellBlockingMACTableGroupID4_Object = MibTableColumn
oriIntraCellBlockingMACTableGroupID4 = _OriIntraCellBlockingMACTableGroupID4_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 6),
    _OriIntraCellBlockingMACTableGroupID4_Type()
)
oriIntraCellBlockingMACTableGroupID4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableGroupID4.setStatus("current")


class _OriIntraCellBlockingMACTableGroupID5_Type(ObjStatusActive):
    """Custom type oriIntraCellBlockingMACTableGroupID5 based on ObjStatusActive"""


_OriIntraCellBlockingMACTableGroupID5_Object = MibTableColumn
oriIntraCellBlockingMACTableGroupID5 = _OriIntraCellBlockingMACTableGroupID5_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 7),
    _OriIntraCellBlockingMACTableGroupID5_Type()
)
oriIntraCellBlockingMACTableGroupID5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableGroupID5.setStatus("current")


class _OriIntraCellBlockingMACTableGroupID6_Type(ObjStatusActive):
    """Custom type oriIntraCellBlockingMACTableGroupID6 based on ObjStatusActive"""


_OriIntraCellBlockingMACTableGroupID6_Object = MibTableColumn
oriIntraCellBlockingMACTableGroupID6 = _OriIntraCellBlockingMACTableGroupID6_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 8),
    _OriIntraCellBlockingMACTableGroupID6_Type()
)
oriIntraCellBlockingMACTableGroupID6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableGroupID6.setStatus("current")


class _OriIntraCellBlockingMACTableGroupID7_Type(ObjStatusActive):
    """Custom type oriIntraCellBlockingMACTableGroupID7 based on ObjStatusActive"""


_OriIntraCellBlockingMACTableGroupID7_Object = MibTableColumn
oriIntraCellBlockingMACTableGroupID7 = _OriIntraCellBlockingMACTableGroupID7_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 9),
    _OriIntraCellBlockingMACTableGroupID7_Type()
)
oriIntraCellBlockingMACTableGroupID7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableGroupID7.setStatus("current")


class _OriIntraCellBlockingMACTableGroupID8_Type(ObjStatusActive):
    """Custom type oriIntraCellBlockingMACTableGroupID8 based on ObjStatusActive"""


_OriIntraCellBlockingMACTableGroupID8_Object = MibTableColumn
oriIntraCellBlockingMACTableGroupID8 = _OriIntraCellBlockingMACTableGroupID8_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 10),
    _OriIntraCellBlockingMACTableGroupID8_Type()
)
oriIntraCellBlockingMACTableGroupID8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableGroupID8.setStatus("current")


class _OriIntraCellBlockingMACTableGroupID9_Type(ObjStatusActive):
    """Custom type oriIntraCellBlockingMACTableGroupID9 based on ObjStatusActive"""


_OriIntraCellBlockingMACTableGroupID9_Object = MibTableColumn
oriIntraCellBlockingMACTableGroupID9 = _OriIntraCellBlockingMACTableGroupID9_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 11),
    _OriIntraCellBlockingMACTableGroupID9_Type()
)
oriIntraCellBlockingMACTableGroupID9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableGroupID9.setStatus("current")


class _OriIntraCellBlockingMACTableGroupID10_Type(ObjStatusActive):
    """Custom type oriIntraCellBlockingMACTableGroupID10 based on ObjStatusActive"""


_OriIntraCellBlockingMACTableGroupID10_Object = MibTableColumn
oriIntraCellBlockingMACTableGroupID10 = _OriIntraCellBlockingMACTableGroupID10_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 12),
    _OriIntraCellBlockingMACTableGroupID10_Type()
)
oriIntraCellBlockingMACTableGroupID10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableGroupID10.setStatus("current")


class _OriIntraCellBlockingMACTableGroupID11_Type(ObjStatusActive):
    """Custom type oriIntraCellBlockingMACTableGroupID11 based on ObjStatusActive"""


_OriIntraCellBlockingMACTableGroupID11_Object = MibTableColumn
oriIntraCellBlockingMACTableGroupID11 = _OriIntraCellBlockingMACTableGroupID11_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 13),
    _OriIntraCellBlockingMACTableGroupID11_Type()
)
oriIntraCellBlockingMACTableGroupID11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableGroupID11.setStatus("current")


class _OriIntraCellBlockingMACTableGroupID12_Type(ObjStatusActive):
    """Custom type oriIntraCellBlockingMACTableGroupID12 based on ObjStatusActive"""


_OriIntraCellBlockingMACTableGroupID12_Object = MibTableColumn
oriIntraCellBlockingMACTableGroupID12 = _OriIntraCellBlockingMACTableGroupID12_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 14),
    _OriIntraCellBlockingMACTableGroupID12_Type()
)
oriIntraCellBlockingMACTableGroupID12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableGroupID12.setStatus("current")


class _OriIntraCellBlockingMACTableGroupID13_Type(ObjStatusActive):
    """Custom type oriIntraCellBlockingMACTableGroupID13 based on ObjStatusActive"""


_OriIntraCellBlockingMACTableGroupID13_Object = MibTableColumn
oriIntraCellBlockingMACTableGroupID13 = _OriIntraCellBlockingMACTableGroupID13_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 15),
    _OriIntraCellBlockingMACTableGroupID13_Type()
)
oriIntraCellBlockingMACTableGroupID13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableGroupID13.setStatus("current")


class _OriIntraCellBlockingMACTableGroupID14_Type(ObjStatusActive):
    """Custom type oriIntraCellBlockingMACTableGroupID14 based on ObjStatusActive"""


_OriIntraCellBlockingMACTableGroupID14_Object = MibTableColumn
oriIntraCellBlockingMACTableGroupID14 = _OriIntraCellBlockingMACTableGroupID14_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 16),
    _OriIntraCellBlockingMACTableGroupID14_Type()
)
oriIntraCellBlockingMACTableGroupID14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableGroupID14.setStatus("current")


class _OriIntraCellBlockingMACTableGroupID15_Type(ObjStatusActive):
    """Custom type oriIntraCellBlockingMACTableGroupID15 based on ObjStatusActive"""


_OriIntraCellBlockingMACTableGroupID15_Object = MibTableColumn
oriIntraCellBlockingMACTableGroupID15 = _OriIntraCellBlockingMACTableGroupID15_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 17),
    _OriIntraCellBlockingMACTableGroupID15_Type()
)
oriIntraCellBlockingMACTableGroupID15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableGroupID15.setStatus("current")


class _OriIntraCellBlockingMACTableGroupID16_Type(ObjStatusActive):
    """Custom type oriIntraCellBlockingMACTableGroupID16 based on ObjStatusActive"""


_OriIntraCellBlockingMACTableGroupID16_Object = MibTableColumn
oriIntraCellBlockingMACTableGroupID16 = _OriIntraCellBlockingMACTableGroupID16_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 18),
    _OriIntraCellBlockingMACTableGroupID16_Type()
)
oriIntraCellBlockingMACTableGroupID16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableGroupID16.setStatus("current")


class _OriIntraCellBlockingMACTableEntryStatus_Type(Integer32):
    """Custom type oriIntraCellBlockingMACTableEntryStatus based on Integer32"""
    defaultValue = 1

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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriIntraCellBlockingMACTableEntryStatus_Type.__name__ = "Integer32"
_OriIntraCellBlockingMACTableEntryStatus_Object = MibTableColumn
oriIntraCellBlockingMACTableEntryStatus = _OriIntraCellBlockingMACTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 2, 1, 19),
    _OriIntraCellBlockingMACTableEntryStatus_Type()
)
oriIntraCellBlockingMACTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingMACTableEntryStatus.setStatus("current")
_OriIntraCellBlockingGroupTable_Object = MibTable
oriIntraCellBlockingGroupTable = _OriIntraCellBlockingGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 3)
)
if mibBuilder.loadTexts:
    oriIntraCellBlockingGroupTable.setStatus("current")
_OriIntraCellBlockingGroupTableEntry_Object = MibTableRow
oriIntraCellBlockingGroupTableEntry = _OriIntraCellBlockingGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 3, 1)
)
oriIntraCellBlockingGroupTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriIntraCellBlockingGroupTableIndex"),
)
if mibBuilder.loadTexts:
    oriIntraCellBlockingGroupTableEntry.setStatus("current")


class _OriIntraCellBlockingGroupTableIndex_Type(Integer32):
    """Custom type oriIntraCellBlockingGroupTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OriIntraCellBlockingGroupTableIndex_Type.__name__ = "Integer32"
_OriIntraCellBlockingGroupTableIndex_Object = MibTableColumn
oriIntraCellBlockingGroupTableIndex = _OriIntraCellBlockingGroupTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 3, 1, 1),
    _OriIntraCellBlockingGroupTableIndex_Type()
)
oriIntraCellBlockingGroupTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIntraCellBlockingGroupTableIndex.setStatus("current")
_OriIntraCellBlockingGroupTableName_Type = DisplayString
_OriIntraCellBlockingGroupTableName_Object = MibTableColumn
oriIntraCellBlockingGroupTableName = _OriIntraCellBlockingGroupTableName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 3, 1, 2),
    _OriIntraCellBlockingGroupTableName_Type()
)
oriIntraCellBlockingGroupTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingGroupTableName.setStatus("current")


class _OriIntraCellBlockingGroupTableEntryStatus_Type(Integer32):
    """Custom type oriIntraCellBlockingGroupTableEntryStatus based on Integer32"""
    defaultValue = 2

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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriIntraCellBlockingGroupTableEntryStatus_Type.__name__ = "Integer32"
_OriIntraCellBlockingGroupTableEntryStatus_Object = MibTableColumn
oriIntraCellBlockingGroupTableEntryStatus = _OriIntraCellBlockingGroupTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 9, 3, 1, 3),
    _OriIntraCellBlockingGroupTableEntryStatus_Type()
)
oriIntraCellBlockingGroupTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIntraCellBlockingGroupTableEntryStatus.setStatus("current")
_OrinocoSecurityGw_ObjectIdentity = ObjectIdentity
orinocoSecurityGw = _OrinocoSecurityGw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 10)
)


class _OriSecurityGwStatus_Type(ObjStatus):
    """Custom type oriSecurityGwStatus based on ObjStatus"""


_OriSecurityGwStatus_Object = MibScalar
oriSecurityGwStatus = _OriSecurityGwStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 10, 1),
    _OriSecurityGwStatus_Type()
)
oriSecurityGwStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSecurityGwStatus.setStatus("current")
_OriSecurityGwMac_Type = MacAddress
_OriSecurityGwMac_Object = MibScalar
oriSecurityGwMac = _OriSecurityGwMac_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 5, 10, 2),
    _OriSecurityGwMac_Type()
)
oriSecurityGwMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSecurityGwMac.setStatus("current")
_OrinocoRADIUS_ObjectIdentity = ObjectIdentity
orinocoRADIUS = _OrinocoRADIUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6)
)
_OrinocoRADIUSAuth_ObjectIdentity = ObjectIdentity
orinocoRADIUSAuth = _OrinocoRADIUSAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1)
)
_OriRADIUSAuthServerTable_Object = MibTable
oriRADIUSAuthServerTable = _OriRADIUSAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    oriRADIUSAuthServerTable.setStatus("current")
_OriRADIUSAuthServerTableEntry_Object = MibTableRow
oriRADIUSAuthServerTableEntry = _OriRADIUSAuthServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1)
)
oriRADIUSAuthServerTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriRADIUSAuthServerTableIndex"),
)
if mibBuilder.loadTexts:
    oriRADIUSAuthServerTableEntry.setStatus("current")


class _OriRADIUSAuthServerTableIndex_Type(Integer32):
    """Custom type oriRADIUSAuthServerTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_OriRADIUSAuthServerTableIndex_Type.__name__ = "Integer32"
_OriRADIUSAuthServerTableIndex_Object = MibTableColumn
oriRADIUSAuthServerTableIndex = _OriRADIUSAuthServerTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 1),
    _OriRADIUSAuthServerTableIndex_Type()
)
oriRADIUSAuthServerTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthServerTableIndex.setStatus("current")


class _OriRADIUSAuthServerType_Type(Integer32):
    """Custom type oriRADIUSAuthServerType based on Integer32"""
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
        *(("accounting", 2),
          ("authAndAcct", 3),
          ("authdot1x", 4),
          ("authentication", 1))
    )


_OriRADIUSAuthServerType_Type.__name__ = "Integer32"
_OriRADIUSAuthServerType_Object = MibTableColumn
oriRADIUSAuthServerType = _OriRADIUSAuthServerType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 2),
    _OriRADIUSAuthServerType_Type()
)
oriRADIUSAuthServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthServerType.setStatus("current")


class _OriRADIUSAuthServerTableEntryStatus_Type(Integer32):
    """Custom type oriRADIUSAuthServerTableEntryStatus based on Integer32"""
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


_OriRADIUSAuthServerTableEntryStatus_Type.__name__ = "Integer32"
_OriRADIUSAuthServerTableEntryStatus_Object = MibTableColumn
oriRADIUSAuthServerTableEntryStatus = _OriRADIUSAuthServerTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 3),
    _OriRADIUSAuthServerTableEntryStatus_Type()
)
oriRADIUSAuthServerTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAuthServerTableEntryStatus.setStatus("current")
_OriRADIUSAuthServerIPAddress_Type = IpAddress
_OriRADIUSAuthServerIPAddress_Object = MibTableColumn
oriRADIUSAuthServerIPAddress = _OriRADIUSAuthServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 4),
    _OriRADIUSAuthServerIPAddress_Type()
)
oriRADIUSAuthServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAuthServerIPAddress.setStatus("deprecated")


class _OriRADIUSAuthServerDestPort_Type(Integer32):
    """Custom type oriRADIUSAuthServerDestPort based on Integer32"""
    defaultValue = 1812


_OriRADIUSAuthServerDestPort_Object = MibTableColumn
oriRADIUSAuthServerDestPort = _OriRADIUSAuthServerDestPort_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 5),
    _OriRADIUSAuthServerDestPort_Type()
)
oriRADIUSAuthServerDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAuthServerDestPort.setStatus("current")
_OriRADIUSAuthServerSharedSecret_Type = DisplayString
_OriRADIUSAuthServerSharedSecret_Object = MibTableColumn
oriRADIUSAuthServerSharedSecret = _OriRADIUSAuthServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 6),
    _OriRADIUSAuthServerSharedSecret_Type()
)
oriRADIUSAuthServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAuthServerSharedSecret.setStatus("current")


class _OriRADIUSAuthServerResponseTime_Type(Integer32):
    """Custom type oriRADIUSAuthServerResponseTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_OriRADIUSAuthServerResponseTime_Type.__name__ = "Integer32"
_OriRADIUSAuthServerResponseTime_Object = MibTableColumn
oriRADIUSAuthServerResponseTime = _OriRADIUSAuthServerResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 7),
    _OriRADIUSAuthServerResponseTime_Type()
)
oriRADIUSAuthServerResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAuthServerResponseTime.setStatus("current")


class _OriRADIUSAuthServerMaximumRetransmission_Type(Integer32):
    """Custom type oriRADIUSAuthServerMaximumRetransmission based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_OriRADIUSAuthServerMaximumRetransmission_Type.__name__ = "Integer32"
_OriRADIUSAuthServerMaximumRetransmission_Object = MibTableColumn
oriRADIUSAuthServerMaximumRetransmission = _OriRADIUSAuthServerMaximumRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 8),
    _OriRADIUSAuthServerMaximumRetransmission_Type()
)
oriRADIUSAuthServerMaximumRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAuthServerMaximumRetransmission.setStatus("current")
_OriRADIUSAuthClientAccessRequests_Type = Counter32
_OriRADIUSAuthClientAccessRequests_Object = MibTableColumn
oriRADIUSAuthClientAccessRequests = _OriRADIUSAuthClientAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 9),
    _OriRADIUSAuthClientAccessRequests_Type()
)
oriRADIUSAuthClientAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientAccessRequests.setStatus("current")
_OriRADIUSAuthClientAccessRetransmissions_Type = Counter32
_OriRADIUSAuthClientAccessRetransmissions_Object = MibTableColumn
oriRADIUSAuthClientAccessRetransmissions = _OriRADIUSAuthClientAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 10),
    _OriRADIUSAuthClientAccessRetransmissions_Type()
)
oriRADIUSAuthClientAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientAccessRetransmissions.setStatus("current")
_OriRADIUSAuthClientAccessAccepts_Type = Counter32
_OriRADIUSAuthClientAccessAccepts_Object = MibTableColumn
oriRADIUSAuthClientAccessAccepts = _OriRADIUSAuthClientAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 11),
    _OriRADIUSAuthClientAccessAccepts_Type()
)
oriRADIUSAuthClientAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientAccessAccepts.setStatus("current")
_OriRADIUSAuthClientAccessChallenges_Type = Counter32
_OriRADIUSAuthClientAccessChallenges_Object = MibTableColumn
oriRADIUSAuthClientAccessChallenges = _OriRADIUSAuthClientAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 12),
    _OriRADIUSAuthClientAccessChallenges_Type()
)
oriRADIUSAuthClientAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientAccessChallenges.setStatus("current")
_OriRADIUSAuthClientAccessRejects_Type = Counter32
_OriRADIUSAuthClientAccessRejects_Object = MibTableColumn
oriRADIUSAuthClientAccessRejects = _OriRADIUSAuthClientAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 13),
    _OriRADIUSAuthClientAccessRejects_Type()
)
oriRADIUSAuthClientAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientAccessRejects.setStatus("current")
_OriRADIUSAuthClientMalformedAccessResponses_Type = Counter32
_OriRADIUSAuthClientMalformedAccessResponses_Object = MibTableColumn
oriRADIUSAuthClientMalformedAccessResponses = _OriRADIUSAuthClientMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 14),
    _OriRADIUSAuthClientMalformedAccessResponses_Type()
)
oriRADIUSAuthClientMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientMalformedAccessResponses.setStatus("current")
_OriRADIUSAuthClientAuthInvalidAuthenticators_Type = Counter32
_OriRADIUSAuthClientAuthInvalidAuthenticators_Object = MibTableColumn
oriRADIUSAuthClientAuthInvalidAuthenticators = _OriRADIUSAuthClientAuthInvalidAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 15),
    _OriRADIUSAuthClientAuthInvalidAuthenticators_Type()
)
oriRADIUSAuthClientAuthInvalidAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientAuthInvalidAuthenticators.setStatus("current")
_OriRADIUSAuthClientTimeouts_Type = Counter32
_OriRADIUSAuthClientTimeouts_Object = MibTableColumn
oriRADIUSAuthClientTimeouts = _OriRADIUSAuthClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 16),
    _OriRADIUSAuthClientTimeouts_Type()
)
oriRADIUSAuthClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientTimeouts.setStatus("current")
_OriRADIUSAuthServerNameOrIPAddress_Type = DisplayString
_OriRADIUSAuthServerNameOrIPAddress_Object = MibTableColumn
oriRADIUSAuthServerNameOrIPAddress = _OriRADIUSAuthServerNameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 17),
    _OriRADIUSAuthServerNameOrIPAddress_Type()
)
oriRADIUSAuthServerNameOrIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAuthServerNameOrIPAddress.setStatus("current")


class _OriRADIUSAuthServerAddressingFormat_Type(Integer32):
    """Custom type oriRADIUSAuthServerAddressingFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipAddress", 1),
          ("name", 2))
    )


_OriRADIUSAuthServerAddressingFormat_Type.__name__ = "Integer32"
_OriRADIUSAuthServerAddressingFormat_Object = MibTableColumn
oriRADIUSAuthServerAddressingFormat = _OriRADIUSAuthServerAddressingFormat_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 1, 1, 1, 18),
    _OriRADIUSAuthServerAddressingFormat_Type()
)
oriRADIUSAuthServerAddressingFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAuthServerAddressingFormat.setStatus("current")
_OrinocoRADIUSAcct_ObjectIdentity = ObjectIdentity
orinocoRADIUSAcct = _OrinocoRADIUSAcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2)
)


class _OriRADIUSAcctStatus_Type(Integer32):
    """Custom type oriRADIUSAcctStatus based on Integer32"""
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


_OriRADIUSAcctStatus_Type.__name__ = "Integer32"
_OriRADIUSAcctStatus_Object = MibScalar
oriRADIUSAcctStatus = _OriRADIUSAcctStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 1),
    _OriRADIUSAcctStatus_Type()
)
oriRADIUSAcctStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAcctStatus.setStatus("deprecated")


class _OriRADIUSAcctInactivityTimer_Type(Integer32):
    """Custom type oriRADIUSAcctInactivityTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_OriRADIUSAcctInactivityTimer_Type.__name__ = "Integer32"
_OriRADIUSAcctInactivityTimer_Object = MibScalar
oriRADIUSAcctInactivityTimer = _OriRADIUSAcctInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 2),
    _OriRADIUSAcctInactivityTimer_Type()
)
oriRADIUSAcctInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAcctInactivityTimer.setStatus("deprecated")
_OriRADIUSAcctServerTable_Object = MibTable
oriRADIUSAcctServerTable = _OriRADIUSAcctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    oriRADIUSAcctServerTable.setStatus("deprecated")
_OriRADIUSAcctServerTableEntry_Object = MibTableRow
oriRADIUSAcctServerTableEntry = _OriRADIUSAcctServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 3, 1)
)
oriRADIUSAcctServerTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriRADIUSAcctServerTableIndex"),
)
if mibBuilder.loadTexts:
    oriRADIUSAcctServerTableEntry.setStatus("deprecated")


class _OriRADIUSAcctServerTableIndex_Type(Integer32):
    """Custom type oriRADIUSAcctServerTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_OriRADIUSAcctServerTableIndex_Type.__name__ = "Integer32"
_OriRADIUSAcctServerTableIndex_Object = MibTableColumn
oriRADIUSAcctServerTableIndex = _OriRADIUSAcctServerTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 3, 1, 1),
    _OriRADIUSAcctServerTableIndex_Type()
)
oriRADIUSAcctServerTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAcctServerTableIndex.setStatus("deprecated")


class _OriRADIUSAcctServerType_Type(Integer32):
    """Custom type oriRADIUSAcctServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 2),
          ("authAndAcct", 3),
          ("authentication", 1))
    )


_OriRADIUSAcctServerType_Type.__name__ = "Integer32"
_OriRADIUSAcctServerType_Object = MibTableColumn
oriRADIUSAcctServerType = _OriRADIUSAcctServerType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 3, 1, 2),
    _OriRADIUSAcctServerType_Type()
)
oriRADIUSAcctServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAcctServerType.setStatus("deprecated")


class _OriRADIUSAcctServerTableEntryStatus_Type(Integer32):
    """Custom type oriRADIUSAcctServerTableEntryStatus based on Integer32"""
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


_OriRADIUSAcctServerTableEntryStatus_Type.__name__ = "Integer32"
_OriRADIUSAcctServerTableEntryStatus_Object = MibTableColumn
oriRADIUSAcctServerTableEntryStatus = _OriRADIUSAcctServerTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 3, 1, 3),
    _OriRADIUSAcctServerTableEntryStatus_Type()
)
oriRADIUSAcctServerTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAcctServerTableEntryStatus.setStatus("deprecated")
_OriRADIUSAcctServerIPAddress_Type = IpAddress
_OriRADIUSAcctServerIPAddress_Object = MibTableColumn
oriRADIUSAcctServerIPAddress = _OriRADIUSAcctServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 3, 1, 4),
    _OriRADIUSAcctServerIPAddress_Type()
)
oriRADIUSAcctServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAcctServerIPAddress.setStatus("deprecated")


class _OriRADIUSAcctServerDestPort_Type(Integer32):
    """Custom type oriRADIUSAcctServerDestPort based on Integer32"""
    defaultValue = 1813


_OriRADIUSAcctServerDestPort_Object = MibTableColumn
oriRADIUSAcctServerDestPort = _OriRADIUSAcctServerDestPort_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 3, 1, 5),
    _OriRADIUSAcctServerDestPort_Type()
)
oriRADIUSAcctServerDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAcctServerDestPort.setStatus("deprecated")
_OriRADIUSAcctServerSharedSecret_Type = DisplayString
_OriRADIUSAcctServerSharedSecret_Object = MibTableColumn
oriRADIUSAcctServerSharedSecret = _OriRADIUSAcctServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 3, 1, 6),
    _OriRADIUSAcctServerSharedSecret_Type()
)
oriRADIUSAcctServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAcctServerSharedSecret.setStatus("deprecated")


class _OriRADIUSAcctServerResponseTime_Type(Integer32):
    """Custom type oriRADIUSAcctServerResponseTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_OriRADIUSAcctServerResponseTime_Type.__name__ = "Integer32"
_OriRADIUSAcctServerResponseTime_Object = MibTableColumn
oriRADIUSAcctServerResponseTime = _OriRADIUSAcctServerResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 3, 1, 7),
    _OriRADIUSAcctServerResponseTime_Type()
)
oriRADIUSAcctServerResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAcctServerResponseTime.setStatus("deprecated")


class _OriRADIUSAcctServerMaximumRetransmission_Type(Integer32):
    """Custom type oriRADIUSAcctServerMaximumRetransmission based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_OriRADIUSAcctServerMaximumRetransmission_Type.__name__ = "Integer32"
_OriRADIUSAcctServerMaximumRetransmission_Object = MibTableColumn
oriRADIUSAcctServerMaximumRetransmission = _OriRADIUSAcctServerMaximumRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 3, 1, 8),
    _OriRADIUSAcctServerMaximumRetransmission_Type()
)
oriRADIUSAcctServerMaximumRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAcctServerMaximumRetransmission.setStatus("deprecated")
_OriRADIUSAcctClientAccountingRequests_Type = Counter32
_OriRADIUSAcctClientAccountingRequests_Object = MibTableColumn
oriRADIUSAcctClientAccountingRequests = _OriRADIUSAcctClientAccountingRequests_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 3, 1, 9),
    _OriRADIUSAcctClientAccountingRequests_Type()
)
oriRADIUSAcctClientAccountingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAcctClientAccountingRequests.setStatus("deprecated")
_OriRADIUSAcctClientAccountingRetransmissions_Type = Counter32
_OriRADIUSAcctClientAccountingRetransmissions_Object = MibTableColumn
oriRADIUSAcctClientAccountingRetransmissions = _OriRADIUSAcctClientAccountingRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 3, 1, 10),
    _OriRADIUSAcctClientAccountingRetransmissions_Type()
)
oriRADIUSAcctClientAccountingRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAcctClientAccountingRetransmissions.setStatus("deprecated")
_OriRADIUSAcctClientAccountingResponses_Type = Counter32
_OriRADIUSAcctClientAccountingResponses_Object = MibTableColumn
oriRADIUSAcctClientAccountingResponses = _OriRADIUSAcctClientAccountingResponses_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 3, 1, 11),
    _OriRADIUSAcctClientAccountingResponses_Type()
)
oriRADIUSAcctClientAccountingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAcctClientAccountingResponses.setStatus("deprecated")
_OriRADIUSAcctClientAcctInvalidAuthenticators_Type = Counter32
_OriRADIUSAcctClientAcctInvalidAuthenticators_Object = MibTableColumn
oriRADIUSAcctClientAcctInvalidAuthenticators = _OriRADIUSAcctClientAcctInvalidAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 3, 1, 12),
    _OriRADIUSAcctClientAcctInvalidAuthenticators_Type()
)
oriRADIUSAcctClientAcctInvalidAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAcctClientAcctInvalidAuthenticators.setStatus("deprecated")
_OriRADIUSAcctServerNameOrIPAddress_Type = DisplayString
_OriRADIUSAcctServerNameOrIPAddress_Object = MibTableColumn
oriRADIUSAcctServerNameOrIPAddress = _OriRADIUSAcctServerNameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 3, 1, 13),
    _OriRADIUSAcctServerNameOrIPAddress_Type()
)
oriRADIUSAcctServerNameOrIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAcctServerNameOrIPAddress.setStatus("deprecated")


class _OriRADIUSAcctServerAddressingFormat_Type(Integer32):
    """Custom type oriRADIUSAcctServerAddressingFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipAddress", 1),
          ("name", 2))
    )


_OriRADIUSAcctServerAddressingFormat_Type.__name__ = "Integer32"
_OriRADIUSAcctServerAddressingFormat_Object = MibTableColumn
oriRADIUSAcctServerAddressingFormat = _OriRADIUSAcctServerAddressingFormat_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 3, 1, 14),
    _OriRADIUSAcctServerAddressingFormat_Type()
)
oriRADIUSAcctServerAddressingFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAcctServerAddressingFormat.setStatus("deprecated")


class _OriRADIUSAcctUpdateInterval_Type(Integer32):
    """Custom type oriRADIUSAcctUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_OriRADIUSAcctUpdateInterval_Type.__name__ = "Integer32"
_OriRADIUSAcctUpdateInterval_Object = MibScalar
oriRADIUSAcctUpdateInterval = _OriRADIUSAcctUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 2, 4),
    _OriRADIUSAcctUpdateInterval_Type()
)
oriRADIUSAcctUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAcctUpdateInterval.setStatus("deprecated")
_OriRADIUSClientInvalidServerAddress_Type = Counter32
_OriRADIUSClientInvalidServerAddress_Object = MibScalar
oriRADIUSClientInvalidServerAddress = _OriRADIUSClientInvalidServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 3),
    _OriRADIUSClientInvalidServerAddress_Type()
)
oriRADIUSClientInvalidServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSClientInvalidServerAddress.setStatus("current")


class _OriRADIUSMACAccessControl_Type(Integer32):
    """Custom type oriRADIUSMACAccessControl based on Integer32"""
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


_OriRADIUSMACAccessControl_Type.__name__ = "Integer32"
_OriRADIUSMACAccessControl_Object = MibScalar
oriRADIUSMACAccessControl = _OriRADIUSMACAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 4),
    _OriRADIUSMACAccessControl_Type()
)
oriRADIUSMACAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSMACAccessControl.setStatus("current")


class _OriRADIUSAuthorizationLifeTime_Type(Integer32):
    """Custom type oriRADIUSAuthorizationLifeTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(7200, 43200),
    )


_OriRADIUSAuthorizationLifeTime_Type.__name__ = "Integer32"
_OriRADIUSAuthorizationLifeTime_Object = MibScalar
oriRADIUSAuthorizationLifeTime = _OriRADIUSAuthorizationLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 5),
    _OriRADIUSAuthorizationLifeTime_Type()
)
oriRADIUSAuthorizationLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSAuthorizationLifeTime.setStatus("current")


class _OriRADIUSMACAddressFormat_Type(Integer32):
    """Custom type oriRADIUSMACAddressFormat based on Integer32"""
    defaultValue = 1

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
        *(("colonDelimited", 2),
          ("dashDelimited", 1),
          ("noDelimiter", 4),
          ("singleDashDelimited", 3))
    )


_OriRADIUSMACAddressFormat_Type.__name__ = "Integer32"
_OriRADIUSMACAddressFormat_Object = MibScalar
oriRADIUSMACAddressFormat = _OriRADIUSMACAddressFormat_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 6),
    _OriRADIUSMACAddressFormat_Type()
)
oriRADIUSMACAddressFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSMACAddressFormat.setStatus("current")


class _OriRADIUSLocalUserStatus_Type(ObjStatus):
    """Custom type oriRADIUSLocalUserStatus based on ObjStatus"""


_OriRADIUSLocalUserStatus_Object = MibScalar
oriRADIUSLocalUserStatus = _OriRADIUSLocalUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 7),
    _OriRADIUSLocalUserStatus_Type()
)
oriRADIUSLocalUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSLocalUserStatus.setStatus("current")


class _OriRADIUSLocalUserPassword_Type(DisplayString):
    """Custom type oriRADIUSLocalUserPassword based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 32),
    )


_OriRADIUSLocalUserPassword_Type.__name__ = "DisplayString"
_OriRADIUSLocalUserPassword_Object = MibScalar
oriRADIUSLocalUserPassword = _OriRADIUSLocalUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 8),
    _OriRADIUSLocalUserPassword_Type()
)
oriRADIUSLocalUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSLocalUserPassword.setStatus("current")
_OriRADIUSbasedManagementAccessProfile_Type = DisplayString
_OriRADIUSbasedManagementAccessProfile_Object = MibScalar
oriRADIUSbasedManagementAccessProfile = _OriRADIUSbasedManagementAccessProfile_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 9),
    _OriRADIUSbasedManagementAccessProfile_Type()
)
oriRADIUSbasedManagementAccessProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSbasedManagementAccessProfile.setStatus("current")
_OrinocoRADIUSSvrProfiles_ObjectIdentity = ObjectIdentity
orinocoRADIUSSvrProfiles = _OrinocoRADIUSSvrProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10)
)
_OriRADIUSSvrTable_Object = MibTable
oriRADIUSSvrTable = _OriRADIUSSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1)
)
if mibBuilder.loadTexts:
    oriRADIUSSvrTable.setStatus("current")
_OriRADIUSSvrTableEntry_Object = MibTableRow
oriRADIUSSvrTableEntry = _OriRADIUSSvrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1, 1)
)
oriRADIUSSvrTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriRADIUSSvrTableProfileIndex"),
    (0, "ORiNOCO-MIB", "oriRADIUSSvrTablePrimaryOrSecondaryIndex"),
)
if mibBuilder.loadTexts:
    oriRADIUSSvrTableEntry.setStatus("current")
_OriRADIUSSvrTableProfileIndex_Type = Integer32
_OriRADIUSSvrTableProfileIndex_Object = MibTableColumn
oriRADIUSSvrTableProfileIndex = _OriRADIUSSvrTableProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1, 1, 1),
    _OriRADIUSSvrTableProfileIndex_Type()
)
oriRADIUSSvrTableProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSSvrTableProfileIndex.setStatus("current")


class _OriRADIUSSvrTablePrimaryOrSecondaryIndex_Type(Integer32):
    """Custom type oriRADIUSSvrTablePrimaryOrSecondaryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_OriRADIUSSvrTablePrimaryOrSecondaryIndex_Type.__name__ = "Integer32"
_OriRADIUSSvrTablePrimaryOrSecondaryIndex_Object = MibTableColumn
oriRADIUSSvrTablePrimaryOrSecondaryIndex = _OriRADIUSSvrTablePrimaryOrSecondaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1, 1, 2),
    _OriRADIUSSvrTablePrimaryOrSecondaryIndex_Type()
)
oriRADIUSSvrTablePrimaryOrSecondaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSSvrTablePrimaryOrSecondaryIndex.setStatus("current")
_OriRADIUSSvrTableProfileName_Type = DisplayString
_OriRADIUSSvrTableProfileName_Object = MibTableColumn
oriRADIUSSvrTableProfileName = _OriRADIUSSvrTableProfileName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1, 1, 3),
    _OriRADIUSSvrTableProfileName_Type()
)
oriRADIUSSvrTableProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriRADIUSSvrTableProfileName.setStatus("current")


class _OriRADIUSSvrTableAddressingFormat_Type(Integer32):
    """Custom type oriRADIUSSvrTableAddressingFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipAddress", 1),
          ("name", 2))
    )


_OriRADIUSSvrTableAddressingFormat_Type.__name__ = "Integer32"
_OriRADIUSSvrTableAddressingFormat_Object = MibTableColumn
oriRADIUSSvrTableAddressingFormat = _OriRADIUSSvrTableAddressingFormat_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1, 1, 4),
    _OriRADIUSSvrTableAddressingFormat_Type()
)
oriRADIUSSvrTableAddressingFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriRADIUSSvrTableAddressingFormat.setStatus("current")
_OriRADIUSSvrTableNameOrIPAddress_Type = DisplayString
_OriRADIUSSvrTableNameOrIPAddress_Object = MibTableColumn
oriRADIUSSvrTableNameOrIPAddress = _OriRADIUSSvrTableNameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1, 1, 5),
    _OriRADIUSSvrTableNameOrIPAddress_Type()
)
oriRADIUSSvrTableNameOrIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriRADIUSSvrTableNameOrIPAddress.setStatus("current")


class _OriRADIUSSvrTableDestPort_Type(Integer32):
    """Custom type oriRADIUSSvrTableDestPort based on Integer32"""
    defaultValue = 1812


_OriRADIUSSvrTableDestPort_Object = MibTableColumn
oriRADIUSSvrTableDestPort = _OriRADIUSSvrTableDestPort_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1, 1, 6),
    _OriRADIUSSvrTableDestPort_Type()
)
oriRADIUSSvrTableDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriRADIUSSvrTableDestPort.setStatus("current")
_OriRADIUSSvrTableSharedSecret_Type = DisplayString
_OriRADIUSSvrTableSharedSecret_Object = MibTableColumn
oriRADIUSSvrTableSharedSecret = _OriRADIUSSvrTableSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1, 1, 7),
    _OriRADIUSSvrTableSharedSecret_Type()
)
oriRADIUSSvrTableSharedSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriRADIUSSvrTableSharedSecret.setStatus("current")


class _OriRADIUSSvrTableResponseTime_Type(Integer32):
    """Custom type oriRADIUSSvrTableResponseTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_OriRADIUSSvrTableResponseTime_Type.__name__ = "Integer32"
_OriRADIUSSvrTableResponseTime_Object = MibTableColumn
oriRADIUSSvrTableResponseTime = _OriRADIUSSvrTableResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1, 1, 8),
    _OriRADIUSSvrTableResponseTime_Type()
)
oriRADIUSSvrTableResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriRADIUSSvrTableResponseTime.setStatus("current")


class _OriRADIUSSvrTableMaximumRetransmission_Type(Integer32):
    """Custom type oriRADIUSSvrTableMaximumRetransmission based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_OriRADIUSSvrTableMaximumRetransmission_Type.__name__ = "Integer32"
_OriRADIUSSvrTableMaximumRetransmission_Object = MibTableColumn
oriRADIUSSvrTableMaximumRetransmission = _OriRADIUSSvrTableMaximumRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1, 1, 9),
    _OriRADIUSSvrTableMaximumRetransmission_Type()
)
oriRADIUSSvrTableMaximumRetransmission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriRADIUSSvrTableMaximumRetransmission.setStatus("current")
_OriRADIUSSvrTableVLANID_Type = VlanId
_OriRADIUSSvrTableVLANID_Object = MibTableColumn
oriRADIUSSvrTableVLANID = _OriRADIUSSvrTableVLANID_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1, 1, 10),
    _OriRADIUSSvrTableVLANID_Type()
)
oriRADIUSSvrTableVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriRADIUSSvrTableVLANID.setStatus("current")


class _OriRADIUSSvrTableMACAddressFormat_Type(Integer32):
    """Custom type oriRADIUSSvrTableMACAddressFormat based on Integer32"""
    defaultValue = 1

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
        *(("colonDelimited", 2),
          ("dashDelimited", 1),
          ("noDelimiter", 4),
          ("singleDashDelimited", 3))
    )


_OriRADIUSSvrTableMACAddressFormat_Type.__name__ = "Integer32"
_OriRADIUSSvrTableMACAddressFormat_Object = MibTableColumn
oriRADIUSSvrTableMACAddressFormat = _OriRADIUSSvrTableMACAddressFormat_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1, 1, 11),
    _OriRADIUSSvrTableMACAddressFormat_Type()
)
oriRADIUSSvrTableMACAddressFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSSvrTableMACAddressFormat.setStatus("current")


class _OriRADIUSSvrTableAuthorizationLifeTime_Type(Integer32):
    """Custom type oriRADIUSSvrTableAuthorizationLifeTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(900, 43200),
    )


_OriRADIUSSvrTableAuthorizationLifeTime_Type.__name__ = "Integer32"
_OriRADIUSSvrTableAuthorizationLifeTime_Object = MibTableColumn
oriRADIUSSvrTableAuthorizationLifeTime = _OriRADIUSSvrTableAuthorizationLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1, 1, 12),
    _OriRADIUSSvrTableAuthorizationLifeTime_Type()
)
oriRADIUSSvrTableAuthorizationLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSSvrTableAuthorizationLifeTime.setStatus("current")


class _OriRADIUSSvrTableAccountingInactivityTimer_Type(Integer32):
    """Custom type oriRADIUSSvrTableAccountingInactivityTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_OriRADIUSSvrTableAccountingInactivityTimer_Type.__name__ = "Integer32"
_OriRADIUSSvrTableAccountingInactivityTimer_Object = MibTableColumn
oriRADIUSSvrTableAccountingInactivityTimer = _OriRADIUSSvrTableAccountingInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1, 1, 13),
    _OriRADIUSSvrTableAccountingInactivityTimer_Type()
)
oriRADIUSSvrTableAccountingInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSSvrTableAccountingInactivityTimer.setStatus("current")


class _OriRADIUSSvrTableAccountingUpdateInterval_Type(Integer32):
    """Custom type oriRADIUSSvrTableAccountingUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 10080),
    )


_OriRADIUSSvrTableAccountingUpdateInterval_Type.__name__ = "Integer32"
_OriRADIUSSvrTableAccountingUpdateInterval_Object = MibTableColumn
oriRADIUSSvrTableAccountingUpdateInterval = _OriRADIUSSvrTableAccountingUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1, 1, 14),
    _OriRADIUSSvrTableAccountingUpdateInterval_Type()
)
oriRADIUSSvrTableAccountingUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADIUSSvrTableAccountingUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    oriRADIUSSvrTableAccountingUpdateInterval.setUnits("minutes")
_OriRADIUSSvrTableRowStatus_Type = RowStatus
_OriRADIUSSvrTableRowStatus_Object = MibTableColumn
oriRADIUSSvrTableRowStatus = _OriRADIUSSvrTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 1, 1, 15),
    _OriRADIUSSvrTableRowStatus_Type()
)
oriRADIUSSvrTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriRADIUSSvrTableRowStatus.setStatus("current")
_OriRADIUSClientInvalidSvrAddress_Type = Counter32
_OriRADIUSClientInvalidSvrAddress_Object = MibScalar
oriRADIUSClientInvalidSvrAddress = _OriRADIUSClientInvalidSvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 2),
    _OriRADIUSClientInvalidSvrAddress_Type()
)
oriRADIUSClientInvalidSvrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSClientInvalidSvrAddress.setStatus("current")
_OriRADIUSAuthClientStatTable_Object = MibTable
oriRADIUSAuthClientStatTable = _OriRADIUSAuthClientStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 3)
)
if mibBuilder.loadTexts:
    oriRADIUSAuthClientStatTable.setStatus("current")
_OriRADIUSAuthClientStatTableEntry_Object = MibTableRow
oriRADIUSAuthClientStatTableEntry = _OriRADIUSAuthClientStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 3, 1)
)
oriRADIUSAuthClientStatTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriRADIUSAuthClientStatTableIndex"),
    (0, "ORiNOCO-MIB", "oriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex"),
)
if mibBuilder.loadTexts:
    oriRADIUSAuthClientStatTableEntry.setStatus("current")
_OriRADIUSAuthClientStatTableIndex_Type = Integer32
_OriRADIUSAuthClientStatTableIndex_Object = MibTableColumn
oriRADIUSAuthClientStatTableIndex = _OriRADIUSAuthClientStatTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 3, 1, 1),
    _OriRADIUSAuthClientStatTableIndex_Type()
)
oriRADIUSAuthClientStatTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientStatTableIndex.setStatus("current")


class _OriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex_Type(Integer32):
    """Custom type oriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_OriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex_Type.__name__ = "Integer32"
_OriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex_Object = MibTableColumn
oriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex = _OriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 3, 1, 2),
    _OriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex_Type()
)
oriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex.setStatus("current")
_OriRADIUSAuthClientStatTableAccessRequests_Type = Counter32
_OriRADIUSAuthClientStatTableAccessRequests_Object = MibTableColumn
oriRADIUSAuthClientStatTableAccessRequests = _OriRADIUSAuthClientStatTableAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 3, 1, 3),
    _OriRADIUSAuthClientStatTableAccessRequests_Type()
)
oriRADIUSAuthClientStatTableAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientStatTableAccessRequests.setStatus("current")
_OriRADIUSAuthClientStatTableAccessRetransmissions_Type = Counter32
_OriRADIUSAuthClientStatTableAccessRetransmissions_Object = MibTableColumn
oriRADIUSAuthClientStatTableAccessRetransmissions = _OriRADIUSAuthClientStatTableAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 3, 1, 4),
    _OriRADIUSAuthClientStatTableAccessRetransmissions_Type()
)
oriRADIUSAuthClientStatTableAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientStatTableAccessRetransmissions.setStatus("current")
_OriRADIUSAuthClientStatTableAccessAccepts_Type = Counter32
_OriRADIUSAuthClientStatTableAccessAccepts_Object = MibTableColumn
oriRADIUSAuthClientStatTableAccessAccepts = _OriRADIUSAuthClientStatTableAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 3, 1, 5),
    _OriRADIUSAuthClientStatTableAccessAccepts_Type()
)
oriRADIUSAuthClientStatTableAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientStatTableAccessAccepts.setStatus("current")
_OriRADIUSAuthClientStatTableAccessChallenges_Type = Counter32
_OriRADIUSAuthClientStatTableAccessChallenges_Object = MibTableColumn
oriRADIUSAuthClientStatTableAccessChallenges = _OriRADIUSAuthClientStatTableAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 3, 1, 6),
    _OriRADIUSAuthClientStatTableAccessChallenges_Type()
)
oriRADIUSAuthClientStatTableAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientStatTableAccessChallenges.setStatus("current")
_OriRADIUSAuthClientStatTableAccessRejects_Type = Counter32
_OriRADIUSAuthClientStatTableAccessRejects_Object = MibTableColumn
oriRADIUSAuthClientStatTableAccessRejects = _OriRADIUSAuthClientStatTableAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 3, 1, 7),
    _OriRADIUSAuthClientStatTableAccessRejects_Type()
)
oriRADIUSAuthClientStatTableAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientStatTableAccessRejects.setStatus("current")
_OriRADIUSAuthClientStatTableMalformedAccessResponses_Type = Counter32
_OriRADIUSAuthClientStatTableMalformedAccessResponses_Object = MibTableColumn
oriRADIUSAuthClientStatTableMalformedAccessResponses = _OriRADIUSAuthClientStatTableMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 3, 1, 8),
    _OriRADIUSAuthClientStatTableMalformedAccessResponses_Type()
)
oriRADIUSAuthClientStatTableMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientStatTableMalformedAccessResponses.setStatus("current")
_OriRADIUSAuthClientStatTableBadAuthenticators_Type = Counter32
_OriRADIUSAuthClientStatTableBadAuthenticators_Object = MibTableColumn
oriRADIUSAuthClientStatTableBadAuthenticators = _OriRADIUSAuthClientStatTableBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 3, 1, 9),
    _OriRADIUSAuthClientStatTableBadAuthenticators_Type()
)
oriRADIUSAuthClientStatTableBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientStatTableBadAuthenticators.setStatus("current")
_OriRADIUSAuthClientStatTableTimeouts_Type = Counter32
_OriRADIUSAuthClientStatTableTimeouts_Object = MibTableColumn
oriRADIUSAuthClientStatTableTimeouts = _OriRADIUSAuthClientStatTableTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 3, 1, 10),
    _OriRADIUSAuthClientStatTableTimeouts_Type()
)
oriRADIUSAuthClientStatTableTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAuthClientStatTableTimeouts.setStatus("current")
_OriRADIUSAcctClientStatTable_Object = MibTable
oriRADIUSAcctClientStatTable = _OriRADIUSAcctClientStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 4)
)
if mibBuilder.loadTexts:
    oriRADIUSAcctClientStatTable.setStatus("current")
_OriRADIUSAcctClientStatTableEntry_Object = MibTableRow
oriRADIUSAcctClientStatTableEntry = _OriRADIUSAcctClientStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 4, 1)
)
oriRADIUSAcctClientStatTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriRADIUSAcctClientStatTableIndex"),
    (0, "ORiNOCO-MIB", "oriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex"),
)
if mibBuilder.loadTexts:
    oriRADIUSAcctClientStatTableEntry.setStatus("current")
_OriRADIUSAcctClientStatTableIndex_Type = Integer32
_OriRADIUSAcctClientStatTableIndex_Object = MibTableColumn
oriRADIUSAcctClientStatTableIndex = _OriRADIUSAcctClientStatTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 4, 1, 1),
    _OriRADIUSAcctClientStatTableIndex_Type()
)
oriRADIUSAcctClientStatTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAcctClientStatTableIndex.setStatus("current")


class _OriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex_Type(Integer32):
    """Custom type oriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_OriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex_Type.__name__ = "Integer32"
_OriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex_Object = MibTableColumn
oriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex = _OriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 4, 1, 2),
    _OriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex_Type()
)
oriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex.setStatus("current")
_OriRADIUSAcctClientStatTableAccountingRequests_Type = Counter32
_OriRADIUSAcctClientStatTableAccountingRequests_Object = MibTableColumn
oriRADIUSAcctClientStatTableAccountingRequests = _OriRADIUSAcctClientStatTableAccountingRequests_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 4, 1, 3),
    _OriRADIUSAcctClientStatTableAccountingRequests_Type()
)
oriRADIUSAcctClientStatTableAccountingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAcctClientStatTableAccountingRequests.setStatus("current")
_OriRADIUSAcctClientStatTableAccountingRetransmissions_Type = Counter32
_OriRADIUSAcctClientStatTableAccountingRetransmissions_Object = MibTableColumn
oriRADIUSAcctClientStatTableAccountingRetransmissions = _OriRADIUSAcctClientStatTableAccountingRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 4, 1, 4),
    _OriRADIUSAcctClientStatTableAccountingRetransmissions_Type()
)
oriRADIUSAcctClientStatTableAccountingRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAcctClientStatTableAccountingRetransmissions.setStatus("current")
_OriRADIUSAcctClientStatTableAccountingResponses_Type = Counter32
_OriRADIUSAcctClientStatTableAccountingResponses_Object = MibTableColumn
oriRADIUSAcctClientStatTableAccountingResponses = _OriRADIUSAcctClientStatTableAccountingResponses_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 4, 1, 5),
    _OriRADIUSAcctClientStatTableAccountingResponses_Type()
)
oriRADIUSAcctClientStatTableAccountingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAcctClientStatTableAccountingResponses.setStatus("current")
_OriRADIUSAcctClientStatTableBadAuthenticators_Type = Counter32
_OriRADIUSAcctClientStatTableBadAuthenticators_Object = MibTableColumn
oriRADIUSAcctClientStatTableBadAuthenticators = _OriRADIUSAcctClientStatTableBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 6, 10, 4, 1, 6),
    _OriRADIUSAcctClientStatTableBadAuthenticators_Type()
)
oriRADIUSAcctClientStatTableBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADIUSAcctClientStatTableBadAuthenticators.setStatus("current")
_OrinocoTelnet_ObjectIdentity = ObjectIdentity
orinocoTelnet = _OrinocoTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 7)
)


class _OriTelnetSessions_Type(Integer32):
    """Custom type oriTelnetSessions based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_OriTelnetSessions_Type.__name__ = "Integer32"
_OriTelnetSessions_Object = MibScalar
oriTelnetSessions = _OriTelnetSessions_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 7, 1),
    _OriTelnetSessions_Type()
)
oriTelnetSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTelnetSessions.setStatus("deprecated")


class _OriTelnetPassword_Type(DisplayString):
    """Custom type oriTelnetPassword based on DisplayString"""
    defaultValue = OctetString("public")


_OriTelnetPassword_Object = MibScalar
oriTelnetPassword = _OriTelnetPassword_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 7, 2),
    _OriTelnetPassword_Type()
)
oriTelnetPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTelnetPassword.setStatus("current")


class _OriTelnetPort_Type(Integer32):
    """Custom type oriTelnetPort based on Integer32"""
    defaultValue = 23


_OriTelnetPort_Object = MibScalar
oriTelnetPort = _OriTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 7, 3),
    _OriTelnetPort_Type()
)
oriTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTelnetPort.setStatus("current")


class _OriTelnetLoginTimeout_Type(Integer32):
    """Custom type oriTelnetLoginTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_OriTelnetLoginTimeout_Type.__name__ = "Integer32"
_OriTelnetLoginTimeout_Object = MibScalar
oriTelnetLoginTimeout = _OriTelnetLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 7, 4),
    _OriTelnetLoginTimeout_Type()
)
oriTelnetLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTelnetLoginTimeout.setStatus("current")


class _OriTelnetIdleTimeout_Type(Integer32):
    """Custom type oriTelnetIdleTimeout based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 36000),
    )


_OriTelnetIdleTimeout_Type.__name__ = "Integer32"
_OriTelnetIdleTimeout_Object = MibScalar
oriTelnetIdleTimeout = _OriTelnetIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 7, 5),
    _OriTelnetIdleTimeout_Type()
)
oriTelnetIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTelnetIdleTimeout.setStatus("current")
_OriTelnetInterfaceBitmask_Type = InterfaceBitmask
_OriTelnetInterfaceBitmask_Object = MibScalar
oriTelnetInterfaceBitmask = _OriTelnetInterfaceBitmask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 7, 6),
    _OriTelnetInterfaceBitmask_Type()
)
oriTelnetInterfaceBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTelnetInterfaceBitmask.setStatus("current")


class _OriTelnetSSHStatus_Type(ObjStatus):
    """Custom type oriTelnetSSHStatus based on ObjStatus"""


_OriTelnetSSHStatus_Object = MibScalar
oriTelnetSSHStatus = _OriTelnetSSHStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 7, 7),
    _OriTelnetSSHStatus_Type()
)
oriTelnetSSHStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTelnetSSHStatus.setStatus("current")


class _OriTelnetSSHHostKeyStatus_Type(Integer32):
    """Custom type oriTelnetSSHHostKeyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_OriTelnetSSHHostKeyStatus_Type.__name__ = "Integer32"
_OriTelnetSSHHostKeyStatus_Object = MibScalar
oriTelnetSSHHostKeyStatus = _OriTelnetSSHHostKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 7, 8),
    _OriTelnetSSHHostKeyStatus_Type()
)
oriTelnetSSHHostKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTelnetSSHHostKeyStatus.setStatus("current")
_OriTelnetSSHFingerPrint_Type = DisplayString
_OriTelnetSSHFingerPrint_Object = MibScalar
oriTelnetSSHFingerPrint = _OriTelnetSSHFingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 7, 9),
    _OriTelnetSSHFingerPrint_Type()
)
oriTelnetSSHFingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTelnetSSHFingerPrint.setStatus("current")


class _OriTelnetRADIUSAccessControl_Type(ObjStatus):
    """Custom type oriTelnetRADIUSAccessControl based on ObjStatus"""


_OriTelnetRADIUSAccessControl_Object = MibScalar
oriTelnetRADIUSAccessControl = _OriTelnetRADIUSAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 7, 10),
    _OriTelnetRADIUSAccessControl_Type()
)
oriTelnetRADIUSAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTelnetRADIUSAccessControl.setStatus("current")
_OrinocoTFTP_ObjectIdentity = ObjectIdentity
orinocoTFTP = _OrinocoTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 8)
)


class _OriTFTPServerIPAddress_Type(IpAddress):
    """Custom type oriTFTPServerIPAddress based on IpAddress"""
    defaultHexValue = "0a000002"


_OriTFTPServerIPAddress_Object = MibScalar
oriTFTPServerIPAddress = _OriTFTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 8, 1),
    _OriTFTPServerIPAddress_Type()
)
oriTFTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTFTPServerIPAddress.setStatus("current")


class _OriTFTPFileName_Type(DisplayString):
    """Custom type oriTFTPFileName based on DisplayString"""
    defaultValue = OctetString("Filename")


_OriTFTPFileName_Object = MibScalar
oriTFTPFileName = _OriTFTPFileName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 8, 2),
    _OriTFTPFileName_Type()
)
oriTFTPFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTFTPFileName.setStatus("current")


class _OriTFTPFileType_Type(Integer32):
    """Custom type oriTFTPFileType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("bootloader", 3),
          ("certificate", 5),
          ("cliBatchFile", 9),
          ("cliBatchLog", 10),
          ("config", 1),
          ("eventlog", 12),
          ("image", 2),
          ("license", 4),
          ("privatekey", 6),
          ("sshHostPrivateKey", 8),
          ("sshHostPublicKey", 7),
          ("templog", 11))
    )


_OriTFTPFileType_Type.__name__ = "Integer32"
_OriTFTPFileType_Object = MibScalar
oriTFTPFileType = _OriTFTPFileType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 8, 3),
    _OriTFTPFileType_Type()
)
oriTFTPFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTFTPFileType.setStatus("current")


class _OriTFTPOperation_Type(Integer32):
    """Custom type oriTFTPOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("download", 2),
          ("downloadAndReboot", 3),
          ("upload", 1))
    )


_OriTFTPOperation_Type.__name__ = "Integer32"
_OriTFTPOperation_Object = MibScalar
oriTFTPOperation = _OriTFTPOperation_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 8, 4),
    _OriTFTPOperation_Type()
)
oriTFTPOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTFTPOperation.setStatus("current")


class _OriTFTPFileMode_Type(Integer32):
    """Custom type oriTFTPFileMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("bin", 2))
    )


_OriTFTPFileMode_Type.__name__ = "Integer32"
_OriTFTPFileMode_Object = MibScalar
oriTFTPFileMode = _OriTFTPFileMode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 8, 5),
    _OriTFTPFileMode_Type()
)
oriTFTPFileMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTFTPFileMode.setStatus("current")


class _OriTFTPOperationStatus_Type(Integer32):
    """Custom type oriTFTPOperationStatus based on Integer32"""
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
        *(("failure", 4),
          ("idle", 1),
          ("inProgress", 2),
          ("successful", 3))
    )


_OriTFTPOperationStatus_Type.__name__ = "Integer32"
_OriTFTPOperationStatus_Object = MibScalar
oriTFTPOperationStatus = _OriTFTPOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 8, 6),
    _OriTFTPOperationStatus_Type()
)
oriTFTPOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTFTPOperationStatus.setStatus("current")
_OriTFTPAutoConfigStatus_Type = ObjStatus
_OriTFTPAutoConfigStatus_Object = MibScalar
oriTFTPAutoConfigStatus = _OriTFTPAutoConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 8, 7),
    _OriTFTPAutoConfigStatus_Type()
)
oriTFTPAutoConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTFTPAutoConfigStatus.setStatus("current")
_OriTFTPAutoConfigFilename_Type = DisplayString
_OriTFTPAutoConfigFilename_Object = MibScalar
oriTFTPAutoConfigFilename = _OriTFTPAutoConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 8, 8),
    _OriTFTPAutoConfigFilename_Type()
)
oriTFTPAutoConfigFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTFTPAutoConfigFilename.setStatus("current")
_OriTFTPAutoConfigServerIPAddress_Type = IpAddress
_OriTFTPAutoConfigServerIPAddress_Object = MibScalar
oriTFTPAutoConfigServerIPAddress = _OriTFTPAutoConfigServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 8, 9),
    _OriTFTPAutoConfigServerIPAddress_Type()
)
oriTFTPAutoConfigServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTFTPAutoConfigServerIPAddress.setStatus("current")


class _OriTFTPDowngrade_Type(Integer32):
    """Custom type oriTFTPDowngrade based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rel201", 2))
    )


_OriTFTPDowngrade_Type.__name__ = "Integer32"
_OriTFTPDowngrade_Object = MibScalar
oriTFTPDowngrade = _OriTFTPDowngrade_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 8, 10),
    _OriTFTPDowngrade_Type()
)
oriTFTPDowngrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTFTPDowngrade.setStatus("current")
_OrinocoSerial_ObjectIdentity = ObjectIdentity
orinocoSerial = _OrinocoSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 9)
)


class _OriSerialBaudRate_Type(Integer32):
    """Custom type oriSerialBaudRate based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("baud19200", 4),
          ("baud2400", 1),
          ("baud38400", 5),
          ("baud4800", 2),
          ("baud57600", 6),
          ("baud9600", 3))
    )


_OriSerialBaudRate_Type.__name__ = "Integer32"
_OriSerialBaudRate_Object = MibScalar
oriSerialBaudRate = _OriSerialBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 9, 1),
    _OriSerialBaudRate_Type()
)
oriSerialBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSerialBaudRate.setStatus("current")


class _OriSerialDataBits_Type(Integer32):
    """Custom type oriSerialDataBits based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_OriSerialDataBits_Type.__name__ = "Integer32"
_OriSerialDataBits_Object = MibScalar
oriSerialDataBits = _OriSerialDataBits_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 9, 2),
    _OriSerialDataBits_Type()
)
oriSerialDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSerialDataBits.setStatus("current")


class _OriSerialParity_Type(Integer32):
    """Custom type oriSerialParity based on Integer32"""
    defaultValue = 3

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
        *(("even", 1),
          ("mark", 4),
          ("none", 3),
          ("odd", 2),
          ("space", 5))
    )


_OriSerialParity_Type.__name__ = "Integer32"
_OriSerialParity_Object = MibScalar
oriSerialParity = _OriSerialParity_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 9, 3),
    _OriSerialParity_Type()
)
oriSerialParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSerialParity.setStatus("current")


class _OriSerialStopBits_Type(Integer32):
    """Custom type oriSerialStopBits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bit1", 1),
          ("bit1dot5", 2),
          ("bit2", 3))
    )


_OriSerialStopBits_Type.__name__ = "Integer32"
_OriSerialStopBits_Object = MibScalar
oriSerialStopBits = _OriSerialStopBits_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 9, 4),
    _OriSerialStopBits_Type()
)
oriSerialStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSerialStopBits.setStatus("current")


class _OriSerialFlowControl_Type(Integer32):
    """Custom type oriSerialFlowControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("xonxoff", 1))
    )


_OriSerialFlowControl_Type.__name__ = "Integer32"
_OriSerialFlowControl_Object = MibScalar
oriSerialFlowControl = _OriSerialFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 9, 5),
    _OriSerialFlowControl_Type()
)
oriSerialFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSerialFlowControl.setStatus("current")
_OrinocoIAPP_ObjectIdentity = ObjectIdentity
orinocoIAPP = _OrinocoIAPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10)
)


class _OriIAPPStatus_Type(Integer32):
    """Custom type oriIAPPStatus based on Integer32"""
    defaultValue = 1

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


_OriIAPPStatus_Type.__name__ = "Integer32"
_OriIAPPStatus_Object = MibScalar
oriIAPPStatus = _OriIAPPStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 1),
    _OriIAPPStatus_Type()
)
oriIAPPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIAPPStatus.setStatus("current")


class _OriIAPPPeriodicAnnounceInterval_Type(Integer32):
    """Custom type oriIAPPPeriodicAnnounceInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(80,
              120,
              160,
              200)
        )
    )
    namedValues = NamedValues(
        *(("eighty", 80),
          ("oneHundredSixty", 160),
          ("oneHundredTwenty", 120),
          ("twoHundred", 200))
    )


_OriIAPPPeriodicAnnounceInterval_Type.__name__ = "Integer32"
_OriIAPPPeriodicAnnounceInterval_Object = MibScalar
oriIAPPPeriodicAnnounceInterval = _OriIAPPPeriodicAnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 2),
    _OriIAPPPeriodicAnnounceInterval_Type()
)
oriIAPPPeriodicAnnounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIAPPPeriodicAnnounceInterval.setStatus("current")
_OriIAPPAnnounceResponseTime_Type = Integer32
_OriIAPPAnnounceResponseTime_Object = MibScalar
oriIAPPAnnounceResponseTime = _OriIAPPAnnounceResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 3),
    _OriIAPPAnnounceResponseTime_Type()
)
oriIAPPAnnounceResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPAnnounceResponseTime.setStatus("current")


class _OriIAPPHandoverTimeout_Type(Integer32):
    """Custom type oriIAPPHandoverTimeout based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(410,
              512,
              614,
              717,
              819)
        )
    )
    namedValues = NamedValues(
        *(("eightHundredNineteen", 819),
          ("fiveHundredTwelve", 512),
          ("fourHundredTen", 410),
          ("sevenHundredSeventeen", 717),
          ("sixHundredFourteen", 614))
    )


_OriIAPPHandoverTimeout_Type.__name__ = "Integer32"
_OriIAPPHandoverTimeout_Object = MibScalar
oriIAPPHandoverTimeout = _OriIAPPHandoverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 4),
    _OriIAPPHandoverTimeout_Type()
)
oriIAPPHandoverTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIAPPHandoverTimeout.setStatus("current")


class _OriIAPPMaximumHandoverRetransmissions_Type(Integer32):
    """Custom type oriIAPPMaximumHandoverRetransmissions based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_OriIAPPMaximumHandoverRetransmissions_Type.__name__ = "Integer32"
_OriIAPPMaximumHandoverRetransmissions_Object = MibScalar
oriIAPPMaximumHandoverRetransmissions = _OriIAPPMaximumHandoverRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 5),
    _OriIAPPMaximumHandoverRetransmissions_Type()
)
oriIAPPMaximumHandoverRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIAPPMaximumHandoverRetransmissions.setStatus("current")
_OriIAPPAnnounceRequestSent_Type = Counter32
_OriIAPPAnnounceRequestSent_Object = MibScalar
oriIAPPAnnounceRequestSent = _OriIAPPAnnounceRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 6),
    _OriIAPPAnnounceRequestSent_Type()
)
oriIAPPAnnounceRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPAnnounceRequestSent.setStatus("current")
_OriIAPPAnnounceRequestReceived_Type = Counter32
_OriIAPPAnnounceRequestReceived_Object = MibScalar
oriIAPPAnnounceRequestReceived = _OriIAPPAnnounceRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 7),
    _OriIAPPAnnounceRequestReceived_Type()
)
oriIAPPAnnounceRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPAnnounceRequestReceived.setStatus("current")
_OriIAPPAnnounceResponseSent_Type = Counter32
_OriIAPPAnnounceResponseSent_Object = MibScalar
oriIAPPAnnounceResponseSent = _OriIAPPAnnounceResponseSent_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 8),
    _OriIAPPAnnounceResponseSent_Type()
)
oriIAPPAnnounceResponseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPAnnounceResponseSent.setStatus("current")
_OriIAPPAnnounceResponseReceived_Type = Counter32
_OriIAPPAnnounceResponseReceived_Object = MibScalar
oriIAPPAnnounceResponseReceived = _OriIAPPAnnounceResponseReceived_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 9),
    _OriIAPPAnnounceResponseReceived_Type()
)
oriIAPPAnnounceResponseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPAnnounceResponseReceived.setStatus("current")
_OriIAPPHandoverRequestSent_Type = Counter32
_OriIAPPHandoverRequestSent_Object = MibScalar
oriIAPPHandoverRequestSent = _OriIAPPHandoverRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 10),
    _OriIAPPHandoverRequestSent_Type()
)
oriIAPPHandoverRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPHandoverRequestSent.setStatus("current")
_OriIAPPHandoverRequestReceived_Type = Counter32
_OriIAPPHandoverRequestReceived_Object = MibScalar
oriIAPPHandoverRequestReceived = _OriIAPPHandoverRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 11),
    _OriIAPPHandoverRequestReceived_Type()
)
oriIAPPHandoverRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPHandoverRequestReceived.setStatus("current")
_OriIAPPHandoverRequestRetransmissions_Type = Counter32
_OriIAPPHandoverRequestRetransmissions_Object = MibScalar
oriIAPPHandoverRequestRetransmissions = _OriIAPPHandoverRequestRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 12),
    _OriIAPPHandoverRequestRetransmissions_Type()
)
oriIAPPHandoverRequestRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPHandoverRequestRetransmissions.setStatus("current")
_OriIAPPHandoverResponseSent_Type = Counter32
_OriIAPPHandoverResponseSent_Object = MibScalar
oriIAPPHandoverResponseSent = _OriIAPPHandoverResponseSent_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 13),
    _OriIAPPHandoverResponseSent_Type()
)
oriIAPPHandoverResponseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPHandoverResponseSent.setStatus("current")
_OriIAPPHandoverResponseReceived_Type = Counter32
_OriIAPPHandoverResponseReceived_Object = MibScalar
oriIAPPHandoverResponseReceived = _OriIAPPHandoverResponseReceived_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 14),
    _OriIAPPHandoverResponseReceived_Type()
)
oriIAPPHandoverResponseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPHandoverResponseReceived.setStatus("current")
_OriIAPPPDUsDropped_Type = Counter32
_OriIAPPPDUsDropped_Object = MibScalar
oriIAPPPDUsDropped = _OriIAPPPDUsDropped_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 15),
    _OriIAPPPDUsDropped_Type()
)
oriIAPPPDUsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPPDUsDropped.setStatus("current")
_OriIAPPRoamingClients_Type = Counter32
_OriIAPPRoamingClients_Object = MibScalar
oriIAPPRoamingClients = _OriIAPPRoamingClients_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 16),
    _OriIAPPRoamingClients_Type()
)
oriIAPPRoamingClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPRoamingClients.setStatus("current")
_OriIAPPMACIPTable_Object = MibTable
oriIAPPMACIPTable = _OriIAPPMACIPTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 21)
)
if mibBuilder.loadTexts:
    oriIAPPMACIPTable.setStatus("current")
_OriIAPPMACIPTableEntry_Object = MibTableRow
oriIAPPMACIPTableEntry = _OriIAPPMACIPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 21, 1)
)
oriIAPPMACIPTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriIAPPMACIPTableIndex"),
)
if mibBuilder.loadTexts:
    oriIAPPMACIPTableEntry.setStatus("current")
_OriIAPPMACIPTableIndex_Type = Integer32
_OriIAPPMACIPTableIndex_Object = MibTableColumn
oriIAPPMACIPTableIndex = _OriIAPPMACIPTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 21, 1, 1),
    _OriIAPPMACIPTableIndex_Type()
)
oriIAPPMACIPTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPMACIPTableIndex.setStatus("current")
_OriIAPPMACIPTableSystemName_Type = DisplayString
_OriIAPPMACIPTableSystemName_Object = MibTableColumn
oriIAPPMACIPTableSystemName = _OriIAPPMACIPTableSystemName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 21, 1, 2),
    _OriIAPPMACIPTableSystemName_Type()
)
oriIAPPMACIPTableSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPMACIPTableSystemName.setStatus("current")
_OriIAPPMACIPTableIPAddress_Type = IpAddress
_OriIAPPMACIPTableIPAddress_Object = MibTableColumn
oriIAPPMACIPTableIPAddress = _OriIAPPMACIPTableIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 21, 1, 3),
    _OriIAPPMACIPTableIPAddress_Type()
)
oriIAPPMACIPTableIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPMACIPTableIPAddress.setStatus("current")
_OriIAPPMACIPTableBSSID_Type = PhysAddress
_OriIAPPMACIPTableBSSID_Object = MibTableColumn
oriIAPPMACIPTableBSSID = _OriIAPPMACIPTableBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 21, 1, 4),
    _OriIAPPMACIPTableBSSID_Type()
)
oriIAPPMACIPTableBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPMACIPTableBSSID.setStatus("current")
_OriIAPPMACIPTableESSID_Type = DisplayString
_OriIAPPMACIPTableESSID_Object = MibTableColumn
oriIAPPMACIPTableESSID = _OriIAPPMACIPTableESSID_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 21, 1, 5),
    _OriIAPPMACIPTableESSID_Type()
)
oriIAPPMACIPTableESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriIAPPMACIPTableESSID.setStatus("current")


class _OriIAPPSendAnnounceRequestOnStart_Type(Integer32):
    """Custom type oriIAPPSendAnnounceRequestOnStart based on Integer32"""
    defaultValue = 1

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


_OriIAPPSendAnnounceRequestOnStart_Type.__name__ = "Integer32"
_OriIAPPSendAnnounceRequestOnStart_Object = MibScalar
oriIAPPSendAnnounceRequestOnStart = _OriIAPPSendAnnounceRequestOnStart_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 10, 22),
    _OriIAPPSendAnnounceRequestOnStart_Type()
)
oriIAPPSendAnnounceRequestOnStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIAPPSendAnnounceRequestOnStart.setStatus("current")
_OrinocoLinkTest_ObjectIdentity = ObjectIdentity
orinocoLinkTest = _OrinocoLinkTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11)
)


class _OriLinkTestTimeOut_Type(Integer32):
    """Custom type oriLinkTestTimeOut based on Integer32"""
    defaultValue = 300


_OriLinkTestTimeOut_Object = MibScalar
oriLinkTestTimeOut = _OriLinkTestTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 1),
    _OriLinkTestTimeOut_Type()
)
oriLinkTestTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriLinkTestTimeOut.setStatus("current")


class _OriLinkTestInterval_Type(Integer32):
    """Custom type oriLinkTestInterval based on Integer32"""
    defaultValue = 200


_OriLinkTestInterval_Object = MibScalar
oriLinkTestInterval = _OriLinkTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 3),
    _OriLinkTestInterval_Type()
)
oriLinkTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriLinkTestInterval.setStatus("current")


class _OriLinkTestExplore_Type(Integer32):
    """Custom type oriLinkTestExplore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exploreResultsAvailable", 3),
          ("exploring", 2),
          ("tableTimedOut", 1))
    )


_OriLinkTestExplore_Type.__name__ = "Integer32"
_OriLinkTestExplore_Object = MibScalar
oriLinkTestExplore = _OriLinkTestExplore_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 4),
    _OriLinkTestExplore_Type()
)
oriLinkTestExplore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriLinkTestExplore.setStatus("current")
_OriLinkTestTable_Object = MibTable
oriLinkTestTable = _OriLinkTestTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5)
)
if mibBuilder.loadTexts:
    oriLinkTestTable.setStatus("current")
_OriLinkTestTableEntry_Object = MibTableRow
oriLinkTestTableEntry = _OriLinkTestTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1)
)
oriLinkTestTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriLinkTestTableIndex"),
)
if mibBuilder.loadTexts:
    oriLinkTestTableEntry.setStatus("current")


class _OriLinkTestTableIndex_Type(Integer32):
    """Custom type oriLinkTestTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_OriLinkTestTableIndex_Type.__name__ = "Integer32"
_OriLinkTestTableIndex_Object = MibTableColumn
oriLinkTestTableIndex = _OriLinkTestTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 1),
    _OriLinkTestTableIndex_Type()
)
oriLinkTestTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestTableIndex.setStatus("current")


class _OriLinkTestInProgress_Type(Integer32):
    """Custom type oriLinkTestInProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkTestIinProgress", 2),
          ("noLinkTestInProgress", 1))
    )


_OriLinkTestInProgress_Type.__name__ = "Integer32"
_OriLinkTestInProgress_Object = MibTableColumn
oriLinkTestInProgress = _OriLinkTestInProgress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 2),
    _OriLinkTestInProgress_Type()
)
oriLinkTestInProgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriLinkTestInProgress.setStatus("current")
_OriLinkTestStationName_Type = DisplayString
_OriLinkTestStationName_Object = MibTableColumn
oriLinkTestStationName = _OriLinkTestStationName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 3),
    _OriLinkTestStationName_Type()
)
oriLinkTestStationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestStationName.setStatus("current")
_OriLinkTestMACAddress_Type = PhysAddress
_OriLinkTestMACAddress_Object = MibTableColumn
oriLinkTestMACAddress = _OriLinkTestMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 4),
    _OriLinkTestMACAddress_Type()
)
oriLinkTestMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestMACAddress.setStatus("current")
_OriLinkTestStationProfile_Type = Integer32
_OriLinkTestStationProfile_Object = MibTableColumn
oriLinkTestStationProfile = _OriLinkTestStationProfile_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 5),
    _OriLinkTestStationProfile_Type()
)
oriLinkTestStationProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestStationProfile.setStatus("current")
_OriLinkTestOurCurSignalLevel_Type = Integer32
_OriLinkTestOurCurSignalLevel_Object = MibTableColumn
oriLinkTestOurCurSignalLevel = _OriLinkTestOurCurSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 6),
    _OriLinkTestOurCurSignalLevel_Type()
)
oriLinkTestOurCurSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurCurSignalLevel.setStatus("current")
_OriLinkTestOurCurNoiseLevel_Type = Integer32
_OriLinkTestOurCurNoiseLevel_Object = MibTableColumn
oriLinkTestOurCurNoiseLevel = _OriLinkTestOurCurNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 7),
    _OriLinkTestOurCurNoiseLevel_Type()
)
oriLinkTestOurCurNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurCurNoiseLevel.setStatus("current")
_OriLinkTestOurCurSNR_Type = Integer32
_OriLinkTestOurCurSNR_Object = MibTableColumn
oriLinkTestOurCurSNR = _OriLinkTestOurCurSNR_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 8),
    _OriLinkTestOurCurSNR_Type()
)
oriLinkTestOurCurSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurCurSNR.setStatus("current")
_OriLinkTestOurMinSignalLevel_Type = Integer32
_OriLinkTestOurMinSignalLevel_Object = MibTableColumn
oriLinkTestOurMinSignalLevel = _OriLinkTestOurMinSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 9),
    _OriLinkTestOurMinSignalLevel_Type()
)
oriLinkTestOurMinSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurMinSignalLevel.setStatus("current")
_OriLinkTestOurMinNoiseLevel_Type = Integer32
_OriLinkTestOurMinNoiseLevel_Object = MibTableColumn
oriLinkTestOurMinNoiseLevel = _OriLinkTestOurMinNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 10),
    _OriLinkTestOurMinNoiseLevel_Type()
)
oriLinkTestOurMinNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurMinNoiseLevel.setStatus("current")
_OriLinkTestOurMinSNR_Type = Integer32
_OriLinkTestOurMinSNR_Object = MibTableColumn
oriLinkTestOurMinSNR = _OriLinkTestOurMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 11),
    _OriLinkTestOurMinSNR_Type()
)
oriLinkTestOurMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurMinSNR.setStatus("current")
_OriLinkTestOurMaxSignalLevel_Type = Integer32
_OriLinkTestOurMaxSignalLevel_Object = MibTableColumn
oriLinkTestOurMaxSignalLevel = _OriLinkTestOurMaxSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 12),
    _OriLinkTestOurMaxSignalLevel_Type()
)
oriLinkTestOurMaxSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurMaxSignalLevel.setStatus("current")
_OriLinkTestOurMaxNoiseLevel_Type = Integer32
_OriLinkTestOurMaxNoiseLevel_Object = MibTableColumn
oriLinkTestOurMaxNoiseLevel = _OriLinkTestOurMaxNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 13),
    _OriLinkTestOurMaxNoiseLevel_Type()
)
oriLinkTestOurMaxNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurMaxNoiseLevel.setStatus("current")
_OriLinkTestOurMaxSNR_Type = Integer32
_OriLinkTestOurMaxSNR_Object = MibTableColumn
oriLinkTestOurMaxSNR = _OriLinkTestOurMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 14),
    _OriLinkTestOurMaxSNR_Type()
)
oriLinkTestOurMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurMaxSNR.setStatus("current")
_OriLinkTestOurLowFrameCount_Type = Integer32
_OriLinkTestOurLowFrameCount_Object = MibTableColumn
oriLinkTestOurLowFrameCount = _OriLinkTestOurLowFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 15),
    _OriLinkTestOurLowFrameCount_Type()
)
oriLinkTestOurLowFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurLowFrameCount.setStatus("current")
_OriLinkTestOurStandardFrameCount_Type = Integer32
_OriLinkTestOurStandardFrameCount_Object = MibTableColumn
oriLinkTestOurStandardFrameCount = _OriLinkTestOurStandardFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 16),
    _OriLinkTestOurStandardFrameCount_Type()
)
oriLinkTestOurStandardFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurStandardFrameCount.setStatus("current")
_OriLinkTestOurMediumFrameCount_Type = Integer32
_OriLinkTestOurMediumFrameCount_Object = MibTableColumn
oriLinkTestOurMediumFrameCount = _OriLinkTestOurMediumFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 17),
    _OriLinkTestOurMediumFrameCount_Type()
)
oriLinkTestOurMediumFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurMediumFrameCount.setStatus("current")
_OriLinkTestOurHighFrameCount_Type = Integer32
_OriLinkTestOurHighFrameCount_Object = MibTableColumn
oriLinkTestOurHighFrameCount = _OriLinkTestOurHighFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 18),
    _OriLinkTestOurHighFrameCount_Type()
)
oriLinkTestOurHighFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurHighFrameCount.setStatus("current")
_OriLinkTestHisCurSignalLevel_Type = Integer32
_OriLinkTestHisCurSignalLevel_Object = MibTableColumn
oriLinkTestHisCurSignalLevel = _OriLinkTestHisCurSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 19),
    _OriLinkTestHisCurSignalLevel_Type()
)
oriLinkTestHisCurSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisCurSignalLevel.setStatus("current")
_OriLinkTestHisCurNoiseLevel_Type = Integer32
_OriLinkTestHisCurNoiseLevel_Object = MibTableColumn
oriLinkTestHisCurNoiseLevel = _OriLinkTestHisCurNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 20),
    _OriLinkTestHisCurNoiseLevel_Type()
)
oriLinkTestHisCurNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisCurNoiseLevel.setStatus("current")
_OriLinkTestHisCurSNR_Type = Integer32
_OriLinkTestHisCurSNR_Object = MibTableColumn
oriLinkTestHisCurSNR = _OriLinkTestHisCurSNR_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 21),
    _OriLinkTestHisCurSNR_Type()
)
oriLinkTestHisCurSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisCurSNR.setStatus("current")
_OriLinkTestHisMinSignalLevel_Type = Integer32
_OriLinkTestHisMinSignalLevel_Object = MibTableColumn
oriLinkTestHisMinSignalLevel = _OriLinkTestHisMinSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 22),
    _OriLinkTestHisMinSignalLevel_Type()
)
oriLinkTestHisMinSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisMinSignalLevel.setStatus("current")
_OriLinkTestHisMinNoiseLevel_Type = Integer32
_OriLinkTestHisMinNoiseLevel_Object = MibTableColumn
oriLinkTestHisMinNoiseLevel = _OriLinkTestHisMinNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 23),
    _OriLinkTestHisMinNoiseLevel_Type()
)
oriLinkTestHisMinNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisMinNoiseLevel.setStatus("current")
_OriLinkTestHisMinSNR_Type = Integer32
_OriLinkTestHisMinSNR_Object = MibTableColumn
oriLinkTestHisMinSNR = _OriLinkTestHisMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 24),
    _OriLinkTestHisMinSNR_Type()
)
oriLinkTestHisMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisMinSNR.setStatus("current")
_OriLinkTestHisMaxSignalLevel_Type = Integer32
_OriLinkTestHisMaxSignalLevel_Object = MibTableColumn
oriLinkTestHisMaxSignalLevel = _OriLinkTestHisMaxSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 25),
    _OriLinkTestHisMaxSignalLevel_Type()
)
oriLinkTestHisMaxSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisMaxSignalLevel.setStatus("current")
_OriLinkTestHisMaxNoiseLevel_Type = Integer32
_OriLinkTestHisMaxNoiseLevel_Object = MibTableColumn
oriLinkTestHisMaxNoiseLevel = _OriLinkTestHisMaxNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 26),
    _OriLinkTestHisMaxNoiseLevel_Type()
)
oriLinkTestHisMaxNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisMaxNoiseLevel.setStatus("current")
_OriLinkTestHisMaxSNR_Type = Integer32
_OriLinkTestHisMaxSNR_Object = MibTableColumn
oriLinkTestHisMaxSNR = _OriLinkTestHisMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 27),
    _OriLinkTestHisMaxSNR_Type()
)
oriLinkTestHisMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisMaxSNR.setStatus("current")
_OriLinkTestHisLowFrameCount_Type = Integer32
_OriLinkTestHisLowFrameCount_Object = MibTableColumn
oriLinkTestHisLowFrameCount = _OriLinkTestHisLowFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 28),
    _OriLinkTestHisLowFrameCount_Type()
)
oriLinkTestHisLowFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisLowFrameCount.setStatus("current")
_OriLinkTestHisStandardFrameCount_Type = Integer32
_OriLinkTestHisStandardFrameCount_Object = MibTableColumn
oriLinkTestHisStandardFrameCount = _OriLinkTestHisStandardFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 29),
    _OriLinkTestHisStandardFrameCount_Type()
)
oriLinkTestHisStandardFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisStandardFrameCount.setStatus("current")
_OriLinkTestHisMediumFrameCount_Type = Integer32
_OriLinkTestHisMediumFrameCount_Object = MibTableColumn
oriLinkTestHisMediumFrameCount = _OriLinkTestHisMediumFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 30),
    _OriLinkTestHisMediumFrameCount_Type()
)
oriLinkTestHisMediumFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisMediumFrameCount.setStatus("current")
_OriLinkTestHisHighFrameCount_Type = Integer32
_OriLinkTestHisHighFrameCount_Object = MibTableColumn
oriLinkTestHisHighFrameCount = _OriLinkTestHisHighFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 31),
    _OriLinkTestHisHighFrameCount_Type()
)
oriLinkTestHisHighFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisHighFrameCount.setStatus("current")
_OriLinkTestInterface_Type = DisplayString
_OriLinkTestInterface_Object = MibTableColumn
oriLinkTestInterface = _OriLinkTestInterface_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 32),
    _OriLinkTestInterface_Type()
)
oriLinkTestInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestInterface.setStatus("current")
_OriLinkTestRadioType_Type = DisplayString
_OriLinkTestRadioType_Object = MibTableColumn
oriLinkTestRadioType = _OriLinkTestRadioType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 5, 1, 33),
    _OriLinkTestRadioType_Type()
)
oriLinkTestRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestRadioType.setStatus("current")
_OriLinkTestDataRateTable_Object = MibTable
oriLinkTestDataRateTable = _OriLinkTestDataRateTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 6)
)
if mibBuilder.loadTexts:
    oriLinkTestDataRateTable.setStatus("current")
_OriLinkTestDataRateTableEntry_Object = MibTableRow
oriLinkTestDataRateTableEntry = _OriLinkTestDataRateTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 6, 1)
)
oriLinkTestDataRateTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriLinkTestTableIndex"),
    (0, "ORiNOCO-MIB", "oriLinkTestDataRateTableIndex"),
)
if mibBuilder.loadTexts:
    oriLinkTestDataRateTableEntry.setStatus("current")
_OriLinkTestDataRateTableIndex_Type = Integer32
_OriLinkTestDataRateTableIndex_Object = MibTableColumn
oriLinkTestDataRateTableIndex = _OriLinkTestDataRateTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 6, 1, 1),
    _OriLinkTestDataRateTableIndex_Type()
)
oriLinkTestDataRateTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestDataRateTableIndex.setStatus("current")
_OriLinkTestDataRateTableRemoteCount_Type = Counter32
_OriLinkTestDataRateTableRemoteCount_Object = MibTableColumn
oriLinkTestDataRateTableRemoteCount = _OriLinkTestDataRateTableRemoteCount_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 6, 1, 2),
    _OriLinkTestDataRateTableRemoteCount_Type()
)
oriLinkTestDataRateTableRemoteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestDataRateTableRemoteCount.setStatus("current")
_OriLinkTestDataRateTableLocalCount_Type = Counter32
_OriLinkTestDataRateTableLocalCount_Object = MibTableColumn
oriLinkTestDataRateTableLocalCount = _OriLinkTestDataRateTableLocalCount_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 11, 6, 1, 3),
    _OriLinkTestDataRateTableLocalCount_Type()
)
oriLinkTestDataRateTableLocalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestDataRateTableLocalCount.setStatus("current")
_OrinocoLinkInt_ObjectIdentity = ObjectIdentity
orinocoLinkInt = _OrinocoLinkInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 12)
)


class _OriLinkIntStatus_Type(Integer32):
    """Custom type oriLinkIntStatus based on Integer32"""
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


_OriLinkIntStatus_Type.__name__ = "Integer32"
_OriLinkIntStatus_Object = MibScalar
oriLinkIntStatus = _OriLinkIntStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 12, 1),
    _OriLinkIntStatus_Type()
)
oriLinkIntStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriLinkIntStatus.setStatus("current")


class _OriLinkIntPollInterval_Type(Integer32):
    """Custom type oriLinkIntPollInterval based on Integer32"""
    defaultValue = 500


_OriLinkIntPollInterval_Object = MibScalar
oriLinkIntPollInterval = _OriLinkIntPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 12, 2),
    _OriLinkIntPollInterval_Type()
)
oriLinkIntPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriLinkIntPollInterval.setStatus("current")
_OriLinkIntPollRetransmissions_Type = Integer32
_OriLinkIntPollRetransmissions_Object = MibScalar
oriLinkIntPollRetransmissions = _OriLinkIntPollRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 12, 3),
    _OriLinkIntPollRetransmissions_Type()
)
oriLinkIntPollRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriLinkIntPollRetransmissions.setStatus("current")
_OriLinkIntTable_Object = MibTable
oriLinkIntTable = _OriLinkIntTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 12, 4)
)
if mibBuilder.loadTexts:
    oriLinkIntTable.setStatus("current")
_OriLinkIntTableEntry_Object = MibTableRow
oriLinkIntTableEntry = _OriLinkIntTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 12, 4, 1)
)
oriLinkIntTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriLinkIntTableIndex"),
)
if mibBuilder.loadTexts:
    oriLinkIntTableEntry.setStatus("current")


class _OriLinkIntTableIndex_Type(Integer32):
    """Custom type oriLinkIntTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_OriLinkIntTableIndex_Type.__name__ = "Integer32"
_OriLinkIntTableIndex_Object = MibTableColumn
oriLinkIntTableIndex = _OriLinkIntTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 12, 4, 1, 1),
    _OriLinkIntTableIndex_Type()
)
oriLinkIntTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkIntTableIndex.setStatus("current")
_OriLinkIntTableTargetIPAddress_Type = IpAddress
_OriLinkIntTableTargetIPAddress_Object = MibTableColumn
oriLinkIntTableTargetIPAddress = _OriLinkIntTableTargetIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 12, 4, 1, 2),
    _OriLinkIntTableTargetIPAddress_Type()
)
oriLinkIntTableTargetIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriLinkIntTableTargetIPAddress.setStatus("current")
_OriLinkIntTableComment_Type = DisplayString
_OriLinkIntTableComment_Object = MibTableColumn
oriLinkIntTableComment = _OriLinkIntTableComment_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 12, 4, 1, 3),
    _OriLinkIntTableComment_Type()
)
oriLinkIntTableComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriLinkIntTableComment.setStatus("current")


class _OriLinkIntTableEntryStatus_Type(Integer32):
    """Custom type oriLinkIntTableEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriLinkIntTableEntryStatus_Type.__name__ = "Integer32"
_OriLinkIntTableEntryStatus_Object = MibTableColumn
oriLinkIntTableEntryStatus = _OriLinkIntTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 12, 4, 1, 4),
    _OriLinkIntTableEntryStatus_Type()
)
oriLinkIntTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriLinkIntTableEntryStatus.setStatus("current")
_OrinocoUPSD_ObjectIdentity = ObjectIdentity
orinocoUPSD = _OrinocoUPSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 13)
)


class _OriUPSDGPRInterval_Type(Integer32):
    """Custom type oriUPSDGPRInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_OriUPSDGPRInterval_Type.__name__ = "Integer32"
_OriUPSDGPRInterval_Object = MibScalar
oriUPSDGPRInterval = _OriUPSDGPRInterval_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 13, 1),
    _OriUPSDGPRInterval_Type()
)
oriUPSDGPRInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriUPSDGPRInterval.setStatus("current")


class _OriUPSDMaxActiveSU_Type(Integer32):
    """Custom type oriUPSDMaxActiveSU based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_OriUPSDMaxActiveSU_Type.__name__ = "Integer32"
_OriUPSDMaxActiveSU_Object = MibScalar
oriUPSDMaxActiveSU = _OriUPSDMaxActiveSU_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 13, 2),
    _OriUPSDMaxActiveSU_Type()
)
oriUPSDMaxActiveSU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriUPSDMaxActiveSU.setStatus("current")


class _OriUPSDE911Reserved_Type(Integer32):
    """Custom type oriUPSDE911Reserved based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_OriUPSDE911Reserved_Type.__name__ = "Integer32"
_OriUPSDE911Reserved_Object = MibScalar
oriUPSDE911Reserved = _OriUPSDE911Reserved_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 13, 3),
    _OriUPSDE911Reserved_Type()
)
oriUPSDE911Reserved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriUPSDE911Reserved.setStatus("current")


class _OriUPSDRoamingReserved_Type(Integer32):
    """Custom type oriUPSDRoamingReserved based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_OriUPSDRoamingReserved_Type.__name__ = "Integer32"
_OriUPSDRoamingReserved_Object = MibScalar
oriUPSDRoamingReserved = _OriUPSDRoamingReserved_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 13, 4),
    _OriUPSDRoamingReserved_Type()
)
oriUPSDRoamingReserved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriUPSDRoamingReserved.setStatus("current")
_OrinocoQoS_ObjectIdentity = ObjectIdentity
orinocoQoS = _OrinocoQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14)
)
_OriQoSPolicyTable_Object = MibTable
oriQoSPolicyTable = _OriQoSPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 1)
)
if mibBuilder.loadTexts:
    oriQoSPolicyTable.setStatus("current")
_OriQoSPolicyTableEntry_Object = MibTableRow
oriQoSPolicyTableEntry = _OriQoSPolicyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 1, 1)
)
oriQoSPolicyTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriQoSPolicyTableIndex"),
    (0, "ORiNOCO-MIB", "oriQoSPolicyTableSecIndex"),
)
if mibBuilder.loadTexts:
    oriQoSPolicyTableEntry.setStatus("current")
_OriQoSPolicyTableIndex_Type = Integer32
_OriQoSPolicyTableIndex_Object = MibTableColumn
oriQoSPolicyTableIndex = _OriQoSPolicyTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 1, 1, 1),
    _OriQoSPolicyTableIndex_Type()
)
oriQoSPolicyTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriQoSPolicyTableIndex.setStatus("current")
_OriQoSPolicyTableSecIndex_Type = Integer32
_OriQoSPolicyTableSecIndex_Object = MibTableColumn
oriQoSPolicyTableSecIndex = _OriQoSPolicyTableSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 1, 1, 2),
    _OriQoSPolicyTableSecIndex_Type()
)
oriQoSPolicyTableSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriQoSPolicyTableSecIndex.setStatus("current")
_OriQoSPolicyName_Type = DisplayString32
_OriQoSPolicyName_Object = MibTableColumn
oriQoSPolicyName = _OriQoSPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 1, 1, 3),
    _OriQoSPolicyName_Type()
)
oriQoSPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriQoSPolicyName.setStatus("current")


class _OriQoSPolicyType_Type(Integer32):
    """Custom type oriQoSPolicyType based on Integer32"""
    defaultValue = 1

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
        *(("inboundLayer2", 1),
          ("inboundLayer3", 2),
          ("outboundLayer2", 3),
          ("outboundLayer3", 4),
          ("spectralink", 5))
    )


_OriQoSPolicyType_Type.__name__ = "Integer32"
_OriQoSPolicyType_Object = MibTableColumn
oriQoSPolicyType = _OriQoSPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 1, 1, 4),
    _OriQoSPolicyType_Type()
)
oriQoSPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriQoSPolicyType.setStatus("current")
_OriQoSPolicyPriorityMapping_Type = Integer32
_OriQoSPolicyPriorityMapping_Object = MibTableColumn
oriQoSPolicyPriorityMapping = _OriQoSPolicyPriorityMapping_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 1, 1, 5),
    _OriQoSPolicyPriorityMapping_Type()
)
oriQoSPolicyPriorityMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriQoSPolicyPriorityMapping.setStatus("current")
_OriQoSPolicyMarkingStatus_Type = ObjStatus
_OriQoSPolicyMarkingStatus_Object = MibTableColumn
oriQoSPolicyMarkingStatus = _OriQoSPolicyMarkingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 1, 1, 6),
    _OriQoSPolicyMarkingStatus_Type()
)
oriQoSPolicyMarkingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriQoSPolicyMarkingStatus.setStatus("current")
_OriQoSPolicyTableRowStatus_Type = RowStatus
_OriQoSPolicyTableRowStatus_Object = MibTableColumn
oriQoSPolicyTableRowStatus = _OriQoSPolicyTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 1, 1, 7),
    _OriQoSPolicyTableRowStatus_Type()
)
oriQoSPolicyTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriQoSPolicyTableRowStatus.setStatus("current")
_OriQoSDot1DToDot1pMappingTable_Object = MibTable
oriQoSDot1DToDot1pMappingTable = _OriQoSDot1DToDot1pMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 2)
)
if mibBuilder.loadTexts:
    oriQoSDot1DToDot1pMappingTable.setStatus("current")
_OriQoSDot1DToDot1pMappingTableEntry_Object = MibTableRow
oriQoSDot1DToDot1pMappingTableEntry = _OriQoSDot1DToDot1pMappingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 2, 1)
)
oriQoSDot1DToDot1pMappingTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriQoSDot1DToDot1pMappingTableIndex"),
    (0, "ORiNOCO-MIB", "oriQoSDot1dPriority"),
)
if mibBuilder.loadTexts:
    oriQoSDot1DToDot1pMappingTableEntry.setStatus("current")
_OriQoSDot1DToDot1pMappingTableIndex_Type = Integer32
_OriQoSDot1DToDot1pMappingTableIndex_Object = MibTableColumn
oriQoSDot1DToDot1pMappingTableIndex = _OriQoSDot1DToDot1pMappingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 2, 1, 1),
    _OriQoSDot1DToDot1pMappingTableIndex_Type()
)
oriQoSDot1DToDot1pMappingTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriQoSDot1DToDot1pMappingTableIndex.setStatus("current")


class _OriQoSDot1dPriority_Type(Integer32):
    """Custom type oriQoSDot1dPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OriQoSDot1dPriority_Type.__name__ = "Integer32"
_OriQoSDot1dPriority_Object = MibTableColumn
oriQoSDot1dPriority = _OriQoSDot1dPriority_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 2, 1, 2),
    _OriQoSDot1dPriority_Type()
)
oriQoSDot1dPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriQoSDot1dPriority.setStatus("current")


class _OriQoSDot1pPriority_Type(Integer32):
    """Custom type oriQoSDot1pPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OriQoSDot1pPriority_Type.__name__ = "Integer32"
_OriQoSDot1pPriority_Object = MibTableColumn
oriQoSDot1pPriority = _OriQoSDot1pPriority_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 2, 1, 3),
    _OriQoSDot1pPriority_Type()
)
oriQoSDot1pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriQoSDot1pPriority.setStatus("current")
_OriQoSDot1DToDot1pMappingTableRowStatus_Type = RowStatus
_OriQoSDot1DToDot1pMappingTableRowStatus_Object = MibTableColumn
oriQoSDot1DToDot1pMappingTableRowStatus = _OriQoSDot1DToDot1pMappingTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 2, 1, 4),
    _OriQoSDot1DToDot1pMappingTableRowStatus_Type()
)
oriQoSDot1DToDot1pMappingTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriQoSDot1DToDot1pMappingTableRowStatus.setStatus("current")
_OriQoSDot1DToIPDSCPMappingTable_Object = MibTable
oriQoSDot1DToIPDSCPMappingTable = _OriQoSDot1DToIPDSCPMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 3)
)
if mibBuilder.loadTexts:
    oriQoSDot1DToIPDSCPMappingTable.setStatus("current")
_OriQoSDot1DToIPDSCPMappingTableEntry_Object = MibTableRow
oriQoSDot1DToIPDSCPMappingTableEntry = _OriQoSDot1DToIPDSCPMappingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 3, 1)
)
oriQoSDot1DToIPDSCPMappingTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriQoSDot1DToIPDSCPMappingTableIndex"),
    (0, "ORiNOCO-MIB", "oriQoSDot1DToIPDSCPPriority"),
)
if mibBuilder.loadTexts:
    oriQoSDot1DToIPDSCPMappingTableEntry.setStatus("current")
_OriQoSDot1DToIPDSCPMappingTableIndex_Type = Integer32
_OriQoSDot1DToIPDSCPMappingTableIndex_Object = MibTableColumn
oriQoSDot1DToIPDSCPMappingTableIndex = _OriQoSDot1DToIPDSCPMappingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 3, 1, 1),
    _OriQoSDot1DToIPDSCPMappingTableIndex_Type()
)
oriQoSDot1DToIPDSCPMappingTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriQoSDot1DToIPDSCPMappingTableIndex.setStatus("current")


class _OriQoSDot1DToIPDSCPPriority_Type(Integer32):
    """Custom type oriQoSDot1DToIPDSCPPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OriQoSDot1DToIPDSCPPriority_Type.__name__ = "Integer32"
_OriQoSDot1DToIPDSCPPriority_Object = MibTableColumn
oriQoSDot1DToIPDSCPPriority = _OriQoSDot1DToIPDSCPPriority_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 3, 1, 2),
    _OriQoSDot1DToIPDSCPPriority_Type()
)
oriQoSDot1DToIPDSCPPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriQoSDot1DToIPDSCPPriority.setStatus("current")


class _OriQoSIPDSCPLowerLimit_Type(Integer32):
    """Custom type oriQoSIPDSCPLowerLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 62),
    )


_OriQoSIPDSCPLowerLimit_Type.__name__ = "Integer32"
_OriQoSIPDSCPLowerLimit_Object = MibTableColumn
oriQoSIPDSCPLowerLimit = _OriQoSIPDSCPLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 3, 1, 3),
    _OriQoSIPDSCPLowerLimit_Type()
)
oriQoSIPDSCPLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriQoSIPDSCPLowerLimit.setStatus("current")


class _OriQoSIPDSCPUpperLimit_Type(Integer32):
    """Custom type oriQoSIPDSCPUpperLimit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_OriQoSIPDSCPUpperLimit_Type.__name__ = "Integer32"
_OriQoSIPDSCPUpperLimit_Object = MibTableColumn
oriQoSIPDSCPUpperLimit = _OriQoSIPDSCPUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 3, 1, 4),
    _OriQoSIPDSCPUpperLimit_Type()
)
oriQoSIPDSCPUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriQoSIPDSCPUpperLimit.setStatus("current")
_OriQoSDot1DToIPDSCPMappingTableRowStatus_Type = RowStatus
_OriQoSDot1DToIPDSCPMappingTableRowStatus_Object = MibTableColumn
oriQoSDot1DToIPDSCPMappingTableRowStatus = _OriQoSDot1DToIPDSCPMappingTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 14, 3, 1, 5),
    _OriQoSDot1DToIPDSCPMappingTableRowStatus_Type()
)
oriQoSDot1DToIPDSCPMappingTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriQoSDot1DToIPDSCPMappingTableRowStatus.setStatus("current")
_OrinocoDHCP_ObjectIdentity = ObjectIdentity
orinocoDHCP = _OrinocoDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15)
)
_OrinocoDHCPServer_ObjectIdentity = ObjectIdentity
orinocoDHCPServer = _OrinocoDHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1)
)


class _OriDHCPServerStatus_Type(Integer32):
    """Custom type oriDHCPServerStatus based on Integer32"""
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


_OriDHCPServerStatus_Type.__name__ = "Integer32"
_OriDHCPServerStatus_Object = MibScalar
oriDHCPServerStatus = _OriDHCPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1, 1),
    _OriDHCPServerStatus_Type()
)
oriDHCPServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPServerStatus.setStatus("current")
_OriDHCPServerIPPoolTable_Object = MibTable
oriDHCPServerIPPoolTable = _OriDHCPServerIPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1, 2)
)
if mibBuilder.loadTexts:
    oriDHCPServerIPPoolTable.setStatus("current")
_OriDHCPServerIPPoolTableEntry_Object = MibTableRow
oriDHCPServerIPPoolTableEntry = _OriDHCPServerIPPoolTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1, 2, 1)
)
oriDHCPServerIPPoolTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriDHCPServerIPPoolTableIndex"),
)
if mibBuilder.loadTexts:
    oriDHCPServerIPPoolTableEntry.setStatus("current")


class _OriDHCPServerIPPoolTableIndex_Type(Integer32):
    """Custom type oriDHCPServerIPPoolTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OriDHCPServerIPPoolTableIndex_Type.__name__ = "Integer32"
_OriDHCPServerIPPoolTableIndex_Object = MibTableColumn
oriDHCPServerIPPoolTableIndex = _OriDHCPServerIPPoolTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1, 2, 1, 1),
    _OriDHCPServerIPPoolTableIndex_Type()
)
oriDHCPServerIPPoolTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriDHCPServerIPPoolTableIndex.setStatus("current")
_OriDHCPServerIPPoolTableStartIPAddress_Type = IpAddress
_OriDHCPServerIPPoolTableStartIPAddress_Object = MibTableColumn
oriDHCPServerIPPoolTableStartIPAddress = _OriDHCPServerIPPoolTableStartIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1, 2, 1, 2),
    _OriDHCPServerIPPoolTableStartIPAddress_Type()
)
oriDHCPServerIPPoolTableStartIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPServerIPPoolTableStartIPAddress.setStatus("current")
_OriDHCPServerIPPoolTableEndIPAddress_Type = IpAddress
_OriDHCPServerIPPoolTableEndIPAddress_Object = MibTableColumn
oriDHCPServerIPPoolTableEndIPAddress = _OriDHCPServerIPPoolTableEndIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1, 2, 1, 3),
    _OriDHCPServerIPPoolTableEndIPAddress_Type()
)
oriDHCPServerIPPoolTableEndIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPServerIPPoolTableEndIPAddress.setStatus("current")
_OriDHCPServerIPPoolTableWidth_Type = Integer32
_OriDHCPServerIPPoolTableWidth_Object = MibTableColumn
oriDHCPServerIPPoolTableWidth = _OriDHCPServerIPPoolTableWidth_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1, 2, 1, 4),
    _OriDHCPServerIPPoolTableWidth_Type()
)
oriDHCPServerIPPoolTableWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPServerIPPoolTableWidth.setStatus("current")


class _OriDHCPServerIPPoolTableDefaultLeaseTime_Type(Integer32):
    """Custom type oriDHCPServerIPPoolTableDefaultLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3600, 86400),
    )


_OriDHCPServerIPPoolTableDefaultLeaseTime_Type.__name__ = "Integer32"
_OriDHCPServerIPPoolTableDefaultLeaseTime_Object = MibTableColumn
oriDHCPServerIPPoolTableDefaultLeaseTime = _OriDHCPServerIPPoolTableDefaultLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1, 2, 1, 5),
    _OriDHCPServerIPPoolTableDefaultLeaseTime_Type()
)
oriDHCPServerIPPoolTableDefaultLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPServerIPPoolTableDefaultLeaseTime.setStatus("current")


class _OriDHCPServerIPPoolTableMaximumLeaseTime_Type(Integer32):
    """Custom type oriDHCPServerIPPoolTableMaximumLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3600, 86400),
    )


_OriDHCPServerIPPoolTableMaximumLeaseTime_Type.__name__ = "Integer32"
_OriDHCPServerIPPoolTableMaximumLeaseTime_Object = MibTableColumn
oriDHCPServerIPPoolTableMaximumLeaseTime = _OriDHCPServerIPPoolTableMaximumLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1, 2, 1, 6),
    _OriDHCPServerIPPoolTableMaximumLeaseTime_Type()
)
oriDHCPServerIPPoolTableMaximumLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPServerIPPoolTableMaximumLeaseTime.setStatus("current")
_OriDHCPServerIPPoolTableComment_Type = DisplayString
_OriDHCPServerIPPoolTableComment_Object = MibTableColumn
oriDHCPServerIPPoolTableComment = _OriDHCPServerIPPoolTableComment_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1, 2, 1, 7),
    _OriDHCPServerIPPoolTableComment_Type()
)
oriDHCPServerIPPoolTableComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPServerIPPoolTableComment.setStatus("current")


class _OriDHCPServerIPPoolTableEntryStatus_Type(Integer32):
    """Custom type oriDHCPServerIPPoolTableEntryStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriDHCPServerIPPoolTableEntryStatus_Type.__name__ = "Integer32"
_OriDHCPServerIPPoolTableEntryStatus_Object = MibTableColumn
oriDHCPServerIPPoolTableEntryStatus = _OriDHCPServerIPPoolTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1, 2, 1, 8),
    _OriDHCPServerIPPoolTableEntryStatus_Type()
)
oriDHCPServerIPPoolTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPServerIPPoolTableEntryStatus.setStatus("current")
_OriDHCPServerDefaultGatewayIPAddress_Type = IpAddress
_OriDHCPServerDefaultGatewayIPAddress_Object = MibScalar
oriDHCPServerDefaultGatewayIPAddress = _OriDHCPServerDefaultGatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1, 3),
    _OriDHCPServerDefaultGatewayIPAddress_Type()
)
oriDHCPServerDefaultGatewayIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPServerDefaultGatewayIPAddress.setStatus("current")
_OriDHCPServerSubnetMask_Type = IpAddress
_OriDHCPServerSubnetMask_Object = MibScalar
oriDHCPServerSubnetMask = _OriDHCPServerSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1, 4),
    _OriDHCPServerSubnetMask_Type()
)
oriDHCPServerSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriDHCPServerSubnetMask.setStatus("current")
_OriDHCPServerNumIPPoolTableEntries_Type = Integer32
_OriDHCPServerNumIPPoolTableEntries_Object = MibScalar
oriDHCPServerNumIPPoolTableEntries = _OriDHCPServerNumIPPoolTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1, 5),
    _OriDHCPServerNumIPPoolTableEntries_Type()
)
oriDHCPServerNumIPPoolTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriDHCPServerNumIPPoolTableEntries.setStatus("current")
_OriDHCPServerPrimaryDNSIPAddress_Type = IpAddress
_OriDHCPServerPrimaryDNSIPAddress_Object = MibScalar
oriDHCPServerPrimaryDNSIPAddress = _OriDHCPServerPrimaryDNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1, 6),
    _OriDHCPServerPrimaryDNSIPAddress_Type()
)
oriDHCPServerPrimaryDNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPServerPrimaryDNSIPAddress.setStatus("current")
_OriDHCPServerSecondaryDNSIPAddress_Type = IpAddress
_OriDHCPServerSecondaryDNSIPAddress_Object = MibScalar
oriDHCPServerSecondaryDNSIPAddress = _OriDHCPServerSecondaryDNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 1, 7),
    _OriDHCPServerSecondaryDNSIPAddress_Type()
)
oriDHCPServerSecondaryDNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPServerSecondaryDNSIPAddress.setStatus("current")
_OrinocoDHCPClient_ObjectIdentity = ObjectIdentity
orinocoDHCPClient = _OrinocoDHCPClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 2)
)
_OriDHCPClientID_Type = DisplayString
_OriDHCPClientID_Object = MibScalar
oriDHCPClientID = _OriDHCPClientID_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 2, 1),
    _OriDHCPClientID_Type()
)
oriDHCPClientID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPClientID.setStatus("current")
_OriDHCPClientInterfaceBitmask_Type = InterfaceBitmask
_OriDHCPClientInterfaceBitmask_Object = MibScalar
oriDHCPClientInterfaceBitmask = _OriDHCPClientInterfaceBitmask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 2, 2),
    _OriDHCPClientInterfaceBitmask_Type()
)
oriDHCPClientInterfaceBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPClientInterfaceBitmask.setStatus("current")
_OrinocoDHCPRelay_ObjectIdentity = ObjectIdentity
orinocoDHCPRelay = _OrinocoDHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 3)
)


class _OriDHCPRelayStatus_Type(Integer32):
    """Custom type oriDHCPRelayStatus based on Integer32"""
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


_OriDHCPRelayStatus_Type.__name__ = "Integer32"
_OriDHCPRelayStatus_Object = MibScalar
oriDHCPRelayStatus = _OriDHCPRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 3, 1),
    _OriDHCPRelayStatus_Type()
)
oriDHCPRelayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPRelayStatus.setStatus("current")
_OriDHCPRelayDHCPServerTable_Object = MibTable
oriDHCPRelayDHCPServerTable = _OriDHCPRelayDHCPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 3, 2)
)
if mibBuilder.loadTexts:
    oriDHCPRelayDHCPServerTable.setStatus("current")
_OriDHCPRelayDHCPServerTableEntry_Object = MibTableRow
oriDHCPRelayDHCPServerTableEntry = _OriDHCPRelayDHCPServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 3, 2, 1)
)
oriDHCPRelayDHCPServerTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriDHCPRelayDHCPServerTableIndex"),
)
if mibBuilder.loadTexts:
    oriDHCPRelayDHCPServerTableEntry.setStatus("current")


class _OriDHCPRelayDHCPServerTableIndex_Type(Integer32):
    """Custom type oriDHCPRelayDHCPServerTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_OriDHCPRelayDHCPServerTableIndex_Type.__name__ = "Integer32"
_OriDHCPRelayDHCPServerTableIndex_Object = MibTableColumn
oriDHCPRelayDHCPServerTableIndex = _OriDHCPRelayDHCPServerTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 3, 2, 1, 1),
    _OriDHCPRelayDHCPServerTableIndex_Type()
)
oriDHCPRelayDHCPServerTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriDHCPRelayDHCPServerTableIndex.setStatus("current")
_OriDHCPRelayDHCPServerTableIpAddress_Type = IpAddress
_OriDHCPRelayDHCPServerTableIpAddress_Object = MibTableColumn
oriDHCPRelayDHCPServerTableIpAddress = _OriDHCPRelayDHCPServerTableIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 3, 2, 1, 2),
    _OriDHCPRelayDHCPServerTableIpAddress_Type()
)
oriDHCPRelayDHCPServerTableIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPRelayDHCPServerTableIpAddress.setStatus("current")
_OriDHCPRelayDHCPServerTableComment_Type = DisplayString
_OriDHCPRelayDHCPServerTableComment_Object = MibTableColumn
oriDHCPRelayDHCPServerTableComment = _OriDHCPRelayDHCPServerTableComment_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 3, 2, 1, 3),
    _OriDHCPRelayDHCPServerTableComment_Type()
)
oriDHCPRelayDHCPServerTableComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPRelayDHCPServerTableComment.setStatus("current")


class _OriDHCPRelayDHCPServerTableEntryStatus_Type(Integer32):
    """Custom type oriDHCPRelayDHCPServerTableEntryStatus based on Integer32"""
    defaultValue = 2

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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriDHCPRelayDHCPServerTableEntryStatus_Type.__name__ = "Integer32"
_OriDHCPRelayDHCPServerTableEntryStatus_Object = MibTableColumn
oriDHCPRelayDHCPServerTableEntryStatus = _OriDHCPRelayDHCPServerTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 15, 3, 2, 1, 4),
    _OriDHCPRelayDHCPServerTableEntryStatus_Type()
)
oriDHCPRelayDHCPServerTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDHCPRelayDHCPServerTableEntryStatus.setStatus("current")
_OrinocoHTTP_ObjectIdentity = ObjectIdentity
orinocoHTTP = _OrinocoHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16)
)
_OriHTTPInterfaceBitmask_Type = InterfaceBitmask
_OriHTTPInterfaceBitmask_Object = MibScalar
oriHTTPInterfaceBitmask = _OriHTTPInterfaceBitmask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16, 1),
    _OriHTTPInterfaceBitmask_Type()
)
oriHTTPInterfaceBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriHTTPInterfaceBitmask.setStatus("current")
_OriHTTPPassword_Type = DisplayString
_OriHTTPPassword_Object = MibScalar
oriHTTPPassword = _OriHTTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16, 2),
    _OriHTTPPassword_Type()
)
oriHTTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriHTTPPassword.setStatus("current")
_OriHTTPPort_Type = Integer32
_OriHTTPPort_Object = MibScalar
oriHTTPPort = _OriHTTPPort_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16, 3),
    _OriHTTPPort_Type()
)
oriHTTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriHTTPPort.setStatus("current")
_OriHTTPWebSitenameTable_Object = MibTable
oriHTTPWebSitenameTable = _OriHTTPWebSitenameTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16, 4)
)
if mibBuilder.loadTexts:
    oriHTTPWebSitenameTable.setStatus("current")
_OriHTTPWebSitenameTableEntry_Object = MibTableRow
oriHTTPWebSitenameTableEntry = _OriHTTPWebSitenameTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16, 4, 1)
)
oriHTTPWebSitenameTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriHTTPWebSitenameTableIndex"),
)
if mibBuilder.loadTexts:
    oriHTTPWebSitenameTableEntry.setStatus("current")
_OriHTTPWebSitenameTableIndex_Type = Integer32
_OriHTTPWebSitenameTableIndex_Object = MibTableColumn
oriHTTPWebSitenameTableIndex = _OriHTTPWebSitenameTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16, 4, 1, 1),
    _OriHTTPWebSitenameTableIndex_Type()
)
oriHTTPWebSitenameTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriHTTPWebSitenameTableIndex.setStatus("current")
_OriHTTPWebSiteFilename_Type = DisplayString
_OriHTTPWebSiteFilename_Object = MibTableColumn
oriHTTPWebSiteFilename = _OriHTTPWebSiteFilename_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16, 4, 1, 2),
    _OriHTTPWebSiteFilename_Type()
)
oriHTTPWebSiteFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriHTTPWebSiteFilename.setStatus("current")
_OriHTTPWebSiteLanguage_Type = DisplayString
_OriHTTPWebSiteLanguage_Object = MibTableColumn
oriHTTPWebSiteLanguage = _OriHTTPWebSiteLanguage_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16, 4, 1, 3),
    _OriHTTPWebSiteLanguage_Type()
)
oriHTTPWebSiteLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriHTTPWebSiteLanguage.setStatus("current")
_OriHTTPWebSiteDescription_Type = DisplayString
_OriHTTPWebSiteDescription_Object = MibTableColumn
oriHTTPWebSiteDescription = _OriHTTPWebSiteDescription_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16, 4, 1, 4),
    _OriHTTPWebSiteDescription_Type()
)
oriHTTPWebSiteDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriHTTPWebSiteDescription.setStatus("current")


class _OriHTTPWebSitenameTableStatus_Type(Integer32):
    """Custom type oriHTTPWebSitenameTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriHTTPWebSitenameTableStatus_Type.__name__ = "Integer32"
_OriHTTPWebSitenameTableStatus_Object = MibTableColumn
oriHTTPWebSitenameTableStatus = _OriHTTPWebSitenameTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16, 4, 1, 5),
    _OriHTTPWebSitenameTableStatus_Type()
)
oriHTTPWebSitenameTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriHTTPWebSitenameTableStatus.setStatus("current")
_OriHTTPRefreshDelay_Type = Integer32
_OriHTTPRefreshDelay_Object = MibScalar
oriHTTPRefreshDelay = _OriHTTPRefreshDelay_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16, 5),
    _OriHTTPRefreshDelay_Type()
)
oriHTTPRefreshDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriHTTPRefreshDelay.setStatus("current")
_OriHTTPHelpInformationLink_Type = DisplayString
_OriHTTPHelpInformationLink_Object = MibScalar
oriHTTPHelpInformationLink = _OriHTTPHelpInformationLink_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16, 6),
    _OriHTTPHelpInformationLink_Type()
)
oriHTTPHelpInformationLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriHTTPHelpInformationLink.setStatus("current")


class _OriHTTPSSLStatus_Type(ObjStatus):
    """Custom type oriHTTPSSLStatus based on ObjStatus"""


_OriHTTPSSLStatus_Object = MibScalar
oriHTTPSSLStatus = _OriHTTPSSLStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16, 7),
    _OriHTTPSSLStatus_Type()
)
oriHTTPSSLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriHTTPSSLStatus.setStatus("current")
_OriHTTPSSLPassphrase_Type = DisplayString
_OriHTTPSSLPassphrase_Object = MibScalar
oriHTTPSSLPassphrase = _OriHTTPSSLPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16, 8),
    _OriHTTPSSLPassphrase_Type()
)
oriHTTPSSLPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriHTTPSSLPassphrase.setStatus("current")


class _OriHTTPSetupWizardStatus_Type(Integer32):
    """Custom type oriHTTPSetupWizardStatus based on Integer32"""
    defaultValue = 1

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


_OriHTTPSetupWizardStatus_Type.__name__ = "Integer32"
_OriHTTPSetupWizardStatus_Object = MibScalar
oriHTTPSetupWizardStatus = _OriHTTPSetupWizardStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16, 9),
    _OriHTTPSetupWizardStatus_Type()
)
oriHTTPSetupWizardStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriHTTPSetupWizardStatus.setStatus("current")


class _OriHTTPRADIUSAccessControl_Type(ObjStatus):
    """Custom type oriHTTPRADIUSAccessControl based on ObjStatus"""


_OriHTTPRADIUSAccessControl_Object = MibScalar
oriHTTPRADIUSAccessControl = _OriHTTPRADIUSAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 16, 10),
    _OriHTTPRADIUSAccessControl_Type()
)
oriHTTPRADIUSAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriHTTPRADIUSAccessControl.setStatus("current")
_OrinocoWDS_ObjectIdentity = ObjectIdentity
orinocoWDS = _OrinocoWDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 17)
)
_OriWDSSetupTable_Object = MibTable
oriWDSSetupTable = _OriWDSSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 17, 1)
)
if mibBuilder.loadTexts:
    oriWDSSetupTable.setStatus("current")
_OriWDSSetupTableEntry_Object = MibTableRow
oriWDSSetupTableEntry = _OriWDSSetupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 17, 1, 1)
)
oriWDSSetupTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ORiNOCO-MIB", "oriWDSSetupTablePortIndex"),
)
if mibBuilder.loadTexts:
    oriWDSSetupTableEntry.setStatus("current")


class _OriWDSSetupTablePortIndex_Type(Integer32):
    """Custom type oriWDSSetupTablePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_OriWDSSetupTablePortIndex_Type.__name__ = "Integer32"
_OriWDSSetupTablePortIndex_Object = MibTableColumn
oriWDSSetupTablePortIndex = _OriWDSSetupTablePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 17, 1, 1, 1),
    _OriWDSSetupTablePortIndex_Type()
)
oriWDSSetupTablePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriWDSSetupTablePortIndex.setStatus("current")


class _OriWDSSetupTableEntryStatus_Type(Integer32):
    """Custom type oriWDSSetupTableEntryStatus based on Integer32"""
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


_OriWDSSetupTableEntryStatus_Type.__name__ = "Integer32"
_OriWDSSetupTableEntryStatus_Object = MibTableColumn
oriWDSSetupTableEntryStatus = _OriWDSSetupTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 17, 1, 1, 2),
    _OriWDSSetupTableEntryStatus_Type()
)
oriWDSSetupTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWDSSetupTableEntryStatus.setStatus("current")
_OriWDSSetupTablePartnerMACAddress_Type = PhysAddress
_OriWDSSetupTablePartnerMACAddress_Object = MibTableColumn
oriWDSSetupTablePartnerMACAddress = _OriWDSSetupTablePartnerMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 17, 1, 1, 3),
    _OriWDSSetupTablePartnerMACAddress_Type()
)
oriWDSSetupTablePartnerMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWDSSetupTablePartnerMACAddress.setStatus("current")
_OriWDSSecurityTable_Object = MibTable
oriWDSSecurityTable = _OriWDSSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 17, 2)
)
if mibBuilder.loadTexts:
    oriWDSSecurityTable.setStatus("current")
_OriWDSSecurityTableEntry_Object = MibTableRow
oriWDSSecurityTableEntry = _OriWDSSecurityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 17, 2, 1)
)
oriWDSSecurityTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oriWDSSecurityTableEntry.setStatus("current")


class _OriWDSSecurityTableSecurityMode_Type(Integer32):
    """Custom type oriWDSSecurityTableSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("wep", 6))
    )


_OriWDSSecurityTableSecurityMode_Type.__name__ = "Integer32"
_OriWDSSecurityTableSecurityMode_Object = MibTableColumn
oriWDSSecurityTableSecurityMode = _OriWDSSecurityTableSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 17, 2, 1, 1),
    _OriWDSSecurityTableSecurityMode_Type()
)
oriWDSSecurityTableSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWDSSecurityTableSecurityMode.setStatus("current")
_OriWDSSecurityTableEncryptionKey0_Type = WEPKeyType
_OriWDSSecurityTableEncryptionKey0_Object = MibTableColumn
oriWDSSecurityTableEncryptionKey0 = _OriWDSSecurityTableEncryptionKey0_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 17, 2, 1, 2),
    _OriWDSSecurityTableEncryptionKey0_Type()
)
oriWDSSecurityTableEncryptionKey0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWDSSecurityTableEncryptionKey0.setStatus("current")
_OrinocoTrap_ObjectIdentity = ObjectIdentity
orinocoTrap = _OrinocoTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18)
)
_OriTrapVariable_ObjectIdentity = ObjectIdentity
oriTrapVariable = _OriTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1)
)
_OriGenericTrapVariable_Type = DisplayString
_OriGenericTrapVariable_Object = MibScalar
oriGenericTrapVariable = _OriGenericTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 1),
    _OriGenericTrapVariable_Type()
)
oriGenericTrapVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriGenericTrapVariable.setStatus("current")
_OriTrapVarMACAddress_Type = PhysAddress
_OriTrapVarMACAddress_Object = MibScalar
oriTrapVarMACAddress = _OriTrapVarMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 2),
    _OriTrapVarMACAddress_Type()
)
oriTrapVarMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarMACAddress.setStatus("current")
_OriTrapVarTFTPIPAddress_Type = IpAddress
_OriTrapVarTFTPIPAddress_Object = MibScalar
oriTrapVarTFTPIPAddress = _OriTrapVarTFTPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 3),
    _OriTrapVarTFTPIPAddress_Type()
)
oriTrapVarTFTPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarTFTPIPAddress.setStatus("current")
_OriTrapVarTFTPFilename_Type = DisplayString
_OriTrapVarTFTPFilename_Object = MibScalar
oriTrapVarTFTPFilename = _OriTrapVarTFTPFilename_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 4),
    _OriTrapVarTFTPFilename_Type()
)
oriTrapVarTFTPFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarTFTPFilename.setStatus("current")


class _OriTrapVarTFTPOperation_Type(Integer32):
    """Custom type oriTrapVarTFTPOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 2),
          ("upload", 1))
    )


_OriTrapVarTFTPOperation_Type.__name__ = "Integer32"
_OriTrapVarTFTPOperation_Object = MibScalar
oriTrapVarTFTPOperation = _OriTrapVarTFTPOperation_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 5),
    _OriTrapVarTFTPOperation_Type()
)
oriTrapVarTFTPOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarTFTPOperation.setStatus("current")
_OriTrapVarUnauthorizedManagerIPaddress_Type = IpAddress
_OriTrapVarUnauthorizedManagerIPaddress_Object = MibScalar
oriTrapVarUnauthorizedManagerIPaddress = _OriTrapVarUnauthorizedManagerIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 6),
    _OriTrapVarUnauthorizedManagerIPaddress_Type()
)
oriTrapVarUnauthorizedManagerIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarUnauthorizedManagerIPaddress.setStatus("current")
_OriTrapVarFailedAuthenticationType_Type = DisplayString
_OriTrapVarFailedAuthenticationType_Object = MibScalar
oriTrapVarFailedAuthenticationType = _OriTrapVarFailedAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 7),
    _OriTrapVarFailedAuthenticationType_Type()
)
oriTrapVarFailedAuthenticationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarFailedAuthenticationType.setStatus("current")
_OriTrapVarUnAuthorizedManagerCount_Type = Counter32
_OriTrapVarUnAuthorizedManagerCount_Object = MibScalar
oriTrapVarUnAuthorizedManagerCount = _OriTrapVarUnAuthorizedManagerCount_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 8),
    _OriTrapVarUnAuthorizedManagerCount_Type()
)
oriTrapVarUnAuthorizedManagerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarUnAuthorizedManagerCount.setStatus("current")
_OriTrapVarTaskSuspended_Type = DisplayString
_OriTrapVarTaskSuspended_Object = MibScalar
oriTrapVarTaskSuspended = _OriTrapVarTaskSuspended_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 9),
    _OriTrapVarTaskSuspended_Type()
)
oriTrapVarTaskSuspended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarTaskSuspended.setStatus("current")


class _OriConfigurationTrapsStatus_Type(Integer32):
    """Custom type oriConfigurationTrapsStatus based on Integer32"""
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


_OriConfigurationTrapsStatus_Type.__name__ = "Integer32"
_OriConfigurationTrapsStatus_Object = MibScalar
oriConfigurationTrapsStatus = _OriConfigurationTrapsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 10),
    _OriConfigurationTrapsStatus_Type()
)
oriConfigurationTrapsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriConfigurationTrapsStatus.setStatus("current")


class _OriSecurityTrapsStatus_Type(Integer32):
    """Custom type oriSecurityTrapsStatus based on Integer32"""
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


_OriSecurityTrapsStatus_Type.__name__ = "Integer32"
_OriSecurityTrapsStatus_Object = MibScalar
oriSecurityTrapsStatus = _OriSecurityTrapsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 11),
    _OriSecurityTrapsStatus_Type()
)
oriSecurityTrapsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSecurityTrapsStatus.setStatus("current")


class _OriWirelessIfTrapsStatus_Type(Integer32):
    """Custom type oriWirelessIfTrapsStatus based on Integer32"""
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


_OriWirelessIfTrapsStatus_Type.__name__ = "Integer32"
_OriWirelessIfTrapsStatus_Object = MibScalar
oriWirelessIfTrapsStatus = _OriWirelessIfTrapsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 12),
    _OriWirelessIfTrapsStatus_Type()
)
oriWirelessIfTrapsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWirelessIfTrapsStatus.setStatus("current")


class _OriOperationalTrapsStatus_Type(Integer32):
    """Custom type oriOperationalTrapsStatus based on Integer32"""
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


_OriOperationalTrapsStatus_Type.__name__ = "Integer32"
_OriOperationalTrapsStatus_Object = MibScalar
oriOperationalTrapsStatus = _OriOperationalTrapsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 13),
    _OriOperationalTrapsStatus_Type()
)
oriOperationalTrapsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriOperationalTrapsStatus.setStatus("current")


class _OriFlashMemoryTrapsStatus_Type(Integer32):
    """Custom type oriFlashMemoryTrapsStatus based on Integer32"""
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


_OriFlashMemoryTrapsStatus_Type.__name__ = "Integer32"
_OriFlashMemoryTrapsStatus_Object = MibScalar
oriFlashMemoryTrapsStatus = _OriFlashMemoryTrapsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 14),
    _OriFlashMemoryTrapsStatus_Type()
)
oriFlashMemoryTrapsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriFlashMemoryTrapsStatus.setStatus("current")


class _OriTFTPTrapsStatus_Type(Integer32):
    """Custom type oriTFTPTrapsStatus based on Integer32"""
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


_OriTFTPTrapsStatus_Type.__name__ = "Integer32"
_OriTFTPTrapsStatus_Object = MibScalar
oriTFTPTrapsStatus = _OriTFTPTrapsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 15),
    _OriTFTPTrapsStatus_Type()
)
oriTFTPTrapsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTFTPTrapsStatus.setStatus("current")


class _OriTrapsImageStatus_Type(Integer32):
    """Custom type oriTrapsImageStatus based on Integer32"""
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


_OriTrapsImageStatus_Type.__name__ = "Integer32"
_OriTrapsImageStatus_Object = MibScalar
oriTrapsImageStatus = _OriTrapsImageStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 16),
    _OriTrapsImageStatus_Type()
)
oriTrapsImageStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriTrapsImageStatus.setStatus("current")
_OriTrapVarUnauthorizedClientMACAddress_Type = PhysAddress
_OriTrapVarUnauthorizedClientMACAddress_Object = MibScalar
oriTrapVarUnauthorizedClientMACAddress = _OriTrapVarUnauthorizedClientMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 17),
    _OriTrapVarUnauthorizedClientMACAddress_Type()
)
oriTrapVarUnauthorizedClientMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarUnauthorizedClientMACAddress.setStatus("current")


class _OriTrapVarWirelessCard_Type(Integer32):
    """Custom type oriTrapVarWirelessCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pcCardA", 1),
          ("pcCardB", 2))
    )


_OriTrapVarWirelessCard_Type.__name__ = "Integer32"
_OriTrapVarWirelessCard_Object = MibScalar
oriTrapVarWirelessCard = _OriTrapVarWirelessCard_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 18),
    _OriTrapVarWirelessCard_Type()
)
oriTrapVarWirelessCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarWirelessCard.setStatus("current")


class _OriADSLIfTrapsStatus_Type(Integer32):
    """Custom type oriADSLIfTrapsStatus based on Integer32"""
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


_OriADSLIfTrapsStatus_Type.__name__ = "Integer32"
_OriADSLIfTrapsStatus_Object = MibScalar
oriADSLIfTrapsStatus = _OriADSLIfTrapsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 19),
    _OriADSLIfTrapsStatus_Type()
)
oriADSLIfTrapsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriADSLIfTrapsStatus.setStatus("current")


class _OriWORPTrapsStatus_Type(Integer32):
    """Custom type oriWORPTrapsStatus based on Integer32"""
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


_OriWORPTrapsStatus_Type.__name__ = "Integer32"
_OriWORPTrapsStatus_Object = MibScalar
oriWORPTrapsStatus = _OriWORPTrapsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 20),
    _OriWORPTrapsStatus_Type()
)
oriWORPTrapsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriWORPTrapsStatus.setStatus("current")
_OriTrapVarInterface_Type = Integer32
_OriTrapVarInterface_Object = MibScalar
oriTrapVarInterface = _OriTrapVarInterface_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 21),
    _OriTrapVarInterface_Type()
)
oriTrapVarInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarInterface.setStatus("current")
_OriTrapVarBatchCLIFilename_Type = DisplayString
_OriTrapVarBatchCLIFilename_Object = MibScalar
oriTrapVarBatchCLIFilename = _OriTrapVarBatchCLIFilename_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 22),
    _OriTrapVarBatchCLIFilename_Type()
)
oriTrapVarBatchCLIFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarBatchCLIFilename.setStatus("current")
_OriTrapVarBatchCLIMessage_Type = DisplayString
_OriTrapVarBatchCLIMessage_Object = MibScalar
oriTrapVarBatchCLIMessage = _OriTrapVarBatchCLIMessage_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 23),
    _OriTrapVarBatchCLIMessage_Type()
)
oriTrapVarBatchCLIMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarBatchCLIMessage.setStatus("current")
_OriTrapVarBatchCLILineNumber_Type = Integer32
_OriTrapVarBatchCLILineNumber_Object = MibScalar
oriTrapVarBatchCLILineNumber = _OriTrapVarBatchCLILineNumber_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 24),
    _OriTrapVarBatchCLILineNumber_Type()
)
oriTrapVarBatchCLILineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarBatchCLILineNumber.setStatus("current")
_OriTrapVarDHCPServerIPAddress_Type = IpAddress
_OriTrapVarDHCPServerIPAddress_Object = MibScalar
oriTrapVarDHCPServerIPAddress = _OriTrapVarDHCPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 25),
    _OriTrapVarDHCPServerIPAddress_Type()
)
oriTrapVarDHCPServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarDHCPServerIPAddress.setStatus("current")
_OriTrapVarIPAddress_Type = IpAddress
_OriTrapVarIPAddress_Object = MibScalar
oriTrapVarIPAddress = _OriTrapVarIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 26),
    _OriTrapVarIPAddress_Type()
)
oriTrapVarIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarIPAddress.setStatus("current")
_OriTrapVarSubnetMask_Type = IpAddress
_OriTrapVarSubnetMask_Object = MibScalar
oriTrapVarSubnetMask = _OriTrapVarSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 27),
    _OriTrapVarSubnetMask_Type()
)
oriTrapVarSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarSubnetMask.setStatus("current")
_OriTrapVarDefaultRouterIPAddress_Type = IpAddress
_OriTrapVarDefaultRouterIPAddress_Object = MibScalar
oriTrapVarDefaultRouterIPAddress = _OriTrapVarDefaultRouterIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 1, 28),
    _OriTrapVarDefaultRouterIPAddress_Type()
)
oriTrapVarDefaultRouterIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriTrapVarDefaultRouterIPAddress.setStatus("current")
_OriConfigurationTraps_ObjectIdentity = ObjectIdentity
oriConfigurationTraps = _OriConfigurationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 2)
)
if mibBuilder.loadTexts:
    oriConfigurationTraps.setStatus("current")
_OriSecurityTraps_ObjectIdentity = ObjectIdentity
oriSecurityTraps = _OriSecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 3)
)
if mibBuilder.loadTexts:
    oriSecurityTraps.setStatus("current")
_OriWirelessIfTraps_ObjectIdentity = ObjectIdentity
oriWirelessIfTraps = _OriWirelessIfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 4)
)
if mibBuilder.loadTexts:
    oriWirelessIfTraps.setStatus("current")
_OriOperationalTraps_ObjectIdentity = ObjectIdentity
oriOperationalTraps = _OriOperationalTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5)
)
if mibBuilder.loadTexts:
    oriOperationalTraps.setStatus("current")
_OriFlashTraps_ObjectIdentity = ObjectIdentity
oriFlashTraps = _OriFlashTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 6)
)
if mibBuilder.loadTexts:
    oriFlashTraps.setStatus("current")
_OriTFTPTraps_ObjectIdentity = ObjectIdentity
oriTFTPTraps = _OriTFTPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 7)
)
if mibBuilder.loadTexts:
    oriTFTPTraps.setStatus("current")
_OriMiscTraps_ObjectIdentity = ObjectIdentity
oriMiscTraps = _OriMiscTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 8)
)
if mibBuilder.loadTexts:
    oriMiscTraps.setStatus("current")
_OriImageTraps_ObjectIdentity = ObjectIdentity
oriImageTraps = _OriImageTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 9)
)
if mibBuilder.loadTexts:
    oriImageTraps.setStatus("current")
_OriWORPTraps_ObjectIdentity = ObjectIdentity
oriWORPTraps = _OriWORPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 11)
)
if mibBuilder.loadTexts:
    oriWORPTraps.setStatus("current")
_OriSysFeatureTraps_ObjectIdentity = ObjectIdentity
oriSysFeatureTraps = _OriSysFeatureTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 12)
)
if mibBuilder.loadTexts:
    oriSysFeatureTraps.setStatus("current")
_OrinocoIPARP_ObjectIdentity = ObjectIdentity
orinocoIPARP = _OrinocoIPARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 19)
)


class _OriProxyARPStatus_Type(Integer32):
    """Custom type oriProxyARPStatus based on Integer32"""
    defaultValue = 1

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


_OriProxyARPStatus_Type.__name__ = "Integer32"
_OriProxyARPStatus_Object = MibScalar
oriProxyARPStatus = _OriProxyARPStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 19, 1),
    _OriProxyARPStatus_Type()
)
oriProxyARPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriProxyARPStatus.setStatus("current")


class _OriIPARPFilteringStatus_Type(Integer32):
    """Custom type oriIPARPFilteringStatus based on Integer32"""
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


_OriIPARPFilteringStatus_Type.__name__ = "Integer32"
_OriIPARPFilteringStatus_Object = MibScalar
oriIPARPFilteringStatus = _OriIPARPFilteringStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 19, 2),
    _OriIPARPFilteringStatus_Type()
)
oriIPARPFilteringStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIPARPFilteringStatus.setStatus("current")
_OriIPARPFilteringIPAddress_Type = IpAddress
_OriIPARPFilteringIPAddress_Object = MibScalar
oriIPARPFilteringIPAddress = _OriIPARPFilteringIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 19, 3),
    _OriIPARPFilteringIPAddress_Type()
)
oriIPARPFilteringIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIPARPFilteringIPAddress.setStatus("current")
_OriIPARPFilteringSubnetMask_Type = IpAddress
_OriIPARPFilteringSubnetMask_Object = MibScalar
oriIPARPFilteringSubnetMask = _OriIPARPFilteringSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 19, 4),
    _OriIPARPFilteringSubnetMask_Type()
)
oriIPARPFilteringSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriIPARPFilteringSubnetMask.setStatus("current")
_OrinocoSpanningTree_ObjectIdentity = ObjectIdentity
orinocoSpanningTree = _OrinocoSpanningTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 20)
)


class _OriSpanningTreeStatus_Type(Integer32):
    """Custom type oriSpanningTreeStatus based on Integer32"""
    defaultValue = 1

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


_OriSpanningTreeStatus_Type.__name__ = "Integer32"
_OriSpanningTreeStatus_Object = MibScalar
oriSpanningTreeStatus = _OriSpanningTreeStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 20, 1),
    _OriSpanningTreeStatus_Type()
)
oriSpanningTreeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSpanningTreeStatus.setStatus("current")
_OrinocoSecurity_ObjectIdentity = ObjectIdentity
orinocoSecurity = _OrinocoSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21)
)


class _OriSecurityConfiguration_Type(Integer32):
    """Custom type oriSecurityConfiguration based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 2),
          ("mixedWepAnddot1x", 3),
          ("none", 1))
    )


_OriSecurityConfiguration_Type.__name__ = "Integer32"
_OriSecurityConfiguration_Object = MibScalar
oriSecurityConfiguration = _OriSecurityConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 1),
    _OriSecurityConfiguration_Type()
)
oriSecurityConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSecurityConfiguration.setStatus("deprecated")
_OriSecurityEncryptionKeyLengthTable_Object = MibTable
oriSecurityEncryptionKeyLengthTable = _OriSecurityEncryptionKeyLengthTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 2)
)
if mibBuilder.loadTexts:
    oriSecurityEncryptionKeyLengthTable.setStatus("deprecated")
_OriSecurityEncryptionKeyLengthTableEntry_Object = MibTableRow
oriSecurityEncryptionKeyLengthTableEntry = _OriSecurityEncryptionKeyLengthTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 2, 1)
)
oriSecurityEncryptionKeyLengthTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oriSecurityEncryptionKeyLengthTableEntry.setStatus("deprecated")


class _OriSecurityEncryptionKeyLength_Type(Integer32):
    """Custom type oriSecurityEncryptionKeyLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneHundredTwentyEightBits", 2),
          ("sixtyFourBits", 1))
    )


_OriSecurityEncryptionKeyLength_Type.__name__ = "Integer32"
_OriSecurityEncryptionKeyLength_Object = MibTableColumn
oriSecurityEncryptionKeyLength = _OriSecurityEncryptionKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 2, 1, 1),
    _OriSecurityEncryptionKeyLength_Type()
)
oriSecurityEncryptionKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSecurityEncryptionKeyLength.setStatus("deprecated")


class _OriSecurityRekeyingInterval_Type(Integer32):
    """Custom type oriSecurityRekeyingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 65535),
    )


_OriSecurityRekeyingInterval_Type.__name__ = "Integer32"
_OriSecurityRekeyingInterval_Object = MibScalar
oriSecurityRekeyingInterval = _OriSecurityRekeyingInterval_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 3),
    _OriSecurityRekeyingInterval_Type()
)
oriSecurityRekeyingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSecurityRekeyingInterval.setStatus("deprecated")
_OrinocoRAD_ObjectIdentity = ObjectIdentity
orinocoRAD = _OrinocoRAD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 4)
)


class _OriRADStatus_Type(ObjStatus):
    """Custom type oriRADStatus based on ObjStatus"""


_OriRADStatus_Object = MibScalar
oriRADStatus = _OriRADStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 4, 1),
    _OriRADStatus_Type()
)
oriRADStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADStatus.setStatus("current")


class _OriRADInterval_Type(Integer32):
    """Custom type oriRADInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 1440),
    )


_OriRADInterval_Type.__name__ = "Integer32"
_OriRADInterval_Object = MibScalar
oriRADInterval = _OriRADInterval_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 4, 2),
    _OriRADInterval_Type()
)
oriRADInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADInterval.setStatus("current")
if mibBuilder.loadTexts:
    oriRADInterval.setUnits("seconds")
_OriRADInterfaceBitmask_Type = InterfaceBitmask
_OriRADInterfaceBitmask_Object = MibScalar
oriRADInterfaceBitmask = _OriRADInterfaceBitmask_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 4, 3),
    _OriRADInterfaceBitmask_Type()
)
oriRADInterfaceBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriRADInterfaceBitmask.setStatus("current")
_OriRADLastSuccessfulScanTime_Type = TimeTicks
_OriRADLastSuccessfulScanTime_Object = MibScalar
oriRADLastSuccessfulScanTime = _OriRADLastSuccessfulScanTime_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 4, 4),
    _OriRADLastSuccessfulScanTime_Type()
)
oriRADLastSuccessfulScanTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADLastSuccessfulScanTime.setStatus("current")
_OriRADAccessPointCount_Type = Counter32
_OriRADAccessPointCount_Object = MibScalar
oriRADAccessPointCount = _OriRADAccessPointCount_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 4, 5),
    _OriRADAccessPointCount_Type()
)
oriRADAccessPointCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADAccessPointCount.setStatus("current")
_OriRADScanResultsTable_Object = MibTable
oriRADScanResultsTable = _OriRADScanResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 4, 6)
)
if mibBuilder.loadTexts:
    oriRADScanResultsTable.setStatus("current")
_OriRADScanResultsTableEntry_Object = MibTableRow
oriRADScanResultsTableEntry = _OriRADScanResultsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 4, 6, 1)
)
oriRADScanResultsTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriRADScanResultsTableIndex"),
)
if mibBuilder.loadTexts:
    oriRADScanResultsTableEntry.setStatus("current")
_OriRADScanResultsTableIndex_Type = Integer32
_OriRADScanResultsTableIndex_Object = MibTableColumn
oriRADScanResultsTableIndex = _OriRADScanResultsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 4, 6, 1, 1),
    _OriRADScanResultsTableIndex_Type()
)
oriRADScanResultsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADScanResultsTableIndex.setStatus("current")
_OriRADScanResultsMACAddress_Type = PhysAddress
_OriRADScanResultsMACAddress_Object = MibTableColumn
oriRADScanResultsMACAddress = _OriRADScanResultsMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 4, 6, 1, 2),
    _OriRADScanResultsMACAddress_Type()
)
oriRADScanResultsMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADScanResultsMACAddress.setStatus("current")
_OriRADScanResultsFrequencyChannel_Type = Integer32
_OriRADScanResultsFrequencyChannel_Object = MibTableColumn
oriRADScanResultsFrequencyChannel = _OriRADScanResultsFrequencyChannel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 4, 6, 1, 3),
    _OriRADScanResultsFrequencyChannel_Type()
)
oriRADScanResultsFrequencyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRADScanResultsFrequencyChannel.setStatus("current")
_OriSecurityConfigTable_Object = MibTable
oriSecurityConfigTable = _OriSecurityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 5)
)
if mibBuilder.loadTexts:
    oriSecurityConfigTable.setStatus("deprecated")
_OriSecurityConfigTableEntry_Object = MibTableRow
oriSecurityConfigTableEntry = _OriSecurityConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 5, 1)
)
oriSecurityConfigTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oriSecurityConfigTableEntry.setStatus("deprecated")
_OriSecurityConfigTableSupportedSecurityModes_Type = DisplayString
_OriSecurityConfigTableSupportedSecurityModes_Object = MibTableColumn
oriSecurityConfigTableSupportedSecurityModes = _OriSecurityConfigTableSupportedSecurityModes_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 5, 1, 1),
    _OriSecurityConfigTableSupportedSecurityModes_Type()
)
oriSecurityConfigTableSupportedSecurityModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSecurityConfigTableSupportedSecurityModes.setStatus("deprecated")


class _OriSecurityConfigTableSecurityMode_Type(Integer32):
    """Custom type oriSecurityConfigTableSecurityMode based on Integer32"""
    defaultValue = 1

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
        *(("dot1x", 2),
          ("mixed", 3),
          ("none", 1),
          ("wpa", 4),
          ("wpa-psk", 5))
    )


_OriSecurityConfigTableSecurityMode_Type.__name__ = "Integer32"
_OriSecurityConfigTableSecurityMode_Object = MibTableColumn
oriSecurityConfigTableSecurityMode = _OriSecurityConfigTableSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 5, 1, 2),
    _OriSecurityConfigTableSecurityMode_Type()
)
oriSecurityConfigTableSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSecurityConfigTableSecurityMode.setStatus("deprecated")


class _OriSecurityConfigTableRekeyingInterval_Type(Integer32):
    """Custom type oriSecurityConfigTableRekeyingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 65535),
    )


_OriSecurityConfigTableRekeyingInterval_Type.__name__ = "Integer32"
_OriSecurityConfigTableRekeyingInterval_Object = MibTableColumn
oriSecurityConfigTableRekeyingInterval = _OriSecurityConfigTableRekeyingInterval_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 5, 1, 3),
    _OriSecurityConfigTableRekeyingInterval_Type()
)
oriSecurityConfigTableRekeyingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSecurityConfigTableRekeyingInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    oriSecurityConfigTableRekeyingInterval.setUnits("seconds")


class _OriSecurityConfigTableEncryptionKeyLength_Type(Integer32):
    """Custom type oriSecurityConfigTableEncryptionKeyLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneHundredFiftyTwoBits", 3),
          ("oneHundredTwentyEightBits", 2),
          ("sixtyFourBits", 1))
    )


_OriSecurityConfigTableEncryptionKeyLength_Type.__name__ = "Integer32"
_OriSecurityConfigTableEncryptionKeyLength_Object = MibTableColumn
oriSecurityConfigTableEncryptionKeyLength = _OriSecurityConfigTableEncryptionKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 5, 1, 4),
    _OriSecurityConfigTableEncryptionKeyLength_Type()
)
oriSecurityConfigTableEncryptionKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSecurityConfigTableEncryptionKeyLength.setStatus("deprecated")


class _OriSecurityHwConfigResetStatus_Type(ObjStatus):
    """Custom type oriSecurityHwConfigResetStatus based on ObjStatus"""


_OriSecurityHwConfigResetStatus_Object = MibScalar
oriSecurityHwConfigResetStatus = _OriSecurityHwConfigResetStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 6),
    _OriSecurityHwConfigResetStatus_Type()
)
oriSecurityHwConfigResetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSecurityHwConfigResetStatus.setStatus("current")


class _OriSecurityHwConfigResetPassword_Type(DisplayString):
    """Custom type oriSecurityHwConfigResetPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 32),
    )


_OriSecurityHwConfigResetPassword_Type.__name__ = "DisplayString"
_OriSecurityHwConfigResetPassword_Object = MibScalar
oriSecurityHwConfigResetPassword = _OriSecurityHwConfigResetPassword_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 7),
    _OriSecurityHwConfigResetPassword_Type()
)
oriSecurityHwConfigResetPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSecurityHwConfigResetPassword.setStatus("current")
_OrinocoRogueScan_ObjectIdentity = ObjectIdentity
orinocoRogueScan = _OrinocoRogueScan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8)
)
_OriRogueScanConfigTable_Object = MibTable
oriRogueScanConfigTable = _OriRogueScanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 1)
)
if mibBuilder.loadTexts:
    oriRogueScanConfigTable.setStatus("current")
_OriRogueScanConfigTableEntry_Object = MibTableRow
oriRogueScanConfigTableEntry = _OriRogueScanConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 1, 1)
)
oriRogueScanConfigTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oriRogueScanConfigTableEntry.setStatus("current")


class _OriRogueScanConfigTableScanMode_Type(Integer32):
    """Custom type oriRogueScanConfigTableScanMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bkScanMode", 1),
          ("contScanMode", 2))
    )


_OriRogueScanConfigTableScanMode_Type.__name__ = "Integer32"
_OriRogueScanConfigTableScanMode_Object = MibTableColumn
oriRogueScanConfigTableScanMode = _OriRogueScanConfigTableScanMode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 1, 1, 1),
    _OriRogueScanConfigTableScanMode_Type()
)
oriRogueScanConfigTableScanMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriRogueScanConfigTableScanMode.setStatus("current")


class _OriRogueScanConfigTableScanCycleTime_Type(Integer32):
    """Custom type oriRogueScanConfigTableScanCycleTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_OriRogueScanConfigTableScanCycleTime_Type.__name__ = "Integer32"
_OriRogueScanConfigTableScanCycleTime_Object = MibTableColumn
oriRogueScanConfigTableScanCycleTime = _OriRogueScanConfigTableScanCycleTime_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 1, 1, 2),
    _OriRogueScanConfigTableScanCycleTime_Type()
)
oriRogueScanConfigTableScanCycleTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriRogueScanConfigTableScanCycleTime.setStatus("current")
_OriRogueScanConfigTableScanStatus_Type = ObjStatus
_OriRogueScanConfigTableScanStatus_Object = MibTableColumn
oriRogueScanConfigTableScanStatus = _OriRogueScanConfigTableScanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 1, 1, 3),
    _OriRogueScanConfigTableScanStatus_Type()
)
oriRogueScanConfigTableScanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriRogueScanConfigTableScanStatus.setStatus("current")
_OriRogueScanStationCountWirelessCardA_Type = Counter32
_OriRogueScanStationCountWirelessCardA_Object = MibScalar
oriRogueScanStationCountWirelessCardA = _OriRogueScanStationCountWirelessCardA_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 2),
    _OriRogueScanStationCountWirelessCardA_Type()
)
oriRogueScanStationCountWirelessCardA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRogueScanStationCountWirelessCardA.setStatus("current")
_OriRogueScanStationCountWirelessCardB_Type = Counter32
_OriRogueScanStationCountWirelessCardB_Object = MibScalar
oriRogueScanStationCountWirelessCardB = _OriRogueScanStationCountWirelessCardB_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 3),
    _OriRogueScanStationCountWirelessCardB_Type()
)
oriRogueScanStationCountWirelessCardB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRogueScanStationCountWirelessCardB.setStatus("current")


class _OriRogueScanResultsTableAgingTime_Type(Integer32):
    """Custom type oriRogueScanResultsTableAgingTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 7200),
    )


_OriRogueScanResultsTableAgingTime_Type.__name__ = "Integer32"
_OriRogueScanResultsTableAgingTime_Object = MibScalar
oriRogueScanResultsTableAgingTime = _OriRogueScanResultsTableAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 4),
    _OriRogueScanResultsTableAgingTime_Type()
)
oriRogueScanResultsTableAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriRogueScanResultsTableAgingTime.setStatus("current")
_OriRogueScanResultsTableClearEntries_Type = Integer32
_OriRogueScanResultsTableClearEntries_Object = MibScalar
oriRogueScanResultsTableClearEntries = _OriRogueScanResultsTableClearEntries_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 5),
    _OriRogueScanResultsTableClearEntries_Type()
)
oriRogueScanResultsTableClearEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriRogueScanResultsTableClearEntries.setStatus("current")


class _OriRogueScanResultsNotificationMode_Type(Integer32):
    """Custom type oriRogueScanResultsNotificationMode based on Integer32"""
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
        *(("noNotification", 1),
          ("notifyAP", 2),
          ("notifyAll", 4),
          ("notifyClient", 3))
    )


_OriRogueScanResultsNotificationMode_Type.__name__ = "Integer32"
_OriRogueScanResultsNotificationMode_Object = MibScalar
oriRogueScanResultsNotificationMode = _OriRogueScanResultsNotificationMode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 6),
    _OriRogueScanResultsNotificationMode_Type()
)
oriRogueScanResultsNotificationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriRogueScanResultsNotificationMode.setStatus("current")


class _OriRogueScanResultsTrapReportType_Type(Integer32):
    """Custom type oriRogueScanResultsTrapReportType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reportSinceLastScan", 1),
          ("reportSinceStartOfScan", 2))
    )


_OriRogueScanResultsTrapReportType_Type.__name__ = "Integer32"
_OriRogueScanResultsTrapReportType_Object = MibScalar
oriRogueScanResultsTrapReportType = _OriRogueScanResultsTrapReportType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 7),
    _OriRogueScanResultsTrapReportType_Type()
)
oriRogueScanResultsTrapReportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriRogueScanResultsTrapReportType.setStatus("current")
_OriRogueScanResultsTable_Object = MibTable
oriRogueScanResultsTable = _OriRogueScanResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 8)
)
if mibBuilder.loadTexts:
    oriRogueScanResultsTable.setStatus("current")
_OriRogueScanResultsTableEntry_Object = MibTableRow
oriRogueScanResultsTableEntry = _OriRogueScanResultsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 8, 1)
)
oriRogueScanResultsTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriRogueScanResultsTableIndex"),
)
if mibBuilder.loadTexts:
    oriRogueScanResultsTableEntry.setStatus("current")
_OriRogueScanResultsTableIndex_Type = Integer32
_OriRogueScanResultsTableIndex_Object = MibTableColumn
oriRogueScanResultsTableIndex = _OriRogueScanResultsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 8, 1, 1),
    _OriRogueScanResultsTableIndex_Type()
)
oriRogueScanResultsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRogueScanResultsTableIndex.setStatus("current")


class _OriRogueScanResultsStationType_Type(Integer32):
    """Custom type oriRogueScanResultsStationType based on Integer32"""
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
        *(("accessPoint", 3),
          ("ibssClient", 4),
          ("infrastructureClient", 2),
          ("unknown", 1))
    )


_OriRogueScanResultsStationType_Type.__name__ = "Integer32"
_OriRogueScanResultsStationType_Object = MibTableColumn
oriRogueScanResultsStationType = _OriRogueScanResultsStationType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 8, 1, 2),
    _OriRogueScanResultsStationType_Type()
)
oriRogueScanResultsStationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRogueScanResultsStationType.setStatus("current")
_OriRogueScanResultsMACAddress_Type = PhysAddress
_OriRogueScanResultsMACAddress_Object = MibTableColumn
oriRogueScanResultsMACAddress = _OriRogueScanResultsMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 8, 1, 3),
    _OriRogueScanResultsMACAddress_Type()
)
oriRogueScanResultsMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRogueScanResultsMACAddress.setStatus("current")


class _OriRogueScanResultsFrequencyChannel_Type(DisplayString):
    """Custom type oriRogueScanResultsFrequencyChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_OriRogueScanResultsFrequencyChannel_Type.__name__ = "DisplayString"
_OriRogueScanResultsFrequencyChannel_Object = MibTableColumn
oriRogueScanResultsFrequencyChannel = _OriRogueScanResultsFrequencyChannel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 8, 1, 5),
    _OriRogueScanResultsFrequencyChannel_Type()
)
oriRogueScanResultsFrequencyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRogueScanResultsFrequencyChannel.setStatus("current")
_OriRogueScanResultsSNR_Type = Integer32
_OriRogueScanResultsSNR_Object = MibTableColumn
oriRogueScanResultsSNR = _OriRogueScanResultsSNR_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 8, 1, 6),
    _OriRogueScanResultsSNR_Type()
)
oriRogueScanResultsSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRogueScanResultsSNR.setStatus("current")
_OriRogueScanResultsBSSID_Type = MacAddress
_OriRogueScanResultsBSSID_Object = MibTableColumn
oriRogueScanResultsBSSID = _OriRogueScanResultsBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 8, 8, 1, 7),
    _OriRogueScanResultsBSSID_Type()
)
oriRogueScanResultsBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriRogueScanResultsBSSID.setStatus("current")
_OriSecurityProfileTable_Object = MibTable
oriSecurityProfileTable = _OriSecurityProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 9)
)
if mibBuilder.loadTexts:
    oriSecurityProfileTable.setStatus("current")
_OriSecurityProfileTableEntry_Object = MibTableRow
oriSecurityProfileTableEntry = _OriSecurityProfileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 9, 1)
)
oriSecurityProfileTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriSecurityProfileTableIndex"),
    (0, "ORiNOCO-MIB", "oriSecurityProfileTableSecModeIndex"),
)
if mibBuilder.loadTexts:
    oriSecurityProfileTableEntry.setStatus("current")
_OriSecurityProfileTableIndex_Type = Integer32
_OriSecurityProfileTableIndex_Object = MibTableColumn
oriSecurityProfileTableIndex = _OriSecurityProfileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 9, 1, 1),
    _OriSecurityProfileTableIndex_Type()
)
oriSecurityProfileTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSecurityProfileTableIndex.setStatus("current")
_OriSecurityProfileTableSecModeIndex_Type = Integer32
_OriSecurityProfileTableSecModeIndex_Object = MibTableColumn
oriSecurityProfileTableSecModeIndex = _OriSecurityProfileTableSecModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 9, 1, 2),
    _OriSecurityProfileTableSecModeIndex_Type()
)
oriSecurityProfileTableSecModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSecurityProfileTableSecModeIndex.setStatus("current")


class _OriSecurityProfileTableAuthenticationMode_Type(Integer32):
    """Custom type oriSecurityProfileTableAuthenticationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 2),
          ("none", 1),
          ("psk", 3))
    )


_OriSecurityProfileTableAuthenticationMode_Type.__name__ = "Integer32"
_OriSecurityProfileTableAuthenticationMode_Object = MibTableColumn
oriSecurityProfileTableAuthenticationMode = _OriSecurityProfileTableAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 9, 1, 3),
    _OriSecurityProfileTableAuthenticationMode_Type()
)
oriSecurityProfileTableAuthenticationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSecurityProfileTableAuthenticationMode.setStatus("current")


class _OriSecurityProfileTableCipherMode_Type(Integer32):
    """Custom type oriSecurityProfileTableCipherMode based on Integer32"""
    defaultValue = 1

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
        *(("aes", 4),
          ("none", 1),
          ("tkip", 3),
          ("wep", 2))
    )


_OriSecurityProfileTableCipherMode_Type.__name__ = "Integer32"
_OriSecurityProfileTableCipherMode_Object = MibTableColumn
oriSecurityProfileTableCipherMode = _OriSecurityProfileTableCipherMode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 9, 1, 4),
    _OriSecurityProfileTableCipherMode_Type()
)
oriSecurityProfileTableCipherMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSecurityProfileTableCipherMode.setStatus("current")
_OriSecurityProfileTableEncryptionKey0_Type = WEPKeyType
_OriSecurityProfileTableEncryptionKey0_Object = MibTableColumn
oriSecurityProfileTableEncryptionKey0 = _OriSecurityProfileTableEncryptionKey0_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 9, 1, 5),
    _OriSecurityProfileTableEncryptionKey0_Type()
)
oriSecurityProfileTableEncryptionKey0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriSecurityProfileTableEncryptionKey0.setStatus("current")
_OriSecurityProfileTableEncryptionKey1_Type = WEPKeyType
_OriSecurityProfileTableEncryptionKey1_Object = MibTableColumn
oriSecurityProfileTableEncryptionKey1 = _OriSecurityProfileTableEncryptionKey1_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 9, 1, 6),
    _OriSecurityProfileTableEncryptionKey1_Type()
)
oriSecurityProfileTableEncryptionKey1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriSecurityProfileTableEncryptionKey1.setStatus("current")
_OriSecurityProfileTableEncryptionKey2_Type = WEPKeyType
_OriSecurityProfileTableEncryptionKey2_Object = MibTableColumn
oriSecurityProfileTableEncryptionKey2 = _OriSecurityProfileTableEncryptionKey2_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 9, 1, 7),
    _OriSecurityProfileTableEncryptionKey2_Type()
)
oriSecurityProfileTableEncryptionKey2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriSecurityProfileTableEncryptionKey2.setStatus("current")
_OriSecurityProfileTableEncryptionKey3_Type = WEPKeyType
_OriSecurityProfileTableEncryptionKey3_Object = MibTableColumn
oriSecurityProfileTableEncryptionKey3 = _OriSecurityProfileTableEncryptionKey3_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 9, 1, 8),
    _OriSecurityProfileTableEncryptionKey3_Type()
)
oriSecurityProfileTableEncryptionKey3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriSecurityProfileTableEncryptionKey3.setStatus("current")


class _OriSecurityProfileTableEncryptionTxKey_Type(Integer32):
    """Custom type oriSecurityProfileTableEncryptionTxKey based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_OriSecurityProfileTableEncryptionTxKey_Type.__name__ = "Integer32"
_OriSecurityProfileTableEncryptionTxKey_Object = MibTableColumn
oriSecurityProfileTableEncryptionTxKey = _OriSecurityProfileTableEncryptionTxKey_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 9, 1, 9),
    _OriSecurityProfileTableEncryptionTxKey_Type()
)
oriSecurityProfileTableEncryptionTxKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriSecurityProfileTableEncryptionTxKey.setStatus("current")


class _OriSecurityProfileTableEncryptionKeyLength_Type(Integer32):
    """Custom type oriSecurityProfileTableEncryptionKeyLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneHundredFiftyTwoBits", 3),
          ("oneHundredTwentyEightBits", 2),
          ("sixtyFourBits", 1))
    )


_OriSecurityProfileTableEncryptionKeyLength_Type.__name__ = "Integer32"
_OriSecurityProfileTableEncryptionKeyLength_Object = MibTableColumn
oriSecurityProfileTableEncryptionKeyLength = _OriSecurityProfileTableEncryptionKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 9, 1, 10),
    _OriSecurityProfileTableEncryptionKeyLength_Type()
)
oriSecurityProfileTableEncryptionKeyLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriSecurityProfileTableEncryptionKeyLength.setStatus("current")


class _OriSecurityProfileTablePSKValue_Type(OctetString):
    """Custom type oriSecurityProfileTablePSKValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_OriSecurityProfileTablePSKValue_Type.__name__ = "OctetString"
_OriSecurityProfileTablePSKValue_Object = MibTableColumn
oriSecurityProfileTablePSKValue = _OriSecurityProfileTablePSKValue_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 9, 1, 11),
    _OriSecurityProfileTablePSKValue_Type()
)
oriSecurityProfileTablePSKValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriSecurityProfileTablePSKValue.setStatus("current")


class _OriSecurityProfileTablePSKPassPhrase_Type(DisplayString):
    """Custom type oriSecurityProfileTablePSKPassPhrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_OriSecurityProfileTablePSKPassPhrase_Type.__name__ = "DisplayString"
_OriSecurityProfileTablePSKPassPhrase_Object = MibTableColumn
oriSecurityProfileTablePSKPassPhrase = _OriSecurityProfileTablePSKPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 9, 1, 12),
    _OriSecurityProfileTablePSKPassPhrase_Type()
)
oriSecurityProfileTablePSKPassPhrase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriSecurityProfileTablePSKPassPhrase.setStatus("current")
_OriSecurityProfileTableStatus_Type = RowStatus
_OriSecurityProfileTableStatus_Object = MibTableColumn
oriSecurityProfileTableStatus = _OriSecurityProfileTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 9, 1, 14),
    _OriSecurityProfileTableStatus_Type()
)
oriSecurityProfileTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oriSecurityProfileTableStatus.setStatus("current")
_OriSecurityProfileFourWEPKeySupport_Type = Integer32
_OriSecurityProfileFourWEPKeySupport_Object = MibScalar
oriSecurityProfileFourWEPKeySupport = _OriSecurityProfileFourWEPKeySupport_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 21, 10),
    _OriSecurityProfileFourWEPKeySupport_Type()
)
oriSecurityProfileFourWEPKeySupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSecurityProfileFourWEPKeySupport.setStatus("current")
_OrinocoPPPoE_ObjectIdentity = ObjectIdentity
orinocoPPPoE = _OrinocoPPPoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22)
)


class _OriPPPoEStatus_Type(Integer32):
    """Custom type oriPPPoEStatus based on Integer32"""
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


_OriPPPoEStatus_Type.__name__ = "Integer32"
_OriPPPoEStatus_Object = MibScalar
oriPPPoEStatus = _OriPPPoEStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 1),
    _OriPPPoEStatus_Type()
)
oriPPPoEStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPPPoEStatus.setStatus("current")


class _OriPPPoEMaximumNumberOfSessions_Type(Integer32):
    """Custom type oriPPPoEMaximumNumberOfSessions based on Integer32"""
    defaultValue = 10


_OriPPPoEMaximumNumberOfSessions_Object = MibScalar
oriPPPoEMaximumNumberOfSessions = _OriPPPoEMaximumNumberOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 2),
    _OriPPPoEMaximumNumberOfSessions_Type()
)
oriPPPoEMaximumNumberOfSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPPPoEMaximumNumberOfSessions.setStatus("current")
_OriPPPoENumberOfActiveSessions_Type = Counter32
_OriPPPoENumberOfActiveSessions_Object = MibScalar
oriPPPoENumberOfActiveSessions = _OriPPPoENumberOfActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 3),
    _OriPPPoENumberOfActiveSessions_Type()
)
oriPPPoENumberOfActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriPPPoENumberOfActiveSessions.setStatus("current")
_OriPPPoESessionTable_Object = MibTable
oriPPPoESessionTable = _OriPPPoESessionTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4)
)
if mibBuilder.loadTexts:
    oriPPPoESessionTable.setStatus("current")
_OriPPPoESessionTableEntry_Object = MibTableRow
oriPPPoESessionTableEntry = _OriPPPoESessionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1)
)
oriPPPoESessionTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriPPPoESessionTableIndex"),
)
if mibBuilder.loadTexts:
    oriPPPoESessionTableEntry.setStatus("current")
_OriPPPoESessionTableIndex_Type = Integer32
_OriPPPoESessionTableIndex_Object = MibTableColumn
oriPPPoESessionTableIndex = _OriPPPoESessionTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 1),
    _OriPPPoESessionTableIndex_Type()
)
oriPPPoESessionTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriPPPoESessionTableIndex.setStatus("current")


class _OriPPPoESessionWANConnectMode_Type(Integer32):
    """Custom type oriPPPoESessionWANConnectMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysOn", 1),
          ("manual", 3),
          ("onDemand", 2))
    )


_OriPPPoESessionWANConnectMode_Type.__name__ = "Integer32"
_OriPPPoESessionWANConnectMode_Object = MibTableColumn
oriPPPoESessionWANConnectMode = _OriPPPoESessionWANConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 2),
    _OriPPPoESessionWANConnectMode_Type()
)
oriPPPoESessionWANConnectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPPPoESessionWANConnectMode.setStatus("current")
_OriPPPoESessionIdleTimeOut_Type = Integer32
_OriPPPoESessionIdleTimeOut_Object = MibTableColumn
oriPPPoESessionIdleTimeOut = _OriPPPoESessionIdleTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 3),
    _OriPPPoESessionIdleTimeOut_Type()
)
oriPPPoESessionIdleTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPPPoESessionIdleTimeOut.setStatus("current")
_OriPPPoESessionConnectTime_Type = Counter32
_OriPPPoESessionConnectTime_Object = MibTableColumn
oriPPPoESessionConnectTime = _OriPPPoESessionConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 4),
    _OriPPPoESessionConnectTime_Type()
)
oriPPPoESessionConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriPPPoESessionConnectTime.setStatus("current")


class _OriPPPoESessionConnectTimeLimitation_Type(Integer32):
    """Custom type oriPPPoESessionConnectTimeLimitation based on Integer32"""
    defaultValue = 0


_OriPPPoESessionConnectTimeLimitation_Object = MibTableColumn
oriPPPoESessionConnectTimeLimitation = _OriPPPoESessionConnectTimeLimitation_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 5),
    _OriPPPoESessionConnectTimeLimitation_Type()
)
oriPPPoESessionConnectTimeLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPPPoESessionConnectTimeLimitation.setStatus("current")
_OriPPPoESessionConfigPADITxInterval_Type = Integer32
_OriPPPoESessionConfigPADITxInterval_Object = MibTableColumn
oriPPPoESessionConfigPADITxInterval = _OriPPPoESessionConfigPADITxInterval_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 6),
    _OriPPPoESessionConfigPADITxInterval_Type()
)
oriPPPoESessionConfigPADITxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPPPoESessionConfigPADITxInterval.setStatus("current")
_OriPPPoESessionConfigPADIMaxNumberOfRetries_Type = Integer32
_OriPPPoESessionConfigPADIMaxNumberOfRetries_Object = MibTableColumn
oriPPPoESessionConfigPADIMaxNumberOfRetries = _OriPPPoESessionConfigPADIMaxNumberOfRetries_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 7),
    _OriPPPoESessionConfigPADIMaxNumberOfRetries_Type()
)
oriPPPoESessionConfigPADIMaxNumberOfRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPPPoESessionConfigPADIMaxNumberOfRetries.setStatus("current")
_OriPPPoESessionBindingsNumberPADITx_Type = Counter32
_OriPPPoESessionBindingsNumberPADITx_Object = MibTableColumn
oriPPPoESessionBindingsNumberPADITx = _OriPPPoESessionBindingsNumberPADITx_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 8),
    _OriPPPoESessionBindingsNumberPADITx_Type()
)
oriPPPoESessionBindingsNumberPADITx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriPPPoESessionBindingsNumberPADITx.setStatus("current")
_OriPPPoESessionBindingsNumberPADTTx_Type = Counter32
_OriPPPoESessionBindingsNumberPADTTx_Object = MibTableColumn
oriPPPoESessionBindingsNumberPADTTx = _OriPPPoESessionBindingsNumberPADTTx_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 9),
    _OriPPPoESessionBindingsNumberPADTTx_Type()
)
oriPPPoESessionBindingsNumberPADTTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriPPPoESessionBindingsNumberPADTTx.setStatus("current")
_OriPPPoESessionBindingsNumberServiceNameErrors_Type = Counter32
_OriPPPoESessionBindingsNumberServiceNameErrors_Object = MibTableColumn
oriPPPoESessionBindingsNumberServiceNameErrors = _OriPPPoESessionBindingsNumberServiceNameErrors_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 10),
    _OriPPPoESessionBindingsNumberServiceNameErrors_Type()
)
oriPPPoESessionBindingsNumberServiceNameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriPPPoESessionBindingsNumberServiceNameErrors.setStatus("current")
_OriPPPoESessionBindingsNumberACSystemErrors_Type = Counter32
_OriPPPoESessionBindingsNumberACSystemErrors_Object = MibTableColumn
oriPPPoESessionBindingsNumberACSystemErrors = _OriPPPoESessionBindingsNumberACSystemErrors_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 11),
    _OriPPPoESessionBindingsNumberACSystemErrors_Type()
)
oriPPPoESessionBindingsNumberACSystemErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriPPPoESessionBindingsNumberACSystemErrors.setStatus("current")
_OriPPPoESessionBindingsNumberGenericErrorsRx_Type = Counter32
_OriPPPoESessionBindingsNumberGenericErrorsRx_Object = MibTableColumn
oriPPPoESessionBindingsNumberGenericErrorsRx = _OriPPPoESessionBindingsNumberGenericErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 12),
    _OriPPPoESessionBindingsNumberGenericErrorsRx_Type()
)
oriPPPoESessionBindingsNumberGenericErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriPPPoESessionBindingsNumberGenericErrorsRx.setStatus("current")
_OriPPPoESessionBindingsNumberGenericErrorsTx_Type = Counter32
_OriPPPoESessionBindingsNumberGenericErrorsTx_Object = MibTableColumn
oriPPPoESessionBindingsNumberGenericErrorsTx = _OriPPPoESessionBindingsNumberGenericErrorsTx_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 13),
    _OriPPPoESessionBindingsNumberGenericErrorsTx_Type()
)
oriPPPoESessionBindingsNumberGenericErrorsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriPPPoESessionBindingsNumberGenericErrorsTx.setStatus("current")
_OriPPPoESessionBindingsNumberMalformedPackets_Type = Counter32
_OriPPPoESessionBindingsNumberMalformedPackets_Object = MibTableColumn
oriPPPoESessionBindingsNumberMalformedPackets = _OriPPPoESessionBindingsNumberMalformedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 14),
    _OriPPPoESessionBindingsNumberMalformedPackets_Type()
)
oriPPPoESessionBindingsNumberMalformedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriPPPoESessionBindingsNumberMalformedPackets.setStatus("current")
_OriPPPoESessionBindingsNumberMultiplePADORx_Type = Counter32
_OriPPPoESessionBindingsNumberMultiplePADORx_Object = MibTableColumn
oriPPPoESessionBindingsNumberMultiplePADORx = _OriPPPoESessionBindingsNumberMultiplePADORx_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 15),
    _OriPPPoESessionBindingsNumberMultiplePADORx_Type()
)
oriPPPoESessionBindingsNumberMultiplePADORx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriPPPoESessionBindingsNumberMultiplePADORx.setStatus("current")
_OriPPPoESessionUserName_Type = DisplayString
_OriPPPoESessionUserName_Object = MibTableColumn
oriPPPoESessionUserName = _OriPPPoESessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 16),
    _OriPPPoESessionUserName_Type()
)
oriPPPoESessionUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPPPoESessionUserName.setStatus("current")
_OriPPPoESessionUserNamePassword_Type = DisplayString
_OriPPPoESessionUserNamePassword_Object = MibTableColumn
oriPPPoESessionUserNamePassword = _OriPPPoESessionUserNamePassword_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 17),
    _OriPPPoESessionUserNamePassword_Type()
)
oriPPPoESessionUserNamePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPPPoESessionUserNamePassword.setStatus("current")
_OriPPPoESessionServiceName_Type = DisplayString
_OriPPPoESessionServiceName_Object = MibTableColumn
oriPPPoESessionServiceName = _OriPPPoESessionServiceName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 18),
    _OriPPPoESessionServiceName_Type()
)
oriPPPoESessionServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPPPoESessionServiceName.setStatus("current")
_OriPPPoESessionISPName_Type = DisplayString
_OriPPPoESessionISPName_Object = MibTableColumn
oriPPPoESessionISPName = _OriPPPoESessionISPName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 19),
    _OriPPPoESessionISPName_Type()
)
oriPPPoESessionISPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPPPoESessionISPName.setStatus("current")


class _OriPPPoESessionTableStatus_Type(Integer32):
    """Custom type oriPPPoESessionTableStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriPPPoESessionTableStatus_Type.__name__ = "Integer32"
_OriPPPoESessionTableStatus_Object = MibTableColumn
oriPPPoESessionTableStatus = _OriPPPoESessionTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 20),
    _OriPPPoESessionTableStatus_Type()
)
oriPPPoESessionTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPPPoESessionTableStatus.setStatus("current")


class _OriPPPoESessionWANManualConnect_Type(Integer32):
    """Custom type oriPPPoESessionWANManualConnect based on Integer32"""
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


_OriPPPoESessionWANManualConnect_Type.__name__ = "Integer32"
_OriPPPoESessionWANManualConnect_Object = MibTableColumn
oriPPPoESessionWANManualConnect = _OriPPPoESessionWANManualConnect_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 21),
    _OriPPPoESessionWANManualConnect_Type()
)
oriPPPoESessionWANManualConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPPPoESessionWANManualConnect.setStatus("current")


class _OriPPPoESessionWANConnectionStatus_Type(Integer32):
    """Custom type oriPPPoESessionWANConnectionStatus based on Integer32"""
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
        *(("addingStack", 3),
          ("authFailed", 7),
          ("connectFailed", 6),
          ("down", 9),
          ("null", 1),
          ("stackAddError", 5),
          ("stackAdded", 4),
          ("start", 2),
          ("suspended", 10),
          ("unknown", 11),
          ("up", 8))
    )


_OriPPPoESessionWANConnectionStatus_Type.__name__ = "Integer32"
_OriPPPoESessionWANConnectionStatus_Object = MibTableColumn
oriPPPoESessionWANConnectionStatus = _OriPPPoESessionWANConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 4, 1, 22),
    _OriPPPoESessionWANConnectionStatus_Type()
)
oriPPPoESessionWANConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriPPPoESessionWANConnectionStatus.setStatus("current")
_OriPPPoEMACtoSessionTable_Object = MibTable
oriPPPoEMACtoSessionTable = _OriPPPoEMACtoSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 5)
)
if mibBuilder.loadTexts:
    oriPPPoEMACtoSessionTable.setStatus("current")
_OriPPPoEMACtoSessionTableEntry_Object = MibTableRow
oriPPPoEMACtoSessionTableEntry = _OriPPPoEMACtoSessionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 5, 1)
)
oriPPPoEMACtoSessionTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriPPPoEMACtoSessionTableIndex"),
)
if mibBuilder.loadTexts:
    oriPPPoEMACtoSessionTableEntry.setStatus("current")
_OriPPPoEMACtoSessionTableIndex_Type = Integer32
_OriPPPoEMACtoSessionTableIndex_Object = MibTableColumn
oriPPPoEMACtoSessionTableIndex = _OriPPPoEMACtoSessionTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 5, 1, 1),
    _OriPPPoEMACtoSessionTableIndex_Type()
)
oriPPPoEMACtoSessionTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriPPPoEMACtoSessionTableIndex.setStatus("current")
_OriPPPoEMACtoSessionTableMACAddress_Type = PhysAddress
_OriPPPoEMACtoSessionTableMACAddress_Object = MibTableColumn
oriPPPoEMACtoSessionTableMACAddress = _OriPPPoEMACtoSessionTableMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 5, 1, 2),
    _OriPPPoEMACtoSessionTableMACAddress_Type()
)
oriPPPoEMACtoSessionTableMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPPPoEMACtoSessionTableMACAddress.setStatus("current")
_OriPPPoEMACtoSessionTableISPName_Type = DisplayString
_OriPPPoEMACtoSessionTableISPName_Object = MibTableColumn
oriPPPoEMACtoSessionTableISPName = _OriPPPoEMACtoSessionTableISPName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 5, 1, 3),
    _OriPPPoEMACtoSessionTableISPName_Type()
)
oriPPPoEMACtoSessionTableISPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPPPoEMACtoSessionTableISPName.setStatus("current")


class _OriPPPoEMACtoSessionTableStatus_Type(Integer32):
    """Custom type oriPPPoEMACtoSessionTableStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriPPPoEMACtoSessionTableStatus_Type.__name__ = "Integer32"
_OriPPPoEMACtoSessionTableStatus_Object = MibTableColumn
oriPPPoEMACtoSessionTableStatus = _OriPPPoEMACtoSessionTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 22, 5, 1, 4),
    _OriPPPoEMACtoSessionTableStatus_Type()
)
oriPPPoEMACtoSessionTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriPPPoEMACtoSessionTableStatus.setStatus("current")
_OrinocoConfig_ObjectIdentity = ObjectIdentity
orinocoConfig = _OrinocoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 23)
)


class _OriConfigResetToDefaults_Type(Integer32):
    """Custom type oriConfigResetToDefaults based on Integer32"""
    defaultValue = 2

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
        *(("bridgeMode", 1),
          ("gatewayMode", 2),
          ("gatewayModeDHCPClient", 3),
          ("gatewayModePPPoE", 4))
    )


_OriConfigResetToDefaults_Type.__name__ = "Integer32"
_OriConfigResetToDefaults_Object = MibScalar
oriConfigResetToDefaults = _OriConfigResetToDefaults_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 23, 1),
    _OriConfigResetToDefaults_Type()
)
oriConfigResetToDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriConfigResetToDefaults.setStatus("current")
_OriConfigFileTable_Object = MibTable
oriConfigFileTable = _OriConfigFileTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 23, 2)
)
if mibBuilder.loadTexts:
    oriConfigFileTable.setStatus("current")
_OriConfigFileTableEntry_Object = MibTableRow
oriConfigFileTableEntry = _OriConfigFileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 23, 2, 1)
)
oriConfigFileTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriConfigFileTableIndex"),
)
if mibBuilder.loadTexts:
    oriConfigFileTableEntry.setStatus("current")
_OriConfigFileTableIndex_Type = Integer32
_OriConfigFileTableIndex_Object = MibTableColumn
oriConfigFileTableIndex = _OriConfigFileTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 23, 2, 1, 1),
    _OriConfigFileTableIndex_Type()
)
oriConfigFileTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriConfigFileTableIndex.setStatus("current")
_OriConfigFileName_Type = DisplayString
_OriConfigFileName_Object = MibTableColumn
oriConfigFileName = _OriConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 23, 2, 1, 2),
    _OriConfigFileName_Type()
)
oriConfigFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriConfigFileName.setStatus("current")


class _OriConfigFileStatus_Type(Integer32):
    """Custom type oriConfigFileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriConfigFileStatus_Type.__name__ = "Integer32"
_OriConfigFileStatus_Object = MibTableColumn
oriConfigFileStatus = _OriConfigFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 23, 2, 1, 3),
    _OriConfigFileStatus_Type()
)
oriConfigFileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriConfigFileStatus.setStatus("current")
_OriConfigSaveFile_Type = DisplayString
_OriConfigSaveFile_Object = MibScalar
oriConfigSaveFile = _OriConfigSaveFile_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 23, 3),
    _OriConfigSaveFile_Type()
)
oriConfigSaveFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriConfigSaveFile.setStatus("current")


class _OriConfigSaveKnownGood_Type(Integer32):
    """Custom type oriConfigSaveKnownGood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("saveKnownGood", 1)
    )


_OriConfigSaveKnownGood_Type.__name__ = "Integer32"
_OriConfigSaveKnownGood_Object = MibScalar
oriConfigSaveKnownGood = _OriConfigSaveKnownGood_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 23, 4),
    _OriConfigSaveKnownGood_Type()
)
oriConfigSaveKnownGood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriConfigSaveKnownGood.setStatus("current")
_OrinocoDNS_ObjectIdentity = ObjectIdentity
orinocoDNS = _OrinocoDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 24)
)


class _OriDNSRedirectStatus_Type(Integer32):
    """Custom type oriDNSRedirectStatus based on Integer32"""
    defaultValue = 1

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


_OriDNSRedirectStatus_Type.__name__ = "Integer32"
_OriDNSRedirectStatus_Object = MibScalar
oriDNSRedirectStatus = _OriDNSRedirectStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 24, 1),
    _OriDNSRedirectStatus_Type()
)
oriDNSRedirectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDNSRedirectStatus.setStatus("current")


class _OriDNSRedirectMaxResponseWaitTime_Type(Integer32):
    """Custom type oriDNSRedirectMaxResponseWaitTime based on Integer32"""
    defaultValue = 10


_OriDNSRedirectMaxResponseWaitTime_Object = MibScalar
oriDNSRedirectMaxResponseWaitTime = _OriDNSRedirectMaxResponseWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 24, 2),
    _OriDNSRedirectMaxResponseWaitTime_Type()
)
oriDNSRedirectMaxResponseWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDNSRedirectMaxResponseWaitTime.setStatus("current")
_OriDNSPrimaryDNSIPAddress_Type = IpAddress
_OriDNSPrimaryDNSIPAddress_Object = MibScalar
oriDNSPrimaryDNSIPAddress = _OriDNSPrimaryDNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 24, 3),
    _OriDNSPrimaryDNSIPAddress_Type()
)
oriDNSPrimaryDNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDNSPrimaryDNSIPAddress.setStatus("current")
_OriDNSSecondaryDNSIPAddress_Type = IpAddress
_OriDNSSecondaryDNSIPAddress_Object = MibScalar
oriDNSSecondaryDNSIPAddress = _OriDNSSecondaryDNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 24, 4),
    _OriDNSSecondaryDNSIPAddress_Type()
)
oriDNSSecondaryDNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDNSSecondaryDNSIPAddress.setStatus("current")
_OrinocoDNSClient_ObjectIdentity = ObjectIdentity
orinocoDNSClient = _OrinocoDNSClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 24, 5)
)


class _OriDNSClientStatus_Type(Integer32):
    """Custom type oriDNSClientStatus based on Integer32"""
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


_OriDNSClientStatus_Type.__name__ = "Integer32"
_OriDNSClientStatus_Object = MibScalar
oriDNSClientStatus = _OriDNSClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 24, 5, 1),
    _OriDNSClientStatus_Type()
)
oriDNSClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDNSClientStatus.setStatus("current")
_OriDNSClientPrimaryServerIPAddress_Type = IpAddress
_OriDNSClientPrimaryServerIPAddress_Object = MibScalar
oriDNSClientPrimaryServerIPAddress = _OriDNSClientPrimaryServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 24, 5, 2),
    _OriDNSClientPrimaryServerIPAddress_Type()
)
oriDNSClientPrimaryServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDNSClientPrimaryServerIPAddress.setStatus("current")
_OriDNSClientSecondaryServerIPAddress_Type = IpAddress
_OriDNSClientSecondaryServerIPAddress_Object = MibScalar
oriDNSClientSecondaryServerIPAddress = _OriDNSClientSecondaryServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 24, 5, 3),
    _OriDNSClientSecondaryServerIPAddress_Type()
)
oriDNSClientSecondaryServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDNSClientSecondaryServerIPAddress.setStatus("current")
_OriDNSClientDefaultDomainName_Type = DisplayString
_OriDNSClientDefaultDomainName_Object = MibScalar
oriDNSClientDefaultDomainName = _OriDNSClientDefaultDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 24, 5, 4),
    _OriDNSClientDefaultDomainName_Type()
)
oriDNSClientDefaultDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDNSClientDefaultDomainName.setStatus("current")
_OrinocoAOL_ObjectIdentity = ObjectIdentity
orinocoAOL = _OrinocoAOL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 25)
)


class _OriAOLNATALGStatus_Type(Integer32):
    """Custom type oriAOLNATALGStatus based on Integer32"""
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


_OriAOLNATALGStatus_Type.__name__ = "Integer32"
_OriAOLNATALGStatus_Object = MibScalar
oriAOLNATALGStatus = _OriAOLNATALGStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 25, 1),
    _OriAOLNATALGStatus_Type()
)
oriAOLNATALGStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriAOLNATALGStatus.setStatus("current")
_OrinocoNAT_ObjectIdentity = ObjectIdentity
orinocoNAT = _OrinocoNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26)
)


class _OriNATStatus_Type(ObjStatus):
    """Custom type oriNATStatus based on ObjStatus"""


_OriNATStatus_Object = MibScalar
oriNATStatus = _OriNATStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 1),
    _OriNATStatus_Type()
)
oriNATStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriNATStatus.setStatus("current")
_OriNATType_Type = Integer32
_OriNATType_Object = MibScalar
oriNATType = _OriNATType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 2),
    _OriNATType_Type()
)
oriNATType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriNATType.setStatus("current")


class _OriNATStaticBindStatus_Type(Integer32):
    """Custom type oriNATStaticBindStatus based on Integer32"""
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


_OriNATStaticBindStatus_Type.__name__ = "Integer32"
_OriNATStaticBindStatus_Object = MibScalar
oriNATStaticBindStatus = _OriNATStaticBindStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 3),
    _OriNATStaticBindStatus_Type()
)
oriNATStaticBindStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriNATStaticBindStatus.setStatus("current")
_OriNATPublicIPAddress_Type = IpAddress
_OriNATPublicIPAddress_Object = MibScalar
oriNATPublicIPAddress = _OriNATPublicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 4),
    _OriNATPublicIPAddress_Type()
)
oriNATPublicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriNATPublicIPAddress.setStatus("current")
_OriNATStaticIPBindTable_Object = MibTable
oriNATStaticIPBindTable = _OriNATStaticIPBindTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 5)
)
if mibBuilder.loadTexts:
    oriNATStaticIPBindTable.setStatus("current")
_OriNATStaticIPBindTableEntry_Object = MibTableRow
oriNATStaticIPBindTableEntry = _OriNATStaticIPBindTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 5, 1)
)
oriNATStaticIPBindTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriNATStaticIPBindTableIndex"),
)
if mibBuilder.loadTexts:
    oriNATStaticIPBindTableEntry.setStatus("current")
_OriNATStaticIPBindTableIndex_Type = Integer32
_OriNATStaticIPBindTableIndex_Object = MibTableColumn
oriNATStaticIPBindTableIndex = _OriNATStaticIPBindTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 5, 1, 1),
    _OriNATStaticIPBindTableIndex_Type()
)
oriNATStaticIPBindTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriNATStaticIPBindTableIndex.setStatus("current")
_OriNATStaticIPBindLocalAddress_Type = IpAddress
_OriNATStaticIPBindLocalAddress_Object = MibTableColumn
oriNATStaticIPBindLocalAddress = _OriNATStaticIPBindLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 5, 1, 2),
    _OriNATStaticIPBindLocalAddress_Type()
)
oriNATStaticIPBindLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriNATStaticIPBindLocalAddress.setStatus("current")
_OriNATStaticIPBindRemoteAddress_Type = IpAddress
_OriNATStaticIPBindRemoteAddress_Object = MibTableColumn
oriNATStaticIPBindRemoteAddress = _OriNATStaticIPBindRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 5, 1, 3),
    _OriNATStaticIPBindRemoteAddress_Type()
)
oriNATStaticIPBindRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriNATStaticIPBindRemoteAddress.setStatus("current")


class _OriNATStaticIPBindTableEntryStatus_Type(Integer32):
    """Custom type oriNATStaticIPBindTableEntryStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriNATStaticIPBindTableEntryStatus_Type.__name__ = "Integer32"
_OriNATStaticIPBindTableEntryStatus_Object = MibTableColumn
oriNATStaticIPBindTableEntryStatus = _OriNATStaticIPBindTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 5, 1, 4),
    _OriNATStaticIPBindTableEntryStatus_Type()
)
oriNATStaticIPBindTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriNATStaticIPBindTableEntryStatus.setStatus("current")
_OriNATStaticPortBindTable_Object = MibTable
oriNATStaticPortBindTable = _OriNATStaticPortBindTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 6)
)
if mibBuilder.loadTexts:
    oriNATStaticPortBindTable.setStatus("current")
_OriNATStaticPortBindTableEntry_Object = MibTableRow
oriNATStaticPortBindTableEntry = _OriNATStaticPortBindTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 6, 1)
)
oriNATStaticPortBindTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriNATStaticPortBindTableIndex"),
)
if mibBuilder.loadTexts:
    oriNATStaticPortBindTableEntry.setStatus("current")
_OriNATStaticPortBindTableIndex_Type = Integer32
_OriNATStaticPortBindTableIndex_Object = MibTableColumn
oriNATStaticPortBindTableIndex = _OriNATStaticPortBindTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 6, 1, 1),
    _OriNATStaticPortBindTableIndex_Type()
)
oriNATStaticPortBindTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriNATStaticPortBindTableIndex.setStatus("current")
_OriNATStaticPortBindLocalAddress_Type = IpAddress
_OriNATStaticPortBindLocalAddress_Object = MibTableColumn
oriNATStaticPortBindLocalAddress = _OriNATStaticPortBindLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 6, 1, 2),
    _OriNATStaticPortBindLocalAddress_Type()
)
oriNATStaticPortBindLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriNATStaticPortBindLocalAddress.setStatus("current")
_OriNATStaticPortBindStartPortNumber_Type = Integer32
_OriNATStaticPortBindStartPortNumber_Object = MibTableColumn
oriNATStaticPortBindStartPortNumber = _OriNATStaticPortBindStartPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 6, 1, 3),
    _OriNATStaticPortBindStartPortNumber_Type()
)
oriNATStaticPortBindStartPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriNATStaticPortBindStartPortNumber.setStatus("current")
_OriNATStaticPortBindEndPortNumber_Type = Integer32
_OriNATStaticPortBindEndPortNumber_Object = MibTableColumn
oriNATStaticPortBindEndPortNumber = _OriNATStaticPortBindEndPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 6, 1, 4),
    _OriNATStaticPortBindEndPortNumber_Type()
)
oriNATStaticPortBindEndPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriNATStaticPortBindEndPortNumber.setStatus("current")


class _OriNATStaticPortBindPortType_Type(Integer32):
    """Custom type oriNATStaticPortBindPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_OriNATStaticPortBindPortType_Type.__name__ = "Integer32"
_OriNATStaticPortBindPortType_Object = MibTableColumn
oriNATStaticPortBindPortType = _OriNATStaticPortBindPortType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 6, 1, 5),
    _OriNATStaticPortBindPortType_Type()
)
oriNATStaticPortBindPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriNATStaticPortBindPortType.setStatus("current")


class _OriNATStaticPortBindTableEntryStatus_Type(Integer32):
    """Custom type oriNATStaticPortBindTableEntryStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriNATStaticPortBindTableEntryStatus_Type.__name__ = "Integer32"
_OriNATStaticPortBindTableEntryStatus_Object = MibTableColumn
oriNATStaticPortBindTableEntryStatus = _OriNATStaticPortBindTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 26, 6, 1, 6),
    _OriNATStaticPortBindTableEntryStatus_Type()
)
oriNATStaticPortBindTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriNATStaticPortBindTableEntryStatus.setStatus("current")
_OrinocoSpectraLink_ObjectIdentity = ObjectIdentity
orinocoSpectraLink = _OrinocoSpectraLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 29)
)


class _OriSpectraLinkStatus_Type(ObjStatus):
    """Custom type oriSpectraLinkStatus based on ObjStatus"""


_OriSpectraLinkStatus_Object = MibScalar
oriSpectraLinkStatus = _OriSpectraLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 29, 1),
    _OriSpectraLinkStatus_Type()
)
oriSpectraLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSpectraLinkStatus.setStatus("current")


class _OriSpectraLinkLegacyDeviceSupport_Type(ObjStatus):
    """Custom type oriSpectraLinkLegacyDeviceSupport based on ObjStatus"""


_OriSpectraLinkLegacyDeviceSupport_Object = MibScalar
oriSpectraLinkLegacyDeviceSupport = _OriSpectraLinkLegacyDeviceSupport_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 29, 2),
    _OriSpectraLinkLegacyDeviceSupport_Type()
)
oriSpectraLinkLegacyDeviceSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSpectraLinkLegacyDeviceSupport.setStatus("current")
_OrinocoVLAN_ObjectIdentity = ObjectIdentity
orinocoVLAN = _OrinocoVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 30)
)


class _OriVLANStatus_Type(ObjStatus):
    """Custom type oriVLANStatus based on ObjStatus"""


_OriVLANStatus_Object = MibScalar
oriVLANStatus = _OriVLANStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 30, 1),
    _OriVLANStatus_Type()
)
oriVLANStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriVLANStatus.setStatus("current")


class _OriVLANMgmtIdentifier_Type(VlanId):
    """Custom type oriVLANMgmtIdentifier based on VlanId"""
    defaultValue = -1


_OriVLANMgmtIdentifier_Object = MibScalar
oriVLANMgmtIdentifier = _OriVLANMgmtIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 30, 2),
    _OriVLANMgmtIdentifier_Type()
)
oriVLANMgmtIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriVLANMgmtIdentifier.setStatus("current")
_OriVLANIDTable_Object = MibTable
oriVLANIDTable = _OriVLANIDTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 30, 3)
)
if mibBuilder.loadTexts:
    oriVLANIDTable.setStatus("deprecated")
_OriVLANIDTableEntry_Object = MibTableRow
oriVLANIDTableEntry = _OriVLANIDTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 30, 3, 1)
)
oriVLANIDTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriVLANIDTableIndex"),
)
if mibBuilder.loadTexts:
    oriVLANIDTableEntry.setStatus("deprecated")
_OriVLANIDTableIndex_Type = Integer32
_OriVLANIDTableIndex_Object = MibTableColumn
oriVLANIDTableIndex = _OriVLANIDTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 30, 3, 1, 1),
    _OriVLANIDTableIndex_Type()
)
oriVLANIDTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriVLANIDTableIndex.setStatus("deprecated")


class _OriVLANIDTableIdentifier_Type(VlanId):
    """Custom type oriVLANIDTableIdentifier based on VlanId"""
    defaultValue = 0


_OriVLANIDTableIdentifier_Object = MibTableColumn
oriVLANIDTableIdentifier = _OriVLANIDTableIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 30, 3, 1, 2),
    _OriVLANIDTableIdentifier_Type()
)
oriVLANIDTableIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriVLANIDTableIdentifier.setStatus("deprecated")
_OrinocoDMZ_ObjectIdentity = ObjectIdentity
orinocoDMZ = _OrinocoDMZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 31)
)
_OriDMZHostTable_Object = MibTable
oriDMZHostTable = _OriDMZHostTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 31, 1)
)
if mibBuilder.loadTexts:
    oriDMZHostTable.setStatus("current")
_OriDMZHostTableEntry_Object = MibTableRow
oriDMZHostTableEntry = _OriDMZHostTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 31, 1, 1)
)
oriDMZHostTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriDMZHostTableIndex"),
)
if mibBuilder.loadTexts:
    oriDMZHostTableEntry.setStatus("current")
_OriDMZHostTableIndex_Type = Integer32
_OriDMZHostTableIndex_Object = MibTableColumn
oriDMZHostTableIndex = _OriDMZHostTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 31, 1, 1, 1),
    _OriDMZHostTableIndex_Type()
)
oriDMZHostTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriDMZHostTableIndex.setStatus("current")
_OriDMZHostTableHostIP_Type = IpAddress
_OriDMZHostTableHostIP_Object = MibTableColumn
oriDMZHostTableHostIP = _OriDMZHostTableHostIP_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 31, 1, 1, 2),
    _OriDMZHostTableHostIP_Type()
)
oriDMZHostTableHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDMZHostTableHostIP.setStatus("current")
_OriDMZHostTableComment_Type = DisplayString
_OriDMZHostTableComment_Object = MibTableColumn
oriDMZHostTableComment = _OriDMZHostTableComment_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 31, 1, 1, 3),
    _OriDMZHostTableComment_Type()
)
oriDMZHostTableComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDMZHostTableComment.setStatus("current")


class _OriDMZHostTableEntryStatus_Type(Integer32):
    """Custom type oriDMZHostTableEntryStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_OriDMZHostTableEntryStatus_Type.__name__ = "Integer32"
_OriDMZHostTableEntryStatus_Object = MibTableColumn
oriDMZHostTableEntryStatus = _OriDMZHostTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 31, 1, 1, 4),
    _OriDMZHostTableEntryStatus_Type()
)
oriDMZHostTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriDMZHostTableEntryStatus.setStatus("current")
_OrinocoOEM_ObjectIdentity = ObjectIdentity
orinocoOEM = _OrinocoOEM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 32)
)
_OriOEMName_Type = DisplayString
_OriOEMName_Object = MibScalar
oriOEMName = _OriOEMName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 32, 1),
    _OriOEMName_Type()
)
oriOEMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriOEMName.setStatus("current")
_OriOEMHomeUrl_Type = DisplayString
_OriOEMHomeUrl_Object = MibScalar
oriOEMHomeUrl = _OriOEMHomeUrl_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 32, 2),
    _OriOEMHomeUrl_Type()
)
oriOEMHomeUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriOEMHomeUrl.setStatus("current")
_OriOEMProductName_Type = DisplayString
_OriOEMProductName_Object = MibScalar
oriOEMProductName = _OriOEMProductName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 32, 3),
    _OriOEMProductName_Type()
)
oriOEMProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriOEMProductName.setStatus("current")
_OriOEMProductModel_Type = DisplayString
_OriOEMProductModel_Object = MibScalar
oriOEMProductModel = _OriOEMProductModel_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 32, 4),
    _OriOEMProductModel_Type()
)
oriOEMProductModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriOEMProductModel.setStatus("current")
_OriOEMLogoImageFile_Type = DisplayString
_OriOEMLogoImageFile_Object = MibScalar
oriOEMLogoImageFile = _OriOEMLogoImageFile_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 32, 5),
    _OriOEMLogoImageFile_Type()
)
oriOEMLogoImageFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriOEMLogoImageFile.setStatus("current")
_OriOEMNoNavLogoImageFile_Type = DisplayString
_OriOEMNoNavLogoImageFile_Object = MibScalar
oriOEMNoNavLogoImageFile = _OriOEMNoNavLogoImageFile_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 32, 6),
    _OriOEMNoNavLogoImageFile_Type()
)
oriOEMNoNavLogoImageFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriOEMNoNavLogoImageFile.setStatus("current")
_OrinocoStationStatistics_ObjectIdentity = ObjectIdentity
orinocoStationStatistics = _OrinocoStationStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33)
)
_OriStationStatTable_Object = MibTable
oriStationStatTable = _OriStationStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1)
)
if mibBuilder.loadTexts:
    oriStationStatTable.setStatus("current")
_OriStationStatTableEntry_Object = MibTableRow
oriStationStatTableEntry = _OriStationStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1)
)
oriStationStatTableEntry.setIndexNames(
    (0, "ORiNOCO-MIB", "oriStationStatTableIndex"),
)
if mibBuilder.loadTexts:
    oriStationStatTableEntry.setStatus("current")


class _OriStationStatTableIndex_Type(Integer32):
    """Custom type oriStationStatTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_OriStationStatTableIndex_Type.__name__ = "Integer32"
_OriStationStatTableIndex_Object = MibTableColumn
oriStationStatTableIndex = _OriStationStatTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 1),
    _OriStationStatTableIndex_Type()
)
oriStationStatTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableIndex.setStatus("current")
_OriStationStatTableMACAddress_Type = MacAddress
_OriStationStatTableMACAddress_Object = MibTableColumn
oriStationStatTableMACAddress = _OriStationStatTableMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 2),
    _OriStationStatTableMACAddress_Type()
)
oriStationStatTableMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableMACAddress.setStatus("current")
_OriStationStatTableIPAddress_Type = IpAddress
_OriStationStatTableIPAddress_Object = MibTableColumn
oriStationStatTableIPAddress = _OriStationStatTableIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 3),
    _OriStationStatTableIPAddress_Type()
)
oriStationStatTableIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableIPAddress.setStatus("current")
_OriStationStatTableInterface_Type = Integer32
_OriStationStatTableInterface_Object = MibTableColumn
oriStationStatTableInterface = _OriStationStatTableInterface_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 4),
    _OriStationStatTableInterface_Type()
)
oriStationStatTableInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableInterface.setStatus("current")
_OriStationStatTableName_Type = DisplayString
_OriStationStatTableName_Object = MibTableColumn
oriStationStatTableName = _OriStationStatTableName_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 5),
    _OriStationStatTableName_Type()
)
oriStationStatTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableName.setStatus("current")


class _OriStationStatTableType_Type(Integer32):
    """Custom type oriStationStatTableType based on Integer32"""
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
        *(("norc", 5),
          ("sta", 1),
          ("wds", 2),
          ("worpBase", 3),
          ("worpSatellite", 4))
    )


_OriStationStatTableType_Type.__name__ = "Integer32"
_OriStationStatTableType_Object = MibTableColumn
oriStationStatTableType = _OriStationStatTableType_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 6),
    _OriStationStatTableType_Type()
)
oriStationStatTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableType.setStatus("current")


class _OriStationStatTableMACProtocol_Type(Integer32):
    """Custom type oriStationStatTableMACProtocol based on Integer32"""
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
        *(("ieee802dot11", 1),
          ("ieee802dot11a", 2),
          ("ieee802dot11b", 3),
          ("ieee802dot11g", 5),
          ("worp", 4))
    )


_OriStationStatTableMACProtocol_Type.__name__ = "Integer32"
_OriStationStatTableMACProtocol_Object = MibTableColumn
oriStationStatTableMACProtocol = _OriStationStatTableMACProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 7),
    _OriStationStatTableMACProtocol_Type()
)
oriStationStatTableMACProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableMACProtocol.setStatus("current")


class _OriStationStatTableAdminStatus_Type(Integer32):
    """Custom type oriStationStatTableAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_OriStationStatTableAdminStatus_Type.__name__ = "Integer32"
_OriStationStatTableAdminStatus_Object = MibTableColumn
oriStationStatTableAdminStatus = _OriStationStatTableAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 8),
    _OriStationStatTableAdminStatus_Type()
)
oriStationStatTableAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableAdminStatus.setStatus("current")


class _OriStationStatTableOperStatus_Type(Integer32):
    """Custom type oriStationStatTableOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_OriStationStatTableOperStatus_Type.__name__ = "Integer32"
_OriStationStatTableOperStatus_Object = MibTableColumn
oriStationStatTableOperStatus = _OriStationStatTableOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 9),
    _OriStationStatTableOperStatus_Type()
)
oriStationStatTableOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableOperStatus.setStatus("current")
_OriStationStatTableLastChange_Type = TimeTicks
_OriStationStatTableLastChange_Object = MibTableColumn
oriStationStatTableLastChange = _OriStationStatTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 10),
    _OriStationStatTableLastChange_Type()
)
oriStationStatTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableLastChange.setStatus("current")


class _OriStationStatTableLastState_Type(Integer32):
    """Custom type oriStationStatTableLastState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("aborded", 6),
          ("authenticating", 3),
          ("linktest", 8),
          ("registered", 4),
          ("registering", 2),
          ("rejected", 7),
          ("timeout", 5),
          ("unknown", 1))
    )


_OriStationStatTableLastState_Type.__name__ = "Integer32"
_OriStationStatTableLastState_Object = MibTableColumn
oriStationStatTableLastState = _OriStationStatTableLastState_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 11),
    _OriStationStatTableLastState_Type()
)
oriStationStatTableLastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableLastState.setStatus("current")
_OriStationStatTableInOctets_Type = Counter32
_OriStationStatTableInOctets_Object = MibTableColumn
oriStationStatTableInOctets = _OriStationStatTableInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 12),
    _OriStationStatTableInOctets_Type()
)
oriStationStatTableInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableInOctets.setStatus("current")
_OriStationStatTableInUcastPkts_Type = Counter32
_OriStationStatTableInUcastPkts_Object = MibTableColumn
oriStationStatTableInUcastPkts = _OriStationStatTableInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 13),
    _OriStationStatTableInUcastPkts_Type()
)
oriStationStatTableInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableInUcastPkts.setStatus("current")
_OriStationStatTableInNUcastPkts_Type = Counter32
_OriStationStatTableInNUcastPkts_Object = MibTableColumn
oriStationStatTableInNUcastPkts = _OriStationStatTableInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 14),
    _OriStationStatTableInNUcastPkts_Type()
)
oriStationStatTableInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableInNUcastPkts.setStatus("current")
_OriStationStatTableInDiscards_Type = Counter32
_OriStationStatTableInDiscards_Object = MibTableColumn
oriStationStatTableInDiscards = _OriStationStatTableInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 15),
    _OriStationStatTableInDiscards_Type()
)
oriStationStatTableInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableInDiscards.setStatus("current")
_OriStationStatTableOutOctets_Type = Counter32
_OriStationStatTableOutOctets_Object = MibTableColumn
oriStationStatTableOutOctets = _OriStationStatTableOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 16),
    _OriStationStatTableOutOctets_Type()
)
oriStationStatTableOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableOutOctets.setStatus("current")
_OriStationStatTableOutUcastPkts_Type = Counter32
_OriStationStatTableOutUcastPkts_Object = MibTableColumn
oriStationStatTableOutUcastPkts = _OriStationStatTableOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 17),
    _OriStationStatTableOutUcastPkts_Type()
)
oriStationStatTableOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableOutUcastPkts.setStatus("current")
_OriStationStatTableOutNUcastPkts_Type = Counter32
_OriStationStatTableOutNUcastPkts_Object = MibTableColumn
oriStationStatTableOutNUcastPkts = _OriStationStatTableOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 18),
    _OriStationStatTableOutNUcastPkts_Type()
)
oriStationStatTableOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableOutNUcastPkts.setStatus("current")
_OriStationStatTableOutDiscards_Type = Counter32
_OriStationStatTableOutDiscards_Object = MibTableColumn
oriStationStatTableOutDiscards = _OriStationStatTableOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 19),
    _OriStationStatTableOutDiscards_Type()
)
oriStationStatTableOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableOutDiscards.setStatus("current")


class _OriStationStatTableInSignal_Type(Integer32):
    """Custom type oriStationStatTableInSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_OriStationStatTableInSignal_Type.__name__ = "Integer32"
_OriStationStatTableInSignal_Object = MibTableColumn
oriStationStatTableInSignal = _OriStationStatTableInSignal_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 20),
    _OriStationStatTableInSignal_Type()
)
oriStationStatTableInSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableInSignal.setStatus("current")


class _OriStationStatTableInNoise_Type(Integer32):
    """Custom type oriStationStatTableInNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_OriStationStatTableInNoise_Type.__name__ = "Integer32"
_OriStationStatTableInNoise_Object = MibTableColumn
oriStationStatTableInNoise = _OriStationStatTableInNoise_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 21),
    _OriStationStatTableInNoise_Type()
)
oriStationStatTableInNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableInNoise.setStatus("current")


class _OriStationStatTableRemoteSignal_Type(Integer32):
    """Custom type oriStationStatTableRemoteSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_OriStationStatTableRemoteSignal_Type.__name__ = "Integer32"
_OriStationStatTableRemoteSignal_Object = MibTableColumn
oriStationStatTableRemoteSignal = _OriStationStatTableRemoteSignal_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 22),
    _OriStationStatTableRemoteSignal_Type()
)
oriStationStatTableRemoteSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableRemoteSignal.setStatus("current")


class _OriStationStatTableRemoteNoise_Type(Integer32):
    """Custom type oriStationStatTableRemoteNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-102, -10),
    )


_OriStationStatTableRemoteNoise_Type.__name__ = "Integer32"
_OriStationStatTableRemoteNoise_Object = MibTableColumn
oriStationStatTableRemoteNoise = _OriStationStatTableRemoteNoise_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 23),
    _OriStationStatTableRemoteNoise_Type()
)
oriStationStatTableRemoteNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableRemoteNoise.setStatus("current")
_OriStationStatTableLastInPktTime_Type = TimeTicks
_OriStationStatTableLastInPktTime_Object = MibTableColumn
oriStationStatTableLastInPktTime = _OriStationStatTableLastInPktTime_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 1, 1, 24),
    _OriStationStatTableLastInPktTime_Type()
)
oriStationStatTableLastInPktTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatTableLastInPktTime.setStatus("current")


class _OriStationStatStatus_Type(Integer32):
    """Custom type oriStationStatStatus based on Integer32"""
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


_OriStationStatStatus_Type.__name__ = "Integer32"
_OriStationStatStatus_Object = MibScalar
oriStationStatStatus = _OriStationStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 2),
    _OriStationStatStatus_Type()
)
oriStationStatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriStationStatStatus.setStatus("current")
_OriStationStatNumberOfClients_Type = Counter32
_OriStationStatNumberOfClients_Object = MibScalar
oriStationStatNumberOfClients = _OriStationStatNumberOfClients_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 33, 3),
    _OriStationStatNumberOfClients_Type()
)
oriStationStatNumberOfClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriStationStatNumberOfClients.setStatus("current")
_OrinocoSNTP_ObjectIdentity = ObjectIdentity
orinocoSNTP = _OrinocoSNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 34)
)


class _OriSNTPStatus_Type(Integer32):
    """Custom type oriSNTPStatus based on Integer32"""
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


_OriSNTPStatus_Type.__name__ = "Integer32"
_OriSNTPStatus_Object = MibScalar
oriSNTPStatus = _OriSNTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 34, 1),
    _OriSNTPStatus_Type()
)
oriSNTPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNTPStatus.setStatus("current")
_OriSNTPPrimaryServerNameOrIPAddress_Type = DisplayString
_OriSNTPPrimaryServerNameOrIPAddress_Object = MibScalar
oriSNTPPrimaryServerNameOrIPAddress = _OriSNTPPrimaryServerNameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 34, 2),
    _OriSNTPPrimaryServerNameOrIPAddress_Type()
)
oriSNTPPrimaryServerNameOrIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNTPPrimaryServerNameOrIPAddress.setStatus("current")
_OriSNTPSecondaryServerNameOrIPAddress_Type = DisplayString
_OriSNTPSecondaryServerNameOrIPAddress_Object = MibScalar
oriSNTPSecondaryServerNameOrIPAddress = _OriSNTPSecondaryServerNameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 34, 3),
    _OriSNTPSecondaryServerNameOrIPAddress_Type()
)
oriSNTPSecondaryServerNameOrIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNTPSecondaryServerNameOrIPAddress.setStatus("current")


class _OriSNTPTimeZone_Type(Integer32):
    """Custom type oriSNTPTimeZone based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41)
        )
    )
    namedValues = NamedValues(
        *(("afghanistan", 26),
          ("alaska", 4),
          ("arabian", 25),
          ("arizona", 7),
          ("atlantic-canada", 12),
          ("australia-ct", 36),
          ("australia-et", 37),
          ("australia-wt", 32),
          ("azores", 18),
          ("bangkok", 31),
          ("bangladesh", 29),
          ("beijing", 34),
          ("brasilia", 15),
          ("buenos-aires", 16),
          ("burma", 30),
          ("cairo", 22),
          ("central-pacific", 38),
          ("central-us", 8),
          ("dateline", 1),
          ("eastern-europe", 21),
          ("eastern-us", 10),
          ("hawaii", 3),
          ("hong-kong", 33),
          ("india", 28),
          ("indiana", 11),
          ("iran", 24),
          ("japan-korea", 35),
          ("london", 19),
          ("mexico-city", 9),
          ("mid-atlantic", 17),
          ("mountain-us", 6),
          ("new-zealand", 39),
          ("newfoundland", 14),
          ("pacific-us", 5),
          ("pakistan", 27),
          ("russia-iraq", 23),
          ("samoa", 2),
          ("santiago", 13),
          ("tonga", 40),
          ("western-europe", 20),
          ("western-samoa", 41))
    )


_OriSNTPTimeZone_Type.__name__ = "Integer32"
_OriSNTPTimeZone_Object = MibScalar
oriSNTPTimeZone = _OriSNTPTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 34, 4),
    _OriSNTPTimeZone_Type()
)
oriSNTPTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNTPTimeZone.setStatus("current")
_OriSNTPDateAndTime_Type = DisplayString
_OriSNTPDateAndTime_Object = MibScalar
oriSNTPDateAndTime = _OriSNTPDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 34, 5),
    _OriSNTPDateAndTime_Type()
)
oriSNTPDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriSNTPDateAndTime.setStatus("current")


class _OriSNTPDayLightSavingTime_Type(Integer32):
    """Custom type oriSNTPDayLightSavingTime based on Integer32"""
    defaultValue = 3

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
        *(("minus-one", 4),
          ("minus-two", 5),
          ("plus-one", 2),
          ("plus-two", 1),
          ("unchanged", 3))
    )


_OriSNTPDayLightSavingTime_Type.__name__ = "Integer32"
_OriSNTPDayLightSavingTime_Object = MibScalar
oriSNTPDayLightSavingTime = _OriSNTPDayLightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 34, 6),
    _OriSNTPDayLightSavingTime_Type()
)
oriSNTPDayLightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNTPDayLightSavingTime.setStatus("current")
_OriSNTPYear_Type = Integer32
_OriSNTPYear_Object = MibScalar
oriSNTPYear = _OriSNTPYear_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 34, 7),
    _OriSNTPYear_Type()
)
oriSNTPYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNTPYear.setStatus("current")


class _OriSNTPMonth_Type(Integer32):
    """Custom type oriSNTPMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_OriSNTPMonth_Type.__name__ = "Integer32"
_OriSNTPMonth_Object = MibScalar
oriSNTPMonth = _OriSNTPMonth_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 34, 8),
    _OriSNTPMonth_Type()
)
oriSNTPMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNTPMonth.setStatus("current")


class _OriSNTPDay_Type(Integer32):
    """Custom type oriSNTPDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_OriSNTPDay_Type.__name__ = "Integer32"
_OriSNTPDay_Object = MibScalar
oriSNTPDay = _OriSNTPDay_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 34, 9),
    _OriSNTPDay_Type()
)
oriSNTPDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNTPDay.setStatus("current")


class _OriSNTPHour_Type(Integer32):
    """Custom type oriSNTPHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_OriSNTPHour_Type.__name__ = "Integer32"
_OriSNTPHour_Object = MibScalar
oriSNTPHour = _OriSNTPHour_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 34, 10),
    _OriSNTPHour_Type()
)
oriSNTPHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNTPHour.setStatus("current")


class _OriSNTPMinutes_Type(Integer32):
    """Custom type oriSNTPMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_OriSNTPMinutes_Type.__name__ = "Integer32"
_OriSNTPMinutes_Object = MibScalar
oriSNTPMinutes = _OriSNTPMinutes_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 34, 11),
    _OriSNTPMinutes_Type()
)
oriSNTPMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNTPMinutes.setStatus("current")


class _OriSNTPSeconds_Type(Integer32):
    """Custom type oriSNTPSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_OriSNTPSeconds_Type.__name__ = "Integer32"
_OriSNTPSeconds_Object = MibScalar
oriSNTPSeconds = _OriSNTPSeconds_Object(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 34, 12),
    _OriSNTPSeconds_Type()
)
oriSNTPSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriSNTPSeconds.setStatus("current")
_OrinocoNotifications_ObjectIdentity = ObjectIdentity
orinocoNotifications = _OrinocoNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 2)
)
_OrinocoConformance_ObjectIdentity = ObjectIdentity
orinocoConformance = _OrinocoConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 3)
)
_OrinocoGroups_ObjectIdentity = ObjectIdentity
orinocoGroups = _OrinocoGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 3, 1)
)
_OrinocoCompliances_ObjectIdentity = ObjectIdentity
orinocoCompliances = _OrinocoCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 3, 2)
)
_OrinocoProducts_ObjectIdentity = ObjectIdentity
orinocoProducts = _OrinocoProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 4)
)
_Ap1000_ObjectIdentity = ObjectIdentity
ap1000 = _Ap1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 4, 1)
)
_Rg1000_ObjectIdentity = ObjectIdentity
rg1000 = _Rg1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 4, 2)
)
_As1000_ObjectIdentity = ObjectIdentity
as1000 = _As1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 4, 3)
)
_As2000_ObjectIdentity = ObjectIdentity
as2000 = _As2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 4, 4)
)
_Ap500_ObjectIdentity = ObjectIdentity
ap500 = _Ap500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 4, 5)
)
_Ap2000_ObjectIdentity = ObjectIdentity
ap2000 = _Ap2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 4, 6)
)
_Bg2000_ObjectIdentity = ObjectIdentity
bg2000 = _Bg2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 4, 7)
)
_Rg1100_ObjectIdentity = ObjectIdentity
rg1100 = _Rg1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 4, 8)
)
_Tmp11_ObjectIdentity = ObjectIdentity
tmp11 = _Tmp11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 4, 9)
)
_Ap600_ObjectIdentity = ObjectIdentity
ap600 = _Ap600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 4, 10)
)
_Ap2500_ObjectIdentity = ObjectIdentity
ap2500 = _Ap2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 4, 11)
)
_Ap4000_ObjectIdentity = ObjectIdentity
ap4000 = _Ap4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 4, 12)
)
_Ap700_ObjectIdentity = ObjectIdentity
ap700 = _Ap700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11898, 2, 4, 13)
)

# Managed Objects groups


# Notification objects

oriTrapDNSIPNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 2, 0, 3)
)
oriTrapDNSIPNotConfigured.setObjects(
      *(("ORiNOCO-MIB", "oriGenericTrapVariable"),
        ("ORiNOCO-MIB", "oriTrapVarMACAddress"))
)
if mibBuilder.loadTexts:
    oriTrapDNSIPNotConfigured.setStatus(
        "current"
    )

oriTrapRADIUSAuthenticationNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 2, 0, 5)
)
oriTrapRADIUSAuthenticationNotConfigured.setObjects(
      *(("ORiNOCO-MIB", "oriGenericTrapVariable"),
        ("ORiNOCO-MIB", "oriTrapVarMACAddress"))
)
if mibBuilder.loadTexts:
    oriTrapRADIUSAuthenticationNotConfigured.setStatus(
        "current"
    )

oriTrapRADIUSAccountingNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 2, 0, 6)
)
oriTrapRADIUSAccountingNotConfigured.setObjects(
      *(("ORiNOCO-MIB", "oriGenericTrapVariable"),
        ("ORiNOCO-MIB", "oriTrapVarMACAddress"))
)
if mibBuilder.loadTexts:
    oriTrapRADIUSAccountingNotConfigured.setStatus(
        "current"
    )

oriTrapDuplicateIPAddressEncountered = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 2, 0, 7)
)
oriTrapDuplicateIPAddressEncountered.setObjects(
      *(("ORiNOCO-MIB", "oriGenericTrapVariable"),
        ("ORiNOCO-MIB", "oriTrapVarMACAddress"))
)
if mibBuilder.loadTexts:
    oriTrapDuplicateIPAddressEncountered.setStatus(
        "current"
    )

oriTrapDHCPRelayServerTableNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 2, 0, 8)
)
if mibBuilder.loadTexts:
    oriTrapDHCPRelayServerTableNotConfigured.setStatus(
        "current"
    )

oriTrapWORPIfNetworkSecretNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 2, 0, 9)
)
if mibBuilder.loadTexts:
    oriTrapWORPIfNetworkSecretNotConfigured.setStatus(
        "current"
    )

oriTrapVLANIDInvalidConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 2, 0, 10)
)
oriTrapVLANIDInvalidConfiguration.setObjects(
      *(("ORiNOCO-MIB", "oriGenericTrapVariable"),
        ("ORiNOCO-MIB", "oriWirelessIfNetworkName"),
        ("ORiNOCO-MIB", "oriVLANIDTableIdentifier"))
)
if mibBuilder.loadTexts:
    oriTrapVLANIDInvalidConfiguration.setStatus(
        "current"
    )

oriTrapAutoConfigFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 2, 0, 11)
)
oriTrapAutoConfigFailure.setObjects(
      *(("ORiNOCO-MIB", "oriGenericTrapVariable"),
        ("ORiNOCO-MIB", "oriTFTPAutoConfigFilename"),
        ("ORiNOCO-MIB", "oriTFTPAutoConfigServerIPAddress"))
)
if mibBuilder.loadTexts:
    oriTrapAutoConfigFailure.setStatus(
        "current"
    )

oriTrapBatchExecFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 2, 0, 12)
)
oriTrapBatchExecFailure.setObjects(
      *(("ORiNOCO-MIB", "oriGenericTrapVariable"),
        ("ORiNOCO-MIB", "oriTrapVarBatchCLIFilename"),
        ("ORiNOCO-MIB", "oriTrapVarBatchCLILineNumber"),
        ("ORiNOCO-MIB", "oriTrapVarBatchCLIMessage"))
)
if mibBuilder.loadTexts:
    oriTrapBatchExecFailure.setStatus(
        "current"
    )

oriTrapBatchFileExecStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 2, 0, 13)
)
oriTrapBatchFileExecStart.setObjects(
      *(("ORiNOCO-MIB", "oriGenericTrapVariable"),
        ("ORiNOCO-MIB", "oriTrapVarBatchCLIFilename"))
)
if mibBuilder.loadTexts:
    oriTrapBatchFileExecStart.setStatus(
        "current"
    )

oriTrapBatchFileExecEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 2, 0, 14)
)
oriTrapBatchFileExecEnd.setObjects(
      *(("ORiNOCO-MIB", "oriGenericTrapVariable"),
        ("ORiNOCO-MIB", "oriTrapVarBatchCLIFilename"),
        ("ORiNOCO-MIB", "oriTrapVarBatchCLIMessage"))
)
if mibBuilder.loadTexts:
    oriTrapBatchFileExecEnd.setStatus(
        "current"
    )

oriTrapInvalidEncryptionKey = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 3, 0, 1)
)
oriTrapInvalidEncryptionKey.setObjects(
    ("ORiNOCO-MIB", "oriTrapVarUnauthorizedClientMACAddress")
)
if mibBuilder.loadTexts:
    oriTrapInvalidEncryptionKey.setStatus(
        "current"
    )

oriTrapAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 3, 0, 2)
)
oriTrapAuthenticationFailure.setObjects(
      *(("ORiNOCO-MIB", "oriTrapVarUnauthorizedClientMACAddress"),
        ("ORiNOCO-MIB", "oriTrapVarFailedAuthenticationType"))
)
if mibBuilder.loadTexts:
    oriTrapAuthenticationFailure.setStatus(
        "current"
    )

oriTrapUnauthorizedManagerDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 3, 0, 3)
)
oriTrapUnauthorizedManagerDetected.setObjects(
      *(("ORiNOCO-MIB", "oriTrapVarUnauthorizedManagerIPaddress"),
        ("ORiNOCO-MIB", "oriTrapVarUnAuthorizedManagerCount"))
)
if mibBuilder.loadTexts:
    oriTrapUnauthorizedManagerDetected.setStatus(
        "current"
    )

oriTrapRADScanComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 3, 0, 4)
)
oriTrapRADScanComplete.setObjects(
    ("ORiNOCO-MIB", "oriGenericTrapVariable")
)
if mibBuilder.loadTexts:
    oriTrapRADScanComplete.setStatus(
        "current"
    )

oriTrapRADScanResults = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 3, 0, 5)
)
oriTrapRADScanResults.setObjects(
    ("ORiNOCO-MIB", "oriGenericTrapVariable")
)
if mibBuilder.loadTexts:
    oriTrapRADScanResults.setStatus(
        "current"
    )

oriTrapRogueScanStationDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 3, 0, 6)
)
oriTrapRogueScanStationDetected.setObjects(
    ("ORiNOCO-MIB", "oriGenericTrapVariable")
)
if mibBuilder.loadTexts:
    oriTrapRogueScanStationDetected.setStatus(
        "current"
    )

oriTrapRogueScanCycleComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 3, 0, 7)
)
oriTrapRogueScanCycleComplete.setObjects(
    ("ORiNOCO-MIB", "oriGenericTrapVariable")
)
if mibBuilder.loadTexts:
    oriTrapRogueScanCycleComplete.setStatus(
        "current"
    )

oriTrapWLCNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 4, 0, 1)
)
oriTrapWLCNotPresent.setObjects(
    ("ORiNOCO-MIB", "oriTrapVarWirelessCard")
)
if mibBuilder.loadTexts:
    oriTrapWLCNotPresent.setStatus(
        "current"
    )

oriTrapWLCFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 4, 0, 2)
)
oriTrapWLCFailure.setObjects(
    ("ORiNOCO-MIB", "oriTrapVarWirelessCard")
)
if mibBuilder.loadTexts:
    oriTrapWLCFailure.setStatus(
        "current"
    )

oriTrapWLCRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 4, 0, 3)
)
oriTrapWLCRemoval.setObjects(
    ("ORiNOCO-MIB", "oriTrapVarWirelessCard")
)
if mibBuilder.loadTexts:
    oriTrapWLCRemoval.setStatus(
        "current"
    )

oriTrapWLCIncompatibleFirmware = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 4, 0, 4)
)
oriTrapWLCIncompatibleFirmware.setObjects(
    ("ORiNOCO-MIB", "oriTrapVarWirelessCard")
)
if mibBuilder.loadTexts:
    oriTrapWLCIncompatibleFirmware.setStatus(
        "current"
    )

oriTrapWLCVoltageDiscrepancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 4, 0, 5)
)
oriTrapWLCVoltageDiscrepancy.setObjects(
    ("ORiNOCO-MIB", "oriTrapVarWirelessCard")
)
if mibBuilder.loadTexts:
    oriTrapWLCVoltageDiscrepancy.setStatus(
        "current"
    )

oriTrapWLCIncompatibleVendor = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 4, 0, 6)
)
oriTrapWLCIncompatibleVendor.setObjects(
    ("ORiNOCO-MIB", "oriTrapVarWirelessCard")
)
if mibBuilder.loadTexts:
    oriTrapWLCIncompatibleVendor.setStatus(
        "current"
    )

oriTrapWLCFirmwareDownloadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 4, 0, 7)
)
oriTrapWLCFirmwareDownloadFailure.setObjects(
    ("ORiNOCO-MIB", "oriTrapVarWirelessCard")
)
if mibBuilder.loadTexts:
    oriTrapWLCFirmwareDownloadFailure.setStatus(
        "current"
    )

oriTrapWLCFirmwareFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 4, 0, 8)
)
oriTrapWLCFirmwareFailure.setObjects(
      *(("ORiNOCO-MIB", "oriTrapVarWirelessCard"),
        ("ORiNOCO-MIB", "oriGenericTrapVariable"))
)
if mibBuilder.loadTexts:
    oriTrapWLCFirmwareFailure.setStatus(
        "current"
    )

oriTrapWLCRadarInterferenceDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 4, 0, 9)
)
oriTrapWLCRadarInterferenceDetected.setObjects(
      *(("ORiNOCO-MIB", "oriTrapVarWirelessCard"),
        ("ORiNOCO-MIB", "oriGenericTrapVariable"))
)
if mibBuilder.loadTexts:
    oriTrapWLCRadarInterferenceDetected.setStatus(
        "current"
    )

oriTrapUnrecoverableSoftwareErrorDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 1)
)
oriTrapUnrecoverableSoftwareErrorDetected.setObjects(
      *(("ORiNOCO-MIB", "oriGenericTrapVariable"),
        ("ORiNOCO-MIB", "oriTrapVarMACAddress"),
        ("ORiNOCO-MIB", "oriTrapVarTaskSuspended"))
)
if mibBuilder.loadTexts:
    oriTrapUnrecoverableSoftwareErrorDetected.setStatus(
        "current"
    )

oriTrapRADIUSServerNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 2)
)
oriTrapRADIUSServerNotResponding.setObjects(
    ("ORiNOCO-MIB", "oriGenericTrapVariable")
)
if mibBuilder.loadTexts:
    oriTrapRADIUSServerNotResponding.setStatus(
        "current"
    )

oriTrapModuleNotInitialized = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 3)
)
oriTrapModuleNotInitialized.setObjects(
    ("ORiNOCO-MIB", "oriGenericTrapVariable")
)
if mibBuilder.loadTexts:
    oriTrapModuleNotInitialized.setStatus(
        "current"
    )

oriTrapDeviceRebooting = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 5)
)
oriTrapDeviceRebooting.setObjects(
      *(("ORiNOCO-MIB", "oriTrapVarMACAddress"),
        ("ORiNOCO-MIB", "oriGenericTrapVariable"),
        ("ORiNOCO-MIB", "oriSystemReboot"))
)
if mibBuilder.loadTexts:
    oriTrapDeviceRebooting.setStatus(
        "current"
    )

oriTrapTaskSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 6)
)
oriTrapTaskSuspended.setObjects(
    ("ORiNOCO-MIB", "oriTrapVarTaskSuspended")
)
if mibBuilder.loadTexts:
    oriTrapTaskSuspended.setStatus(
        "current"
    )

oriTrapBootPFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 7)
)
oriTrapBootPFailed.setObjects(
    ("ORiNOCO-MIB", "oriTrapVarMACAddress")
)
if mibBuilder.loadTexts:
    oriTrapBootPFailed.setStatus(
        "current"
    )

oriTrapDHCPFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 8)
)
oriTrapDHCPFailed.setObjects(
    ("ORiNOCO-MIB", "oriTrapVarMACAddress")
)
if mibBuilder.loadTexts:
    oriTrapDHCPFailed.setStatus(
        "current"
    )

oriTrapDNSClientLookupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 9)
)
oriTrapDNSClientLookupFailure.setObjects(
    ("ORiNOCO-MIB", "oriGenericTrapVariable")
)
if mibBuilder.loadTexts:
    oriTrapDNSClientLookupFailure.setStatus(
        "current"
    )

oriTrapSNTPFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 10)
)
if mibBuilder.loadTexts:
    oriTrapSNTPFailure.setStatus(
        "current"
    )

oriTrapMaximumNumberOfSubscribersReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 11)
)
if mibBuilder.loadTexts:
    oriTrapMaximumNumberOfSubscribersReached.setStatus(
        "current"
    )

oriTrapSSLInitializationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 12)
)
if mibBuilder.loadTexts:
    oriTrapSSLInitializationFailure.setStatus(
        "current"
    )

oriTrapWirelessServiceShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 13)
)
oriTrapWirelessServiceShutdown.setObjects(
    ("ORiNOCO-MIB", "oriTrapVarWirelessCard")
)
if mibBuilder.loadTexts:
    oriTrapWirelessServiceShutdown.setStatus(
        "current"
    )

oriTrapWirelessServiceResumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 14)
)
oriTrapWirelessServiceResumed.setObjects(
    ("ORiNOCO-MIB", "oriTrapVarWirelessCard")
)
if mibBuilder.loadTexts:
    oriTrapWirelessServiceResumed.setStatus(
        "current"
    )

oriTrapSSHInitializationStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 15)
)
oriTrapSSHInitializationStatus.setObjects(
    ("ORiNOCO-MIB", "oriGenericTrapVariable")
)
if mibBuilder.loadTexts:
    oriTrapSSHInitializationStatus.setStatus(
        "current"
    )

oriTrapVLANIDUserAssignment = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 16)
)
oriTrapVLANIDUserAssignment.setObjects(
    ("ORiNOCO-MIB", "oriGenericTrapVariable")
)
if mibBuilder.loadTexts:
    oriTrapVLANIDUserAssignment.setStatus(
        "current"
    )

oriTrapDHCPLeaseRenewal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 17)
)
oriTrapDHCPLeaseRenewal.setObjects(
      *(("ORiNOCO-MIB", "oriTrapVarDHCPServerIPAddress"),
        ("ORiNOCO-MIB", "oriTrapVarIPAddress"),
        ("ORiNOCO-MIB", "oriTrapVarSubnetMask"),
        ("ORiNOCO-MIB", "oriTrapVarDefaultRouterIPAddress"))
)
if mibBuilder.loadTexts:
    oriTrapDHCPLeaseRenewal.setStatus(
        "current"
    )

oriTrapTemperatureAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 5, 0, 18)
)
oriTrapTemperatureAlert.setObjects(
      *(("ORiNOCO-MIB", "oriGenericTrapVariable"),
        ("ORiNOCO-MIB", "oriUnitTemp"))
)
if mibBuilder.loadTexts:
    oriTrapTemperatureAlert.setStatus(
        "current"
    )

oriTrapFlashMemoryEmpty = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 6, 0, 1)
)
if mibBuilder.loadTexts:
    oriTrapFlashMemoryEmpty.setStatus(
        "current"
    )

oriTrapFlashMemoryCorrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 6, 0, 2)
)
oriTrapFlashMemoryCorrupted.setObjects(
    ("ORiNOCO-MIB", "oriGenericTrapVariable")
)
if mibBuilder.loadTexts:
    oriTrapFlashMemoryCorrupted.setStatus(
        "current"
    )

oriTrapFlashMemoryRestoringLastKnownGoodConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 6, 0, 3)
)
if mibBuilder.loadTexts:
    oriTrapFlashMemoryRestoringLastKnownGoodConfiguration.setStatus(
        "current"
    )

oriTrapTFTPFailedOperation = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 7, 0, 1)
)
oriTrapTFTPFailedOperation.setObjects(
      *(("ORiNOCO-MIB", "oriTrapVarTFTPIPAddress"),
        ("ORiNOCO-MIB", "oriTrapVarTFTPFilename"),
        ("ORiNOCO-MIB", "oriTrapVarTFTPOperation"))
)
if mibBuilder.loadTexts:
    oriTrapTFTPFailedOperation.setStatus(
        "current"
    )

oriTrapTFTPOperationInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 7, 0, 2)
)
oriTrapTFTPOperationInitiated.setObjects(
      *(("ORiNOCO-MIB", "oriTrapVarTFTPIPAddress"),
        ("ORiNOCO-MIB", "oriTrapVarTFTPFilename"),
        ("ORiNOCO-MIB", "oriTrapVarTFTPOperation"))
)
if mibBuilder.loadTexts:
    oriTrapTFTPOperationInitiated.setStatus(
        "current"
    )

oriTrapTFTPOperationCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 7, 0, 3)
)
oriTrapTFTPOperationCompleted.setObjects(
      *(("ORiNOCO-MIB", "oriTrapVarTFTPIPAddress"),
        ("ORiNOCO-MIB", "oriTrapVarTFTPFilename"),
        ("ORiNOCO-MIB", "oriTrapVarTFTPOperation"))
)
if mibBuilder.loadTexts:
    oriTrapTFTPOperationCompleted.setStatus(
        "current"
    )

oriTrapZeroSizeImage = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 9, 0, 1)
)
if mibBuilder.loadTexts:
    oriTrapZeroSizeImage.setStatus(
        "current"
    )

oriTrapInvalidImage = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 9, 0, 2)
)
if mibBuilder.loadTexts:
    oriTrapInvalidImage.setStatus(
        "current"
    )

oriTrapImageTooLarge = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 9, 0, 3)
)
if mibBuilder.loadTexts:
    oriTrapImageTooLarge.setStatus(
        "current"
    )

oriTrapIncompatibleImage = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 9, 0, 4)
)
if mibBuilder.loadTexts:
    oriTrapIncompatibleImage.setStatus(
        "current"
    )

oriTrapInvalidImageDigitalSignature = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 9, 0, 5)
)
if mibBuilder.loadTexts:
    oriTrapInvalidImageDigitalSignature.setStatus(
        "current"
    )

oriWORPStationRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 11, 0, 1)
)
oriWORPStationRegister.setObjects(
      *(("ORiNOCO-MIB", "oriTrapVarInterface"),
        ("ORiNOCO-MIB", "oriTrapVarMACAddress"))
)
if mibBuilder.loadTexts:
    oriWORPStationRegister.setStatus(
        "current"
    )

oriWORPStationDeRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 11, 0, 2)
)
oriWORPStationDeRegister.setObjects(
      *(("ORiNOCO-MIB", "oriTrapVarInterface"),
        ("ORiNOCO-MIB", "oriTrapVarMACAddress"))
)
if mibBuilder.loadTexts:
    oriWORPStationDeRegister.setStatus(
        "current"
    )

oriTrapIncompatibleLicenseFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 12, 0, 1)
)
oriTrapIncompatibleLicenseFile.setObjects(
    ("ORiNOCO-MIB", "oriGenericTrapVariable")
)
if mibBuilder.loadTexts:
    oriTrapIncompatibleLicenseFile.setStatus(
        "current"
    )

oriTrapFeatureNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 12, 0, 2)
)
oriTrapFeatureNotSupported.setObjects(
    ("ORiNOCO-MIB", "oriSystemFeatureTableCode")
)
if mibBuilder.loadTexts:
    oriTrapFeatureNotSupported.setStatus(
        "current"
    )

oriTrapZeroLicenseFiles = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 12, 0, 3)
)
if mibBuilder.loadTexts:
    oriTrapZeroLicenseFiles.setStatus(
        "current"
    )

oriTrapInvalidLicenseFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 12, 0, 4)
)
oriTrapInvalidLicenseFile.setObjects(
    ("ORiNOCO-MIB", "oriGenericTrapVariable")
)
if mibBuilder.loadTexts:
    oriTrapInvalidLicenseFile.setStatus(
        "current"
    )

oriTrapUselessLicense = NotificationType(
    (1, 3, 6, 1, 4, 1, 11898, 2, 1, 18, 12, 0, 5)
)
oriTrapUselessLicense.setObjects(
    ("ORiNOCO-MIB", "oriGenericTrapVariable")
)
if mibBuilder.loadTexts:
    oriTrapUselessLicense.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ORiNOCO-MIB",
    **{"VlanId": VlanId,
       "InterfaceBitmask": InterfaceBitmask,
       "ObjStatus": ObjStatus,
       "WEPKeyType": WEPKeyType,
       "ObjStatusActive": ObjStatusActive,
       "DisplayString80": DisplayString80,
       "DisplayString55": DisplayString55,
       "DisplayString32": DisplayString32,
       "agere": agere,
       "orinoco": orinoco,
       "orinocoObjects": orinocoObjects,
       "orinocoSys": orinocoSys,
       "orinocoSysInvMgmt": orinocoSysInvMgmt,
       "oriSystemInvMgmtComponentTable": oriSystemInvMgmtComponentTable,
       "oriSystemInvMgmtComponentTableEntry": oriSystemInvMgmtComponentTableEntry,
       "oriSystemInvMgmtTableComponentIndex": oriSystemInvMgmtTableComponentIndex,
       "oriSystemInvMgmtTableComponentSerialNumber": oriSystemInvMgmtTableComponentSerialNumber,
       "oriSystemInvMgmtTableComponentName": oriSystemInvMgmtTableComponentName,
       "oriSystemInvMgmtTableComponentId": oriSystemInvMgmtTableComponentId,
       "oriSystemInvMgmtTableComponentVariant": oriSystemInvMgmtTableComponentVariant,
       "oriSystemInvMgmtTableComponentReleaseVersion": oriSystemInvMgmtTableComponentReleaseVersion,
       "oriSystemInvMgmtTableComponentMajorVersion": oriSystemInvMgmtTableComponentMajorVersion,
       "oriSystemInvMgmtTableComponentMinorVersion": oriSystemInvMgmtTableComponentMinorVersion,
       "oriSystemInvMgmtTableComponentIfTable": oriSystemInvMgmtTableComponentIfTable,
       "oriSystemInvMgmtTableComponentIfTableEntry": oriSystemInvMgmtTableComponentIfTableEntry,
       "oriSystemInvMgmtInterfaceTableIndex": oriSystemInvMgmtInterfaceTableIndex,
       "oriSystemInvMgmtInterfaceId": oriSystemInvMgmtInterfaceId,
       "oriSystemInvMgmtInterfaceRole": oriSystemInvMgmtInterfaceRole,
       "oriSystemInvMgmtInterfaceVariant": oriSystemInvMgmtInterfaceVariant,
       "oriSystemInvMgmtInterfaceBottomNumber": oriSystemInvMgmtInterfaceBottomNumber,
       "oriSystemInvMgmtInterfaceTopNumber": oriSystemInvMgmtInterfaceTopNumber,
       "oriSystemReboot": oriSystemReboot,
       "oriSystemContactEmail": oriSystemContactEmail,
       "oriSystemContactPhoneNumber": oriSystemContactPhoneNumber,
       "oriSystemFlashUpdate": oriSystemFlashUpdate,
       "oriSystemFlashBackupInterval": oriSystemFlashBackupInterval,
       "oriSystemEmergencyResetToDefault": oriSystemEmergencyResetToDefault,
       "oriSystemMode": oriSystemMode,
       "oriSystemEventLogTable": oriSystemEventLogTable,
       "oriSystemEventLogTableEntry": oriSystemEventLogTableEntry,
       "oriSystemEventLogMessage": oriSystemEventLogMessage,
       "oriSystemEventLogTableReset": oriSystemEventLogTableReset,
       "oriSystemEventLogMask": oriSystemEventLogMask,
       "oriSystemAccessUserName": oriSystemAccessUserName,
       "oriSystemAccessPassword": oriSystemAccessPassword,
       "oriSystemAccessLoginTimeout": oriSystemAccessLoginTimeout,
       "oriSystemAccessIdleTimeout": oriSystemAccessIdleTimeout,
       "oriSystemEventLogNumberOfMessages": oriSystemEventLogNumberOfMessages,
       "orinocoSysFeature": orinocoSysFeature,
       "oriSystemFeatureTable": oriSystemFeatureTable,
       "oriSystemFeatureTableEntry": oriSystemFeatureTableEntry,
       "oriSystemFeatureTableCode": oriSystemFeatureTableCode,
       "oriSystemFeatureTableSupported": oriSystemFeatureTableSupported,
       "oriSystemFeatureTableLicensed": oriSystemFeatureTableLicensed,
       "oriSystemFeatureTableDescription": oriSystemFeatureTableDescription,
       "oriSystemAccessMaxSessions": oriSystemAccessMaxSessions,
       "orinocoSyslog": orinocoSyslog,
       "oriSyslogStatus": oriSyslogStatus,
       "oriSyslogPort": oriSyslogPort,
       "oriSyslogPriority": oriSyslogPriority,
       "oriSyslogHeartbeatStatus": oriSyslogHeartbeatStatus,
       "oriSyslogHeartbeatInterval": oriSyslogHeartbeatInterval,
       "oriSyslogHostTable": oriSyslogHostTable,
       "oriSyslogHostTableEntry": oriSyslogHostTableEntry,
       "oriSyslogHostTableIndex": oriSyslogHostTableIndex,
       "oriSyslogHostIPAddress": oriSyslogHostIPAddress,
       "oriSyslogHostComment": oriSyslogHostComment,
       "oriSyslogHostTableEntryStatus": oriSyslogHostTableEntryStatus,
       "oriSystemCountryCode": oriSystemCountryCode,
       "orinocoTempLog": orinocoTempLog,
       "oriUnitTemp": oriUnitTemp,
       "oriTempLoggingInterval": oriTempLoggingInterval,
       "oriTempLogTable": oriTempLogTable,
       "oriTempLogTableEntry": oriTempLogTableEntry,
       "oriTempLogMessage": oriTempLogMessage,
       "oriTempLogTableReset": oriTempLogTableReset,
       "oriSystemHwType": oriSystemHwType,
       "orinocoIf": orinocoIf,
       "orinocoWirelessIf": orinocoWirelessIf,
       "oriWirelessIfPropertiesTable": oriWirelessIfPropertiesTable,
       "oriWirelessIfPropertiesEntry": oriWirelessIfPropertiesEntry,
       "oriWirelessIfPropertiesIndex": oriWirelessIfPropertiesIndex,
       "oriWirelessIfNetworkName": oriWirelessIfNetworkName,
       "oriWirelessIfMediumReservation": oriWirelessIfMediumReservation,
       "oriWirelessIfInterferenceRobustness": oriWirelessIfInterferenceRobustness,
       "oriWirelessIfDTIMPeriod": oriWirelessIfDTIMPeriod,
       "oriWirelessIfChannel": oriWirelessIfChannel,
       "oriWirelessIfDistancebetweenAPs": oriWirelessIfDistancebetweenAPs,
       "oriWirelessIfMulticastRate": oriWirelessIfMulticastRate,
       "oriWirelessIfClosedSystem": oriWirelessIfClosedSystem,
       "oriWirelessIfAllowedSupportedDataRates": oriWirelessIfAllowedSupportedDataRates,
       "oriWirelessIfRegulatoryDomainList": oriWirelessIfRegulatoryDomainList,
       "oriWirelessIfAllowedChannels": oriWirelessIfAllowedChannels,
       "oriWirelessIfMACAddress": oriWirelessIfMACAddress,
       "oriWirelessIfLoadBalancing": oriWirelessIfLoadBalancing,
       "oriWirelessIfMediumDensityDistribution": oriWirelessIfMediumDensityDistribution,
       "oriWirelessIfTxRate": oriWirelessIfTxRate,
       "oriWirelessIfAutoChannelSelectStatus": oriWirelessIfAutoChannelSelectStatus,
       "oriWirelessIfBandwidthLimitIn": oriWirelessIfBandwidthLimitIn,
       "oriWirelessIfBandwidthLimitOut": oriWirelessIfBandwidthLimitOut,
       "oriWirelessIfTurboModeStatus": oriWirelessIfTurboModeStatus,
       "oriWirelessIfSupportedOperationalModes": oriWirelessIfSupportedOperationalModes,
       "oriWirelessIfOperationalMode": oriWirelessIfOperationalMode,
       "oriWirelessIfPreambleType": oriWirelessIfPreambleType,
       "oriWirelessIfProtectionMechanismStatus": oriWirelessIfProtectionMechanismStatus,
       "oriWirelessIfSupportedMulticastRates": oriWirelessIfSupportedMulticastRates,
       "oriWirelessIfCapabilities": oriWirelessIfCapabilities,
       "oriWirelessIfLBTxTimeThreshold": oriWirelessIfLBTxTimeThreshold,
       "oriWirelessIfLBAdjAPTimeDiffThreshold": oriWirelessIfLBAdjAPTimeDiffThreshold,
       "oriWirelessIfACSFrequencyBandScan": oriWirelessIfACSFrequencyBandScan,
       "oriWirelessIfSecurityPerSSIDStatus": oriWirelessIfSecurityPerSSIDStatus,
       "oriWirelessIfDFSStatus": oriWirelessIfDFSStatus,
       "oriWirelessIfAntenna": oriWirelessIfAntenna,
       "oriWirelessIfTPCMode": oriWirelessIfTPCMode,
       "oriWirelessIfSuperModeStatus": oriWirelessIfSuperModeStatus,
       "oriWirelessIfWSSStatus": oriWirelessIfWSSStatus,
       "oriWirelessIfSupportedAuthenticationModes": oriWirelessIfSupportedAuthenticationModes,
       "oriWirelessIfSupportedCipherModes": oriWirelessIfSupportedCipherModes,
       "oriWirelessIfQoSStatus": oriWirelessIfQoSStatus,
       "oriWirelessIfQoSMaxMediumThreshold": oriWirelessIfQoSMaxMediumThreshold,
       "oriWirelessIfAntennaGain": oriWirelessIfAntennaGain,
       "oriWirelessIfSecurityTable": oriWirelessIfSecurityTable,
       "oriWirelessIfSecurityEntry": oriWirelessIfSecurityEntry,
       "oriWirelessIfSecurityIndex": oriWirelessIfSecurityIndex,
       "oriWirelessIfEncryptionOptions": oriWirelessIfEncryptionOptions,
       "oriWirelessIfEncryptionStatus": oriWirelessIfEncryptionStatus,
       "oriWirelessIfEncryptionKey1": oriWirelessIfEncryptionKey1,
       "oriWirelessIfEncryptionKey2": oriWirelessIfEncryptionKey2,
       "oriWirelessIfEncryptionKey3": oriWirelessIfEncryptionKey3,
       "oriWirelessIfEncryptionKey4": oriWirelessIfEncryptionKey4,
       "oriWirelessIfEncryptionTxKey": oriWirelessIfEncryptionTxKey,
       "oriWirelessIfDenyNonEncryptedData": oriWirelessIfDenyNonEncryptedData,
       "oriWirelessIfProfileCode": oriWirelessIfProfileCode,
       "oriWirelessIfSSIDTable": oriWirelessIfSSIDTable,
       "oriWirelessIfSSIDTableEntry": oriWirelessIfSSIDTableEntry,
       "oriWirelessIfSSIDTableIndex": oriWirelessIfSSIDTableIndex,
       "oriWirelessIfSSIDTableSSID": oriWirelessIfSSIDTableSSID,
       "oriWirelessIfSSIDTableVLANID": oriWirelessIfSSIDTableVLANID,
       "oriWirelessIfSSIDTableStatus": oriWirelessIfSSIDTableStatus,
       "oriWirelessIfSSIDTableSecurityMode": oriWirelessIfSSIDTableSecurityMode,
       "oriWirelessIfSSIDTableBroadcastSSID": oriWirelessIfSSIDTableBroadcastSSID,
       "oriWirelessIfSSIDTableClosedSystem": oriWirelessIfSSIDTableClosedSystem,
       "oriWirelessIfSSIDTableSupportedSecurityModes": oriWirelessIfSSIDTableSupportedSecurityModes,
       "oriWirelessIfSSIDTableEncryptionKey0": oriWirelessIfSSIDTableEncryptionKey0,
       "oriWirelessIfSSIDTableEncryptionKey1": oriWirelessIfSSIDTableEncryptionKey1,
       "oriWirelessIfSSIDTableEncryptionKey2": oriWirelessIfSSIDTableEncryptionKey2,
       "oriWirelessIfSSIDTableEncryptionKey3": oriWirelessIfSSIDTableEncryptionKey3,
       "oriWirelessIfSSIDTableEncryptionTxKey": oriWirelessIfSSIDTableEncryptionTxKey,
       "oriWirelessIfSSIDTableEncryptionKeyLength": oriWirelessIfSSIDTableEncryptionKeyLength,
       "oriWirelessIfSSIDTableRekeyingInterval": oriWirelessIfSSIDTableRekeyingInterval,
       "oriWirelessIfSSIDTablePSKValue": oriWirelessIfSSIDTablePSKValue,
       "oriWirelessIfSSIDTablePSKPassPhrase": oriWirelessIfSSIDTablePSKPassPhrase,
       "oriWirelessIfSSIDTableDenyNonEncryptedData": oriWirelessIfSSIDTableDenyNonEncryptedData,
       "oriWirelessIfSSIDTableSSIDAuthorizationStatus": oriWirelessIfSSIDTableSSIDAuthorizationStatus,
       "oriWirelessIfSSIDTableMACAccessControl": oriWirelessIfSSIDTableMACAccessControl,
       "oriWirelessIfSSIDTableRADIUSMACAccessControl": oriWirelessIfSSIDTableRADIUSMACAccessControl,
       "oriWirelessIfSSIDTableSecurityProfile": oriWirelessIfSSIDTableSecurityProfile,
       "oriWirelessIfSSIDTableRADIUSDot1xProfile": oriWirelessIfSSIDTableRADIUSDot1xProfile,
       "oriWirelessIfSSIDTableRADIUSMACAuthProfile": oriWirelessIfSSIDTableRADIUSMACAuthProfile,
       "oriWirelessIfSSIDTableRADIUSAccountingStatus": oriWirelessIfSSIDTableRADIUSAccountingStatus,
       "oriWirelessIfSSIDTableRADIUSAccountingProfile": oriWirelessIfSSIDTableRADIUSAccountingProfile,
       "oriWirelessIfSSIDTableQoSPolicy": oriWirelessIfSSIDTableQoSPolicy,
       "oriWirelessIfTxPowerControl": oriWirelessIfTxPowerControl,
       "orinocoEthernetIf": orinocoEthernetIf,
       "oriEthernetIfConfigTable": oriEthernetIfConfigTable,
       "oriEthernetIfConfigTableEntry": oriEthernetIfConfigTableEntry,
       "oriEthernetIfConfigTableIndex": oriEthernetIfConfigTableIndex,
       "oriEthernetIfConfigSettings": oriEthernetIfConfigSettings,
       "oriEthernetIfConfigBandwidthLimitIn": oriEthernetIfConfigBandwidthLimitIn,
       "oriEthernetIfConfigBandwidthLimitOut": oriEthernetIfConfigBandwidthLimitOut,
       "oriIfWANInterfaceMACAddress": oriIfWANInterfaceMACAddress,
       "orinocoWORPIf": orinocoWORPIf,
       "oriWORPIfConfigTable": oriWORPIfConfigTable,
       "oriWORPIfConfigTableEntry": oriWORPIfConfigTableEntry,
       "oriWORPIfConfigTableMode": oriWORPIfConfigTableMode,
       "oriWORPIfConfigTableBaseStationName": oriWORPIfConfigTableBaseStationName,
       "oriWORPIfConfigTableMaxSatellites": oriWORPIfConfigTableMaxSatellites,
       "oriWORPIfConfigTableRegistrationTimeout": oriWORPIfConfigTableRegistrationTimeout,
       "oriWORPIfConfigTableRetries": oriWORPIfConfigTableRetries,
       "oriWORPIfConfigTableNetworkSecret": oriWORPIfConfigTableNetworkSecret,
       "oriWORPIfConfigTableNoSleepMode": oriWORPIfConfigTableNoSleepMode,
       "oriWORPIfStatTable": oriWORPIfStatTable,
       "oriWORPIfStatTableEntry": oriWORPIfStatTableEntry,
       "oriWORPIfStatTableRemotePartners": oriWORPIfStatTableRemotePartners,
       "oriWORPIfStatTableAverageLocalSignal": oriWORPIfStatTableAverageLocalSignal,
       "oriWORPIfStatTableAverageLocalNoise": oriWORPIfStatTableAverageLocalNoise,
       "oriWORPIfStatTableAverageRemoteSignal": oriWORPIfStatTableAverageRemoteSignal,
       "oriWORPIfStatTableAverageRemoteNoise": oriWORPIfStatTableAverageRemoteNoise,
       "oriWORPIfStatTableBaseStationAnnounces": oriWORPIfStatTableBaseStationAnnounces,
       "oriWORPIfStatTableRegistrationRequests": oriWORPIfStatTableRegistrationRequests,
       "oriWORPIfStatTableRegistrationRejects": oriWORPIfStatTableRegistrationRejects,
       "oriWORPIfStatTableAuthenticationRequests": oriWORPIfStatTableAuthenticationRequests,
       "oriWORPIfStatTableAuthenticationConfirms": oriWORPIfStatTableAuthenticationConfirms,
       "oriWORPIfStatTableRegistrationAttempts": oriWORPIfStatTableRegistrationAttempts,
       "oriWORPIfStatTableRegistrationIncompletes": oriWORPIfStatTableRegistrationIncompletes,
       "oriWORPIfStatTableRegistrationTimeouts": oriWORPIfStatTableRegistrationTimeouts,
       "oriWORPIfStatTableRegistrationLastReason": oriWORPIfStatTableRegistrationLastReason,
       "oriWORPIfStatTablePollData": oriWORPIfStatTablePollData,
       "oriWORPIfStatTablePollNoData": oriWORPIfStatTablePollNoData,
       "oriWORPIfStatTableReplyData": oriWORPIfStatTableReplyData,
       "oriWORPIfStatTableReplyMoreData": oriWORPIfStatTableReplyMoreData,
       "oriWORPIfStatTableReplyNoData": oriWORPIfStatTableReplyNoData,
       "oriWORPIfStatTableRequestForService": oriWORPIfStatTableRequestForService,
       "oriWORPIfStatTableSendSuccess": oriWORPIfStatTableSendSuccess,
       "oriWORPIfStatTableSendRetries": oriWORPIfStatTableSendRetries,
       "oriWORPIfStatTableSendFailures": oriWORPIfStatTableSendFailures,
       "oriWORPIfStatTableReceiveSuccess": oriWORPIfStatTableReceiveSuccess,
       "oriWORPIfStatTableReceiveRetries": oriWORPIfStatTableReceiveRetries,
       "oriWORPIfStatTableReceiveFailures": oriWORPIfStatTableReceiveFailures,
       "oriWORPIfStatTablePollNoReplies": oriWORPIfStatTablePollNoReplies,
       "orinocoWORPIfSat": orinocoWORPIfSat,
       "orinocoWORPIfSatConfig": orinocoWORPIfSatConfig,
       "oriWORPIfSatConfigStatus": oriWORPIfSatConfigStatus,
       "oriWORPIfSatConfigTable": oriWORPIfSatConfigTable,
       "oriWORPIfSatConfigTableEntry": oriWORPIfSatConfigTableEntry,
       "oriWORPIfSatConfigTableIndex": oriWORPIfSatConfigTableIndex,
       "oriWORPIfSatConfigTableEntryStatus": oriWORPIfSatConfigTableEntryStatus,
       "oriWORPIfSatConfigTableMacAddress": oriWORPIfSatConfigTableMacAddress,
       "oriWORPIfSatConfigTableMinimumBandwidthLimitDownlink": oriWORPIfSatConfigTableMinimumBandwidthLimitDownlink,
       "oriWORPIfSatConfigTableMaximumBandwidthLimitDownlink": oriWORPIfSatConfigTableMaximumBandwidthLimitDownlink,
       "oriWORPIfSatConfigTableMinimumBandwidthLimitUplink": oriWORPIfSatConfigTableMinimumBandwidthLimitUplink,
       "oriWORPIfSatConfigTableMaximumBandwidthLimitUplink": oriWORPIfSatConfigTableMaximumBandwidthLimitUplink,
       "oriWORPIfSatConfigTableComment": oriWORPIfSatConfigTableComment,
       "orinocoWORPIfSatStat": orinocoWORPIfSatStat,
       "oriWORPIfSatStatTable": oriWORPIfSatStatTable,
       "oriWORPIfSatStatTableEntry": oriWORPIfSatStatTableEntry,
       "oriWORPIfSatStatTableIndex": oriWORPIfSatStatTableIndex,
       "oriWORPIfSatStatTableMacAddress": oriWORPIfSatStatTableMacAddress,
       "oriWORPIfSatStatTableAverageLocalSignal": oriWORPIfSatStatTableAverageLocalSignal,
       "oriWORPIfSatStatTableAverageLocalNoise": oriWORPIfSatStatTableAverageLocalNoise,
       "oriWORPIfSatStatTableAverageRemoteSignal": oriWORPIfSatStatTableAverageRemoteSignal,
       "oriWORPIfSatStatTableAverageRemoteNoise": oriWORPIfSatStatTableAverageRemoteNoise,
       "oriWORPIfSatStatTablePollData": oriWORPIfSatStatTablePollData,
       "oriWORPIfSatStatTablePollNoData": oriWORPIfSatStatTablePollNoData,
       "oriWORPIfSatStatTableReplyData": oriWORPIfSatStatTableReplyData,
       "oriWORPIfSatStatTableReplyNoData": oriWORPIfSatStatTableReplyNoData,
       "oriWORPIfSatStatTableRequestForService": oriWORPIfSatStatTableRequestForService,
       "oriWORPIfSatStatTableSendSuccess": oriWORPIfSatStatTableSendSuccess,
       "oriWORPIfSatStatTableSendRetries": oriWORPIfSatStatTableSendRetries,
       "oriWORPIfSatStatTableSendFailures": oriWORPIfSatStatTableSendFailures,
       "oriWORPIfSatStatTableReceiveSuccess": oriWORPIfSatStatTableReceiveSuccess,
       "oriWORPIfSatStatTableReceiveRetries": oriWORPIfSatStatTableReceiveRetries,
       "oriWORPIfSatStatTableReceiveFailures": oriWORPIfSatStatTableReceiveFailures,
       "oriWORPIfSatStatTablePollNoReplies": oriWORPIfSatStatTablePollNoReplies,
       "oriWORPIfSatStatTableLocalTxRate": oriWORPIfSatStatTableLocalTxRate,
       "oriWORPIfSatStatTableRemoteTxRate": oriWORPIfSatStatTableRemoteTxRate,
       "orinocoWORPIfSiteSurvey": orinocoWORPIfSiteSurvey,
       "oriWORPIfSiteSurveyOperation": oriWORPIfSiteSurveyOperation,
       "oriWORPIfSiteSurveyTable": oriWORPIfSiteSurveyTable,
       "oriWORPIfSiteSurveySignalQualityTableEntry": oriWORPIfSiteSurveySignalQualityTableEntry,
       "oriWORPIfSiteSurveyTableIndex": oriWORPIfSiteSurveyTableIndex,
       "oriWORPIfSiteSurveyBaseMACAddress": oriWORPIfSiteSurveyBaseMACAddress,
       "oriWORPIfSiteSurveyBaseName": oriWORPIfSiteSurveyBaseName,
       "oriWORPIfSiteSurveyMaxSatAllowed": oriWORPIfSiteSurveyMaxSatAllowed,
       "oriWORPIfSiteSurveyNumSatRegistered": oriWORPIfSiteSurveyNumSatRegistered,
       "oriWORPIfSiteSurveyCurrentSatRegistered": oriWORPIfSiteSurveyCurrentSatRegistered,
       "oriWORPIfSiteSurveyLocalSignalLevel": oriWORPIfSiteSurveyLocalSignalLevel,
       "oriWORPIfSiteSurveyLocalNoiseLevel": oriWORPIfSiteSurveyLocalNoiseLevel,
       "oriWORPIfSiteSurveyLocalSNR": oriWORPIfSiteSurveyLocalSNR,
       "oriWORPIfSiteSurveyRemoteSignalLevel": oriWORPIfSiteSurveyRemoteSignalLevel,
       "oriWORPIfSiteSurveyRemoteNoiseLevel": oriWORPIfSiteSurveyRemoteNoiseLevel,
       "oriWORPIfSiteSurveyRemoteSNR": oriWORPIfSiteSurveyRemoteSNR,
       "orinocoWORPIfRoaming": orinocoWORPIfRoaming,
       "oriWORPIfRoamingStatus": oriWORPIfRoamingStatus,
       "oriWORPIfRoamingSlowScanThreshold": oriWORPIfRoamingSlowScanThreshold,
       "oriWORPIfRoamingFastScanThreshold": oriWORPIfRoamingFastScanThreshold,
       "oriWORPIfRoamingThreshold": oriWORPIfRoamingThreshold,
       "oriWORPIfRoamingSlowScanPercentThreshold": oriWORPIfRoamingSlowScanPercentThreshold,
       "oriWORPIfRoamingFastScanPercentThreshold": oriWORPIfRoamingFastScanPercentThreshold,
       "orinocoWORPIfDDRS": orinocoWORPIfDDRS,
       "oriWORPIfDDRSStatus": oriWORPIfDDRSStatus,
       "oriWORPIfDDRSDefDataRate": oriWORPIfDDRSDefDataRate,
       "oriWORPIfDDRSMaxDataRate": oriWORPIfDDRSMaxDataRate,
       "oriWORPIfDDRSMinReqSNRdot11an6Mbps": oriWORPIfDDRSMinReqSNRdot11an6Mbps,
       "oriWORPIfDDRSMinReqSNRdot11an9Mbps": oriWORPIfDDRSMinReqSNRdot11an9Mbps,
       "oriWORPIfDDRSMinReqSNRdot11an12Mbps": oriWORPIfDDRSMinReqSNRdot11an12Mbps,
       "oriWORPIfDDRSMinReqSNRdot11an18Mbps": oriWORPIfDDRSMinReqSNRdot11an18Mbps,
       "oriWORPIfDDRSMinReqSNRdot11an24Mbps": oriWORPIfDDRSMinReqSNRdot11an24Mbps,
       "oriWORPIfDDRSMinReqSNRdot11an36Mbps": oriWORPIfDDRSMinReqSNRdot11an36Mbps,
       "oriWORPIfDDRSMinReqSNRdot11an48Mbps": oriWORPIfDDRSMinReqSNRdot11an48Mbps,
       "oriWORPIfDDRSMinReqSNRdot11an54Mbps": oriWORPIfDDRSMinReqSNRdot11an54Mbps,
       "oriWORPIfDDRSMinReqSNRdot11at12Mbps": oriWORPIfDDRSMinReqSNRdot11at12Mbps,
       "oriWORPIfDDRSMinReqSNRdot11at18Mbps": oriWORPIfDDRSMinReqSNRdot11at18Mbps,
       "oriWORPIfDDRSMinReqSNRdot11at24Mbps": oriWORPIfDDRSMinReqSNRdot11at24Mbps,
       "oriWORPIfDDRSMinReqSNRdot11at36Mbps": oriWORPIfDDRSMinReqSNRdot11at36Mbps,
       "oriWORPIfDDRSMinReqSNRdot11at48Mbps": oriWORPIfDDRSMinReqSNRdot11at48Mbps,
       "oriWORPIfDDRSMinReqSNRdot11at72Mbps": oriWORPIfDDRSMinReqSNRdot11at72Mbps,
       "oriWORPIfDDRSMinReqSNRdot11at96Mbps": oriWORPIfDDRSMinReqSNRdot11at96Mbps,
       "oriWORPIfDDRSMinReqSNRdot11at108Mbps": oriWORPIfDDRSMinReqSNRdot11at108Mbps,
       "oriWORPIfDDRSDataRateIncAvgSNRThreshold": oriWORPIfDDRSDataRateIncAvgSNRThreshold,
       "oriWORPIfDDRSDataRateIncReqSNRThreshold": oriWORPIfDDRSDataRateIncReqSNRThreshold,
       "oriWORPIfDDRSDataRateDecReqSNRThreshold": oriWORPIfDDRSDataRateDecReqSNRThreshold,
       "oriWORPIfDDRSDataRateIncPercentThreshold": oriWORPIfDDRSDataRateIncPercentThreshold,
       "oriWORPIfDDRSDataRateDecPercentThreshold": oriWORPIfDDRSDataRateDecPercentThreshold,
       "orinocoWORPIfBSU": orinocoWORPIfBSU,
       "orinocoWORPIfBSUStat": orinocoWORPIfBSUStat,
       "orinocoWORPIfBSUStatMACAddress": orinocoWORPIfBSUStatMACAddress,
       "orinocoWORPIfBSUStatLocalTxRate": orinocoWORPIfBSUStatLocalTxRate,
       "orinocoWORPIfBSUStatRemoteTxRate": orinocoWORPIfBSUStatRemoteTxRate,
       "orinocoWORPIfBSUStatAverageLocalSignal": orinocoWORPIfBSUStatAverageLocalSignal,
       "orinocoWORPIfBSUStatAverageLocalNoise": orinocoWORPIfBSUStatAverageLocalNoise,
       "orinocoWORPIfBSUStatAverageRemoteSignal": orinocoWORPIfBSUStatAverageRemoteSignal,
       "orinocoWORPIfBSUStatAverageRemoteNoise": orinocoWORPIfBSUStatAverageRemoteNoise,
       "orinocoNet": orinocoNet,
       "orinocoNetIP": orinocoNetIP,
       "oriNetworkIPConfigTable": oriNetworkIPConfigTable,
       "oriNetworkIPConfigTableEntry": oriNetworkIPConfigTableEntry,
       "oriNetworkIPConfigTableIndex": oriNetworkIPConfigTableIndex,
       "oriNetworkIPConfigIPAddress": oriNetworkIPConfigIPAddress,
       "oriNetworkIPConfigSubnetMask": oriNetworkIPConfigSubnetMask,
       "oriNetworkIPDefaultRouterIPAddress": oriNetworkIPDefaultRouterIPAddress,
       "oriNetworkIPDefaultTTL": oriNetworkIPDefaultTTL,
       "oriNetworkIPAddressType": oriNetworkIPAddressType,
       "orinocoSNMP": orinocoSNMP,
       "oriSNMPReadPassword": oriSNMPReadPassword,
       "oriSNMPReadWritePassword": oriSNMPReadWritePassword,
       "oriSNMPAuthorizedManagerCount": oriSNMPAuthorizedManagerCount,
       "oriSNMPAccessTable": oriSNMPAccessTable,
       "oriSNMPAccessTableEntry": oriSNMPAccessTableEntry,
       "oriSNMPAccessTableIndex": oriSNMPAccessTableIndex,
       "oriSNMPAccessTableIPAddress": oriSNMPAccessTableIPAddress,
       "oriSNMPAccessTableIPMask": oriSNMPAccessTableIPMask,
       "oriSNMPAccessTableInterfaceBitmask": oriSNMPAccessTableInterfaceBitmask,
       "oriSNMPAccessTableComment": oriSNMPAccessTableComment,
       "oriSNMPAccessTableEntryStatus": oriSNMPAccessTableEntryStatus,
       "oriSNMPTrapHostTable": oriSNMPTrapHostTable,
       "oriSNMPTrapHostTableEntry": oriSNMPTrapHostTableEntry,
       "oriSNMPTrapHostTableIndex": oriSNMPTrapHostTableIndex,
       "oriSNMPTrapHostTableIPAddress": oriSNMPTrapHostTableIPAddress,
       "oriSNMPTrapHostTablePassword": oriSNMPTrapHostTablePassword,
       "oriSNMPTrapHostTableComment": oriSNMPTrapHostTableComment,
       "oriSNMPTrapHostTableEntryStatus": oriSNMPTrapHostTableEntryStatus,
       "oriSNMPInterfaceBitmask": oriSNMPInterfaceBitmask,
       "oriSNMPErrorMessage": oriSNMPErrorMessage,
       "oriSNMPAccessTableStatus": oriSNMPAccessTableStatus,
       "oriSNMPTrapType": oriSNMPTrapType,
       "oriSNMPSecureManagementStatus": oriSNMPSecureManagementStatus,
       "oriSNMPV3AuthPassword": oriSNMPV3AuthPassword,
       "oriSNMPV3PrivPassword": oriSNMPV3PrivPassword,
       "orinocoFiltering": orinocoFiltering,
       "orinocoProtocolFilter": orinocoProtocolFilter,
       "oriProtocolFilterOperationType": oriProtocolFilterOperationType,
       "oriProtocolFilterTable": oriProtocolFilterTable,
       "oriProtocolFilterTableEntry": oriProtocolFilterTableEntry,
       "oriProtocolFilterTableIndex": oriProtocolFilterTableIndex,
       "oriProtocolFilterProtocol": oriProtocolFilterProtocol,
       "oriProtocolFilterProtocolComment": oriProtocolFilterProtocolComment,
       "oriProtocolFilterTableEntryStatus": oriProtocolFilterTableEntryStatus,
       "oriProtocolFilterTableInterfaceBitmask": oriProtocolFilterTableInterfaceBitmask,
       "oriProtocolFilterProtocolString": oriProtocolFilterProtocolString,
       "oriProtocolFilterInterfaceBitmask": oriProtocolFilterInterfaceBitmask,
       "orinocoAccessControl": orinocoAccessControl,
       "oriAccessControlStatus": oriAccessControlStatus,
       "oriAccessControlOperationType": oriAccessControlOperationType,
       "oriAccessControlTable": oriAccessControlTable,
       "oriAccessControlEntry": oriAccessControlEntry,
       "oriAccessControlTableIndex": oriAccessControlTableIndex,
       "oriAccessControlTableMACAddress": oriAccessControlTableMACAddress,
       "oriAccessControlTableComment": oriAccessControlTableComment,
       "oriAccessControlTableEntryStatus": oriAccessControlTableEntryStatus,
       "orinocoStaticMACAddressFilter": orinocoStaticMACAddressFilter,
       "oriStaticMACAddressFilterTable": oriStaticMACAddressFilterTable,
       "oriStaticMACAddressFilterEntry": oriStaticMACAddressFilterEntry,
       "oriStaticMACAddressFilterTableIndex": oriStaticMACAddressFilterTableIndex,
       "oriStaticMACAddressFilterWiredAddress": oriStaticMACAddressFilterWiredAddress,
       "oriStaticMACAddressFilterWiredMask": oriStaticMACAddressFilterWiredMask,
       "oriStaticMACAddressFilterWirelessAddress": oriStaticMACAddressFilterWirelessAddress,
       "oriStaticMACAddressFilterWirelessMask": oriStaticMACAddressFilterWirelessMask,
       "oriStaticMACAddressFilterTableEntryStatus": oriStaticMACAddressFilterTableEntryStatus,
       "oriStaticMACAddressFilterComment": oriStaticMACAddressFilterComment,
       "orinocoStormThreshold": orinocoStormThreshold,
       "oriBroadcastAddressThreshold": oriBroadcastAddressThreshold,
       "oriMulticastAddressThreshold": oriMulticastAddressThreshold,
       "oriStormThresholdTable": oriStormThresholdTable,
       "oriStormThresholdTableEntry": oriStormThresholdTableEntry,
       "oriStormThresholdIfBroadcast": oriStormThresholdIfBroadcast,
       "oriStormThresholdIfMulticast": oriStormThresholdIfMulticast,
       "orinocoPortFilter": orinocoPortFilter,
       "oriPortFilterStatus": oriPortFilterStatus,
       "oriPortFilterOperationType": oriPortFilterOperationType,
       "oriPortFilterTable": oriPortFilterTable,
       "oriPortFilterTableEntry": oriPortFilterTableEntry,
       "oriPortFilterTableEntryIndex": oriPortFilterTableEntryIndex,
       "oriPortFilterTableEntryPort": oriPortFilterTableEntryPort,
       "oriPortFilterTableEntryPortType": oriPortFilterTableEntryPortType,
       "oriPortFilterTableEntryInterfaceBitmask": oriPortFilterTableEntryInterfaceBitmask,
       "oriPortFilterTableEntryComment": oriPortFilterTableEntryComment,
       "oriPortFilterTableEntryStatus": oriPortFilterTableEntryStatus,
       "orinocoAdvancedFiltering": orinocoAdvancedFiltering,
       "oriBroadcastFilteringTable": oriBroadcastFilteringTable,
       "oriBroadcastFilteringTableEntry": oriBroadcastFilteringTableEntry,
       "oriBroadcastFilteringTableIndex": oriBroadcastFilteringTableIndex,
       "oriBroadcastFilteringProtocolName": oriBroadcastFilteringProtocolName,
       "oriBroadcastFilteringDirection": oriBroadcastFilteringDirection,
       "oriBroadcastFilteringTableEntryStatus": oriBroadcastFilteringTableEntryStatus,
       "orinocoPacketForwarding": orinocoPacketForwarding,
       "oriPacketForwardingStatus": oriPacketForwardingStatus,
       "oriPacketForwardingMACAddress": oriPacketForwardingMACAddress,
       "oriPacketForwardingInterface": oriPacketForwardingInterface,
       "orinocoIBSSTraffic": orinocoIBSSTraffic,
       "oriIBSSTrafficOperation": oriIBSSTrafficOperation,
       "orinocoIntraCellBlocking": orinocoIntraCellBlocking,
       "oriIntraCellBlockingStatus": oriIntraCellBlockingStatus,
       "oriIntraCellBlockingMACTable": oriIntraCellBlockingMACTable,
       "oriIntraCellBlockingMACTableEntry": oriIntraCellBlockingMACTableEntry,
       "oriIntraCellBlockingMACTableIndex": oriIntraCellBlockingMACTableIndex,
       "oriIntraCellBlockingMACTableMACAddress": oriIntraCellBlockingMACTableMACAddress,
       "oriIntraCellBlockingMACTableGroupID1": oriIntraCellBlockingMACTableGroupID1,
       "oriIntraCellBlockingMACTableGroupID2": oriIntraCellBlockingMACTableGroupID2,
       "oriIntraCellBlockingMACTableGroupID3": oriIntraCellBlockingMACTableGroupID3,
       "oriIntraCellBlockingMACTableGroupID4": oriIntraCellBlockingMACTableGroupID4,
       "oriIntraCellBlockingMACTableGroupID5": oriIntraCellBlockingMACTableGroupID5,
       "oriIntraCellBlockingMACTableGroupID6": oriIntraCellBlockingMACTableGroupID6,
       "oriIntraCellBlockingMACTableGroupID7": oriIntraCellBlockingMACTableGroupID7,
       "oriIntraCellBlockingMACTableGroupID8": oriIntraCellBlockingMACTableGroupID8,
       "oriIntraCellBlockingMACTableGroupID9": oriIntraCellBlockingMACTableGroupID9,
       "oriIntraCellBlockingMACTableGroupID10": oriIntraCellBlockingMACTableGroupID10,
       "oriIntraCellBlockingMACTableGroupID11": oriIntraCellBlockingMACTableGroupID11,
       "oriIntraCellBlockingMACTableGroupID12": oriIntraCellBlockingMACTableGroupID12,
       "oriIntraCellBlockingMACTableGroupID13": oriIntraCellBlockingMACTableGroupID13,
       "oriIntraCellBlockingMACTableGroupID14": oriIntraCellBlockingMACTableGroupID14,
       "oriIntraCellBlockingMACTableGroupID15": oriIntraCellBlockingMACTableGroupID15,
       "oriIntraCellBlockingMACTableGroupID16": oriIntraCellBlockingMACTableGroupID16,
       "oriIntraCellBlockingMACTableEntryStatus": oriIntraCellBlockingMACTableEntryStatus,
       "oriIntraCellBlockingGroupTable": oriIntraCellBlockingGroupTable,
       "oriIntraCellBlockingGroupTableEntry": oriIntraCellBlockingGroupTableEntry,
       "oriIntraCellBlockingGroupTableIndex": oriIntraCellBlockingGroupTableIndex,
       "oriIntraCellBlockingGroupTableName": oriIntraCellBlockingGroupTableName,
       "oriIntraCellBlockingGroupTableEntryStatus": oriIntraCellBlockingGroupTableEntryStatus,
       "orinocoSecurityGw": orinocoSecurityGw,
       "oriSecurityGwStatus": oriSecurityGwStatus,
       "oriSecurityGwMac": oriSecurityGwMac,
       "orinocoRADIUS": orinocoRADIUS,
       "orinocoRADIUSAuth": orinocoRADIUSAuth,
       "oriRADIUSAuthServerTable": oriRADIUSAuthServerTable,
       "oriRADIUSAuthServerTableEntry": oriRADIUSAuthServerTableEntry,
       "oriRADIUSAuthServerTableIndex": oriRADIUSAuthServerTableIndex,
       "oriRADIUSAuthServerType": oriRADIUSAuthServerType,
       "oriRADIUSAuthServerTableEntryStatus": oriRADIUSAuthServerTableEntryStatus,
       "oriRADIUSAuthServerIPAddress": oriRADIUSAuthServerIPAddress,
       "oriRADIUSAuthServerDestPort": oriRADIUSAuthServerDestPort,
       "oriRADIUSAuthServerSharedSecret": oriRADIUSAuthServerSharedSecret,
       "oriRADIUSAuthServerResponseTime": oriRADIUSAuthServerResponseTime,
       "oriRADIUSAuthServerMaximumRetransmission": oriRADIUSAuthServerMaximumRetransmission,
       "oriRADIUSAuthClientAccessRequests": oriRADIUSAuthClientAccessRequests,
       "oriRADIUSAuthClientAccessRetransmissions": oriRADIUSAuthClientAccessRetransmissions,
       "oriRADIUSAuthClientAccessAccepts": oriRADIUSAuthClientAccessAccepts,
       "oriRADIUSAuthClientAccessChallenges": oriRADIUSAuthClientAccessChallenges,
       "oriRADIUSAuthClientAccessRejects": oriRADIUSAuthClientAccessRejects,
       "oriRADIUSAuthClientMalformedAccessResponses": oriRADIUSAuthClientMalformedAccessResponses,
       "oriRADIUSAuthClientAuthInvalidAuthenticators": oriRADIUSAuthClientAuthInvalidAuthenticators,
       "oriRADIUSAuthClientTimeouts": oriRADIUSAuthClientTimeouts,
       "oriRADIUSAuthServerNameOrIPAddress": oriRADIUSAuthServerNameOrIPAddress,
       "oriRADIUSAuthServerAddressingFormat": oriRADIUSAuthServerAddressingFormat,
       "orinocoRADIUSAcct": orinocoRADIUSAcct,
       "oriRADIUSAcctStatus": oriRADIUSAcctStatus,
       "oriRADIUSAcctInactivityTimer": oriRADIUSAcctInactivityTimer,
       "oriRADIUSAcctServerTable": oriRADIUSAcctServerTable,
       "oriRADIUSAcctServerTableEntry": oriRADIUSAcctServerTableEntry,
       "oriRADIUSAcctServerTableIndex": oriRADIUSAcctServerTableIndex,
       "oriRADIUSAcctServerType": oriRADIUSAcctServerType,
       "oriRADIUSAcctServerTableEntryStatus": oriRADIUSAcctServerTableEntryStatus,
       "oriRADIUSAcctServerIPAddress": oriRADIUSAcctServerIPAddress,
       "oriRADIUSAcctServerDestPort": oriRADIUSAcctServerDestPort,
       "oriRADIUSAcctServerSharedSecret": oriRADIUSAcctServerSharedSecret,
       "oriRADIUSAcctServerResponseTime": oriRADIUSAcctServerResponseTime,
       "oriRADIUSAcctServerMaximumRetransmission": oriRADIUSAcctServerMaximumRetransmission,
       "oriRADIUSAcctClientAccountingRequests": oriRADIUSAcctClientAccountingRequests,
       "oriRADIUSAcctClientAccountingRetransmissions": oriRADIUSAcctClientAccountingRetransmissions,
       "oriRADIUSAcctClientAccountingResponses": oriRADIUSAcctClientAccountingResponses,
       "oriRADIUSAcctClientAcctInvalidAuthenticators": oriRADIUSAcctClientAcctInvalidAuthenticators,
       "oriRADIUSAcctServerNameOrIPAddress": oriRADIUSAcctServerNameOrIPAddress,
       "oriRADIUSAcctServerAddressingFormat": oriRADIUSAcctServerAddressingFormat,
       "oriRADIUSAcctUpdateInterval": oriRADIUSAcctUpdateInterval,
       "oriRADIUSClientInvalidServerAddress": oriRADIUSClientInvalidServerAddress,
       "oriRADIUSMACAccessControl": oriRADIUSMACAccessControl,
       "oriRADIUSAuthorizationLifeTime": oriRADIUSAuthorizationLifeTime,
       "oriRADIUSMACAddressFormat": oriRADIUSMACAddressFormat,
       "oriRADIUSLocalUserStatus": oriRADIUSLocalUserStatus,
       "oriRADIUSLocalUserPassword": oriRADIUSLocalUserPassword,
       "oriRADIUSbasedManagementAccessProfile": oriRADIUSbasedManagementAccessProfile,
       "orinocoRADIUSSvrProfiles": orinocoRADIUSSvrProfiles,
       "oriRADIUSSvrTable": oriRADIUSSvrTable,
       "oriRADIUSSvrTableEntry": oriRADIUSSvrTableEntry,
       "oriRADIUSSvrTableProfileIndex": oriRADIUSSvrTableProfileIndex,
       "oriRADIUSSvrTablePrimaryOrSecondaryIndex": oriRADIUSSvrTablePrimaryOrSecondaryIndex,
       "oriRADIUSSvrTableProfileName": oriRADIUSSvrTableProfileName,
       "oriRADIUSSvrTableAddressingFormat": oriRADIUSSvrTableAddressingFormat,
       "oriRADIUSSvrTableNameOrIPAddress": oriRADIUSSvrTableNameOrIPAddress,
       "oriRADIUSSvrTableDestPort": oriRADIUSSvrTableDestPort,
       "oriRADIUSSvrTableSharedSecret": oriRADIUSSvrTableSharedSecret,
       "oriRADIUSSvrTableResponseTime": oriRADIUSSvrTableResponseTime,
       "oriRADIUSSvrTableMaximumRetransmission": oriRADIUSSvrTableMaximumRetransmission,
       "oriRADIUSSvrTableVLANID": oriRADIUSSvrTableVLANID,
       "oriRADIUSSvrTableMACAddressFormat": oriRADIUSSvrTableMACAddressFormat,
       "oriRADIUSSvrTableAuthorizationLifeTime": oriRADIUSSvrTableAuthorizationLifeTime,
       "oriRADIUSSvrTableAccountingInactivityTimer": oriRADIUSSvrTableAccountingInactivityTimer,
       "oriRADIUSSvrTableAccountingUpdateInterval": oriRADIUSSvrTableAccountingUpdateInterval,
       "oriRADIUSSvrTableRowStatus": oriRADIUSSvrTableRowStatus,
       "oriRADIUSClientInvalidSvrAddress": oriRADIUSClientInvalidSvrAddress,
       "oriRADIUSAuthClientStatTable": oriRADIUSAuthClientStatTable,
       "oriRADIUSAuthClientStatTableEntry": oriRADIUSAuthClientStatTableEntry,
       "oriRADIUSAuthClientStatTableIndex": oriRADIUSAuthClientStatTableIndex,
       "oriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex": oriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex,
       "oriRADIUSAuthClientStatTableAccessRequests": oriRADIUSAuthClientStatTableAccessRequests,
       "oriRADIUSAuthClientStatTableAccessRetransmissions": oriRADIUSAuthClientStatTableAccessRetransmissions,
       "oriRADIUSAuthClientStatTableAccessAccepts": oriRADIUSAuthClientStatTableAccessAccepts,
       "oriRADIUSAuthClientStatTableAccessChallenges": oriRADIUSAuthClientStatTableAccessChallenges,
       "oriRADIUSAuthClientStatTableAccessRejects": oriRADIUSAuthClientStatTableAccessRejects,
       "oriRADIUSAuthClientStatTableMalformedAccessResponses": oriRADIUSAuthClientStatTableMalformedAccessResponses,
       "oriRADIUSAuthClientStatTableBadAuthenticators": oriRADIUSAuthClientStatTableBadAuthenticators,
       "oriRADIUSAuthClientStatTableTimeouts": oriRADIUSAuthClientStatTableTimeouts,
       "oriRADIUSAcctClientStatTable": oriRADIUSAcctClientStatTable,
       "oriRADIUSAcctClientStatTableEntry": oriRADIUSAcctClientStatTableEntry,
       "oriRADIUSAcctClientStatTableIndex": oriRADIUSAcctClientStatTableIndex,
       "oriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex": oriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex,
       "oriRADIUSAcctClientStatTableAccountingRequests": oriRADIUSAcctClientStatTableAccountingRequests,
       "oriRADIUSAcctClientStatTableAccountingRetransmissions": oriRADIUSAcctClientStatTableAccountingRetransmissions,
       "oriRADIUSAcctClientStatTableAccountingResponses": oriRADIUSAcctClientStatTableAccountingResponses,
       "oriRADIUSAcctClientStatTableBadAuthenticators": oriRADIUSAcctClientStatTableBadAuthenticators,
       "orinocoTelnet": orinocoTelnet,
       "oriTelnetSessions": oriTelnetSessions,
       "oriTelnetPassword": oriTelnetPassword,
       "oriTelnetPort": oriTelnetPort,
       "oriTelnetLoginTimeout": oriTelnetLoginTimeout,
       "oriTelnetIdleTimeout": oriTelnetIdleTimeout,
       "oriTelnetInterfaceBitmask": oriTelnetInterfaceBitmask,
       "oriTelnetSSHStatus": oriTelnetSSHStatus,
       "oriTelnetSSHHostKeyStatus": oriTelnetSSHHostKeyStatus,
       "oriTelnetSSHFingerPrint": oriTelnetSSHFingerPrint,
       "oriTelnetRADIUSAccessControl": oriTelnetRADIUSAccessControl,
       "orinocoTFTP": orinocoTFTP,
       "oriTFTPServerIPAddress": oriTFTPServerIPAddress,
       "oriTFTPFileName": oriTFTPFileName,
       "oriTFTPFileType": oriTFTPFileType,
       "oriTFTPOperation": oriTFTPOperation,
       "oriTFTPFileMode": oriTFTPFileMode,
       "oriTFTPOperationStatus": oriTFTPOperationStatus,
       "oriTFTPAutoConfigStatus": oriTFTPAutoConfigStatus,
       "oriTFTPAutoConfigFilename": oriTFTPAutoConfigFilename,
       "oriTFTPAutoConfigServerIPAddress": oriTFTPAutoConfigServerIPAddress,
       "oriTFTPDowngrade": oriTFTPDowngrade,
       "orinocoSerial": orinocoSerial,
       "oriSerialBaudRate": oriSerialBaudRate,
       "oriSerialDataBits": oriSerialDataBits,
       "oriSerialParity": oriSerialParity,
       "oriSerialStopBits": oriSerialStopBits,
       "oriSerialFlowControl": oriSerialFlowControl,
       "orinocoIAPP": orinocoIAPP,
       "oriIAPPStatus": oriIAPPStatus,
       "oriIAPPPeriodicAnnounceInterval": oriIAPPPeriodicAnnounceInterval,
       "oriIAPPAnnounceResponseTime": oriIAPPAnnounceResponseTime,
       "oriIAPPHandoverTimeout": oriIAPPHandoverTimeout,
       "oriIAPPMaximumHandoverRetransmissions": oriIAPPMaximumHandoverRetransmissions,
       "oriIAPPAnnounceRequestSent": oriIAPPAnnounceRequestSent,
       "oriIAPPAnnounceRequestReceived": oriIAPPAnnounceRequestReceived,
       "oriIAPPAnnounceResponseSent": oriIAPPAnnounceResponseSent,
       "oriIAPPAnnounceResponseReceived": oriIAPPAnnounceResponseReceived,
       "oriIAPPHandoverRequestSent": oriIAPPHandoverRequestSent,
       "oriIAPPHandoverRequestReceived": oriIAPPHandoverRequestReceived,
       "oriIAPPHandoverRequestRetransmissions": oriIAPPHandoverRequestRetransmissions,
       "oriIAPPHandoverResponseSent": oriIAPPHandoverResponseSent,
       "oriIAPPHandoverResponseReceived": oriIAPPHandoverResponseReceived,
       "oriIAPPPDUsDropped": oriIAPPPDUsDropped,
       "oriIAPPRoamingClients": oriIAPPRoamingClients,
       "oriIAPPMACIPTable": oriIAPPMACIPTable,
       "oriIAPPMACIPTableEntry": oriIAPPMACIPTableEntry,
       "oriIAPPMACIPTableIndex": oriIAPPMACIPTableIndex,
       "oriIAPPMACIPTableSystemName": oriIAPPMACIPTableSystemName,
       "oriIAPPMACIPTableIPAddress": oriIAPPMACIPTableIPAddress,
       "oriIAPPMACIPTableBSSID": oriIAPPMACIPTableBSSID,
       "oriIAPPMACIPTableESSID": oriIAPPMACIPTableESSID,
       "oriIAPPSendAnnounceRequestOnStart": oriIAPPSendAnnounceRequestOnStart,
       "orinocoLinkTest": orinocoLinkTest,
       "oriLinkTestTimeOut": oriLinkTestTimeOut,
       "oriLinkTestInterval": oriLinkTestInterval,
       "oriLinkTestExplore": oriLinkTestExplore,
       "oriLinkTestTable": oriLinkTestTable,
       "oriLinkTestTableEntry": oriLinkTestTableEntry,
       "oriLinkTestTableIndex": oriLinkTestTableIndex,
       "oriLinkTestInProgress": oriLinkTestInProgress,
       "oriLinkTestStationName": oriLinkTestStationName,
       "oriLinkTestMACAddress": oriLinkTestMACAddress,
       "oriLinkTestStationProfile": oriLinkTestStationProfile,
       "oriLinkTestOurCurSignalLevel": oriLinkTestOurCurSignalLevel,
       "oriLinkTestOurCurNoiseLevel": oriLinkTestOurCurNoiseLevel,
       "oriLinkTestOurCurSNR": oriLinkTestOurCurSNR,
       "oriLinkTestOurMinSignalLevel": oriLinkTestOurMinSignalLevel,
       "oriLinkTestOurMinNoiseLevel": oriLinkTestOurMinNoiseLevel,
       "oriLinkTestOurMinSNR": oriLinkTestOurMinSNR,
       "oriLinkTestOurMaxSignalLevel": oriLinkTestOurMaxSignalLevel,
       "oriLinkTestOurMaxNoiseLevel": oriLinkTestOurMaxNoiseLevel,
       "oriLinkTestOurMaxSNR": oriLinkTestOurMaxSNR,
       "oriLinkTestOurLowFrameCount": oriLinkTestOurLowFrameCount,
       "oriLinkTestOurStandardFrameCount": oriLinkTestOurStandardFrameCount,
       "oriLinkTestOurMediumFrameCount": oriLinkTestOurMediumFrameCount,
       "oriLinkTestOurHighFrameCount": oriLinkTestOurHighFrameCount,
       "oriLinkTestHisCurSignalLevel": oriLinkTestHisCurSignalLevel,
       "oriLinkTestHisCurNoiseLevel": oriLinkTestHisCurNoiseLevel,
       "oriLinkTestHisCurSNR": oriLinkTestHisCurSNR,
       "oriLinkTestHisMinSignalLevel": oriLinkTestHisMinSignalLevel,
       "oriLinkTestHisMinNoiseLevel": oriLinkTestHisMinNoiseLevel,
       "oriLinkTestHisMinSNR": oriLinkTestHisMinSNR,
       "oriLinkTestHisMaxSignalLevel": oriLinkTestHisMaxSignalLevel,
       "oriLinkTestHisMaxNoiseLevel": oriLinkTestHisMaxNoiseLevel,
       "oriLinkTestHisMaxSNR": oriLinkTestHisMaxSNR,
       "oriLinkTestHisLowFrameCount": oriLinkTestHisLowFrameCount,
       "oriLinkTestHisStandardFrameCount": oriLinkTestHisStandardFrameCount,
       "oriLinkTestHisMediumFrameCount": oriLinkTestHisMediumFrameCount,
       "oriLinkTestHisHighFrameCount": oriLinkTestHisHighFrameCount,
       "oriLinkTestInterface": oriLinkTestInterface,
       "oriLinkTestRadioType": oriLinkTestRadioType,
       "oriLinkTestDataRateTable": oriLinkTestDataRateTable,
       "oriLinkTestDataRateTableEntry": oriLinkTestDataRateTableEntry,
       "oriLinkTestDataRateTableIndex": oriLinkTestDataRateTableIndex,
       "oriLinkTestDataRateTableRemoteCount": oriLinkTestDataRateTableRemoteCount,
       "oriLinkTestDataRateTableLocalCount": oriLinkTestDataRateTableLocalCount,
       "orinocoLinkInt": orinocoLinkInt,
       "oriLinkIntStatus": oriLinkIntStatus,
       "oriLinkIntPollInterval": oriLinkIntPollInterval,
       "oriLinkIntPollRetransmissions": oriLinkIntPollRetransmissions,
       "oriLinkIntTable": oriLinkIntTable,
       "oriLinkIntTableEntry": oriLinkIntTableEntry,
       "oriLinkIntTableIndex": oriLinkIntTableIndex,
       "oriLinkIntTableTargetIPAddress": oriLinkIntTableTargetIPAddress,
       "oriLinkIntTableComment": oriLinkIntTableComment,
       "oriLinkIntTableEntryStatus": oriLinkIntTableEntryStatus,
       "orinocoUPSD": orinocoUPSD,
       "oriUPSDGPRInterval": oriUPSDGPRInterval,
       "oriUPSDMaxActiveSU": oriUPSDMaxActiveSU,
       "oriUPSDE911Reserved": oriUPSDE911Reserved,
       "oriUPSDRoamingReserved": oriUPSDRoamingReserved,
       "orinocoQoS": orinocoQoS,
       "oriQoSPolicyTable": oriQoSPolicyTable,
       "oriQoSPolicyTableEntry": oriQoSPolicyTableEntry,
       "oriQoSPolicyTableIndex": oriQoSPolicyTableIndex,
       "oriQoSPolicyTableSecIndex": oriQoSPolicyTableSecIndex,
       "oriQoSPolicyName": oriQoSPolicyName,
       "oriQoSPolicyType": oriQoSPolicyType,
       "oriQoSPolicyPriorityMapping": oriQoSPolicyPriorityMapping,
       "oriQoSPolicyMarkingStatus": oriQoSPolicyMarkingStatus,
       "oriQoSPolicyTableRowStatus": oriQoSPolicyTableRowStatus,
       "oriQoSDot1DToDot1pMappingTable": oriQoSDot1DToDot1pMappingTable,
       "oriQoSDot1DToDot1pMappingTableEntry": oriQoSDot1DToDot1pMappingTableEntry,
       "oriQoSDot1DToDot1pMappingTableIndex": oriQoSDot1DToDot1pMappingTableIndex,
       "oriQoSDot1dPriority": oriQoSDot1dPriority,
       "oriQoSDot1pPriority": oriQoSDot1pPriority,
       "oriQoSDot1DToDot1pMappingTableRowStatus": oriQoSDot1DToDot1pMappingTableRowStatus,
       "oriQoSDot1DToIPDSCPMappingTable": oriQoSDot1DToIPDSCPMappingTable,
       "oriQoSDot1DToIPDSCPMappingTableEntry": oriQoSDot1DToIPDSCPMappingTableEntry,
       "oriQoSDot1DToIPDSCPMappingTableIndex": oriQoSDot1DToIPDSCPMappingTableIndex,
       "oriQoSDot1DToIPDSCPPriority": oriQoSDot1DToIPDSCPPriority,
       "oriQoSIPDSCPLowerLimit": oriQoSIPDSCPLowerLimit,
       "oriQoSIPDSCPUpperLimit": oriQoSIPDSCPUpperLimit,
       "oriQoSDot1DToIPDSCPMappingTableRowStatus": oriQoSDot1DToIPDSCPMappingTableRowStatus,
       "orinocoDHCP": orinocoDHCP,
       "orinocoDHCPServer": orinocoDHCPServer,
       "oriDHCPServerStatus": oriDHCPServerStatus,
       "oriDHCPServerIPPoolTable": oriDHCPServerIPPoolTable,
       "oriDHCPServerIPPoolTableEntry": oriDHCPServerIPPoolTableEntry,
       "oriDHCPServerIPPoolTableIndex": oriDHCPServerIPPoolTableIndex,
       "oriDHCPServerIPPoolTableStartIPAddress": oriDHCPServerIPPoolTableStartIPAddress,
       "oriDHCPServerIPPoolTableEndIPAddress": oriDHCPServerIPPoolTableEndIPAddress,
       "oriDHCPServerIPPoolTableWidth": oriDHCPServerIPPoolTableWidth,
       "oriDHCPServerIPPoolTableDefaultLeaseTime": oriDHCPServerIPPoolTableDefaultLeaseTime,
       "oriDHCPServerIPPoolTableMaximumLeaseTime": oriDHCPServerIPPoolTableMaximumLeaseTime,
       "oriDHCPServerIPPoolTableComment": oriDHCPServerIPPoolTableComment,
       "oriDHCPServerIPPoolTableEntryStatus": oriDHCPServerIPPoolTableEntryStatus,
       "oriDHCPServerDefaultGatewayIPAddress": oriDHCPServerDefaultGatewayIPAddress,
       "oriDHCPServerSubnetMask": oriDHCPServerSubnetMask,
       "oriDHCPServerNumIPPoolTableEntries": oriDHCPServerNumIPPoolTableEntries,
       "oriDHCPServerPrimaryDNSIPAddress": oriDHCPServerPrimaryDNSIPAddress,
       "oriDHCPServerSecondaryDNSIPAddress": oriDHCPServerSecondaryDNSIPAddress,
       "orinocoDHCPClient": orinocoDHCPClient,
       "oriDHCPClientID": oriDHCPClientID,
       "oriDHCPClientInterfaceBitmask": oriDHCPClientInterfaceBitmask,
       "orinocoDHCPRelay": orinocoDHCPRelay,
       "oriDHCPRelayStatus": oriDHCPRelayStatus,
       "oriDHCPRelayDHCPServerTable": oriDHCPRelayDHCPServerTable,
       "oriDHCPRelayDHCPServerTableEntry": oriDHCPRelayDHCPServerTableEntry,
       "oriDHCPRelayDHCPServerTableIndex": oriDHCPRelayDHCPServerTableIndex,
       "oriDHCPRelayDHCPServerTableIpAddress": oriDHCPRelayDHCPServerTableIpAddress,
       "oriDHCPRelayDHCPServerTableComment": oriDHCPRelayDHCPServerTableComment,
       "oriDHCPRelayDHCPServerTableEntryStatus": oriDHCPRelayDHCPServerTableEntryStatus,
       "orinocoHTTP": orinocoHTTP,
       "oriHTTPInterfaceBitmask": oriHTTPInterfaceBitmask,
       "oriHTTPPassword": oriHTTPPassword,
       "oriHTTPPort": oriHTTPPort,
       "oriHTTPWebSitenameTable": oriHTTPWebSitenameTable,
       "oriHTTPWebSitenameTableEntry": oriHTTPWebSitenameTableEntry,
       "oriHTTPWebSitenameTableIndex": oriHTTPWebSitenameTableIndex,
       "oriHTTPWebSiteFilename": oriHTTPWebSiteFilename,
       "oriHTTPWebSiteLanguage": oriHTTPWebSiteLanguage,
       "oriHTTPWebSiteDescription": oriHTTPWebSiteDescription,
       "oriHTTPWebSitenameTableStatus": oriHTTPWebSitenameTableStatus,
       "oriHTTPRefreshDelay": oriHTTPRefreshDelay,
       "oriHTTPHelpInformationLink": oriHTTPHelpInformationLink,
       "oriHTTPSSLStatus": oriHTTPSSLStatus,
       "oriHTTPSSLPassphrase": oriHTTPSSLPassphrase,
       "oriHTTPSetupWizardStatus": oriHTTPSetupWizardStatus,
       "oriHTTPRADIUSAccessControl": oriHTTPRADIUSAccessControl,
       "orinocoWDS": orinocoWDS,
       "oriWDSSetupTable": oriWDSSetupTable,
       "oriWDSSetupTableEntry": oriWDSSetupTableEntry,
       "oriWDSSetupTablePortIndex": oriWDSSetupTablePortIndex,
       "oriWDSSetupTableEntryStatus": oriWDSSetupTableEntryStatus,
       "oriWDSSetupTablePartnerMACAddress": oriWDSSetupTablePartnerMACAddress,
       "oriWDSSecurityTable": oriWDSSecurityTable,
       "oriWDSSecurityTableEntry": oriWDSSecurityTableEntry,
       "oriWDSSecurityTableSecurityMode": oriWDSSecurityTableSecurityMode,
       "oriWDSSecurityTableEncryptionKey0": oriWDSSecurityTableEncryptionKey0,
       "orinocoTrap": orinocoTrap,
       "oriTrapVariable": oriTrapVariable,
       "oriGenericTrapVariable": oriGenericTrapVariable,
       "oriTrapVarMACAddress": oriTrapVarMACAddress,
       "oriTrapVarTFTPIPAddress": oriTrapVarTFTPIPAddress,
       "oriTrapVarTFTPFilename": oriTrapVarTFTPFilename,
       "oriTrapVarTFTPOperation": oriTrapVarTFTPOperation,
       "oriTrapVarUnauthorizedManagerIPaddress": oriTrapVarUnauthorizedManagerIPaddress,
       "oriTrapVarFailedAuthenticationType": oriTrapVarFailedAuthenticationType,
       "oriTrapVarUnAuthorizedManagerCount": oriTrapVarUnAuthorizedManagerCount,
       "oriTrapVarTaskSuspended": oriTrapVarTaskSuspended,
       "oriConfigurationTrapsStatus": oriConfigurationTrapsStatus,
       "oriSecurityTrapsStatus": oriSecurityTrapsStatus,
       "oriWirelessIfTrapsStatus": oriWirelessIfTrapsStatus,
       "oriOperationalTrapsStatus": oriOperationalTrapsStatus,
       "oriFlashMemoryTrapsStatus": oriFlashMemoryTrapsStatus,
       "oriTFTPTrapsStatus": oriTFTPTrapsStatus,
       "oriTrapsImageStatus": oriTrapsImageStatus,
       "oriTrapVarUnauthorizedClientMACAddress": oriTrapVarUnauthorizedClientMACAddress,
       "oriTrapVarWirelessCard": oriTrapVarWirelessCard,
       "oriADSLIfTrapsStatus": oriADSLIfTrapsStatus,
       "oriWORPTrapsStatus": oriWORPTrapsStatus,
       "oriTrapVarInterface": oriTrapVarInterface,
       "oriTrapVarBatchCLIFilename": oriTrapVarBatchCLIFilename,
       "oriTrapVarBatchCLIMessage": oriTrapVarBatchCLIMessage,
       "oriTrapVarBatchCLILineNumber": oriTrapVarBatchCLILineNumber,
       "oriTrapVarDHCPServerIPAddress": oriTrapVarDHCPServerIPAddress,
       "oriTrapVarIPAddress": oriTrapVarIPAddress,
       "oriTrapVarSubnetMask": oriTrapVarSubnetMask,
       "oriTrapVarDefaultRouterIPAddress": oriTrapVarDefaultRouterIPAddress,
       "oriConfigurationTraps": oriConfigurationTraps,
       "oriTrapDNSIPNotConfigured": oriTrapDNSIPNotConfigured,
       "oriTrapRADIUSAuthenticationNotConfigured": oriTrapRADIUSAuthenticationNotConfigured,
       "oriTrapRADIUSAccountingNotConfigured": oriTrapRADIUSAccountingNotConfigured,
       "oriTrapDuplicateIPAddressEncountered": oriTrapDuplicateIPAddressEncountered,
       "oriTrapDHCPRelayServerTableNotConfigured": oriTrapDHCPRelayServerTableNotConfigured,
       "oriTrapWORPIfNetworkSecretNotConfigured": oriTrapWORPIfNetworkSecretNotConfigured,
       "oriTrapVLANIDInvalidConfiguration": oriTrapVLANIDInvalidConfiguration,
       "oriTrapAutoConfigFailure": oriTrapAutoConfigFailure,
       "oriTrapBatchExecFailure": oriTrapBatchExecFailure,
       "oriTrapBatchFileExecStart": oriTrapBatchFileExecStart,
       "oriTrapBatchFileExecEnd": oriTrapBatchFileExecEnd,
       "oriSecurityTraps": oriSecurityTraps,
       "oriTrapInvalidEncryptionKey": oriTrapInvalidEncryptionKey,
       "oriTrapAuthenticationFailure": oriTrapAuthenticationFailure,
       "oriTrapUnauthorizedManagerDetected": oriTrapUnauthorizedManagerDetected,
       "oriTrapRADScanComplete": oriTrapRADScanComplete,
       "oriTrapRADScanResults": oriTrapRADScanResults,
       "oriTrapRogueScanStationDetected": oriTrapRogueScanStationDetected,
       "oriTrapRogueScanCycleComplete": oriTrapRogueScanCycleComplete,
       "oriWirelessIfTraps": oriWirelessIfTraps,
       "oriTrapWLCNotPresent": oriTrapWLCNotPresent,
       "oriTrapWLCFailure": oriTrapWLCFailure,
       "oriTrapWLCRemoval": oriTrapWLCRemoval,
       "oriTrapWLCIncompatibleFirmware": oriTrapWLCIncompatibleFirmware,
       "oriTrapWLCVoltageDiscrepancy": oriTrapWLCVoltageDiscrepancy,
       "oriTrapWLCIncompatibleVendor": oriTrapWLCIncompatibleVendor,
       "oriTrapWLCFirmwareDownloadFailure": oriTrapWLCFirmwareDownloadFailure,
       "oriTrapWLCFirmwareFailure": oriTrapWLCFirmwareFailure,
       "oriTrapWLCRadarInterferenceDetected": oriTrapWLCRadarInterferenceDetected,
       "oriOperationalTraps": oriOperationalTraps,
       "oriTrapUnrecoverableSoftwareErrorDetected": oriTrapUnrecoverableSoftwareErrorDetected,
       "oriTrapRADIUSServerNotResponding": oriTrapRADIUSServerNotResponding,
       "oriTrapModuleNotInitialized": oriTrapModuleNotInitialized,
       "oriTrapDeviceRebooting": oriTrapDeviceRebooting,
       "oriTrapTaskSuspended": oriTrapTaskSuspended,
       "oriTrapBootPFailed": oriTrapBootPFailed,
       "oriTrapDHCPFailed": oriTrapDHCPFailed,
       "oriTrapDNSClientLookupFailure": oriTrapDNSClientLookupFailure,
       "oriTrapSNTPFailure": oriTrapSNTPFailure,
       "oriTrapMaximumNumberOfSubscribersReached": oriTrapMaximumNumberOfSubscribersReached,
       "oriTrapSSLInitializationFailure": oriTrapSSLInitializationFailure,
       "oriTrapWirelessServiceShutdown": oriTrapWirelessServiceShutdown,
       "oriTrapWirelessServiceResumed": oriTrapWirelessServiceResumed,
       "oriTrapSSHInitializationStatus": oriTrapSSHInitializationStatus,
       "oriTrapVLANIDUserAssignment": oriTrapVLANIDUserAssignment,
       "oriTrapDHCPLeaseRenewal": oriTrapDHCPLeaseRenewal,
       "oriTrapTemperatureAlert": oriTrapTemperatureAlert,
       "oriFlashTraps": oriFlashTraps,
       "oriTrapFlashMemoryEmpty": oriTrapFlashMemoryEmpty,
       "oriTrapFlashMemoryCorrupted": oriTrapFlashMemoryCorrupted,
       "oriTrapFlashMemoryRestoringLastKnownGoodConfiguration": oriTrapFlashMemoryRestoringLastKnownGoodConfiguration,
       "oriTFTPTraps": oriTFTPTraps,
       "oriTrapTFTPFailedOperation": oriTrapTFTPFailedOperation,
       "oriTrapTFTPOperationInitiated": oriTrapTFTPOperationInitiated,
       "oriTrapTFTPOperationCompleted": oriTrapTFTPOperationCompleted,
       "oriMiscTraps": oriMiscTraps,
       "oriImageTraps": oriImageTraps,
       "oriTrapZeroSizeImage": oriTrapZeroSizeImage,
       "oriTrapInvalidImage": oriTrapInvalidImage,
       "oriTrapImageTooLarge": oriTrapImageTooLarge,
       "oriTrapIncompatibleImage": oriTrapIncompatibleImage,
       "oriTrapInvalidImageDigitalSignature": oriTrapInvalidImageDigitalSignature,
       "oriWORPTraps": oriWORPTraps,
       "oriWORPStationRegister": oriWORPStationRegister,
       "oriWORPStationDeRegister": oriWORPStationDeRegister,
       "oriSysFeatureTraps": oriSysFeatureTraps,
       "oriTrapIncompatibleLicenseFile": oriTrapIncompatibleLicenseFile,
       "oriTrapFeatureNotSupported": oriTrapFeatureNotSupported,
       "oriTrapZeroLicenseFiles": oriTrapZeroLicenseFiles,
       "oriTrapInvalidLicenseFile": oriTrapInvalidLicenseFile,
       "oriTrapUselessLicense": oriTrapUselessLicense,
       "orinocoIPARP": orinocoIPARP,
       "oriProxyARPStatus": oriProxyARPStatus,
       "oriIPARPFilteringStatus": oriIPARPFilteringStatus,
       "oriIPARPFilteringIPAddress": oriIPARPFilteringIPAddress,
       "oriIPARPFilteringSubnetMask": oriIPARPFilteringSubnetMask,
       "orinocoSpanningTree": orinocoSpanningTree,
       "oriSpanningTreeStatus": oriSpanningTreeStatus,
       "orinocoSecurity": orinocoSecurity,
       "oriSecurityConfiguration": oriSecurityConfiguration,
       "oriSecurityEncryptionKeyLengthTable": oriSecurityEncryptionKeyLengthTable,
       "oriSecurityEncryptionKeyLengthTableEntry": oriSecurityEncryptionKeyLengthTableEntry,
       "oriSecurityEncryptionKeyLength": oriSecurityEncryptionKeyLength,
       "oriSecurityRekeyingInterval": oriSecurityRekeyingInterval,
       "orinocoRAD": orinocoRAD,
       "oriRADStatus": oriRADStatus,
       "oriRADInterval": oriRADInterval,
       "oriRADInterfaceBitmask": oriRADInterfaceBitmask,
       "oriRADLastSuccessfulScanTime": oriRADLastSuccessfulScanTime,
       "oriRADAccessPointCount": oriRADAccessPointCount,
       "oriRADScanResultsTable": oriRADScanResultsTable,
       "oriRADScanResultsTableEntry": oriRADScanResultsTableEntry,
       "oriRADScanResultsTableIndex": oriRADScanResultsTableIndex,
       "oriRADScanResultsMACAddress": oriRADScanResultsMACAddress,
       "oriRADScanResultsFrequencyChannel": oriRADScanResultsFrequencyChannel,
       "oriSecurityConfigTable": oriSecurityConfigTable,
       "oriSecurityConfigTableEntry": oriSecurityConfigTableEntry,
       "oriSecurityConfigTableSupportedSecurityModes": oriSecurityConfigTableSupportedSecurityModes,
       "oriSecurityConfigTableSecurityMode": oriSecurityConfigTableSecurityMode,
       "oriSecurityConfigTableRekeyingInterval": oriSecurityConfigTableRekeyingInterval,
       "oriSecurityConfigTableEncryptionKeyLength": oriSecurityConfigTableEncryptionKeyLength,
       "oriSecurityHwConfigResetStatus": oriSecurityHwConfigResetStatus,
       "oriSecurityHwConfigResetPassword": oriSecurityHwConfigResetPassword,
       "orinocoRogueScan": orinocoRogueScan,
       "oriRogueScanConfigTable": oriRogueScanConfigTable,
       "oriRogueScanConfigTableEntry": oriRogueScanConfigTableEntry,
       "oriRogueScanConfigTableScanMode": oriRogueScanConfigTableScanMode,
       "oriRogueScanConfigTableScanCycleTime": oriRogueScanConfigTableScanCycleTime,
       "oriRogueScanConfigTableScanStatus": oriRogueScanConfigTableScanStatus,
       "oriRogueScanStationCountWirelessCardA": oriRogueScanStationCountWirelessCardA,
       "oriRogueScanStationCountWirelessCardB": oriRogueScanStationCountWirelessCardB,
       "oriRogueScanResultsTableAgingTime": oriRogueScanResultsTableAgingTime,
       "oriRogueScanResultsTableClearEntries": oriRogueScanResultsTableClearEntries,
       "oriRogueScanResultsNotificationMode": oriRogueScanResultsNotificationMode,
       "oriRogueScanResultsTrapReportType": oriRogueScanResultsTrapReportType,
       "oriRogueScanResultsTable": oriRogueScanResultsTable,
       "oriRogueScanResultsTableEntry": oriRogueScanResultsTableEntry,
       "oriRogueScanResultsTableIndex": oriRogueScanResultsTableIndex,
       "oriRogueScanResultsStationType": oriRogueScanResultsStationType,
       "oriRogueScanResultsMACAddress": oriRogueScanResultsMACAddress,
       "oriRogueScanResultsFrequencyChannel": oriRogueScanResultsFrequencyChannel,
       "oriRogueScanResultsSNR": oriRogueScanResultsSNR,
       "oriRogueScanResultsBSSID": oriRogueScanResultsBSSID,
       "oriSecurityProfileTable": oriSecurityProfileTable,
       "oriSecurityProfileTableEntry": oriSecurityProfileTableEntry,
       "oriSecurityProfileTableIndex": oriSecurityProfileTableIndex,
       "oriSecurityProfileTableSecModeIndex": oriSecurityProfileTableSecModeIndex,
       "oriSecurityProfileTableAuthenticationMode": oriSecurityProfileTableAuthenticationMode,
       "oriSecurityProfileTableCipherMode": oriSecurityProfileTableCipherMode,
       "oriSecurityProfileTableEncryptionKey0": oriSecurityProfileTableEncryptionKey0,
       "oriSecurityProfileTableEncryptionKey1": oriSecurityProfileTableEncryptionKey1,
       "oriSecurityProfileTableEncryptionKey2": oriSecurityProfileTableEncryptionKey2,
       "oriSecurityProfileTableEncryptionKey3": oriSecurityProfileTableEncryptionKey3,
       "oriSecurityProfileTableEncryptionTxKey": oriSecurityProfileTableEncryptionTxKey,
       "oriSecurityProfileTableEncryptionKeyLength": oriSecurityProfileTableEncryptionKeyLength,
       "oriSecurityProfileTablePSKValue": oriSecurityProfileTablePSKValue,
       "oriSecurityProfileTablePSKPassPhrase": oriSecurityProfileTablePSKPassPhrase,
       "oriSecurityProfileTableStatus": oriSecurityProfileTableStatus,
       "oriSecurityProfileFourWEPKeySupport": oriSecurityProfileFourWEPKeySupport,
       "orinocoPPPoE": orinocoPPPoE,
       "oriPPPoEStatus": oriPPPoEStatus,
       "oriPPPoEMaximumNumberOfSessions": oriPPPoEMaximumNumberOfSessions,
       "oriPPPoENumberOfActiveSessions": oriPPPoENumberOfActiveSessions,
       "oriPPPoESessionTable": oriPPPoESessionTable,
       "oriPPPoESessionTableEntry": oriPPPoESessionTableEntry,
       "oriPPPoESessionTableIndex": oriPPPoESessionTableIndex,
       "oriPPPoESessionWANConnectMode": oriPPPoESessionWANConnectMode,
       "oriPPPoESessionIdleTimeOut": oriPPPoESessionIdleTimeOut,
       "oriPPPoESessionConnectTime": oriPPPoESessionConnectTime,
       "oriPPPoESessionConnectTimeLimitation": oriPPPoESessionConnectTimeLimitation,
       "oriPPPoESessionConfigPADITxInterval": oriPPPoESessionConfigPADITxInterval,
       "oriPPPoESessionConfigPADIMaxNumberOfRetries": oriPPPoESessionConfigPADIMaxNumberOfRetries,
       "oriPPPoESessionBindingsNumberPADITx": oriPPPoESessionBindingsNumberPADITx,
       "oriPPPoESessionBindingsNumberPADTTx": oriPPPoESessionBindingsNumberPADTTx,
       "oriPPPoESessionBindingsNumberServiceNameErrors": oriPPPoESessionBindingsNumberServiceNameErrors,
       "oriPPPoESessionBindingsNumberACSystemErrors": oriPPPoESessionBindingsNumberACSystemErrors,
       "oriPPPoESessionBindingsNumberGenericErrorsRx": oriPPPoESessionBindingsNumberGenericErrorsRx,
       "oriPPPoESessionBindingsNumberGenericErrorsTx": oriPPPoESessionBindingsNumberGenericErrorsTx,
       "oriPPPoESessionBindingsNumberMalformedPackets": oriPPPoESessionBindingsNumberMalformedPackets,
       "oriPPPoESessionBindingsNumberMultiplePADORx": oriPPPoESessionBindingsNumberMultiplePADORx,
       "oriPPPoESessionUserName": oriPPPoESessionUserName,
       "oriPPPoESessionUserNamePassword": oriPPPoESessionUserNamePassword,
       "oriPPPoESessionServiceName": oriPPPoESessionServiceName,
       "oriPPPoESessionISPName": oriPPPoESessionISPName,
       "oriPPPoESessionTableStatus": oriPPPoESessionTableStatus,
       "oriPPPoESessionWANManualConnect": oriPPPoESessionWANManualConnect,
       "oriPPPoESessionWANConnectionStatus": oriPPPoESessionWANConnectionStatus,
       "oriPPPoEMACtoSessionTable": oriPPPoEMACtoSessionTable,
       "oriPPPoEMACtoSessionTableEntry": oriPPPoEMACtoSessionTableEntry,
       "oriPPPoEMACtoSessionTableIndex": oriPPPoEMACtoSessionTableIndex,
       "oriPPPoEMACtoSessionTableMACAddress": oriPPPoEMACtoSessionTableMACAddress,
       "oriPPPoEMACtoSessionTableISPName": oriPPPoEMACtoSessionTableISPName,
       "oriPPPoEMACtoSessionTableStatus": oriPPPoEMACtoSessionTableStatus,
       "orinocoConfig": orinocoConfig,
       "oriConfigResetToDefaults": oriConfigResetToDefaults,
       "oriConfigFileTable": oriConfigFileTable,
       "oriConfigFileTableEntry": oriConfigFileTableEntry,
       "oriConfigFileTableIndex": oriConfigFileTableIndex,
       "oriConfigFileName": oriConfigFileName,
       "oriConfigFileStatus": oriConfigFileStatus,
       "oriConfigSaveFile": oriConfigSaveFile,
       "oriConfigSaveKnownGood": oriConfigSaveKnownGood,
       "orinocoDNS": orinocoDNS,
       "oriDNSRedirectStatus": oriDNSRedirectStatus,
       "oriDNSRedirectMaxResponseWaitTime": oriDNSRedirectMaxResponseWaitTime,
       "oriDNSPrimaryDNSIPAddress": oriDNSPrimaryDNSIPAddress,
       "oriDNSSecondaryDNSIPAddress": oriDNSSecondaryDNSIPAddress,
       "orinocoDNSClient": orinocoDNSClient,
       "oriDNSClientStatus": oriDNSClientStatus,
       "oriDNSClientPrimaryServerIPAddress": oriDNSClientPrimaryServerIPAddress,
       "oriDNSClientSecondaryServerIPAddress": oriDNSClientSecondaryServerIPAddress,
       "oriDNSClientDefaultDomainName": oriDNSClientDefaultDomainName,
       "orinocoAOL": orinocoAOL,
       "oriAOLNATALGStatus": oriAOLNATALGStatus,
       "orinocoNAT": orinocoNAT,
       "oriNATStatus": oriNATStatus,
       "oriNATType": oriNATType,
       "oriNATStaticBindStatus": oriNATStaticBindStatus,
       "oriNATPublicIPAddress": oriNATPublicIPAddress,
       "oriNATStaticIPBindTable": oriNATStaticIPBindTable,
       "oriNATStaticIPBindTableEntry": oriNATStaticIPBindTableEntry,
       "oriNATStaticIPBindTableIndex": oriNATStaticIPBindTableIndex,
       "oriNATStaticIPBindLocalAddress": oriNATStaticIPBindLocalAddress,
       "oriNATStaticIPBindRemoteAddress": oriNATStaticIPBindRemoteAddress,
       "oriNATStaticIPBindTableEntryStatus": oriNATStaticIPBindTableEntryStatus,
       "oriNATStaticPortBindTable": oriNATStaticPortBindTable,
       "oriNATStaticPortBindTableEntry": oriNATStaticPortBindTableEntry,
       "oriNATStaticPortBindTableIndex": oriNATStaticPortBindTableIndex,
       "oriNATStaticPortBindLocalAddress": oriNATStaticPortBindLocalAddress,
       "oriNATStaticPortBindStartPortNumber": oriNATStaticPortBindStartPortNumber,
       "oriNATStaticPortBindEndPortNumber": oriNATStaticPortBindEndPortNumber,
       "oriNATStaticPortBindPortType": oriNATStaticPortBindPortType,
       "oriNATStaticPortBindTableEntryStatus": oriNATStaticPortBindTableEntryStatus,
       "orinocoSpectraLink": orinocoSpectraLink,
       "oriSpectraLinkStatus": oriSpectraLinkStatus,
       "oriSpectraLinkLegacyDeviceSupport": oriSpectraLinkLegacyDeviceSupport,
       "orinocoVLAN": orinocoVLAN,
       "oriVLANStatus": oriVLANStatus,
       "oriVLANMgmtIdentifier": oriVLANMgmtIdentifier,
       "oriVLANIDTable": oriVLANIDTable,
       "oriVLANIDTableEntry": oriVLANIDTableEntry,
       "oriVLANIDTableIndex": oriVLANIDTableIndex,
       "oriVLANIDTableIdentifier": oriVLANIDTableIdentifier,
       "orinocoDMZ": orinocoDMZ,
       "oriDMZHostTable": oriDMZHostTable,
       "oriDMZHostTableEntry": oriDMZHostTableEntry,
       "oriDMZHostTableIndex": oriDMZHostTableIndex,
       "oriDMZHostTableHostIP": oriDMZHostTableHostIP,
       "oriDMZHostTableComment": oriDMZHostTableComment,
       "oriDMZHostTableEntryStatus": oriDMZHostTableEntryStatus,
       "orinocoOEM": orinocoOEM,
       "oriOEMName": oriOEMName,
       "oriOEMHomeUrl": oriOEMHomeUrl,
       "oriOEMProductName": oriOEMProductName,
       "oriOEMProductModel": oriOEMProductModel,
       "oriOEMLogoImageFile": oriOEMLogoImageFile,
       "oriOEMNoNavLogoImageFile": oriOEMNoNavLogoImageFile,
       "orinocoStationStatistics": orinocoStationStatistics,
       "oriStationStatTable": oriStationStatTable,
       "oriStationStatTableEntry": oriStationStatTableEntry,
       "oriStationStatTableIndex": oriStationStatTableIndex,
       "oriStationStatTableMACAddress": oriStationStatTableMACAddress,
       "oriStationStatTableIPAddress": oriStationStatTableIPAddress,
       "oriStationStatTableInterface": oriStationStatTableInterface,
       "oriStationStatTableName": oriStationStatTableName,
       "oriStationStatTableType": oriStationStatTableType,
       "oriStationStatTableMACProtocol": oriStationStatTableMACProtocol,
       "oriStationStatTableAdminStatus": oriStationStatTableAdminStatus,
       "oriStationStatTableOperStatus": oriStationStatTableOperStatus,
       "oriStationStatTableLastChange": oriStationStatTableLastChange,
       "oriStationStatTableLastState": oriStationStatTableLastState,
       "oriStationStatTableInOctets": oriStationStatTableInOctets,
       "oriStationStatTableInUcastPkts": oriStationStatTableInUcastPkts,
       "oriStationStatTableInNUcastPkts": oriStationStatTableInNUcastPkts,
       "oriStationStatTableInDiscards": oriStationStatTableInDiscards,
       "oriStationStatTableOutOctets": oriStationStatTableOutOctets,
       "oriStationStatTableOutUcastPkts": oriStationStatTableOutUcastPkts,
       "oriStationStatTableOutNUcastPkts": oriStationStatTableOutNUcastPkts,
       "oriStationStatTableOutDiscards": oriStationStatTableOutDiscards,
       "oriStationStatTableInSignal": oriStationStatTableInSignal,
       "oriStationStatTableInNoise": oriStationStatTableInNoise,
       "oriStationStatTableRemoteSignal": oriStationStatTableRemoteSignal,
       "oriStationStatTableRemoteNoise": oriStationStatTableRemoteNoise,
       "oriStationStatTableLastInPktTime": oriStationStatTableLastInPktTime,
       "oriStationStatStatus": oriStationStatStatus,
       "oriStationStatNumberOfClients": oriStationStatNumberOfClients,
       "orinocoSNTP": orinocoSNTP,
       "oriSNTPStatus": oriSNTPStatus,
       "oriSNTPPrimaryServerNameOrIPAddress": oriSNTPPrimaryServerNameOrIPAddress,
       "oriSNTPSecondaryServerNameOrIPAddress": oriSNTPSecondaryServerNameOrIPAddress,
       "oriSNTPTimeZone": oriSNTPTimeZone,
       "oriSNTPDateAndTime": oriSNTPDateAndTime,
       "oriSNTPDayLightSavingTime": oriSNTPDayLightSavingTime,
       "oriSNTPYear": oriSNTPYear,
       "oriSNTPMonth": oriSNTPMonth,
       "oriSNTPDay": oriSNTPDay,
       "oriSNTPHour": oriSNTPHour,
       "oriSNTPMinutes": oriSNTPMinutes,
       "oriSNTPSeconds": oriSNTPSeconds,
       "orinocoNotifications": orinocoNotifications,
       "orinocoConformance": orinocoConformance,
       "orinocoGroups": orinocoGroups,
       "orinocoCompliances": orinocoCompliances,
       "orinocoProducts": orinocoProducts,
       "ap1000": ap1000,
       "rg1000": rg1000,
       "as1000": as1000,
       "as2000": as2000,
       "ap500": ap500,
       "ap2000": ap2000,
       "bg2000": bg2000,
       "rg1100": rg1100,
       "tmp11": tmp11,
       "ap600": ap600,
       "ap2500": ap2500,
       "ap4000": ap4000,
       "ap700": ap700}
)
