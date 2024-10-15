# SNMP MIB module (SINGLE-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SINGLE-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:20 2024
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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swSingleIPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwSingleIPMgmt_ObjectIdentity = ObjectIdentity
swSingleIPMgmt = _SwSingleIPMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1)
)
_SwSingleIPInfo_ObjectIdentity = ObjectIdentity
swSingleIPInfo = _SwSingleIPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 1)
)


class _SwSingleIPVersion_Type(DisplayString):
    """Custom type swSingleIPVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSingleIPVersion_Type.__name__ = "DisplayString"
_SwSingleIPVersion_Object = MibScalar
swSingleIPVersion = _SwSingleIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 1, 1),
    _SwSingleIPVersion_Type()
)
swSingleIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPVersion.setStatus("current")


class _SwSingleIPCapability_Type(DisplayString):
    """Custom type swSingleIPCapability based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSingleIPCapability_Type.__name__ = "DisplayString"
_SwSingleIPCapability_Object = MibScalar
swSingleIPCapability = _SwSingleIPCapability_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 1, 2),
    _SwSingleIPCapability_Type()
)
swSingleIPCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPCapability.setStatus("current")


class _SwSingleIPPlatform_Type(DisplayString):
    """Custom type swSingleIPPlatform based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSingleIPPlatform_Type.__name__ = "DisplayString"
_SwSingleIPPlatform_Object = MibScalar
swSingleIPPlatform = _SwSingleIPPlatform_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 1, 3),
    _SwSingleIPPlatform_Type()
)
swSingleIPPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPPlatform.setStatus("current")
_SwSingleIPCtrl_ObjectIdentity = ObjectIdentity
swSingleIPCtrl = _SwSingleIPCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 2)
)


class _SwSingleIPAdmin_Type(Integer32):
    """Custom type swSingleIPAdmin based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwSingleIPAdmin_Type.__name__ = "Integer32"
_SwSingleIPAdmin_Object = MibScalar
swSingleIPAdmin = _SwSingleIPAdmin_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 2, 1),
    _SwSingleIPAdmin_Type()
)
swSingleIPAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSingleIPAdmin.setStatus("current")


class _SwSingleIPRoleState_Type(Integer32):
    """Custom type swSingleIPRoleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cas", 2),
          ("cs", 1),
          ("ms", 3))
    )


_SwSingleIPRoleState_Type.__name__ = "Integer32"
_SwSingleIPRoleState_Object = MibScalar
swSingleIPRoleState = _SwSingleIPRoleState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 2, 2),
    _SwSingleIPRoleState_Type()
)
swSingleIPRoleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSingleIPRoleState.setStatus("current")


class _SwSingleIPHoldtime_Type(Integer32):
    """Custom type swSingleIPHoldtime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 255),
    )


_SwSingleIPHoldtime_Type.__name__ = "Integer32"
_SwSingleIPHoldtime_Object = MibScalar
swSingleIPHoldtime = _SwSingleIPHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 2, 3),
    _SwSingleIPHoldtime_Type()
)
swSingleIPHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSingleIPHoldtime.setStatus("current")


class _SwSingleIPTimeInterval_Type(Integer32):
    """Custom type swSingleIPTimeInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 90),
    )


_SwSingleIPTimeInterval_Type.__name__ = "Integer32"
_SwSingleIPTimeInterval_Object = MibScalar
swSingleIPTimeInterval = _SwSingleIPTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 2, 4),
    _SwSingleIPTimeInterval_Type()
)
swSingleIPTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSingleIPTimeInterval.setStatus("current")
_SwSingleIPMSTable_Object = MibTable
swSingleIPMSTable = _SwSingleIPMSTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3)
)
if mibBuilder.loadTexts:
    swSingleIPMSTable.setStatus("current")
_SwSingleIPMSEntry_Object = MibTableRow
swSingleIPMSEntry = _SwSingleIPMSEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1)
)
swSingleIPMSEntry.setIndexNames(
    (0, "SINGLE-IP-MIB", "swSingleIPMSID"),
)
if mibBuilder.loadTexts:
    swSingleIPMSEntry.setStatus("current")


class _SwSingleIPMSID_Type(Integer32):
    """Custom type swSingleIPMSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SwSingleIPMSID_Type.__name__ = "Integer32"
