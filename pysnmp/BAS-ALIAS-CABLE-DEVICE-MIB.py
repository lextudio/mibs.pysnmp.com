# SNMP MIB module (BAS-ALIAS-CABLE-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-ALIAS-CABLE-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:15 2024
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

(BasChassisId,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 basAliasDocsCd) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basAliasDocsCd")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

basAliasDocsCdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_BasDocsDevMIBObjects_ObjectIdentity = ObjectIdentity
basDocsDevMIBObjects = _BasDocsDevMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1)
)
_BasDocsDevBase_ObjectIdentity = ObjectIdentity
basDocsDevBase = _BasDocsDevBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 1)
)
_BasDocsDevBaseTable_Object = MibTable
basDocsDevBaseTable = _BasDocsDevBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    basDocsDevBaseTable.setStatus("current")
_BasDocsDevBaseEntry_Object = MibTableRow
basDocsDevBaseEntry = _BasDocsDevBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 1, 1, 1)
)
basDocsDevBaseEntry.setIndexNames(
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevChassis"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevSlot"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevIf"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevLPort"),
)
if mibBuilder.loadTexts:
    basDocsDevBaseEntry.setStatus("current")


class _BasDocsDevRole_Type(Integer32):
    """Custom type basDocsDevRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cm", 1),
          ("cmtsActive", 2),
          ("cmtsBackup", 3))
    )


_BasDocsDevRole_Type.__name__ = "Integer32"
_BasDocsDevRole_Object = MibTableColumn
basDocsDevRole = _BasDocsDevRole_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 1, 1, 1, 1),
    _BasDocsDevRole_Type()
)
basDocsDevRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevRole.setStatus("current")
_BasDocsDevDateTime_Type = DateAndTime
_BasDocsDevDateTime_Object = MibTableColumn
basDocsDevDateTime = _BasDocsDevDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 1, 1, 1, 2),
    _BasDocsDevDateTime_Type()
)
basDocsDevDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDocsDevDateTime.setStatus("current")
_BasDocsDevResetNow_Type = TruthValue
_BasDocsDevResetNow_Object = MibTableColumn
basDocsDevResetNow = _BasDocsDevResetNow_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 1, 1, 1, 3),
    _BasDocsDevResetNow_Type()
)
basDocsDevResetNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDocsDevResetNow.setStatus("current")
_BasDocsDevSerialNumber_Type = DisplayString
_BasDocsDevSerialNumber_Object = MibTableColumn
basDocsDevSerialNumber = _BasDocsDevSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 1, 1, 1, 4),
    _BasDocsDevSerialNumber_Type()
)
basDocsDevSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevSerialNumber.setStatus("current")


class _BasDocsDevSTPControl_Type(Integer32):
    """Custom type basDocsDevSTPControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noStFilterBpdu", 2),
          ("noStPassBpdu", 3),
          ("stEnabled", 1))
    )


_BasDocsDevSTPControl_Type.__name__ = "Integer32"
_BasDocsDevSTPControl_Object = MibTableColumn
basDocsDevSTPControl = _BasDocsDevSTPControl_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 1, 1, 1, 5),
    _BasDocsDevSTPControl_Type()
)
basDocsDevSTPControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDocsDevSTPControl.setStatus("current")
_BasDocsDevChassis_Type = BasChassisId
_BasDocsDevChassis_Object = MibTableColumn
basDocsDevChassis = _BasDocsDevChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 1, 1, 1, 6),
    _BasDocsDevChassis_Type()
)
basDocsDevChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevChassis.setStatus("current")
_BasDocsDevSlot_Type = BasSlotId
_BasDocsDevSlot_Object = MibTableColumn
basDocsDevSlot = _BasDocsDevSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 1, 1, 1, 7),
    _BasDocsDevSlot_Type()
)
basDocsDevSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevSlot.setStatus("current")
_BasDocsDevIf_Type = BasInterfaceId
_BasDocsDevIf_Object = MibTableColumn
basDocsDevIf = _BasDocsDevIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 1, 1, 1, 8),
    _BasDocsDevIf_Type()
)
basDocsDevIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevIf.setStatus("current")
_BasDocsDevLPort_Type = BasLogicalPortId
_BasDocsDevLPort_Object = MibTableColumn
basDocsDevLPort = _BasDocsDevLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 1, 1, 1, 9),
    _BasDocsDevLPort_Type()
)
basDocsDevLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevLPort.setStatus("current")
_BasDocsDevNmAccessTable_Object = MibTable
basDocsDevNmAccessTable = _BasDocsDevNmAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 2)
)
if mibBuilder.loadTexts:
    basDocsDevNmAccessTable.setStatus("current")
_BasDocsDevNmAccessEntry_Object = MibTableRow
basDocsDevNmAccessEntry = _BasDocsDevNmAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 2, 1)
)
basDocsDevNmAccessEntry.setIndexNames(
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevNmAccessChassis"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevNmAccessSlot"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevNmAccessIf"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevNmAccessLPort"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevNmAccessIndex"),
)
if mibBuilder.loadTexts:
    basDocsDevNmAccessEntry.setStatus("current")


class _BasDocsDevNmAccessIndex_Type(Integer32):
    """Custom type basDocsDevNmAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BasDocsDevNmAccessIndex_Type.__name__ = "Integer32"
_BasDocsDevNmAccessIndex_Object = MibTableColumn
basDocsDevNmAccessIndex = _BasDocsDevNmAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 2, 1, 1),
    _BasDocsDevNmAccessIndex_Type()
)
basDocsDevNmAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevNmAccessIndex.setStatus("current")


class _BasDocsDevNmAccessIp_Type(IpAddress):
    """Custom type basDocsDevNmAccessIp based on IpAddress"""
    defaultHexValue = "ffffffff"


_BasDocsDevNmAccessIp_Object = MibTableColumn
basDocsDevNmAccessIp = _BasDocsDevNmAccessIp_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 2, 1, 2),
    _BasDocsDevNmAccessIp_Type()
)
basDocsDevNmAccessIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevNmAccessIp.setStatus("current")


class _BasDocsDevNmAccessIpMask_Type(IpAddress):
    """Custom type basDocsDevNmAccessIpMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_BasDocsDevNmAccessIpMask_Object = MibTableColumn
basDocsDevNmAccessIpMask = _BasDocsDevNmAccessIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 2, 1, 3),
    _BasDocsDevNmAccessIpMask_Type()
)
basDocsDevNmAccessIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevNmAccessIpMask.setStatus("current")


class _BasDocsDevNmAccessCommunity_Type(DisplayString):
    """Custom type basDocsDevNmAccessCommunity based on DisplayString"""
    defaultValue = OctetString("public")


_BasDocsDevNmAccessCommunity_Object = MibTableColumn
basDocsDevNmAccessCommunity = _BasDocsDevNmAccessCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 2, 1, 4),
    _BasDocsDevNmAccessCommunity_Type()
)
basDocsDevNmAccessCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevNmAccessCommunity.setStatus("current")


class _BasDocsDevNmAccessControl_Type(Integer32):
    """Custom type basDocsDevNmAccessControl based on Integer32"""
    defaultValue = 2

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
        *(("none", 1),
          ("read", 2),
          ("readWrite", 3),
          ("roWithTraps", 4),
          ("rwWithTraps", 5),
          ("trapsOnly", 6))
    )