_SwSingleIPMSID_Object = MibTableColumn
swSingleIPMSID = _SwSingleIPMSID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 1),
    _SwSingleIPMSID_Type()
)
swSingleIPMSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPMSID.setStatus("current")


class _SwSingleIPMSDeviceName_Type(DisplayString):
    """Custom type swSingleIPMSDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSingleIPMSDeviceName_Type.__name__ = "DisplayString"
_SwSingleIPMSDeviceName_Object = MibTableColumn
swSingleIPMSDeviceName = _SwSingleIPMSDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 2),
    _SwSingleIPMSDeviceName_Type()
)
swSingleIPMSDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPMSDeviceName.setStatus("current")
_SwSingleIPMSMacAddr_Type = MacAddress
_SwSingleIPMSMacAddr_Object = MibTableColumn
swSingleIPMSMacAddr = _SwSingleIPMSMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 3),
    _SwSingleIPMSMacAddr_Type()
)
swSingleIPMSMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPMSMacAddr.setStatus("current")


class _SwSingleIPMSFirmwareVer_Type(DisplayString):
    """Custom type swSingleIPMSFirmwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSingleIPMSFirmwareVer_Type.__name__ = "DisplayString"
_SwSingleIPMSFirmwareVer_Object = MibTableColumn
swSingleIPMSFirmwareVer = _SwSingleIPMSFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 4),
    _SwSingleIPMSFirmwareVer_Type()
)
swSingleIPMSFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPMSFirmwareVer.setStatus("current")


class _SwSingleIPMSCapability_Type(DisplayString):
    """Custom type swSingleIPMSCapability based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSingleIPMSCapability_Type.__name__ = "DisplayString"
_SwSingleIPMSCapability_Object = MibTableColumn
swSingleIPMSCapability = _SwSingleIPMSCapability_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 5),
    _SwSingleIPMSCapability_Type()
)
swSingleIPMSCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPMSCapability.setStatus("current")


class _SwSingleIPMSPlatform_Type(DisplayString):
    """Custom type swSingleIPMSPlatform based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSingleIPMSPlatform_Type.__name__ = "DisplayString"
_SwSingleIPMSPlatform_Object = MibTableColumn
swSingleIPMSPlatform = _SwSingleIPMSPlatform_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 6),
    _SwSingleIPMSPlatform_Type()
)
swSingleIPMSPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPMSPlatform.setStatus("current")
_SwSingleIPMSHoldtime_Type = Integer32
_SwSingleIPMSHoldtime_Object = MibTableColumn
swSingleIPMSHoldtime = _SwSingleIPMSHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 7),
    _SwSingleIPMSHoldtime_Type()
)
swSingleIPMSHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPMSHoldtime.setStatus("current")
_SwSingleIPMSCasSource_Type = Integer32
_SwSingleIPMSCasSource_Object = MibTableColumn
swSingleIPMSCasSource = _SwSingleIPMSCasSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 8),
    _SwSingleIPMSCasSource_Type()
)
swSingleIPMSCasSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSingleIPMSCasSource.setStatus("current")


class _SwSingleIPMSPassword_Type(OctetString):
    """Custom type swSingleIPMSPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwSingleIPMSPassword_Type.__name__ = "OctetString"
_SwSingleIPMSPassword_Object = MibTableColumn
swSingleIPMSPassword = _SwSingleIPMSPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 9),
    _SwSingleIPMSPassword_Type()
)
swSingleIPMSPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSingleIPMSPassword.setStatus("current")
_SwSingleIPMSRowStatus_Type = RowStatus
_SwSingleIPMSRowStatus_Object = MibTableColumn
swSingleIPMSRowStatus = _SwSingleIPMSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 10),
    _SwSingleIPMSRowStatus_Type()
)
swSingleIPMSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSingleIPMSRowStatus.setStatus("current")
_SwSingleIPCaSTable_Object = MibTable
swSingleIPCaSTable = _SwSingleIPCaSTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4)
)
if mibBuilder.loadTexts:
    swSingleIPCaSTable.setStatus("current")
_SwSingleIPCaSEntry_Object = MibTableRow
swSingleIPCaSEntry = _SwSingleIPCaSEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4, 1)
)
swSingleIPCaSEntry.setIndexNames(
    (0, "SINGLE-IP-MIB", "swSingleIPCaSID"),
)
if mibBuilder.loadTexts:
    swSingleIPCaSEntry.setStatus("current")


class _SwSingleIPCaSID_Type(Integer32):
    """Custom type swSingleIPCaSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SwSingleIPCaSID_Type.__name__ = "Integer32"
_SwSingleIPCaSID_Object = MibTableColumn
swSingleIPCaSID = _SwSingleIPCaSID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4, 1, 1),
    _SwSingleIPCaSID_Type()
)
swSingleIPCaSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPCaSID.setStatus("current")


class _SwSingleIPCaSDeviceName_Type(DisplayString):
    """Custom type swSingleIPCaSDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSingleIPCaSDeviceName_Type.__name__ = "DisplayString"
_SwSingleIPCaSDeviceName_Object = MibTableColumn
swSingleIPCaSDeviceName = _SwSingleIPCaSDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4, 1, 2),
    _SwSingleIPCaSDeviceName_Type()
)
swSingleIPCaSDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPCaSDeviceName.setStatus("current")
_SwSingleIPCaSMacAddr_Type = MacAddress
_SwSingleIPCaSMacAddr_Object = MibTableColumn
swSingleIPCaSMacAddr = _SwSingleIPCaSMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4, 1, 3),
    _SwSingleIPCaSMacAddr_Type()
)
swSingleIPCaSMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPCaSMacAddr.setStatus("current")


class _SwSingleIPCaSFirmwareVer_Type(DisplayString):
    """Custom type swSingleIPCaSFirmwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSingleIPCaSFirmwareVer_Type.__name__ = "DisplayString"
_SwSingleIPCaSFirmwareVer_Object = MibTableColumn
swSingleIPCaSFirmwareVer = _SwSingleIPCaSFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4, 1, 4),
    _SwSingleIPCaSFirmwareVer_Type()
)
swSingleIPCaSFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPCaSFirmwareVer.setStatus("current")


class _SwSingleIPCaSCapability_Type(DisplayString):
    """Custom type swSingleIPCaSCapability based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSingleIPCaSCapability_Type.__name__ = "DisplayString"
_SwSingleIPCaSCapability_Object = MibTableColumn
swSingleIPCaSCapability = _SwSingleIPCaSCapability_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4, 1, 5),
    _SwSingleIPCaSCapability_Type()
)
swSingleIPCaSCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPCaSCapability.setStatus("current")


class _SwSingleIPCaSPlatform_Type(DisplayString):
    """Custom type swSingleIPCaSPlatform based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSingleIPCaSPlatform_Type.__name__ = "DisplayString"
_SwSingleIPCaSPlatform_Object = MibTableColumn
swSingleIPCaSPlatform = _SwSingleIPCaSPlatform_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4, 1, 6),
    _SwSingleIPCaSPlatform_Type()
)
swSingleIPCaSPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPCaSPlatform.setStatus("current")
_SwSingleIPCaSHoldtime_Type = Integer32
_SwSingleIPCaSHoldtime_Object = MibTableColumn
swSingleIPCaSHoldtime = _SwSingleIPCaSHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4, 1, 7),
    _SwSingleIPCaSHoldtime_Type()
)
swSingleIPCaSHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPCaSHoldtime.setStatus("current")
_SwSingleIPGroupTable_Object = MibTable
swSingleIPGroupTable = _SwSingleIPGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5)
)
if mibBuilder.loadTexts:
    swSingleIPGroupTable.setStatus("current")