_BasDocsDevNmAccessControl_Type.__name__ = "Integer32"
_BasDocsDevNmAccessControl_Object = MibTableColumn
basDocsDevNmAccessControl = _BasDocsDevNmAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 2, 1, 5),
    _BasDocsDevNmAccessControl_Type()
)
basDocsDevNmAccessControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevNmAccessControl.setStatus("current")
_BasDocsDevNmAccessInterfaces_Type = OctetString
_BasDocsDevNmAccessInterfaces_Object = MibTableColumn
basDocsDevNmAccessInterfaces = _BasDocsDevNmAccessInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 2, 1, 6),
    _BasDocsDevNmAccessInterfaces_Type()
)
basDocsDevNmAccessInterfaces.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevNmAccessInterfaces.setStatus("current")
_BasDocsDevNmAccessStatus_Type = RowStatus
_BasDocsDevNmAccessStatus_Object = MibTableColumn
basDocsDevNmAccessStatus = _BasDocsDevNmAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 2, 1, 7),
    _BasDocsDevNmAccessStatus_Type()
)
basDocsDevNmAccessStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevNmAccessStatus.setStatus("current")
_BasDocsDevNmAccessChassis_Type = BasChassisId
_BasDocsDevNmAccessChassis_Object = MibTableColumn
basDocsDevNmAccessChassis = _BasDocsDevNmAccessChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 2, 1, 8),
    _BasDocsDevNmAccessChassis_Type()
)
basDocsDevNmAccessChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevNmAccessChassis.setStatus("current")
_BasDocsDevNmAccessSlot_Type = BasSlotId
_BasDocsDevNmAccessSlot_Object = MibTableColumn
basDocsDevNmAccessSlot = _BasDocsDevNmAccessSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 2, 1, 9),
    _BasDocsDevNmAccessSlot_Type()
)
basDocsDevNmAccessSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevNmAccessSlot.setStatus("current")
_BasDocsDevNmAccessIf_Type = BasInterfaceId
_BasDocsDevNmAccessIf_Object = MibTableColumn
basDocsDevNmAccessIf = _BasDocsDevNmAccessIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 2, 1, 10),
    _BasDocsDevNmAccessIf_Type()
)
basDocsDevNmAccessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevNmAccessIf.setStatus("current")
_BasDocsDevNmAccessLPort_Type = BasLogicalPortId
_BasDocsDevNmAccessLPort_Object = MibTableColumn
basDocsDevNmAccessLPort = _BasDocsDevNmAccessLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 2, 1, 11),
    _BasDocsDevNmAccessLPort_Type()
)
basDocsDevNmAccessLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevNmAccessLPort.setStatus("current")
_BasDocsDevSoftware_ObjectIdentity = ObjectIdentity
basDocsDevSoftware = _BasDocsDevSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 3)
)
_BasDocsDevSwTable_Object = MibTable
basDocsDevSwTable = _BasDocsDevSwTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    basDocsDevSwTable.setStatus("current")
_BasDocsDevSwEntry_Object = MibTableRow
basDocsDevSwEntry = _BasDocsDevSwEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 3, 1, 1)
)
basDocsDevSwEntry.setIndexNames(
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevSwChassis"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevSwSlot"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevSwIf"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevSwLPort"),
)
if mibBuilder.loadTexts:
    basDocsDevSwEntry.setStatus("current")
_BasDocsDevSwServer_Type = IpAddress
_BasDocsDevSwServer_Object = MibTableColumn
basDocsDevSwServer = _BasDocsDevSwServer_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 3, 1, 1, 1),
    _BasDocsDevSwServer_Type()
)
basDocsDevSwServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDocsDevSwServer.setStatus("current")


class _BasDocsDevSwFilename_Type(DisplayString):
    """Custom type basDocsDevSwFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BasDocsDevSwFilename_Type.__name__ = "DisplayString"
_BasDocsDevSwFilename_Object = MibTableColumn
basDocsDevSwFilename = _BasDocsDevSwFilename_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 3, 1, 1, 2),
    _BasDocsDevSwFilename_Type()
)
basDocsDevSwFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDocsDevSwFilename.setStatus("current")


class _BasDocsDevSwAdminStatus_Type(Integer32):
    """Custom type basDocsDevSwAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowProvisioningUpgrade", 2),
          ("ignoreProvisioningUpgrade", 3),
          ("upgradeFromMgt", 1))
    )


_BasDocsDevSwAdminStatus_Type.__name__ = "Integer32"
_BasDocsDevSwAdminStatus_Object = MibTableColumn
basDocsDevSwAdminStatus = _BasDocsDevSwAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 3, 1, 1, 3),
    _BasDocsDevSwAdminStatus_Type()
)
basDocsDevSwAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDocsDevSwAdminStatus.setStatus("current")


class _BasDocsDevSwOperStatus_Type(Integer32):
    """Custom type basDocsDevSwOperStatus based on Integer32"""
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
        *(("completeFromMgt", 3),
          ("completeFromProvisioning", 2),
          ("failed", 4),
          ("inProgress", 1),
          ("other", 5))
    )


_BasDocsDevSwOperStatus_Type.__name__ = "Integer32"
_BasDocsDevSwOperStatus_Object = MibTableColumn
basDocsDevSwOperStatus = _BasDocsDevSwOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 3, 1, 1, 4),
    _BasDocsDevSwOperStatus_Type()
)
basDocsDevSwOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevSwOperStatus.setStatus("current")
_BasDocsDevSwChassis_Type = BasChassisId
_BasDocsDevSwChassis_Object = MibTableColumn
basDocsDevSwChassis = _BasDocsDevSwChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 3, 1, 1, 5),
    _BasDocsDevSwChassis_Type()
)
basDocsDevSwChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevSwChassis.setStatus("current")
_BasDocsDevSwSlot_Type = BasSlotId
_BasDocsDevSwSlot_Object = MibTableColumn
basDocsDevSwSlot = _BasDocsDevSwSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 3, 1, 1, 6),
    _BasDocsDevSwSlot_Type()
)
basDocsDevSwSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevSwSlot.setStatus("current")
_BasDocsDevSwIf_Type = BasInterfaceId
_BasDocsDevSwIf_Object = MibTableColumn
basDocsDevSwIf = _BasDocsDevSwIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 3, 1, 1, 7),
    _BasDocsDevSwIf_Type()
)
basDocsDevSwIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevSwIf.setStatus("current")
_BasDocsDevSwLPort_Type = BasLogicalPortId
_BasDocsDevSwLPort_Object = MibTableColumn
basDocsDevSwLPort = _BasDocsDevSwLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 3, 1, 1, 8),
    _BasDocsDevSwLPort_Type()
)
basDocsDevSwLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevSwLPort.setStatus("current")
_BasDocsDevServer_ObjectIdentity = ObjectIdentity
basDocsDevServer = _BasDocsDevServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 4)
)
_BasDocsDevServerTable_Object = MibTable
basDocsDevServerTable = _BasDocsDevServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    basDocsDevServerTable.setStatus("current")
_BasDocsDevServerEntry_Object = MibTableRow
basDocsDevServerEntry = _BasDocsDevServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 4, 1, 1)
)
basDocsDevServerEntry.setIndexNames(
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevServerChassis"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevServerSlot"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevServerIf"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevServerLPort"),
)
if mibBuilder.loadTexts:
    basDocsDevServerEntry.setStatus("current")


class _BasDocsDevServerBootState_Type(Integer32):
    """Custom type basDocsDevServerBootState based on Integer32"""
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
        *(("disabled", 2),
          ("forwardingDenied", 8),
          ("operational", 1),
          ("other", 9),
          ("refusedByCmts", 7),
          ("unknown", 10),
          ("waitingForDhcpOffer", 3),
          ("waitingForDhcpResponse", 4),
          ("waitingForTftp", 6),
          ("waitingForTimeServer", 5))
    )