_SwSingleIPGroupEntry_Object = MibTableRow
swSingleIPGroupEntry = _SwSingleIPGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1)
)
swSingleIPGroupEntry.setIndexNames(
    (0, "SINGLE-IP-MIB", "swSingleIPGroupMacAddr"),
)
if mibBuilder.loadTexts:
    swSingleIPGroupEntry.setStatus("current")
_SwSingleIPGroupMacAddr_Type = MacAddress
_SwSingleIPGroupMacAddr_Object = MibTableColumn
swSingleIPGroupMacAddr = _SwSingleIPGroupMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1, 1),
    _SwSingleIPGroupMacAddr_Type()
)
swSingleIPGroupMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPGroupMacAddr.setStatus("current")


class _SwSingleIPGroupName_Type(DisplayString):
    """Custom type swSingleIPGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSingleIPGroupName_Type.__name__ = "DisplayString"
_SwSingleIPGroupName_Object = MibTableColumn
swSingleIPGroupName = _SwSingleIPGroupName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1, 2),
    _SwSingleIPGroupName_Type()
)
swSingleIPGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPGroupName.setStatus("current")


class _SwSingleIPGroupDeviceName_Type(DisplayString):
    """Custom type swSingleIPGroupDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSingleIPGroupDeviceName_Type.__name__ = "DisplayString"
_SwSingleIPGroupDeviceName_Object = MibTableColumn
swSingleIPGroupDeviceName = _SwSingleIPGroupDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1, 3),
    _SwSingleIPGroupDeviceName_Type()
)
swSingleIPGroupDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPGroupDeviceName.setStatus("current")
_SwSingleIPGroupMSNumber_Type = Integer32
_SwSingleIPGroupMSNumber_Object = MibTableColumn
swSingleIPGroupMSNumber = _SwSingleIPGroupMSNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1, 4),
    _SwSingleIPGroupMSNumber_Type()
)
swSingleIPGroupMSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPGroupMSNumber.setStatus("current")


class _SwSingleIPGroupFirmwareVer_Type(DisplayString):
    """Custom type swSingleIPGroupFirmwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSingleIPGroupFirmwareVer_Type.__name__ = "DisplayString"
_SwSingleIPGroupFirmwareVer_Object = MibTableColumn
swSingleIPGroupFirmwareVer = _SwSingleIPGroupFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1, 5),
    _SwSingleIPGroupFirmwareVer_Type()
)
swSingleIPGroupFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPGroupFirmwareVer.setStatus("current")


class _SwSingleIPGroupCapability_Type(DisplayString):
    """Custom type swSingleIPGroupCapability based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSingleIPGroupCapability_Type.__name__ = "DisplayString"
_SwSingleIPGroupCapability_Object = MibTableColumn
swSingleIPGroupCapability = _SwSingleIPGroupCapability_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1, 6),
    _SwSingleIPGroupCapability_Type()
)
swSingleIPGroupCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPGroupCapability.setStatus("current")


class _SwSingleIPGroupPlatform_Type(DisplayString):
    """Custom type swSingleIPGroupPlatform based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSingleIPGroupPlatform_Type.__name__ = "DisplayString"
_SwSingleIPGroupPlatform_Object = MibTableColumn
swSingleIPGroupPlatform = _SwSingleIPGroupPlatform_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1, 7),
    _SwSingleIPGroupPlatform_Type()
)
swSingleIPGroupPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPGroupPlatform.setStatus("current")
_SwSingleIPGroupHoldtime_Type = Integer32
_SwSingleIPGroupHoldtime_Object = MibTableColumn
swSingleIPGroupHoldtime = _SwSingleIPGroupHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1, 8),
    _SwSingleIPGroupHoldtime_Type()
)
swSingleIPGroupHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPGroupHoldtime.setStatus("current")
_SwSingleIPNeighborTable_Object = MibTable
swSingleIPNeighborTable = _SwSingleIPNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 6)
)
if mibBuilder.loadTexts:
    swSingleIPNeighborTable.setStatus("current")
_SwSingleIPNeighborEntry_Object = MibTableRow
swSingleIPNeighborEntry = _SwSingleIPNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 6, 1)
)
swSingleIPNeighborEntry.setIndexNames(
    (0, "SINGLE-IP-MIB", "swSingleIPNBReceivedPort"),
    (0, "SINGLE-IP-MIB", "swSingleIPNBMacAddr"),
)
if mibBuilder.loadTexts:
    swSingleIPNeighborEntry.setStatus("current")
_SwSingleIPNBReceivedPort_Type = Integer32
_SwSingleIPNBReceivedPort_Object = MibTableColumn
swSingleIPNBReceivedPort = _SwSingleIPNBReceivedPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 6, 1, 1),
    _SwSingleIPNBReceivedPort_Type()
)
swSingleIPNBReceivedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPNBReceivedPort.setStatus("current")
_SwSingleIPNBMacAddr_Type = MacAddress
_SwSingleIPNBMacAddr_Object = MibTableColumn
swSingleIPNBMacAddr = _SwSingleIPNBMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 6, 1, 2),
    _SwSingleIPNBMacAddr_Type()
)
swSingleIPNBMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPNBMacAddr.setStatus("current")


class _SwSingleIPNBRoleState_Type(Integer32):
    """Custom type swSingleIPNBRoleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("candidate", 2),
          ("commander", 1),
          ("member", 3))
    )


_SwSingleIPNBRoleState_Type.__name__ = "Integer32"
_SwSingleIPNBRoleState_Object = MibTableColumn
swSingleIPNBRoleState = _SwSingleIPNBRoleState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 6, 1, 3),
    _SwSingleIPNBRoleState_Type()
)
swSingleIPNBRoleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPNBRoleState.setStatus("current")
_SingleIPMSNotify_ObjectIdentity = ObjectIdentity
singleIPMSNotify = _SingleIPMSNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6)
)
_SingleIPMSNotifyPrefix_ObjectIdentity = ObjectIdentity
singleIPMSNotifyPrefix = _SingleIPMSNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0)
)
_SingleIPNotifyBidings_ObjectIdentity = ObjectIdentity
singleIPNotifyBidings = _SingleIPNotifyBidings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 1)
)