_BasDocsDevServerBootState_Type.__name__ = "Integer32"
_BasDocsDevServerBootState_Object = MibTableColumn
basDocsDevServerBootState = _BasDocsDevServerBootState_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 4, 1, 1, 1),
    _BasDocsDevServerBootState_Type()
)
basDocsDevServerBootState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevServerBootState.setStatus("current")
_BasDocsDevServerDhcp_Type = IpAddress
_BasDocsDevServerDhcp_Object = MibTableColumn
basDocsDevServerDhcp = _BasDocsDevServerDhcp_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 4, 1, 1, 2),
    _BasDocsDevServerDhcp_Type()
)
basDocsDevServerDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevServerDhcp.setStatus("current")
_BasDocsDevServerTime_Type = IpAddress
_BasDocsDevServerTime_Object = MibTableColumn
basDocsDevServerTime = _BasDocsDevServerTime_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 4, 1, 1, 3),
    _BasDocsDevServerTime_Type()
)
basDocsDevServerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevServerTime.setStatus("current")
_BasDocsDevServerTftp_Type = IpAddress
_BasDocsDevServerTftp_Object = MibTableColumn
basDocsDevServerTftp = _BasDocsDevServerTftp_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 4, 1, 1, 4),
    _BasDocsDevServerTftp_Type()
)
basDocsDevServerTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevServerTftp.setStatus("current")
_BasDocsDevServerConfigFile_Type = DisplayString
_BasDocsDevServerConfigFile_Object = MibTableColumn
basDocsDevServerConfigFile = _BasDocsDevServerConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 4, 1, 1, 5),
    _BasDocsDevServerConfigFile_Type()
)
basDocsDevServerConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevServerConfigFile.setStatus("current")
_BasDocsDevServerChassis_Type = BasChassisId
_BasDocsDevServerChassis_Object = MibTableColumn
basDocsDevServerChassis = _BasDocsDevServerChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 4, 1, 1, 6),
    _BasDocsDevServerChassis_Type()
)
basDocsDevServerChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevServerChassis.setStatus("current")
_BasDocsDevServerSlot_Type = BasSlotId
_BasDocsDevServerSlot_Object = MibTableColumn
basDocsDevServerSlot = _BasDocsDevServerSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 4, 1, 1, 7),
    _BasDocsDevServerSlot_Type()
)
basDocsDevServerSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevServerSlot.setStatus("current")
_BasDocsDevServerIf_Type = BasInterfaceId
_BasDocsDevServerIf_Object = MibTableColumn
basDocsDevServerIf = _BasDocsDevServerIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 4, 1, 1, 8),
    _BasDocsDevServerIf_Type()
)
basDocsDevServerIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevServerIf.setStatus("current")
_BasDocsDevServerLPort_Type = BasLogicalPortId
_BasDocsDevServerLPort_Object = MibTableColumn
basDocsDevServerLPort = _BasDocsDevServerLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 4, 1, 1, 9),
    _BasDocsDevServerLPort_Type()
)
basDocsDevServerLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevServerLPort.setStatus("current")
_BasDocsDevEvent_ObjectIdentity = ObjectIdentity
basDocsDevEvent = _BasDocsDevEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5)
)
_BasDocsDevEvTable_Object = MibTable
basDocsDevEvTable = _BasDocsDevEvTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    basDocsDevEvTable.setStatus("current")
_BasDocsDevEvEntry_Object = MibTableRow
basDocsDevEvEntry = _BasDocsDevEvEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 1, 1)
)
basDocsDevEvEntry.setIndexNames(
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevEvChassis"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevEvSlot"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevEvIf"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevEvLPort"),
)
if mibBuilder.loadTexts:
    basDocsDevEvEntry.setStatus("current")


class _BasDocsDevEvControl_Type(Integer32):
    """Custom type basDocsDevEvControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resetLog", 1),
          ("useDefaultReporting", 2))
    )


_BasDocsDevEvControl_Type.__name__ = "Integer32"
_BasDocsDevEvControl_Object = MibTableColumn
basDocsDevEvControl = _BasDocsDevEvControl_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 1, 1, 1),
    _BasDocsDevEvControl_Type()
)
basDocsDevEvControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDocsDevEvControl.setStatus("current")
_BasDocsDevEvSyslog_Type = IpAddress
_BasDocsDevEvSyslog_Object = MibTableColumn
basDocsDevEvSyslog = _BasDocsDevEvSyslog_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 1, 1, 2),
    _BasDocsDevEvSyslog_Type()
)
basDocsDevEvSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDocsDevEvSyslog.setStatus("current")


class _BasDocsDevEvThrottleAdminStatus_Type(Integer32):
    """Custom type basDocsDevEvThrottleAdminStatus based on Integer32"""
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
        *(("inhibited", 4),
          ("maintainBelowThreshold", 2),
          ("stopAtThreshold", 3),
          ("unconstrained", 1))
    )


_BasDocsDevEvThrottleAdminStatus_Type.__name__ = "Integer32"
_BasDocsDevEvThrottleAdminStatus_Object = MibTableColumn
basDocsDevEvThrottleAdminStatus = _BasDocsDevEvThrottleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 1, 1, 3),
    _BasDocsDevEvThrottleAdminStatus_Type()
)
basDocsDevEvThrottleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDocsDevEvThrottleAdminStatus.setStatus("current")
_BasDocsDevEvThrottleInhibited_Type = TruthValue
_BasDocsDevEvThrottleInhibited_Object = MibTableColumn
basDocsDevEvThrottleInhibited = _BasDocsDevEvThrottleInhibited_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 1, 1, 4),
    _BasDocsDevEvThrottleInhibited_Type()
)
basDocsDevEvThrottleInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevEvThrottleInhibited.setStatus("current")
_BasDocsDevEvThrottleThreshold_Type = Unsigned32
_BasDocsDevEvThrottleThreshold_Object = MibTableColumn
basDocsDevEvThrottleThreshold = _BasDocsDevEvThrottleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 1, 1, 5),
    _BasDocsDevEvThrottleThreshold_Type()
)
basDocsDevEvThrottleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDocsDevEvThrottleThreshold.setStatus("current")


class _BasDocsDevEvThrottleInterval_Type(Integer32):
    """Custom type basDocsDevEvThrottleInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BasDocsDevEvThrottleInterval_Type.__name__ = "Integer32"
_BasDocsDevEvThrottleInterval_Object = MibTableColumn
basDocsDevEvThrottleInterval = _BasDocsDevEvThrottleInterval_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 1, 1, 6),
    _BasDocsDevEvThrottleInterval_Type()
)
basDocsDevEvThrottleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDocsDevEvThrottleInterval.setStatus("current")
if mibBuilder.loadTexts:
    basDocsDevEvThrottleInterval.setUnits("seconds")
_BasDocsDevEvChassis_Type = BasChassisId
_BasDocsDevEvChassis_Object = MibTableColumn
basDocsDevEvChassis = _BasDocsDevEvChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 1, 1, 7),
    _BasDocsDevEvChassis_Type()
)
basDocsDevEvChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevEvChassis.setStatus("current")
_BasDocsDevEvSlot_Type = BasSlotId
_BasDocsDevEvSlot_Object = MibTableColumn
basDocsDevEvSlot = _BasDocsDevEvSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 1, 1, 8),
    _BasDocsDevEvSlot_Type()
)
basDocsDevEvSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevEvSlot.setStatus("current")
_BasDocsDevEvIf_Type = BasInterfaceId
_BasDocsDevEvIf_Object = MibTableColumn
basDocsDevEvIf = _BasDocsDevEvIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 1, 1, 9),
    _BasDocsDevEvIf_Type()
)
basDocsDevEvIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevEvIf.setStatus("current")
_BasDocsDevEvLPort_Type = BasLogicalPortId
_BasDocsDevEvLPort_Object = MibTableColumn
basDocsDevEvLPort = _BasDocsDevEvLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 1, 1, 10),
    _BasDocsDevEvLPort_Type()
)
basDocsDevEvLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevEvLPort.setStatus("current")
_BasDocsDevEvControlTable_Object = MibTable
basDocsDevEvControlTable = _BasDocsDevEvControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 7)
)
if mibBuilder.loadTexts:
    basDocsDevEvControlTable.setStatus("current")