class _SwSingleIPMSTrapMessage_Type(OctetString):
    """Custom type swSingleIPMSTrapMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SwSingleIPMSTrapMessage_Type.__name__ = "OctetString"
_SwSingleIPMSTrapMessage_Object = MibScalar
swSingleIPMSTrapMessage = _SwSingleIPMSTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 1, 1),
    _SwSingleIPMSTrapMessage_Type()
)
swSingleIPMSTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSingleIPMSTrapMessage.setStatus("current")

# Managed Objects groups


# Notification objects

swSingleIPMSColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 11)
)
swSingleIPMSColdStart.setObjects(
      *(("SINGLE-IP-MIB", "swSingleIPMSID"),
        ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"))
)
if mibBuilder.loadTexts:
    swSingleIPMSColdStart.setStatus(
        "current"
    )

swSingleIPMSWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 12)
)
swSingleIPMSWarmStart.setObjects(
      *(("SINGLE-IP-MIB", "swSingleIPMSID"),
        ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"))
)
if mibBuilder.loadTexts:
    swSingleIPMSWarmStart.setStatus(
        "current"
    )

swSingleIPMSLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 13)
)
swSingleIPMSLinkDown.setObjects(
      *(("SINGLE-IP-MIB", "swSingleIPMSID"),
        ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    swSingleIPMSLinkDown.setStatus(
        "current"
    )

swSingleIPMSLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 14)
)
swSingleIPMSLinkUp.setObjects(
      *(("SINGLE-IP-MIB", "swSingleIPMSID"),
        ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    swSingleIPMSLinkUp.setStatus(
        "current"
    )

swSingleIPMSAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 15)
)
swSingleIPMSAuthFail.setObjects(
      *(("SINGLE-IP-MIB", "swSingleIPMSID"),
        ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"))
)
if mibBuilder.loadTexts:
    swSingleIPMSAuthFail.setStatus(
        "current"
    )

swSingleIPMSnewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 16)
)
swSingleIPMSnewRoot.setObjects(
      *(("SINGLE-IP-MIB", "swSingleIPMSID"),
        ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"))
)
if mibBuilder.loadTexts:
    swSingleIPMSnewRoot.setStatus(
        "current"
    )

swSingleIPMSTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 17)
)
swSingleIPMSTopologyChange.setObjects(
      *(("SINGLE-IP-MIB", "swSingleIPMSID"),
        ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"))
)
if mibBuilder.loadTexts:
    swSingleIPMSTopologyChange.setStatus(
        "current"
    )

swSingleIPMSrisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 18)
)
swSingleIPMSrisingAlarm.setObjects(
      *(("SINGLE-IP-MIB", "swSingleIPMSID"),
        ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"))
)
if mibBuilder.loadTexts:
    swSingleIPMSrisingAlarm.setStatus(
        "current"
    )

swSingleIPMSfallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 19)
)
swSingleIPMSfallingAlarm.setObjects(
      *(("SINGLE-IP-MIB", "swSingleIPMSID"),
        ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"))
)
if mibBuilder.loadTexts:
    swSingleIPMSfallingAlarm.setStatus(
        "current"
    )

swSingleIPMSmacNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 20)
)
swSingleIPMSmacNotification.setObjects(
      *(("SINGLE-IP-MIB", "swSingleIPMSID"),
        ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"),
        ("SINGLE-IP-MIB", "swSingleIPMSTrapMessage"))
)
if mibBuilder.loadTexts:
    swSingleIPMSmacNotification.setStatus(
        "current"
    )

swSingleIPMSPortTypeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 21)
)
swSingleIPMSPortTypeChange.setObjects(
      *(("SINGLE-IP-MIB", "swSingleIPMSID"),
        ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"),
        ("IF-MIB", "ifIndex"),
        ("SINGLE-IP-MIB", "swSingleIPMSTrapMessage"))
)
if mibBuilder.loadTexts:
    swSingleIPMSPortTypeChange.setStatus(
        "current"
    )

swSingleIPMSPowerStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 22)
)
swSingleIPMSPowerStatusChg.setObjects(
      *(("SINGLE-IP-MIB", "swSingleIPMSID"),
        ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"),
        ("SINGLE-IP-MIB", "swSingleIPMSTrapMessage"))
)
if mibBuilder.loadTexts:
    swSingleIPMSPowerStatusChg.setStatus(
        "current"
    )

swSingleIPMSPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 23)
)
swSingleIPMSPowerFailure.setObjects(
      *(("SINGLE-IP-MIB", "swSingleIPMSID"),
        ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"),
        ("SINGLE-IP-MIB", "swSingleIPMSTrapMessage"))
)
if mibBuilder.loadTexts:
    swSingleIPMSPowerFailure.setStatus(
        "current"
    )

swSingleIPMSPowerRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 24)
)
swSingleIPMSPowerRecover.setObjects(
      *(("SINGLE-IP-MIB", "swSingleIPMSID"),
        ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"),
        ("SINGLE-IP-MIB", "swSingleIPMSTrapMessage"))
)
if mibBuilder.loadTexts:
    swSingleIPMSPowerRecover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SINGLE-IP-MIB",
    **{"swSingleIPMIB": swSingleIPMIB,
       "swSingleIPMgmt": swSingleIPMgmt,
       "swSingleIPInfo": swSingleIPInfo,
       "swSingleIPVersion": swSingleIPVersion,
       "swSingleIPCapability": swSingleIPCapability,
       "swSingleIPPlatform": swSingleIPPlatform,
       "swSingleIPCtrl": swSingleIPCtrl,
       "swSingleIPAdmin": swSingleIPAdmin,
       "swSingleIPRoleState": swSingleIPRoleState,
       "swSingleIPHoldtime": swSingleIPHoldtime,
       "swSingleIPTimeInterval": swSingleIPTimeInterval,
       "swSingleIPMSTable": swSingleIPMSTable,
       "swSingleIPMSEntry": swSingleIPMSEntry,
       "swSingleIPMSID": swSingleIPMSID,
       "swSingleIPMSDeviceName": swSingleIPMSDeviceName,
       "swSingleIPMSMacAddr": swSingleIPMSMacAddr,
       "swSingleIPMSFirmwareVer": swSingleIPMSFirmwareVer,
       "swSingleIPMSCapability": swSingleIPMSCapability,
       "swSingleIPMSPlatform": swSingleIPMSPlatform,
       "swSingleIPMSHoldtime": swSingleIPMSHoldtime,
       "swSingleIPMSCasSource": swSingleIPMSCasSource,
       "swSingleIPMSPassword": swSingleIPMSPassword,
       "swSingleIPMSRowStatus": swSingleIPMSRowStatus,
       "swSingleIPCaSTable": swSingleIPCaSTable,
       "swSingleIPCaSEntry": swSingleIPCaSEntry,
       "swSingleIPCaSID": swSingleIPCaSID,
       "swSingleIPCaSDeviceName": swSingleIPCaSDeviceName,
       "swSingleIPCaSMacAddr": swSingleIPCaSMacAddr,
       "swSingleIPCaSFirmwareVer": swSingleIPCaSFirmwareVer,
       "swSingleIPCaSCapability": swSingleIPCaSCapability,
       "swSingleIPCaSPlatform": swSingleIPCaSPlatform,
       "swSingleIPCaSHoldtime": swSingleIPCaSHoldtime,
       "swSingleIPGroupTable": swSingleIPGroupTable,
       "swSingleIPGroupEntry": swSingleIPGroupEntry,
       "swSingleIPGroupMacAddr": swSingleIPGroupMacAddr,
       "swSingleIPGroupName": swSingleIPGroupName,
       "swSingleIPGroupDeviceName": swSingleIPGroupDeviceName,
       "swSingleIPGroupMSNumber": swSingleIPGroupMSNumber,
       "swSingleIPGroupFirmwareVer": swSingleIPGroupFirmwareVer,
       "swSingleIPGroupCapability": swSingleIPGroupCapability,
       "swSingleIPGroupPlatform": swSingleIPGroupPlatform,
       "swSingleIPGroupHoldtime": swSingleIPGroupHoldtime,
       "swSingleIPNeighborTable": swSingleIPNeighborTable,
       "swSingleIPNeighborEntry": swSingleIPNeighborEntry,
       "swSingleIPNBReceivedPort": swSingleIPNBReceivedPort,
       "swSingleIPNBMacAddr": swSingleIPNBMacAddr,
       "swSingleIPNBRoleState": swSingleIPNBRoleState,
       "singleIPMSNotify": singleIPMSNotify,
       "singleIPMSNotifyPrefix": singleIPMSNotifyPrefix,
       "swSingleIPMSColdStart": swSingleIPMSColdStart,
       "swSingleIPMSWarmStart": swSingleIPMSWarmStart,
       "swSingleIPMSLinkDown": swSingleIPMSLinkDown,
       "swSingleIPMSLinkUp": swSingleIPMSLinkUp,
       "swSingleIPMSAuthFail": swSingleIPMSAuthFail,
       "swSingleIPMSnewRoot": swSingleIPMSnewRoot,
       "swSingleIPMSTopologyChange": swSingleIPMSTopologyChange,
       "swSingleIPMSrisingAlarm": swSingleIPMSrisingAlarm,
       "swSingleIPMSfallingAlarm": swSingleIPMSfallingAlarm,
       "swSingleIPMSmacNotification": swSingleIPMSmacNotification,
       "swSingleIPMSPortTypeChange": swSingleIPMSPortTypeChange,
       "swSingleIPMSPowerStatusChg": swSingleIPMSPowerStatusChg,
       "swSingleIPMSPowerFailure": swSingleIPMSPowerFailure,
       "swSingleIPMSPowerRecover": swSingleIPMSPowerRecover,
       "singleIPNotifyBidings": singleIPNotifyBidings,
       "swSingleIPMSTrapMessage": swSingleIPMSTrapMessage}
)