_BasDocsDevEvControlEntry_Object = MibTableRow
basDocsDevEvControlEntry = _BasDocsDevEvControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 7, 1)
)
basDocsDevEvControlEntry.setIndexNames(
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevEvControlChassis"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevEvControlSlot"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevEvControlIf"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevEvControlLPort"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevEvPriority"),
)
if mibBuilder.loadTexts:
    basDocsDevEvControlEntry.setStatus("current")


class _BasDocsDevEvPriority_Type(Integer32):
    """Custom type basDocsDevEvPriority based on Integer32"""
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
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("information", 7),
          ("notice", 6),
          ("warning", 5))
    )


_BasDocsDevEvPriority_Type.__name__ = "Integer32"
_BasDocsDevEvPriority_Object = MibTableColumn
basDocsDevEvPriority = _BasDocsDevEvPriority_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 7, 1, 1),
    _BasDocsDevEvPriority_Type()
)
basDocsDevEvPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevEvPriority.setStatus("current")


class _BasDocsDevEvReporting_Type(Bits):
    """Custom type basDocsDevEvReporting based on Bits"""
    namedValues = NamedValues(
        *(("local", 0),
          ("syslog", 2),
          ("traps", 1))
    )

_BasDocsDevEvReporting_Type.__name__ = "Bits"
_BasDocsDevEvReporting_Object = MibTableColumn
basDocsDevEvReporting = _BasDocsDevEvReporting_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 7, 1, 2),
    _BasDocsDevEvReporting_Type()
)
basDocsDevEvReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDocsDevEvReporting.setStatus("current")
_BasDocsDevEvControlChassis_Type = BasChassisId
_BasDocsDevEvControlChassis_Object = MibTableColumn
basDocsDevEvControlChassis = _BasDocsDevEvControlChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 7, 1, 3),
    _BasDocsDevEvControlChassis_Type()
)
basDocsDevEvControlChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevEvControlChassis.setStatus("current")
_BasDocsDevEvControlSlot_Type = BasSlotId
_BasDocsDevEvControlSlot_Object = MibTableColumn
basDocsDevEvControlSlot = _BasDocsDevEvControlSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 7, 1, 4),
    _BasDocsDevEvControlSlot_Type()
)
basDocsDevEvControlSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevEvControlSlot.setStatus("current")
_BasDocsDevEvControlIf_Type = BasInterfaceId
_BasDocsDevEvControlIf_Object = MibTableColumn
basDocsDevEvControlIf = _BasDocsDevEvControlIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 7, 1, 5),
    _BasDocsDevEvControlIf_Type()
)
basDocsDevEvControlIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevEvControlIf.setStatus("current")
_BasDocsDevEvControlLPort_Type = BasLogicalPortId
_BasDocsDevEvControlLPort_Object = MibTableColumn
basDocsDevEvControlLPort = _BasDocsDevEvControlLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 7, 1, 6),
    _BasDocsDevEvControlLPort_Type()
)
basDocsDevEvControlLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevEvControlLPort.setStatus("current")
_BasDocsDevEventTable_Object = MibTable
basDocsDevEventTable = _BasDocsDevEventTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 8)
)
if mibBuilder.loadTexts:
    basDocsDevEventTable.setStatus("current")
_BasDocsDevEventEntry_Object = MibTableRow
basDocsDevEventEntry = _BasDocsDevEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 8, 1)
)
basDocsDevEventEntry.setIndexNames(
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevEvEventChassis"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevEvEventSlot"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevEvEventIf"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevEvEventLPort"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevEvIndex"),
)
if mibBuilder.loadTexts:
    basDocsDevEventEntry.setStatus("current")


class _BasDocsDevEvIndex_Type(Integer32):
    """Custom type basDocsDevEvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BasDocsDevEvIndex_Type.__name__ = "Integer32"
_BasDocsDevEvIndex_Object = MibTableColumn
basDocsDevEvIndex = _BasDocsDevEvIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 8, 1, 1),
    _BasDocsDevEvIndex_Type()
)
basDocsDevEvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevEvIndex.setStatus("current")
_BasDocsDevEvFirstTime_Type = DateAndTime
_BasDocsDevEvFirstTime_Object = MibTableColumn
basDocsDevEvFirstTime = _BasDocsDevEvFirstTime_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 8, 1, 2),
    _BasDocsDevEvFirstTime_Type()
)
basDocsDevEvFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevEvFirstTime.setStatus("current")
_BasDocsDevEvLastTime_Type = DateAndTime
_BasDocsDevEvLastTime_Object = MibTableColumn
basDocsDevEvLastTime = _BasDocsDevEvLastTime_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 8, 1, 3),
    _BasDocsDevEvLastTime_Type()
)
basDocsDevEvLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevEvLastTime.setStatus("current")
_BasDocsDevEvCount_Type = Counter32
_BasDocsDevEvCount_Object = MibTableColumn
basDocsDevEvCount = _BasDocsDevEvCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 8, 1, 4),
    _BasDocsDevEvCount_Type()
)
basDocsDevEvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevEvCount.setStatus("current")


class _BasDocsDevEvLevel_Type(Integer32):
    """Custom type basDocsDevEvLevel based on Integer32"""
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
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("information", 7),
          ("notice", 6),
          ("warning", 5))
    )


_BasDocsDevEvLevel_Type.__name__ = "Integer32"
_BasDocsDevEvLevel_Object = MibTableColumn
basDocsDevEvLevel = _BasDocsDevEvLevel_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 8, 1, 5),
    _BasDocsDevEvLevel_Type()
)
basDocsDevEvLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevEvLevel.setStatus("current")
_BasDocsDevEvId_Type = Unsigned32
_BasDocsDevEvId_Object = MibTableColumn
basDocsDevEvId = _BasDocsDevEvId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 8, 1, 6),
    _BasDocsDevEvId_Type()
)
basDocsDevEvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevEvId.setStatus("current")
_BasDocsDevEvText_Type = DisplayString
_BasDocsDevEvText_Object = MibTableColumn
basDocsDevEvText = _BasDocsDevEvText_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 8, 1, 7),
    _BasDocsDevEvText_Type()
)
basDocsDevEvText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevEvText.setStatus("current")
_BasDocsDevEvEventChassis_Type = BasChassisId
_BasDocsDevEvEventChassis_Object = MibTableColumn
basDocsDevEvEventChassis = _BasDocsDevEvEventChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 8, 1, 8),
    _BasDocsDevEvEventChassis_Type()
)
basDocsDevEvEventChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevEvEventChassis.setStatus("current")
_BasDocsDevEvEventSlot_Type = BasSlotId
_BasDocsDevEvEventSlot_Object = MibTableColumn
basDocsDevEvEventSlot = _BasDocsDevEvEventSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 8, 1, 9),
    _BasDocsDevEvEventSlot_Type()
)
basDocsDevEvEventSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevEvEventSlot.setStatus("current")
_BasDocsDevEvEventIf_Type = BasInterfaceId
_BasDocsDevEvEventIf_Object = MibTableColumn
basDocsDevEvEventIf = _BasDocsDevEvEventIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 8, 1, 10),
    _BasDocsDevEvEventIf_Type()
)
basDocsDevEvEventIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevEvEventIf.setStatus("current")
_BasDocsDevEvEventLPort_Type = BasLogicalPortId
_BasDocsDevEvEventLPort_Object = MibTableColumn
basDocsDevEvEventLPort = _BasDocsDevEvEventLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 5, 8, 1, 11),
    _BasDocsDevEvEventLPort_Type()
)
basDocsDevEvEventLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevEvEventLPort.setStatus("current")
_BasDocsDevFilter_ObjectIdentity = ObjectIdentity
basDocsDevFilter = _BasDocsDevFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6)
)
_BasDocsDevFilterTable_Object = MibTable
basDocsDevFilterTable = _BasDocsDevFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    basDocsDevFilterTable.setStatus("current")
_BasDocsDevFilterEntry_Object = MibTableRow
basDocsDevFilterEntry = _BasDocsDevFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 1, 1)
)
basDocsDevFilterEntry.setIndexNames(
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterChassis"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterSlot"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterIf"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterLPort"),
)
if mibBuilder.loadTexts:
    basDocsDevFilterEntry.setStatus("current")


class _BasDocsDevFilterLLCDefault_Type(Integer32):
    """Custom type basDocsDevFilterLLCDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("discard", 1))
    )


_BasDocsDevFilterLLCDefault_Type.__name__ = "Integer32"
_BasDocsDevFilterLLCDefault_Object = MibTableColumn
basDocsDevFilterLLCDefault = _BasDocsDevFilterLLCDefault_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 1, 1, 1),
    _BasDocsDevFilterLLCDefault_Type()
)
basDocsDevFilterLLCDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDocsDevFilterLLCDefault.setStatus("current")
_BasDocsDevFilterChassis_Type = BasChassisId
_BasDocsDevFilterChassis_Object = MibTableColumn
basDocsDevFilterChassis = _BasDocsDevFilterChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 1, 1, 2),
    _BasDocsDevFilterChassis_Type()
)
basDocsDevFilterChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterChassis.setStatus("current")
_BasDocsDevFilterSlot_Type = BasSlotId
_BasDocsDevFilterSlot_Object = MibTableColumn
basDocsDevFilterSlot = _BasDocsDevFilterSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 1, 1, 3),
    _BasDocsDevFilterSlot_Type()
)
basDocsDevFilterSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterSlot.setStatus("current")
_BasDocsDevFilterIf_Type = BasInterfaceId
_BasDocsDevFilterIf_Object = MibTableColumn
basDocsDevFilterIf = _BasDocsDevFilterIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 1, 1, 4),
    _BasDocsDevFilterIf_Type()
)
basDocsDevFilterIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterIf.setStatus("current")
_BasDocsDevFilterLPort_Type = BasLogicalPortId
_BasDocsDevFilterLPort_Object = MibTableColumn
basDocsDevFilterLPort = _BasDocsDevFilterLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 1, 1, 5),
    _BasDocsDevFilterLPort_Type()
)
basDocsDevFilterLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterLPort.setStatus("current")
_BasDocsDevFilterLLCTable_Object = MibTable
basDocsDevFilterLLCTable = _BasDocsDevFilterLLCTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    basDocsDevFilterLLCTable.setStatus("current")
_BasDocsDevFilterLLCEntry_Object = MibTableRow
basDocsDevFilterLLCEntry = _BasDocsDevFilterLLCEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 2, 1)
)
basDocsDevFilterLLCEntry.setIndexNames(
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterLLCChassis"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterLLCSlot"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterLLCIf"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterLLCLPort"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterLLCIndex"),
)
if mibBuilder.loadTexts:
    basDocsDevFilterLLCEntry.setStatus("current")


class _BasDocsDevFilterLLCIndex_Type(Integer32):
    """Custom type basDocsDevFilterLLCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BasDocsDevFilterLLCIndex_Type.__name__ = "Integer32"
_BasDocsDevFilterLLCIndex_Object = MibTableColumn
basDocsDevFilterLLCIndex = _BasDocsDevFilterLLCIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 2, 1, 1),
    _BasDocsDevFilterLLCIndex_Type()
)
basDocsDevFilterLLCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterLLCIndex.setStatus("current")
_BasDocsDevFilterLLCStatus_Type = RowStatus
_BasDocsDevFilterLLCStatus_Object = MibTableColumn
basDocsDevFilterLLCStatus = _BasDocsDevFilterLLCStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 2, 1, 2),
    _BasDocsDevFilterLLCStatus_Type()
)
basDocsDevFilterLLCStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterLLCStatus.setStatus("current")
_BasDocsDevFilterLLCIfIndex_Type = InterfaceIndexOrZero
_BasDocsDevFilterLLCIfIndex_Object = MibTableColumn
basDocsDevFilterLLCIfIndex = _BasDocsDevFilterLLCIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 2, 1, 3),
    _BasDocsDevFilterLLCIfIndex_Type()
)
basDocsDevFilterLLCIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterLLCIfIndex.setStatus("current")


class _BasDocsDevFilterLLCProtocolType_Type(Integer32):
    """Custom type basDocsDevFilterLLCProtocolType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsap", 2),
          ("ethertype", 1))
    )


_BasDocsDevFilterLLCProtocolType_Type.__name__ = "Integer32"
_BasDocsDevFilterLLCProtocolType_Object = MibTableColumn
basDocsDevFilterLLCProtocolType = _BasDocsDevFilterLLCProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 2, 1, 4),
    _BasDocsDevFilterLLCProtocolType_Type()
)
basDocsDevFilterLLCProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterLLCProtocolType.setStatus("current")


class _BasDocsDevFilterLLCProtocol_Type(Integer32):
    """Custom type basDocsDevFilterLLCProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BasDocsDevFilterLLCProtocol_Type.__name__ = "Integer32"
_BasDocsDevFilterLLCProtocol_Object = MibTableColumn
basDocsDevFilterLLCProtocol = _BasDocsDevFilterLLCProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 2, 1, 5),
    _BasDocsDevFilterLLCProtocol_Type()
)
basDocsDevFilterLLCProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterLLCProtocol.setStatus("current")
_BasDocsDevFilterLLCMatches_Type = Counter32
_BasDocsDevFilterLLCMatches_Object = MibTableColumn
basDocsDevFilterLLCMatches = _BasDocsDevFilterLLCMatches_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 2, 1, 6),
    _BasDocsDevFilterLLCMatches_Type()
)
basDocsDevFilterLLCMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevFilterLLCMatches.setStatus("current")
_BasDocsDevFilterLLCChassis_Type = BasChassisId
_BasDocsDevFilterLLCChassis_Object = MibTableColumn
basDocsDevFilterLLCChassis = _BasDocsDevFilterLLCChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 2, 1, 7),
    _BasDocsDevFilterLLCChassis_Type()
)
basDocsDevFilterLLCChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterLLCChassis.setStatus("current")
_BasDocsDevFilterLLCSlot_Type = BasSlotId
_BasDocsDevFilterLLCSlot_Object = MibTableColumn
basDocsDevFilterLLCSlot = _BasDocsDevFilterLLCSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 2, 1, 8),
    _BasDocsDevFilterLLCSlot_Type()
)
basDocsDevFilterLLCSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterLLCSlot.setStatus("current")
_BasDocsDevFilterLLCIf_Type = BasInterfaceId
_BasDocsDevFilterLLCIf_Object = MibTableColumn
basDocsDevFilterLLCIf = _BasDocsDevFilterLLCIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 2, 1, 9),
    _BasDocsDevFilterLLCIf_Type()
)
basDocsDevFilterLLCIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterLLCIf.setStatus("current")
_BasDocsDevFilterLLCLPort_Type = BasLogicalPortId
_BasDocsDevFilterLLCLPort_Object = MibTableColumn
basDocsDevFilterLLCLPort = _BasDocsDevFilterLLCLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 2, 1, 10),
    _BasDocsDevFilterLLCLPort_Type()
)
basDocsDevFilterLLCLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterLLCLPort.setStatus("current")
_BasDocsDevFilterIpDefTable_Object = MibTable
basDocsDevFilterIpDefTable = _BasDocsDevFilterIpDefTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    basDocsDevFilterIpDefTable.setStatus("current")
_BasDocsDevFilterIpDefEntry_Object = MibTableRow
basDocsDevFilterIpDefEntry = _BasDocsDevFilterIpDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 3, 1)
)
basDocsDevFilterIpDefEntry.setIndexNames(
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterIpDefChassis"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterIpDefSlot"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterIpDefIf"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterIpDefLPort"),
)
if mibBuilder.loadTexts:
    basDocsDevFilterIpDefEntry.setStatus("current")


class _BasDocsDevFilterIpDefault_Type(Integer32):
    """Custom type basDocsDevFilterIpDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("discard", 1))
    )


_BasDocsDevFilterIpDefault_Type.__name__ = "Integer32"
_BasDocsDevFilterIpDefault_Object = MibTableColumn
basDocsDevFilterIpDefault = _BasDocsDevFilterIpDefault_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 3, 1, 1),
    _BasDocsDevFilterIpDefault_Type()
)
basDocsDevFilterIpDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDocsDevFilterIpDefault.setStatus("current")
_BasDocsDevFilterIpDefChassis_Type = BasChassisId
_BasDocsDevFilterIpDefChassis_Object = MibTableColumn
basDocsDevFilterIpDefChassis = _BasDocsDevFilterIpDefChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 3, 1, 2),
    _BasDocsDevFilterIpDefChassis_Type()
)
basDocsDevFilterIpDefChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterIpDefChassis.setStatus("current")
_BasDocsDevFilterIpDefSlot_Type = BasSlotId
_BasDocsDevFilterIpDefSlot_Object = MibTableColumn
basDocsDevFilterIpDefSlot = _BasDocsDevFilterIpDefSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 3, 1, 3),
    _BasDocsDevFilterIpDefSlot_Type()
)
basDocsDevFilterIpDefSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterIpDefSlot.setStatus("current")
_BasDocsDevFilterIpDefIf_Type = BasInterfaceId
_BasDocsDevFilterIpDefIf_Object = MibTableColumn
basDocsDevFilterIpDefIf = _BasDocsDevFilterIpDefIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 3, 1, 4),
    _BasDocsDevFilterIpDefIf_Type()
)
basDocsDevFilterIpDefIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterIpDefIf.setStatus("current")
_BasDocsDevFilterIpDefLPort_Type = BasLogicalPortId
_BasDocsDevFilterIpDefLPort_Object = MibTableColumn
basDocsDevFilterIpDefLPort = _BasDocsDevFilterIpDefLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 3, 1, 5),
    _BasDocsDevFilterIpDefLPort_Type()
)
basDocsDevFilterIpDefLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterIpDefLPort.setStatus("current")
_BasDocsDevFilterIpTable_Object = MibTable
basDocsDevFilterIpTable = _BasDocsDevFilterIpTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    basDocsDevFilterIpTable.setStatus("current")
_BasDocsDevFilterIpEntry_Object = MibTableRow
basDocsDevFilterIpEntry = _BasDocsDevFilterIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1)
)
basDocsDevFilterIpEntry.setIndexNames(
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterIpChassis"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterIpSlot"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterIpIf"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterIpLPort"),
    (0, "BAS-ALIAS-CABLE-DEVICE-MIB", "basDocsDevFilterIpIndex"),
)
if mibBuilder.loadTexts:
    basDocsDevFilterIpEntry.setStatus("current")


class _BasDocsDevFilterIpIndex_Type(Integer32):
    """Custom type basDocsDevFilterIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BasDocsDevFilterIpIndex_Type.__name__ = "Integer32"
_BasDocsDevFilterIpIndex_Object = MibTableColumn
basDocsDevFilterIpIndex = _BasDocsDevFilterIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 1),
    _BasDocsDevFilterIpIndex_Type()
)
basDocsDevFilterIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterIpIndex.setStatus("current")
_BasDocsDevFilterIpStatus_Type = RowStatus
_BasDocsDevFilterIpStatus_Object = MibTableColumn
basDocsDevFilterIpStatus = _BasDocsDevFilterIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 2),
    _BasDocsDevFilterIpStatus_Type()
)
basDocsDevFilterIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterIpStatus.setStatus("current")


class _BasDocsDevFilterIpControl_Type(Integer32):
    """Custom type basDocsDevFilterIpControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("discard", 1))
    )


_BasDocsDevFilterIpControl_Type.__name__ = "Integer32"
_BasDocsDevFilterIpControl_Object = MibTableColumn
basDocsDevFilterIpControl = _BasDocsDevFilterIpControl_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 3),
    _BasDocsDevFilterIpControl_Type()
)
basDocsDevFilterIpControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterIpControl.setStatus("current")
_BasDocsDevFilterIpIfIndex_Type = InterfaceIndexOrZero
_BasDocsDevFilterIpIfIndex_Object = MibTableColumn
basDocsDevFilterIpIfIndex = _BasDocsDevFilterIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 4),
    _BasDocsDevFilterIpIfIndex_Type()
)
basDocsDevFilterIpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterIpIfIndex.setStatus("current")


class _BasDocsDevFilterIpDirection_Type(Integer32):
    """Custom type basDocsDevFilterIpDirection based on Integer32"""
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
        *(("both", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_BasDocsDevFilterIpDirection_Type.__name__ = "Integer32"
_BasDocsDevFilterIpDirection_Object = MibTableColumn
basDocsDevFilterIpDirection = _BasDocsDevFilterIpDirection_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 5),
    _BasDocsDevFilterIpDirection_Type()
)
basDocsDevFilterIpDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterIpDirection.setStatus("current")


class _BasDocsDevFilterIpBroadcast_Type(TruthValue):
    """Custom type basDocsDevFilterIpBroadcast based on TruthValue"""


_BasDocsDevFilterIpBroadcast_Object = MibTableColumn
basDocsDevFilterIpBroadcast = _BasDocsDevFilterIpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 6),
    _BasDocsDevFilterIpBroadcast_Type()
)
basDocsDevFilterIpBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterIpBroadcast.setStatus("current")


class _BasDocsDevFilterIpSaddr_Type(IpAddress):
    """Custom type basDocsDevFilterIpSaddr based on IpAddress"""
    defaultHexValue = "00000000"


_BasDocsDevFilterIpSaddr_Object = MibTableColumn
basDocsDevFilterIpSaddr = _BasDocsDevFilterIpSaddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 7),
    _BasDocsDevFilterIpSaddr_Type()
)
basDocsDevFilterIpSaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterIpSaddr.setStatus("current")


class _BasDocsDevFilterIpSmask_Type(IpAddress):
    """Custom type basDocsDevFilterIpSmask based on IpAddress"""
    defaultHexValue = "00000000"


_BasDocsDevFilterIpSmask_Object = MibTableColumn
basDocsDevFilterIpSmask = _BasDocsDevFilterIpSmask_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 8),
    _BasDocsDevFilterIpSmask_Type()
)
basDocsDevFilterIpSmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterIpSmask.setStatus("current")


class _BasDocsDevFilterIpDaddr_Type(IpAddress):
    """Custom type basDocsDevFilterIpDaddr based on IpAddress"""
    defaultHexValue = "00000000"


_BasDocsDevFilterIpDaddr_Object = MibTableColumn
basDocsDevFilterIpDaddr = _BasDocsDevFilterIpDaddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 9),
    _BasDocsDevFilterIpDaddr_Type()
)
basDocsDevFilterIpDaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterIpDaddr.setStatus("current")


class _BasDocsDevFilterIpDmask_Type(IpAddress):
    """Custom type basDocsDevFilterIpDmask based on IpAddress"""
    defaultHexValue = "00000000"


_BasDocsDevFilterIpDmask_Object = MibTableColumn
basDocsDevFilterIpDmask = _BasDocsDevFilterIpDmask_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 10),
    _BasDocsDevFilterIpDmask_Type()
)
basDocsDevFilterIpDmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterIpDmask.setStatus("current")


class _BasDocsDevFilterIpProtocol_Type(Integer32):
    """Custom type basDocsDevFilterIpProtocol based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              17,
              256)
        )
    )
    namedValues = NamedValues(
        *(("any", 256),
          ("icmp", 1),
          ("tcp", 6),
          ("udp", 17))
    )


_BasDocsDevFilterIpProtocol_Type.__name__ = "Integer32"
_BasDocsDevFilterIpProtocol_Object = MibTableColumn
basDocsDevFilterIpProtocol = _BasDocsDevFilterIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 11),
    _BasDocsDevFilterIpProtocol_Type()
)
basDocsDevFilterIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterIpProtocol.setStatus("current")


class _BasDocsDevFilterIpSourcePortLow_Type(Integer32):
    """Custom type basDocsDevFilterIpSourcePortLow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BasDocsDevFilterIpSourcePortLow_Type.__name__ = "Integer32"
_BasDocsDevFilterIpSourcePortLow_Object = MibTableColumn
basDocsDevFilterIpSourcePortLow = _BasDocsDevFilterIpSourcePortLow_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 12),
    _BasDocsDevFilterIpSourcePortLow_Type()
)
basDocsDevFilterIpSourcePortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterIpSourcePortLow.setStatus("current")


class _BasDocsDevFilterIpSourcePortHigh_Type(Integer32):
    """Custom type basDocsDevFilterIpSourcePortHigh based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BasDocsDevFilterIpSourcePortHigh_Type.__name__ = "Integer32"
_BasDocsDevFilterIpSourcePortHigh_Object = MibTableColumn
basDocsDevFilterIpSourcePortHigh = _BasDocsDevFilterIpSourcePortHigh_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 13),
    _BasDocsDevFilterIpSourcePortHigh_Type()
)
basDocsDevFilterIpSourcePortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterIpSourcePortHigh.setStatus("current")


class _BasDocsDevFilterIpDestPortLow_Type(Integer32):
    """Custom type basDocsDevFilterIpDestPortLow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BasDocsDevFilterIpDestPortLow_Type.__name__ = "Integer32"
_BasDocsDevFilterIpDestPortLow_Object = MibTableColumn
basDocsDevFilterIpDestPortLow = _BasDocsDevFilterIpDestPortLow_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 14),
    _BasDocsDevFilterIpDestPortLow_Type()
)
basDocsDevFilterIpDestPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterIpDestPortLow.setStatus("current")


class _BasDocsDevFilterIpDestPortHigh_Type(Integer32):
    """Custom type basDocsDevFilterIpDestPortHigh based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BasDocsDevFilterIpDestPortHigh_Type.__name__ = "Integer32"
_BasDocsDevFilterIpDestPortHigh_Object = MibTableColumn
basDocsDevFilterIpDestPortHigh = _BasDocsDevFilterIpDestPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 15),
    _BasDocsDevFilterIpDestPortHigh_Type()
)
basDocsDevFilterIpDestPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsDevFilterIpDestPortHigh.setStatus("current")
_BasDocsDevFilterIpMatches_Type = Counter32
_BasDocsDevFilterIpMatches_Object = MibTableColumn
basDocsDevFilterIpMatches = _BasDocsDevFilterIpMatches_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 16),
    _BasDocsDevFilterIpMatches_Type()
)
basDocsDevFilterIpMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsDevFilterIpMatches.setStatus("current")
_BasDocsDevFilterIpChassis_Type = BasChassisId
_BasDocsDevFilterIpChassis_Object = MibTableColumn
basDocsDevFilterIpChassis = _BasDocsDevFilterIpChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 17),
    _BasDocsDevFilterIpChassis_Type()
)
basDocsDevFilterIpChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterIpChassis.setStatus("current")
_BasDocsDevFilterIpSlot_Type = BasSlotId
_BasDocsDevFilterIpSlot_Object = MibTableColumn
basDocsDevFilterIpSlot = _BasDocsDevFilterIpSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 18),
    _BasDocsDevFilterIpSlot_Type()
)
basDocsDevFilterIpSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterIpSlot.setStatus("current")
_BasDocsDevFilterIpIf_Type = BasInterfaceId
_BasDocsDevFilterIpIf_Object = MibTableColumn
basDocsDevFilterIpIf = _BasDocsDevFilterIpIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 19),
    _BasDocsDevFilterIpIf_Type()
)
basDocsDevFilterIpIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterIpIf.setStatus("current")
_BasDocsDevFilterIpLPort_Type = BasLogicalPortId
_BasDocsDevFilterIpLPort_Object = MibTableColumn
basDocsDevFilterIpLPort = _BasDocsDevFilterIpLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9, 1, 1, 6, 4, 1, 20),
    _BasDocsDevFilterIpLPort_Type()
)
basDocsDevFilterIpLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsDevFilterIpLPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-ALIAS-CABLE-DEVICE-MIB",
    **{"InterfaceIndexOrZero": InterfaceIndexOrZero,
       "basAliasDocsCdMib": basAliasDocsCdMib,
       "basDocsDevMIBObjects": basDocsDevMIBObjects,
       "basDocsDevBase": basDocsDevBase,
       "basDocsDevBaseTable": basDocsDevBaseTable,
       "basDocsDevBaseEntry": basDocsDevBaseEntry,
       "basDocsDevRole": basDocsDevRole,
       "basDocsDevDateTime": basDocsDevDateTime,
       "basDocsDevResetNow": basDocsDevResetNow,
       "basDocsDevSerialNumber": basDocsDevSerialNumber,
       "basDocsDevSTPControl": basDocsDevSTPControl,
       "basDocsDevChassis": basDocsDevChassis,
       "basDocsDevSlot": basDocsDevSlot,
       "basDocsDevIf": basDocsDevIf,
       "basDocsDevLPort": basDocsDevLPort,
       "basDocsDevNmAccessTable": basDocsDevNmAccessTable,
       "basDocsDevNmAccessEntry": basDocsDevNmAccessEntry,
       "basDocsDevNmAccessIndex": basDocsDevNmAccessIndex,
       "basDocsDevNmAccessIp": basDocsDevNmAccessIp,
       "basDocsDevNmAccessIpMask": basDocsDevNmAccessIpMask,
       "basDocsDevNmAccessCommunity": basDocsDevNmAccessCommunity,
       "basDocsDevNmAccessControl": basDocsDevNmAccessControl,
       "basDocsDevNmAccessInterfaces": basDocsDevNmAccessInterfaces,
       "basDocsDevNmAccessStatus": basDocsDevNmAccessStatus,
       "basDocsDevNmAccessChassis": basDocsDevNmAccessChassis,
       "basDocsDevNmAccessSlot": basDocsDevNmAccessSlot,
       "basDocsDevNmAccessIf": basDocsDevNmAccessIf,
       "basDocsDevNmAccessLPort": basDocsDevNmAccessLPort,
       "basDocsDevSoftware": basDocsDevSoftware,
       "basDocsDevSwTable": basDocsDevSwTable,
       "basDocsDevSwEntry": basDocsDevSwEntry,
       "basDocsDevSwServer": basDocsDevSwServer,
       "basDocsDevSwFilename": basDocsDevSwFilename,
       "basDocsDevSwAdminStatus": basDocsDevSwAdminStatus,
       "basDocsDevSwOperStatus": basDocsDevSwOperStatus,
       "basDocsDevSwChassis": basDocsDevSwChassis,
       "basDocsDevSwSlot": basDocsDevSwSlot,
       "basDocsDevSwIf": basDocsDevSwIf,
       "basDocsDevSwLPort": basDocsDevSwLPort,
       "basDocsDevServer": basDocsDevServer,
       "basDocsDevServerTable": basDocsDevServerTable,
       "basDocsDevServerEntry": basDocsDevServerEntry,
       "basDocsDevServerBootState": basDocsDevServerBootState,
       "basDocsDevServerDhcp": basDocsDevServerDhcp,
       "basDocsDevServerTime": basDocsDevServerTime,
       "basDocsDevServerTftp": basDocsDevServerTftp,
       "basDocsDevServerConfigFile": basDocsDevServerConfigFile,
       "basDocsDevServerChassis": basDocsDevServerChassis,
       "basDocsDevServerSlot": basDocsDevServerSlot,
       "basDocsDevServerIf": basDocsDevServerIf,
       "basDocsDevServerLPort": basDocsDevServerLPort,
       "basDocsDevEvent": basDocsDevEvent,
       "basDocsDevEvTable": basDocsDevEvTable,
       "basDocsDevEvEntry": basDocsDevEvEntry,
       "basDocsDevEvControl": basDocsDevEvControl,
       "basDocsDevEvSyslog": basDocsDevEvSyslog,
       "basDocsDevEvThrottleAdminStatus": basDocsDevEvThrottleAdminStatus,
       "basDocsDevEvThrottleInhibited": basDocsDevEvThrottleInhibited,
       "basDocsDevEvThrottleThreshold": basDocsDevEvThrottleThreshold,
       "basDocsDevEvThrottleInterval": basDocsDevEvThrottleInterval,
       "basDocsDevEvChassis": basDocsDevEvChassis,
       "basDocsDevEvSlot": basDocsDevEvSlot,
       "basDocsDevEvIf": basDocsDevEvIf,
       "basDocsDevEvLPort": basDocsDevEvLPort,
       "basDocsDevEvControlTable": basDocsDevEvControlTable,
       "basDocsDevEvControlEntry": basDocsDevEvControlEntry,
       "basDocsDevEvPriority": basDocsDevEvPriority,
       "basDocsDevEvReporting": basDocsDevEvReporting,
       "basDocsDevEvControlChassis": basDocsDevEvControlChassis,
       "basDocsDevEvControlSlot": basDocsDevEvControlSlot,
       "basDocsDevEvControlIf": basDocsDevEvControlIf,
       "basDocsDevEvControlLPort": basDocsDevEvControlLPort,
       "basDocsDevEventTable": basDocsDevEventTable,
       "basDocsDevEventEntry": basDocsDevEventEntry,
       "basDocsDevEvIndex": basDocsDevEvIndex,
       "basDocsDevEvFirstTime": basDocsDevEvFirstTime,
       "basDocsDevEvLastTime": basDocsDevEvLastTime,
       "basDocsDevEvCount": basDocsDevEvCount,
       "basDocsDevEvLevel": basDocsDevEvLevel,
       "basDocsDevEvId": basDocsDevEvId,
       "basDocsDevEvText": basDocsDevEvText,
       "basDocsDevEvEventChassis": basDocsDevEvEventChassis,
       "basDocsDevEvEventSlot": basDocsDevEvEventSlot,
       "basDocsDevEvEventIf": basDocsDevEvEventIf,
       "basDocsDevEvEventLPort": basDocsDevEvEventLPort,
       "basDocsDevFilter": basDocsDevFilter,
       "basDocsDevFilterTable": basDocsDevFilterTable,
       "basDocsDevFilterEntry": basDocsDevFilterEntry,
       "basDocsDevFilterLLCDefault": basDocsDevFilterLLCDefault,
       "basDocsDevFilterChassis": basDocsDevFilterChassis,
       "basDocsDevFilterSlot": basDocsDevFilterSlot,
       "basDocsDevFilterIf": basDocsDevFilterIf,
       "basDocsDevFilterLPort": basDocsDevFilterLPort,
       "basDocsDevFilterLLCTable": basDocsDevFilterLLCTable,
       "basDocsDevFilterLLCEntry": basDocsDevFilterLLCEntry,
       "basDocsDevFilterLLCIndex": basDocsDevFilterLLCIndex,
       "basDocsDevFilterLLCStatus": basDocsDevFilterLLCStatus,
       "basDocsDevFilterLLCIfIndex": basDocsDevFilterLLCIfIndex,
       "basDocsDevFilterLLCProtocolType": basDocsDevFilterLLCProtocolType,
       "basDocsDevFilterLLCProtocol": basDocsDevFilterLLCProtocol,
       "basDocsDevFilterLLCMatches": basDocsDevFilterLLCMatches,
       "basDocsDevFilterLLCChassis": basDocsDevFilterLLCChassis,
       "basDocsDevFilterLLCSlot": basDocsDevFilterLLCSlot,
       "basDocsDevFilterLLCIf": basDocsDevFilterLLCIf,
       "basDocsDevFilterLLCLPort": basDocsDevFilterLLCLPort,
       "basDocsDevFilterIpDefTable": basDocsDevFilterIpDefTable,
       "basDocsDevFilterIpDefEntry": basDocsDevFilterIpDefEntry,
       "basDocsDevFilterIpDefault": basDocsDevFilterIpDefault,
       "basDocsDevFilterIpDefChassis": basDocsDevFilterIpDefChassis,
       "basDocsDevFilterIpDefSlot": basDocsDevFilterIpDefSlot,
       "basDocsDevFilterIpDefIf": basDocsDevFilterIpDefIf,
       "basDocsDevFilterIpDefLPort": basDocsDevFilterIpDefLPort,
       "basDocsDevFilterIpTable": basDocsDevFilterIpTable,
       "basDocsDevFilterIpEntry": basDocsDevFilterIpEntry,
       "basDocsDevFilterIpIndex": basDocsDevFilterIpIndex,
       "basDocsDevFilterIpStatus": basDocsDevFilterIpStatus,
       "basDocsDevFilterIpControl": basDocsDevFilterIpControl,
       "basDocsDevFilterIpIfIndex": basDocsDevFilterIpIfIndex,
       "basDocsDevFilterIpDirection": basDocsDevFilterIpDirection,
       "basDocsDevFilterIpBroadcast": basDocsDevFilterIpBroadcast,
       "basDocsDevFilterIpSaddr": basDocsDevFilterIpSaddr,
       "basDocsDevFilterIpSmask": basDocsDevFilterIpSmask,
       "basDocsDevFilterIpDaddr": basDocsDevFilterIpDaddr,
       "basDocsDevFilterIpDmask": basDocsDevFilterIpDmask,
       "basDocsDevFilterIpProtocol": basDocsDevFilterIpProtocol,
       "basDocsDevFilterIpSourcePortLow": basDocsDevFilterIpSourcePortLow,
       "basDocsDevFilterIpSourcePortHigh": basDocsDevFilterIpSourcePortHigh,
       "basDocsDevFilterIpDestPortLow": basDocsDevFilterIpDestPortLow,
       "basDocsDevFilterIpDestPortHigh": basDocsDevFilterIpDestPortHigh,
       "basDocsDevFilterIpMatches": basDocsDevFilterIpMatches,
       "basDocsDevFilterIpChassis": basDocsDevFilterIpChassis,
       "basDocsDevFilterIpSlot": basDocsDevFilterIpSlot,
       "basDocsDevFilterIpIf": basDocsDevFilterIpIf,
       "basDocsDevFilterIpLPort": basDocsDevFilterIpLPort}
)
